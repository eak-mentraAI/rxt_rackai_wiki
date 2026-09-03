---
id: met-ttft
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [ttft, time to first token, p95 ttft, latency to first token]
related: [met-output-throughput, met-tokens-per-gpu-second, met-availability, wf-admission-control, wf-canary-rollback, pol-admission-control, ent-model-deployment, ent-traffic-class]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Time to first token — how quickly users begin receiving a response; track P50/P95/P99 and queueing delay."
---

# TTFT

## Definition

**Time to first token** — how quickly a user begins receiving a response after issuing a request. This is the canonical TTFT note. Track P50, P95, and P99 plus queueing delay. TTFT is measured independently from output-token throughput because the two require different optimization strategies, and it is a primary latency guardrail across canary, admission control, and the performance regression gate.

## Unit

milliseconds (per request; reported as P50/P95/P99 percentiles).

## Source or Formula

- Measured from: request-level serving telemetry (timestamp of request → timestamp of first streamed token), including queueing delay, per [[Model Deployment]] and [[Traffic Class]].
- Not derived from a formula — measured directly.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↓ | Minimize P50/P95/P99 (no measured baseline yet) | Protected guardrail under [[Admission Control]] and [[Canary & Rollback]] |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — direction (↓) is roadmap-mandated (KPI #3), but no measured Rack AI percentiles exist yet. Values become `measured` from production telemetry once deployments serve traffic.

## See Also

- [[Operations Hub]]
