---
id: met-availability
type: metric
status: draft
owner: reliability
domain: reliability
aliases: [availability, uptime, endpoint availability]
related: [met-ttft, met-gpu-utilization, wf-canary-rollback, wf-admission-control, pol-admission-control, ent-model-deployment, ent-openrouter-integration, evt-deployment-canary-passed, evd-kpi-telemetry-targets]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Endpoint uptime for priority models; guardrail metric with a >99.9% target."
---

# Availability

## Definition

Measures whether the endpoint can reliably receive and serve traffic — performance is irrelevant if requests cannot land. Availability is a guardrail metric: it constrains autoscaling, admission control, and canary promotion rather than being independently maximized. Supporting reliability measures include inference error rate, timeout rate, capacity rejection rate, and failed model requests.

## KPI Job

Serves internal operating decisions (guardrail on autoscaling, admission, canary) and commercial commitment (the >99.9% target is a customer-facing promise) — jobs 1 and 3 per [[KPI Telemetry Target List]]. As an SLA-grade number it needs a durable record and a measured baseline before the target is contractually promised.

## Unit

percentage (uptime over a measurement window).

## Source or Formula

- Measured from: endpoint health/status telemetry via the [[OpenRouter Provider Integration]] and per [[Model Deployment]].
- Not a formula — measured directly.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | >99.9% for priority models (roadmap target) | Protected under [[Admission Control]] and [[Canary & Rollback]] |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model Deployment]] | → | Per deployment endpoint |
| DEPENDS_ON | [[OpenRouter Provider Integration]] | → | Endpoint health/status telemetry source |
| CONSTRAINS | [[Admission Control]] | → | Secondary protected guardrail |
| CONSTRAINS | [[Canary & Rollback]] | → | Availability rollback signal |

## Evidence

- Confidence rationale: `assumed` — the >99.9% figure is a roadmap target, not a measured Rack AI value. It becomes `measured` from production uptime telemetry once deployments serve traffic.

## See Also

- [[Operations Hub]]
