---
id: ent-customer-observability
type: entity
status: draft
owner: rackai-product
domain: product
aliases: [customer observability, customer observability surface, tenant observability, in-tenant observability surface, customer metrics, workload observability]
related: [ent-evidence-report, prd-customer-observability-evidence, spec-customer-observability-evidence, ent-workload-declaration, ent-model-deployment, ent-organization, met-slo-attainment, wf-monitoring, wf-metering, src-monitoring-audit-spec, src-metering-spec, wiki-milestone-release-map]
source_docs: ["05-wiki/Milestone Release Map.md", "06-sources/rackai-platform/Monitoring and Auditability Spec.md", "05-wiki/RackAI Roadmap.csv", "RSS-Engineering/rackai@79ca4de (read-only)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: the customer view of how their workloads perform and what they use; not operator intelligence."
---

# Customer Observability

## Definition

**Customer Observability** is the customer-facing surface that answers *how is my workload performing, and what am I consuming?* For each of a customer's workloads it shows latency percentiles, time to first token, inter-token latency, output throughput, requests and errors, usage, quota and spend, the workload's state, and its [[SLO Attainment]] against the service level in its [[Workload Declaration]].

It is one of the two observability products in the ratified "observability is two products" decision ([[Milestone Release Map]], 2026-10-06). The other is **operator intelligence** (GPU and VRAM, queue depth, cache, power, placement signals), which feeds the [[Empirical Map]]. Both use the same telemetry pipeline ([[Monitoring & Observability]]). They differ in purpose and audience: customer observability shows a tenant only its own workloads, through an explicit allowlist, and never nodes, supply internals or other tenants.

> **Status: partly built substrate, product surface not built.** A tenant metrics API, a workload-status API and a usage API exist, but the metrics API returns empty series (no metric source is shipped), TTFT and throughput are not in it, and no console page shows any of it (read-only survey, `RSS-Engineering/rackai@79ca4de`, `rackai-ui@89bddb4`; [[Monitoring and Auditability Spec]]). The product contract is [[Customer Observability & Evidence Report PRD]].

## Layer

L1 — Entity Ontology. It observes the serving chain from the customer's side and never bypasses a layer:

**[[Workload Declaration]] → [[Model Deployment]] → [[Serving Runtime]]** (telemetry source) → **Customer Observability** → [[Evidence Report]] (periodic proof)

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Scope | Tenant ([[Organization]]) and project; a project-confined user sees only their projects | ref | derived (project filter built in the observability service) |
| Performance metrics | Latency p50/p95/p99, TTFT, inter-token latency, output tokens/s, request rate, error rate. Latency is labelled server-side, never end-to-end; runtimes without parity-checked series show these as unavailable | series | assumed (latency p99, request and error rate designed and wired, no data) |
| Usage | Tokens (input, output, cached), requests, GPU time, per project, model and period | totals | derived (usage API built; inference latency and compute fields are zero by omission) |
| Quota | Utilisation against quota policy | ratio | assumed (no quota policy exists) |
| Spend | What the customer is charged; never RackAI internal cost or margin | money | assumed (no price source) |
| Workload state | Declaration state and reasons; deployment availability | enum | derived for deployment availability; assumed for declaration state |
| Attainment | Canonical joint [[SLO Attainment]] against the declared service level and the ratified per-profile thresholds, or `not_measured`; per-threshold histogram figures are labelled estimates and never shown as met | percent | assumed (thresholds not ratified) |
| Data state | *available*, *no traffic*, *no data source*, *backend unavailable*, with an as-of time | enum | assumed |

## Lifecycle States

The surface itself has no lifecycle; each metric it shows has a **data state**:

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| No data source | Nothing produces this metric for this workload (e.g. a runtime without the series) | Source not configured or not emitted | A source is enabled |
| No traffic | The source exists and the workload received no requests in the window | Source present, zero samples | Traffic arrives |
| Available | Values exist for the window, with an as-of time | Samples present | Source removed, or backend fails |
| Backend unavailable | The telemetry store could not be queried | Query error | Backend recovers |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model Deployment]] | → | Performance and usage per deployment |
| MEASURES | [[Workload Declaration]] | → | Attainment against the declared service level |
| USES | [[SLO Attainment]] | → | The attainment measure |
| CONSUMES | [[Monitoring & Observability]] | → | Same pipeline as operator intelligence |
| CONSUMES | [[Metering]] | → | Usage records |
| BELONGS_TO | [[Organization]] | → | Tenant-scoped |
| SUPPORTS | [[Evidence Report]] | → | Its telemetry-derived values become evidence for the report |

## Evidence

- Source: `source_docs`; read-only code survey at `RSS-Engineering/rackai@79ca4de` (`internal/observabilityservice`, `internal/usageservice`, `charts/rackai-monitoring`) and `rackai-ui@89bddb4`.
- Confidence rationale: `assumed`. The product surface is proposed; the built substrate (APIs, usage records) is `derived` from code and noted per attribute.

## See Also

- [[Customer Observability & Evidence Report PRD]]: the product contract
- [[Customer Observability & Evidence Report Tech Spec]]: the proposed design (draft)
- [[Evidence Report]]: the periodic proof built partly from this surface's data
- [[Milestone Release Map]]: the two-products decision
- [[Entity Ontology Hub]]
