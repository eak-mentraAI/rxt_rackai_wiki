---
id: fml-cost-per-1m-tokens
type: formula
status: draft
owner: finops
domain: commercial
aliases: [cost per 1m tokens, cost per million tokens, cost/token]
related: [fml-gpu-hours-per-1m-tokens, fml-tokens-per-gpu-second, fml-revenue-per-gpu-hour, fml-gross-margin-per-model, coeff-cost-per-gpu-hour, ent-model-deployment]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Computes internal infrastructure cost to produce one million tokens."
---

# Cost per 1M Tokens

## Purpose

Computes the internal infrastructure cost to produce one million tokens for a [[Model Deployment]]. It is the cost side of unit economics and feeds [[Gross Margin per Model]]. It also powers the economic-routing decision in [[Request Routing]].

## Definition

```
cost_per_1m = gpu_hours_per_1m × cost_per_gpu_hour
```

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| gpu_hours_per_1m | Derived | [[GPU-Hours per 1M Tokens]] | assumed |
| cost_per_gpu_hour | Coefficient | [[Cost per GPU-Hour]] | assumed |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| [[Cost per GPU-Hour]] | coeff-cost-per-gpu-hour | assumed |

## Consumed By

| Consumer | Type |
|----------|------|
| [[Gross Margin per Model]] | CONSUMES |
| [[Request Routing]] | CONSUMES |
| FinOps scorecard | CONSUMES |

## Worked Example

Illustrative only (assumed inputs — `cost_per_gpu_hour` is a TBD placeholder pending the roadmap Milestone 0.3 cost model):

- gpu_hours_per_1m = 0.370 (assumed / illustrative, from [[GPU-Hours per 1M Tokens]])
- cost_per_gpu_hour = 3.00 USD/GPU-hour (assumed / illustrative placeholder — NOT a measured value)

cost_per_1m = 0.370 × 3.00 = **~1.11 USD per 1M tokens (assumed / illustrative)**.

## Note on Replica Fixed Cost

This formula captures **marginal** cost per token via `gpu_hours_per_1m` (which already reflects per-GPU throughput). It does **not** capture the fixed cost of holding a replica resident. On small per-GPU memory (e.g. 80 GB [[NVIDIA H100]]) a large MoE model needs many GPUs per replica ([[GPUs per Replica]]); if a replica is under-utilized, its fixed GPU-hours are spread over fewer tokens, raising effective cost/token. Larger-memory GPUs ([[AMD Instinct]] MI300X/MI325X) lower GPUs-per-replica and improve this. See [[Model Portfolio Capacity]] and [[Fleet Competitiveness]].

## See Also

- [[Operations Hub]]
- [[GPUs per Replica]]
