---
id: fml-gross-margin-per-model
type: formula
status: draft
owner: finops
domain: commercial
aliases: [gross margin per model, contribution margin, margin per model]
related: [fml-cost-per-1m-tokens, fml-revenue-per-gpu-hour, coeff-openrouter-price, coeff-cost-per-gpu-hour, ent-model, ent-model-deployment, wf-gpu-reallocation, idx-unit-economics]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Computes gross margin per model from revenue and cost per 1M tokens."
---

# Gross Margin per Model

## Purpose

Computes gross margin for a [[Model]] from its revenue and cost per 1M tokens. It is the contribution signal used to rank models during [[GPU Reallocation]] and to judge whether tokens should be produced at all.

## Definition

```
gross_margin = (revenue_per_1m − cost_per_1m) / revenue_per_1m
```

Where `revenue_per_1m = price_per_1m_tokens` (the OpenRouter price for the model).

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| revenue_per_1m | Coefficient (price) | [[OpenRouter Price]] | assumed |
| cost_per_1m | Derived | [[Cost per 1M Tokens]] | assumed |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| [[OpenRouter Price]] | coeff-openrouter-price | assumed |
| [[Cost per GPU-Hour]] | coeff-cost-per-gpu-hour | assumed |

## Consumed By

| Consumer | Type |
|----------|------|
| [[GPU Reallocation]] | CONSUMES |
| FinOps scorecard | CONSUMES |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMES | [[OpenRouter Price]] | → | `revenue_per_1m` = price per 1M tokens |
| CONSUMES | [[Cost per 1M Tokens]] | → | `cost_per_1m` input |
| DEPENDS_ON | [[Cost per GPU-Hour]] | → | Indirect, through Cost per 1M Tokens |
| DEPENDS_ON | [[Revenue per GPU-Hour]] | → | Same margin seen per GPU-hour; the per-1M definition uses OpenRouter Price directly |
| MEASURES | [[Model]] | → | Margin is computed per Model |
| CONSUMES | [[GPU Reallocation]] | ← | Marginal-contribution ranking |

## Worked Example

Illustrative only (assumed inputs — prices/costs are TBD placeholders, NOT measured):

- revenue_per_1m = 2.00 USD (assumed / illustrative)
- cost_per_1m = 1.11 USD (assumed / illustrative, from [[Cost per 1M Tokens]])

gross_margin = (2.00 − 1.11) / 2.00 = 0.89 / 2.00 = **~0.445, i.e. ~44.5% (assumed / illustrative)**.

## See Also

- [[Operations Hub]]
