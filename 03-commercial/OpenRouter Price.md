---
id: coeff-openrouter-price
type: coefficient
status: draft
owner: finops
domain: commercial
aliases: [openrouter price, list price, per-1m-token price, model price]
related: [hub-commercial, fml-revenue-per-gpu-hour, fml-gross-margin-per-model, idx-unit-economics, ent-model]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-commercial
summary: "The per-1M-token price Rack AI lists for a model on OpenRouter — the revenue side of unit economics."
---

# OpenRouter Price

## Definition

The **OpenRouter Price** is the per-1M-token price that Rack AI lists for a [[Model]] on OpenRouter. It is the revenue side of unit economics: multiplied by throughput it yields [[Revenue per GPU-Hour]], and compared against [[Cost per 1M Tokens]] it determines [[Gross Margin per Model]]. Prices are set per model, not per GPU.

## Value

| Value | Unit | Confidence | As Of |
|-------|------|:----------:|-------|
| TBD | USD / 1M tokens | assumed | TBD |

No Rack AI OpenRouter price has been published yet, so the value is a TBD placeholder rather than a measured figure.

## Evidence

- Source: OpenRouter provider documentation — providers supply pricing and capability metadata, and OpenRouter routes requests on price alongside latency, throughput, uptime, and quantization, with better-performing providers receiving proportionally more traffic ([openrouter.ai/providers/apply](https://openrouter.ai/providers/apply)). Roadmap Milestone 2.1 lists pricing as required provider-integration metadata, and Milestone 6.5 factors OpenRouter pricing into economic routing. Content was rephrased for compliance with licensing restrictions.
- Exit criterion to upgrade confidence: a published Rack AI OpenRouter price for a priority model plus an observed traffic response tying that price to routed volume.

## Used By

| Formula | ID |
|---------|----|
| [[Revenue per GPU-Hour]] | fml-revenue-per-gpu-hour |
| [[Gross Margin per Model]] | fml-gross-margin-per-model |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Coefficient created; no price published yet | — → assumed |

## See Also

- [[Commercial & Capacity Hub]]
