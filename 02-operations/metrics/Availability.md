---
id: met-availability
type: metric
status: draft
owner: reliability
domain: reliability
aliases: [availability, uptime, endpoint availability]
related: [met-ttft, met-gpu-utilization, wf-canary-rollback, wf-admission-control, pol-admission-control, ent-model-deployment, ent-openrouter-provider-integration]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Endpoint uptime for priority models; guardrail metric with a >99.9% target."
---

# Availability

## Definition

Measures whether the endpoint can reliably receive and serve traffic — performance is irrelevant if requests cannot land. Availability is a guardrail metric: it constrains autoscaling, admission control, and canary promotion rather than being independently maximized. Supporting reliability measures include inference error rate, timeout rate, capacity rejection rate, and failed model requests.

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

## Evidence

- Confidence rationale: `assumed` — the >99.9% figure is a roadmap target, not a measured Rack AI value. It becomes `measured` from production uptime telemetry once deployments serve traffic.

## See Also

- [[Operations Hub]]
