---
id: src-monitoring-audit-spec
type: source
status: reviewed
owner: reliability
domain: reliability
aliases: [monitoring prd, platform monitoring tech spec, observability spec, auditability spec, compliance spec]
related: [hub-rackai-platform, src-rackai-release-1-0-0]
source_docs: []
confidence: derived
last_reviewed: 2026-10-10
parent: hub-rackai-platform
summary: "Source: RackAI Monitoring + Auditability PRDs and tech specs with as-built deltas (observability, audit)."
---

# Monitoring and Auditability Spec

## Provenance

- Origin (current): `reference/PRD/Platform_Monitoring_TechSpec.docx` (v0.2, 2026-05-12), `reference/PRD/InTenant_Observability_TechSpec.docx` (v0.9, 2026-05-19), `reference/PRD/Auditability_Compliance_TechSpec.docx` (v0.9, 2026-05-14) — received 2026-10-10; these supersede the rackai-platform copies of the three tech specs. Headers are unchanged; the new copies add AS BUILT / PROPOSED-NOT-BUILT annotations dated 2026-09-14 → 2026-09-16.
- Origin (prior, ingested 2026-09-04): `reference/rackai-platform/PRD - Monitoring.docx`, `Platform_Monitoring_TechSpec.docx`, `PRD - Auditability and Observability.docx`, `Auditability_Compliance_TechSpec.docx`, `InTenant_Observability_TechSpec.docx`. The two PRDs are unchanged in `reference/PRD/`.
- Classification: planning / architecture, with as-built annotations

## Summary

Two related concerns:

- **Platform monitoring** — operator-facing telemetry (Prometheus scrape targets incl. kube-state-metrics, AMD GPU, kubelet/cAdvisor; a `rackai-monitoring` Helm chart shipped in 1.0.0). This is the operator view.
- **In-tenant observability & auditability** — tenant-facing metrics, logs, and an immutable **audit** trail. Partly **built** as of 2026-09-14/16: the audit store (PostgreSQL, append-only with RLS), the `rackai-audit-api` read API and outbox drainer, and the In-Tenant Observability service exist. But the tenant inference-metrics endpoint returns empty series (its recording rules are unshipped), and several audit pieces (Audit Webhook, workload/billing audit tables, jobs endpoint) are not built — see As-Built Deltas.

Compliance: the specs describe aspirational controls (immutable audit, OIDC/RBAC/mTLS) but make **no concrete HIPAA/SOC2/GDPR/zero-data-retention claims** — relevant to the [[OpenRouter Initiative]] "declare compliance per model" requirement, where we currently can declare little.

## As-Built Deltas (spec revisions through 2026-09-29)

Source: annotations in the 2026-10-10 copies of the three tech specs. Shipped behaviour takes precedence over the original design text.

