---
id: fml-revenue-per-gpu-hour
type: formula
status: draft
owner: finops
domain: commercial
aliases: [revenue per gpu-hour, revenue/gpu-hour, gpu-hour yield]
related: [fml-tokens-per-gpu-second, fml-gross-margin-per-model, fml-cost-per-1m-tokens, coeff-openrouter-price, met-tokens-per-gpu-second, ent-model-deployment, ent-capacity-pool]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Computes revenue produced per GPU-hour from throughput and OpenRouter token price."
---

# Revenue per GPU-Hour

## Purpose

Computes the revenue a [[Model Deployment]] produces per GPU-hour, combining throughput with the OpenRouter token price. It is the yield signal that ranks pools during [[GPU Reallocation]] and [[Request Routing]].

## Definition

```
revenue_per_gpu_hour = (tokens_per_gpu_second × 3600 / 1e6) × price_per_1m_tokens
```

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| tokens_per_gpu_second | Derived | [[Tokens per GPU-Second]] | assumed |
| price_per_1m_tokens | Coefficient | [[OpenRouter Price]] | assumed |
| 3600 | Constant (seconds per hour) | — | validated |
| 1e6 | Constant (tokens per 1M) | — | validated |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| [[OpenRouter Price]] | coeff-openrouter-price | assumed |

## Consumed By

| Consumer | Type |
|----------|------|
| [[Gross Margin per Model]] | CONSUMES |
| [[GPU Reallocation]] | CONSUMES |
| [[Request Routing]] | CONSUMES |

## Worked Example

Illustrative only (assumed inputs — `price_per_1m_tokens` is a TBD placeholder):

- tokens_per_gpu_second = 750 (assumed / illustrative)
- price_per_1m_tokens = 2.00 USD/1M tokens (assumed / illustrative placeholder — NOT a measured value)

tokens_per_gpu_hour = 750 × 3600 = 2,700,000 → 2.7 (in millions)
revenue_per_gpu_hour = 2.7 × 2.00 = **~5.40 USD per GPU-hour (assumed / illustrative)**.

## See Also

- [[Operations Hub]]
