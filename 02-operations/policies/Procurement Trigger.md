---
id: pol-procurement-trigger
type: policy
status: draft
owner: finops
domain: capacity
aliases: [procurement trigger, capacity procurement policy, buy signal]
related: [pol-capacity-reservation, wf-gpu-reallocation, wf-autoscaling, evt-capacity-reallocation-triggered, met-gpu-utilization, fml-revenue-per-gpu-hour, ent-capacity-pool, ent-gpu-node]
source_docs: [openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
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

## Enforcement

Evaluated when [[Capacity Reallocation Triggered]] fires and reallocation cannot resolve a sustained shortfall; escalates a procurement recommendation to FinOps/Infrastructure. Confidence is `derived` because the specific thresholds follow from Phase 5 economics rather than being stated verbatim in the roadmap.

## See Also

- [[Governance Hub]]
