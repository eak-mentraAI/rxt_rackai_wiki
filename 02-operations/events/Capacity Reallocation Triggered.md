---
id: evt-capacity-reallocation-triggered
type: event
status: draft
owner: infrastructure
domain: capacity
aliases: [capacity reallocation triggered, reallocation signal, rebalance trigger]
related: [wf-gpu-reallocation, wf-autoscaling, wf-admission-control, pol-procurement-trigger, met-gpu-utilization, fml-revenue-per-gpu-hour, ent-capacity-pool, ent-gpu-node, wf-request-routing]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Signals that demand or economics crossed a threshold warranting GPU capacity reallocation."
---

# Capacity Reallocation Triggered

## Definition

Signals that demand or economics have crossed a reallocation threshold, warranting movement of GPU capacity among model [[Capacity Pool]]s. The event drives [[GPU Reallocation]] and may follow sustained [[Autoscaling]] or [[Admission Control]] pressure. (Roadmap Milestone 5.5.)

## Payload

| Field | Type | Description |
|-------|------|-------------|
| source_pool | ref | Pool with excess or low-yield capacity |
| target_pool | ref | Pool needing capacity |
| trigger_signal | enum | demand / utilization / queue-depth / revenue-per-gpu-hour / marginal-contribution / strategic-priority |
| observed_value | float | Signal value that crossed the threshold |
| threshold | float | Configured reallocation threshold |
| triggered_at | timestamp | When the threshold was crossed |

## Emitted By

| Source | Workflow | Condition |
|--------|----------|-----------|
| Capacity monitor | [[GPU Reallocation]] | Demand/economics cross a reallocation threshold |
| Scaling evaluator | [[Autoscaling]] | Scaling need exceeds pool headroom |
| Admission monitor | [[Admission Control]] | Sustained shedding indicates capacity shortfall |

## Consumed By

| Consumer | Action Taken |
|----------|--------------|
| [[GPU Reallocation]] | Recommends or executes a GPU move between pools |
| [[Procurement Trigger]] | Escalates to procurement if shortfall is sustained |
| Capacity dashboards | Records the reallocation signal |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GENERATES | [[GPU Reallocation]] | ← | Capacity monitor threshold |
| GENERATES | [[Autoscaling]] | ← | Scaling need exceeds pool headroom |
| GENERATES | [[Admission Control]] | ← | Sustained shedding |
| GENERATES | [[Request Routing]] | ← | Routing pressure indicates systemic imbalance |
| GENERATES | [[Productive GPU Utilization]] | ← | `trigger_signal` = utilization |
| GENERATES | [[Revenue per GPU-Hour]] | ← | `trigger_signal` = revenue-per-gpu-hour |
| CONSUMES | [[GPU Reallocation]] | ← | Recommends or executes a GPU move |
| CONSUMES | [[Procurement Trigger]] | ← | Escalates sustained shortfall |
| DEPENDS_ON | [[Capacity Pool]] | → | `source_pool` / `target_pool` |

## See Also

- [[Operations Hub]]
