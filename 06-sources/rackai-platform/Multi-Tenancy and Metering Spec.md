---
id: src-metering-spec
type: source
status: reviewed
owner: platform-eng
domain: commercial
aliases: [metering spec, multi tenancy prd, metering tech spec, usage metering]
related: [hub-rackai-platform, hub-commercial, src-rackai-platform-prd]
source_docs: []
confidence: derived
last_reviewed: 2026-10-10
parent: hub-rackai-platform
summary: "Source: RackAI Multi-Tenancy & Metering PRD + tech spec with as-built deltas (usage capture, quotas, billing link)."
---

# Multi-Tenancy and Metering Spec

## Provenance

- Origin (current): `reference/PRD/Multi_Tenants_Metering_TechSpec.docx` (received 2026-10-10) — supersedes the rackai-platform copy of the tech spec; same header (v0.2, Draft, created 30/04/2026) but adds AS BUILT / PROPOSED-NOT-BUILT annotations (2026-09-14 → 2026-10-08) and records open-question resolutions dated 2026-07-28.
- Origin (prior, ingested 2026-09-04): `reference/rackai-platform/PRD - Multi Tenancy and Metering.docx`, `Multi_Tenants_Metering_TechSpec.docx`. The PRD is unchanged in `reference/PRD/`.
- Status: Draft (spec v0.2)
- Classification: planning / architecture, with as-built annotations

## Summary

Defines tenant isolation, usage **metering** (capturing token/request usage per tenant into `usage_records`), and **quotas** (`QuotaPolicy`, Quota Enforcement Service). Introduces Projects and UsageRecord concepts. The spec is still draft, but parts are now **built**: the PostgreSQL metering outbox/drainer, `FineTuningJob.spec.project`, and fine-tuning metering via a per-pod sidecar (as of 2026-10-08). Live mid-job quota enforcement for fine-tuning, `Model.spec.project`, and the billing-account link are not built — see As-Built Deltas.

> **Critical for the OpenRouter Initiative:** this spec explicitly lists **"defining pricing rates or billing logic" as a non-goal**. Metering ≠ billing. The 2026-09-18 annotations *propose* (not built) a billing join — `usage_records.org_id` → `CustomerOrg.spec.cmsAccountId` (Rackspace RCN) — so org-level usage could be invoiced by Rackspace CMS; until it exists, org rollups are "computable but not billable". There is still no pricing, rating, or payment mechanism, which remains the headline P0 gap for the OpenRouter public-provider path. Tracked as an open question and modeled in [[Billing & Payment]].

## As-Built Deltas (spec revisions through 2026-10-08)

Source: annotations in the 2026-10-10 copy of the metering tech spec (v0.2). Note the latest annotations (RACKAI-515) are dated 2026-10-08, after 2026-09-29. Shipped behaviour takes precedence over the original design text.

**Tenancy / attribution**
- **Org attribution from namespace (AS BUILT 2026-09-14).** `spec.orgRef.name` was built then removed; `usage_records.org_id` is populated from the Organization's `metadata.namespace` (its CustomerOrg). `org_id` is a grouping key, not a billing identity.
- **`FineTuningJob.spec.project` is a bare string (AS BUILT 2026-09-29, RACKAI-501)**, not the `spec.projectRef.name` object originally specified; empty = default Project; webhook rejects unresolvable names because `project_id` is immutable. Job list/get is filtered by `spec.project`. (`APIKey`/`RoleBinding` keep `projectRef` objects.)
- **`Model.spec.project` — not yet built**; will follow the same bare-name shape.
- **Audit-attribution fields on FineTuningJob NOT BUILT (verified 2026-09-15).** `submittedBy`, `submissionRequestId`, `cancelRequested`, `cancelledBy`, `cancellationRequestId` (migration `audit-003`) do not exist; fine-tuning cancellation has no attribution source and the two-step PATCH-then-delete cancel is not implemented. Ownership between the rackai repo and metering chart is unsettled.

**Fine-tuning metering transport (AS BUILT 2026-10-08, RACKAI-515)**
- Events come from a native Kubernetes **sidecar** (`rackai-ft-metering-sidecar`, needs K8s 1.29+) in each trainer pod, not the FTJ controller. A startup gate holds the trainer until the sidecar can write, so jobs never run unmetered (and cannot start while the metering DB is down).
- Heartbeats (every 5 min, cumulative `computeSeconds` = elapsed × GPU count, plus `tokensProcessed`/`tokensTrainable` scraped from the trainer) and the SIGTERM completion are both upserted into **`metering_event_outbox`** keyed on `workload_id`; heartbeats are held, not drained; the completion replaces the row and yields one `usage_records` row.
- **No Redis for fine-tuning.** `compute:gpu_secs`, `ft:job_count`, `ft:concurrent` are not implemented: no live mid-job GPU-spend quota enforcement, no counter reconciliation on completion, no counter rebuild after Redis restart. The QES pre-execution concurrency check still applies.
- Billing semantics: billed from sidecar start (includes image pull/model load) to trainer exit, at the trainer's GPU limit; failures and OOM are billed; usage appears only after the job ends. A lost completion (node loss, hard kill) is dead-lettered after 48 h and billed zero until manually promoted. Crediting platform-caused failures is an open policy question. `datasetSizeGb` is not populated; token fields are NULL for AMD jobs.
- `usage_records` gains `tokens_processed` / `tokens_trainable` (BIGINT); migration 000006 must precede the drainer.

**Billing link — PROPOSED 2026-09-18, NOT BUILT**
- Invoicing joins `usage_records.org_id` → `CustomerOrg.spec.cmsAccountId` (RCN) at query time; the RCN is deliberately not stored in `usage_records`. `/customerorgs/{org}/usagesummary` would return `cmsAccountId` and fail closed (409) if absent. Cross-instance invoices would need an `instance_id` column on `usage_records`.

**Open questions resolved (2026-07-28)**
- **Retention:** per-installation `retentionDays` (1–2557 d, default 365), mirroring audit `complianceRetentionDays`; hot PostgreSQL, archive-ready (no cold tier built). Usage records are not erasable within the window.
- **QuotaPolicy:** platform-operator-configurable only (tenants cannot self-raise); tenant-authored policy deferred.
- **UsageSummary freshness SLA:** P95 < 500 ms.
- **KV-cache hit rate:** internal to the runtime, not in UsageRecords.
- **Counter reconstruction:** pass at conservative (configurable) limits during reconstruction, not block-all or full limits.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Metering / usage capture | [[Metering]] | L2 |
| Billing gap (non-goal) | [[Billing & Payment]] | L3 |
| Multi-tenancy | [[Organization]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
- [[Open Questions]]
