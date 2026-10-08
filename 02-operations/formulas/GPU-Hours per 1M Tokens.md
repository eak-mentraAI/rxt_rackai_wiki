---
id: fml-gpu-hours-per-1m-tokens
type: formula
status: draft
owner: finops
domain: capacity
aliases: [gpu-hours per 1m tokens, gpu hours per million tokens]
related: [fml-tokens-per-gpu-second, fml-cost-per-1m-tokens, met-tokens-per-gpu-second, coeff-cost-per-gpu-hour, ent-model-deployment, hub-inference-optimization, idx-gpu-capacity-demand-rationale, idx-unit-economics]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Converts tokens-per-GPU-second into the GPU-hours required to produce one million tokens."
---

# GPU-Hours per 1M Tokens

## Purpose

Converts efficiency ([[Tokens per GPU-Second]]) into the GPU-hours needed to produce one million tokens. This is the bridge between raw throughput and unit cost, feeding [[Cost per 1M Tokens]].

## Definition

```
gpu_hours_per_1m = 1e6 / (tokens_per_gpu_second × 3600)
```

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| tokens_per_gpu_second | Derived | [[Tokens per GPU-Second]] | assumed |
| 3600 | Constant (seconds per hour) | — | validated |
| 1e6 | Constant (tokens per 1M) | — | validated |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| (none directly — consumes throughput) | — | — |

## Consumed By

| Consumer | Type |
|----------|------|
| [[Cost per 1M Tokens]] | CONSUMES |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMES | [[Tokens per GPU-Second]] | → | `tokens_per_gpu_second` input |
| DEPENDS_ON | [[Tokens per GPU-Second Formula]] | → | Upstream formula that computes the input |
| CONSUMES | [[Cost per 1M Tokens]] | ← | Cost formula multiplies by cost per GPU-hour |
| CONSUMES | [[GPU Capacity Demand Rationale]] | ← | Capacity sizing |

## Worked Example

Illustrative only (assumed inputs):

- tokens_per_gpu_second = 750 (assumed / illustrative, from [[Tokens per GPU-Second Formula]])

gpu_hours_per_1m = 1,000,000 / (750 × 3600) = 1,000,000 / 2,700,000 ≈ **0.370 GPU-hours per 1M tokens (assumed / illustrative)**.

## See Also

- [[Operations Hub]]
