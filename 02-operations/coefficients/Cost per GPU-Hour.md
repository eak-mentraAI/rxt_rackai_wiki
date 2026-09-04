---
id: coeff-cost-per-gpu-hour
type: coefficient
status: draft
owner: finops
domain: capacity
aliases: [cost per gpu-hour, gpu-hour cost, internal gpu cost]
related: [fml-cost-per-1m-tokens, fml-gross-margin-per-model, met-gpu-utilization, ent-gpu-node, ent-capacity-pool]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Internal all-in cost to run one GPU for one hour: power, DC, depreciation, network, storage, licensing, ops."
---

# Cost per GPU-Hour

## Definition

The internal all-in cost to operate one GPU for one hour for a given hardware configuration. It aggregates power, datacenter allocation, hardware depreciation / lease economics, networking, storage, software/licensing, and operational overhead. It is the foundational cost coefficient behind cost/1M tokens, revenue/GPU-hour, and gross margin, established by roadmap Milestone 0.3.

## Value

| Value | Unit | Confidence | As Of |
|-------|------|:----------:|-------|
| TBD (per hardware config; placeholder range pending cost model) | USD / GPU-hour | assumed | 2026-09-03 |

## Evidence

- Benchmark run / source: roadmap Milestone 0.3 (Cost Model) — enumerates the cost components (power, DC allocation, depreciation/lease, networking, storage, licensing, ops overhead). No measured Rack AI figure exists yet; the source defines the method, not a value.
- Exit criterion to upgrade confidence: a completed Milestone 0.3 cost model producing a per-configuration all-in USD/GPU-hour, upgrading confidence from `assumed` to `derived` (and to `measured` once reconciled against actuals).

## Used By

| Formula | ID |
|---------|----|
| [[Cost per 1M Tokens]] | fml-cost-per-1m-tokens |
| [[Gross Margin per Model]] | fml-gross-margin-per-model |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Initial note; awaiting Milestone 0.3 cost model | — → assumed |

## See Also

- [[Operations Hub]]
