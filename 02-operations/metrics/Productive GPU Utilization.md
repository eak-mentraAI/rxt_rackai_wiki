---
id: met-gpu-utilization
type: metric
status: draft
owner: infrastructure
domain: capacity
aliases: [productive gpu utilization, gpu utilization, hbm utilization, idle capacity]
related: [met-tokens-per-gpu-second, met-availability, wf-autoscaling, wf-gpu-reallocation, pol-procurement-trigger, ent-capacity-pool, ent-gpu-node]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Productive inference GPU-hours over available GPU-hours; also HBM utilization and idle capacity %."
---

# Productive GPU Utilization

## Definition

Measures how effectively available GPU capacity is producing useful inference work — productive inference GPU-hours divided by available GPU-hours. It answers whether we are actually monetizing the fleet. Supporting measures include HBM utilization and idle capacity %, tracked by model and cluster across each [[Capacity Pool]] and [[GPU Node]].

## Unit

ratio / percentage (productive GPU-hours ÷ available GPU-hours). Supporting: HBM utilization %, idle capacity %.

## Source or Formula

- Measured from: GPU telemetry (GPU-hours available vs consumed, HBM utilization) per cluster and pool.
- Not a single formula — an aggregation of telemetry counters.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | Maximize productive utilization (no measured baseline yet) | Without degrading [[TTFT]] or [[Availability]] |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Capacity Pool]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — direction (↑) is roadmap-mandated (KPI #1), but no measured Rack AI utilization exists yet. Feeds [[Autoscaling]], [[GPU Reallocation]], and [[Procurement Trigger]].

## See Also

- [[Operations Hub]]
