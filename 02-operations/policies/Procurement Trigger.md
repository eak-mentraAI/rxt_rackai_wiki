---
id: pol-procurement-trigger
type: policy
status: draft
owner: finops
domain: capacity
aliases: [procurement trigger, capacity procurement policy, buy signal]
related: [pol-capacity-reservation, wf-gpu-reallocation, wf-autoscaling, evt-capacity-reallocation-triggered, met-gpu-utilization, fml-revenue-per-gpu-hour, ent-capacity-pool, ent-gpu-node, evt-demand-forecast-published]
source_docs: [openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-10-08
parent: hub-governance
summary: "Conditions under which sustained high utilization and demand forecast trigger capacity procurement."
---

# Procurement Trigger

## Purpose

Define when sustained demand pressure should convert into buying more GPU capacity rather than continually reshuffling a fully committed fleet. Derived from the Phase 5 fleet economics. (Roadmap Phase 5.)

## Rule

When productive utilization is sustained near saturation, the warm-pool floor from [[Capacity Reservation Policy]] can no longer be held while meeting demand, and demand forecast plus revenue/GPU-hour justify the spend, a capacity-procurement recommendation must be raised. The trigger combines sustained [[Productive GPU Utilization]], forecast demand growth, and [[Revenue per GPU-Hour]] economics rather than any single instantaneous reading.

## Scope

Applies at fleet and [[Capacity Pool]] level, informed by demand forecasting at Model × cluster × time window.

## Governs

| Target | Relationship |
|--------|--------------|
| [[GPU Reallocation]] | CONSTRAINS → |
| [[Capacity Pool]] | GOVERNS → |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSTRAINS | [[GPU Reallocation]] | → | Sustained shortfall escalates beyond reshuffling |
| GOVERNS | [[Capacity Pool]] | → | Fleet and pool level |
| CONSUMES | [[Productive GPU Utilization]] | → | Sustained near-saturation |
| CONSUMES | [[Revenue per GPU-Hour]] | → | Spend justification |
| CONSUMES | [[Demand Forecast Published]] | → | Forecast demand growth |
| CONSUMES | [[Capacity Reallocation Triggered]] | → | Evaluated when the event fires |
| DEPENDS_ON | [[Capacity Reservation Policy]] | → | Warm-pool floor that can no longer be held |

## Enforcement

Evaluated when [[Capacity Reallocation Triggered]] fires and reallocation cannot resolve a sustained shortfall; escalates a procurement recommendation to FinOps/Infrastructure. Confidence is `derived` because the specific thresholds follow from Phase 5 economics rather than being stated verbatim in the roadmap.

## See Also

- [[Governance Hub]]
