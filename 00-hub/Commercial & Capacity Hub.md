---
id: hub-commercial
type: hub
status: draft
owner: finops
domain: commercial
aliases: [commercial hub, capacity hub, L3 hub, economics hub]
related: [hub-root, hub-operations, hub-evidence]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Layer 3 navigation hub for unit economics, capacity allocation, and forecasting."
---

# Commercial & Capacity Hub

Layer 3 — how demand maps to capacity and economics. Unit economics, metering and [[Billing & Payment]], pricing (OpenRouter and direct), capacity pools and dynamic allocation, demand forecasting, and fleet yield optimization. OpenRouter is one pricing channel among the platform's commercial surfaces.

## Unit Economics

The [[Unit Economics Model]] ties the loop together. Underlying formulas and coefficients:

| Concept | ID |
|---------|----|
| [[Cost per 1M Tokens]] | fml-cost-per-1m-tokens |
| [[GPU-Hours per 1M Tokens]] | fml-gpu-hours-per-1m-tokens |
| [[Revenue per GPU-Hour]] | fml-revenue-per-gpu-hour |
| [[Gross Margin per Model]] | fml-gross-margin-per-model |
| [[Cost per GPU-Hour]] | coeff-cost-per-gpu-hour |
| [[OpenRouter Price]] | coeff-openrouter-price |

## Capacity & Allocation

| Concept | ID |
|---------|----|
| [[Capacity Pool]] | ent-capacity-pool |
| [[Capacity Pool Model]] | idx-capacity-pools |
| [[Model Portfolio Capacity]] | idx-model-portfolio |
| [[Demand Forecasting]] | wf-demand-forecasting |
| [[Fleet Yield Optimization]] | idx-fleet-yield |
| [[GPU Reallocation]] | wf-gpu-reallocation |
| [[Capacity Reservation Policy]] | pol-capacity-reservation |
| [[Procurement Trigger]] | pol-procurement-trigger |

## Fleet Reality

- [[Fleet Inventory]] — ground truth (H100/A30/L40S; AMD incoming)
- [[Fleet Competitiveness]] — the size + quantity competitive gap
- [[GPUs per Replica]] — replica sizing that gates how many models fit

## Related Hubs

- [[Operations Hub]]
- [[Evidence Hub]]