**Auditability & Compliance (v0.9) — AS BUILT 2026-09-14**
- **Transport changed, guarantees kept.** No gRPC audit ingress and no separate audit-service repo: producers embed the in-process `pkg/audit` writer and write to PostgreSQL directly (cost: every producer needs audit-DB credentials).
- **No Redis Streams.** Tier 1 durability is a **PostgreSQL outbox** (`audit.event_outbox`, drained with `SKIP LOCKED`, per-row savepoint) with poison rows moved to `audit.event_dead_letter` rather than dropped — decided 2026-09-11 because airgap installs already require PostgreSQL. The Redis Streams design is kept in the spec only as a decision record.
- **Three write shapes:** (a) synchronous insert into `rbac_audit_log` for role-change and API-key lifecycle events (error → controller requeue); (b) outbox enqueue drained into `audit.<category>_audit_log` (config changes such as `customerorg_deleted`, `tenant_deprovisioned`); (c) async bounded buffer for request-path events (Tier 2, drops with a metric).
- **`rackai-audit-api` is a reader + drainer, not a write endpoint** (drain every 5 s, batch 100). Audit-DB outage now gates controller paths (reconcile error/requeue) rather than queueing writes.
- **Not built:** the Audit Webhook and proposed-/last-actor annotations (deferred to M4) — so a raw `kubectl delete` records actor `unknown`, not `kubectl:{user}`; `audit.workload_audit_log` (M1-deferred) and `audit.billing_audit_log` (M3); the `/audit/jobs/{job_id}` endpoint. Only `customerorg_deleted` and `tenant_deprovisioned` config events are emitted so far.
- **Read API:** `/audit`, `/audit/{category}`, `/audit/requests/{requestId}` built; all six categories accepted (workload/billing return empty pages); `from`/`to` are required on every endpoint. A deprovisioned tenant's terminal event stays readable because the path is not checked for namespace existence.
- **RLS:** the three M2 category tables (quota/dataset/config) have forced row-level security with a purge-outside-window policy; outbox/dead-letter tables have none (internal plumbing). A non-empty dead-letter table is an alertable condition.
- **Deletion cascade attribution (§5.5.1):** CustomerOrg deletion stamps its deleter/request ID onto each tenant before teardown so all rows share one `request_id`. Known hole: force-removing a stuck finalizer skips the audit event.
- Idempotency keys for controller events are deterministic UUIDv5 over (object UID, event kind). NFRs restated for the outbox: producer insert P99 < 100 ms; drain lag P99 < one interval (5 s); 5,000 events/s throughput not load-tested.
- Unchanged from the prior copy: audit retention cap raised 366 → 2557 days (resolved 2026-07-28).

**Platform Monitoring (v0.2) — AS BUILT 2026-09-15/16**
- **No `rackai:*` recording rules are shipped** — no `PrometheusRule` exists in any chart. *(Code check 2026-10-10: as of `rackai@79ca4de`, `charts/rackai-monitoring` ships seven PrometheusRule templates (RACKAI-475, 2026-09-25); the tenant recording-rule template is off by default and still sources `rackai_gateway_*`.)* The gateway-sourced rules depend on `rackai_gateway_*` metrics that **no code emits**: the gateway is Envoy (`rackai-frontproxy`), there is no Go gateway.
- **Correction:** vLLM metrics *do* carry tenant context — tenant workloads run in namespaces named after the tenant and the ServiceMonitor scrape stamps `namespace` (and the InferenceService name) on every `vllm:*` series. Rules are re-sourced from vLLM histograms via `label_replace(namespace → tenant_id)`.
- **PROPOSED, NOT BUILT (2026-09-16):** per-tenant/per-model streaming-quality rules — TTFT P50/P99, inter-token latency P50/P99, output tokens/s — plus sourced replacements for per-tenant P99 latency and request rate. AMD/AIM parity of the `vllm:` metrics is unverified.
- **Audit metrics renamed as built:** `audit_events_written_total` (unprefixed counter, not a gauge) and `audit_events_dropped_total` (unprefixed). **No ServiceMonitor targets `rackai-audit`** and no alert rule exists, so the Tier 2 drop counter is emitted but never observed (NOT BUILT as of 2026-09-15).
- OQ2 (resolved 2026-07-28): dedicated per-tenant recording rules chosen over query-time filtering; per-tenant queue depth still needs a tenant-labelled gateway metric (M2).

**In-Tenant Observability (v0.9) — AS BUILT 2026-09-16**
- The Observability service is built but `/metrics/inference` **returns empty series**: it queries recording rules that are not shipped and, as originally specified, have no metric source. "Until those rules ship, this endpoint is an API without data."
- **PROPOSED, NOT BUILT:** TTFT, inter-token latency and output-throughput rows in the Metrics API (identifiers `inference.ttft.p50_ms`, `inference.itl.p99_ms`, `inference.output_tokens_per_second`, etc., per model), and a future TTFT alert type.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Monitoring / observability | [[Monitoring & Observability]] | L2 |
| Audit trail | [[Audit]] | L2 |
| Operator telemetry (shipped) | [[Productive GPU Utilization]] and fleet metrics | L2 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
