---
id: idx-fleet-yield
type: index
status: draft
owner: finops
domain: capacity
aliases: [fleet yield optimization, capacity yield optimization, yield management, fleet economics]
related: [hub-commercial, wf-demand-forecasting, idx-capacity-pools, fml-revenue-per-gpu-hour, ent-capacity-pool]
source_docs: [openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-commercial
summary: "Fleet yield objective: maximize productive utilization and gross contribution within SLOs and reservations."
---

# Fleet Yield Optimization

## Purpose

This index frames the fleet optimization objective from roadmap Milestone 5.7 and links the workflows, metrics, and policies that implement it. It is a synthesis note; it links to canonical homes rather than redefining them.

The objective, approximately:

> Maximize productive GPU utilization and gross contribution while maintaining performance SLOs and strategic capacity reservations.

The scheduler moves from a binary view of capacity (GPU available / unavailable) toward one that understands **utilization + performance + economics** together. This makes it a yield-management layer over the fleet — the same idea the roadmap extends in Milestone 6.5 (economic routing), where real-time economics feed scheduling. Yield reasoning operates over [[Model]]s and [[Capacity Pool]]s, never individual GPUs.

## Objective Dimensions

- Productive utilization — measured by [[Productive GPU Utilization]].
- Gross contribution — ranked using [[Revenue per GPU-Hour]].
- Performance SLOs — latency/availability guardrails the scheduler must respect.
- Strategic reservations — capacity held under the [[Capacity Reservation Policy]].

## Entries

| Item | ID | Type | Confidence |
|------|----|------|:----------:|
| [[Closed-Loop Optimization]] | wf-closed-loop-optimization | workflow | derived |
| [[GPU Reallocation]] | wf-gpu-reallocation | workflow | derived |
| [[Productive GPU Utilization]] | met-productive-gpu-utilization | metric | derived |
| [[Revenue per GPU-Hour]] | fml-revenue-per-gpu-hour | formula | assumed |
| [[Capacity Reservation Policy]] | pol-capacity-reservation | policy | derived |
| [[Procurement Trigger]] | pol-procurement-trigger | policy | derived |

## See Also

- [[Demand Forecasting]]
- [[Capacity Pool Model]]
- [[Commercial & Capacity Hub]]
