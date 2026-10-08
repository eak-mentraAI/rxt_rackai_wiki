---
id: evt-deployment-canary-passed
type: event
status: draft
owner: reliability
domain: reliability
aliases: [deployment canary passed, canary gate passed, canary cleared]
related: [wf-canary-rollback, wf-model-launch-factory, wf-closed-loop-optimization, ent-model-deployment, ent-benchmark-run, wf-request-routing, met-model-launch-lag, met-ttft, met-availability]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Signals that a deployment cleared the canary gate and may proceed to full production."
---

# Deployment Canary Passed

## Definition

Signals that a [[Model Deployment]] has cleared the canary gate — no breach of error, latency ([[TTFT]]), correctness, GPU-failure, or [[Availability]] thresholds during the canary and limited-external stages — and may be promoted to full OpenRouter production traffic. Emitted by [[Canary & Rollback]]. (Roadmap Milestone 4.7.)

## Payload

| Field | Type | Description |
|-------|------|-------------|
| deployment_id | string | The [[Model Deployment]] that passed |
| model | ref | Model and weight version served |
| canary_window | duration | Observation window of the canary stage |
| ttft_p95 | float | Observed P95 TTFT during canary |
| error_rate | float | Observed error rate during canary |
| benchmark_ref | ref | Reference [[Benchmark Run]] compared against |
| decided_at | timestamp | When the gate cleared |

## Emitted By

| Source | Workflow | Condition |
|--------|----------|-----------|
| Canary gate | [[Canary & Rollback]] | Canary and limited-external stages pass without rollback |
| Promotion step | [[Closed-Loop Optimization]] | Promoted config clears canary |

## Consumed By

| Consumer | Action Taken |
|----------|--------------|
| [[Model Launch Factory]] | Proceeds to OpenRouter publication |
| [[Request Routing]] | Adds deployment to eligible production pools |
| Reliability dashboards | Records promotion event |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GENERATES | [[Canary & Rollback]] | ← | Canary gate cleared |
| GENERATES | [[Closed-Loop Optimization]] | ← | Promoted config clears canary |
| CONSUMES | [[Model Launch Factory]] | ← | Proceeds to OpenRouter publication |
| CONSUMES | [[Request Routing]] | ← | Adds deployment to eligible pools |
| DEPENDS_ON | [[Model Launch Lag]] | ← | Stops the launch-lag clock |
| DEPENDS_ON | [[TTFT]] | → | Gate threshold (`ttft_p95`) |
| DEPENDS_ON | [[Availability]] | → | Gate threshold |
| DEPENDS_ON | [[Benchmark Run]] | → | `benchmark_ref` comparison baseline |
| SUPPORTS | [[Model Deployment]] | → | Marks the Canary → Production lifecycle transition |

## See Also

- [[Operations Hub]]
