---
id: evt-deployment-canary-passed
type: event
status: draft
owner: reliability
domain: reliability
aliases: [deployment canary passed, canary gate passed, canary cleared]
related: [wf-canary-rollback, wf-model-launch-factory, wf-closed-loop-optimization, ent-model-deployment, ent-benchmark-run]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
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

## See Also

- [[Operations Hub]]
