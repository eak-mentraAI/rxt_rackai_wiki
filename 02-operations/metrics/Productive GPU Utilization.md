---
id: met-gpu-utilization
type: metric
status: draft
owner: infrastructure
domain: capacity
aliases: [productive gpu utilization, gpu utilization, hbm utilization, idle capacity]
related: [met-tokens-per-gpu-second, met-availability, wf-autoscaling, wf-gpu-reallocation, pol-procurement-trigger, ent-capacity-pool, ent-gpu-node, hub-inference-optimization, ent-gpu-fleet, evt-capacity-reallocation-triggered, asm-openrouter-initial-share, asm-traffic-follows-performance, met-output-throughput, coeff-cost-per-gpu-hour, pol-capacity-reservation, evd-kpi-telemetry-targets]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Productive inference GPU-hours over available GPU-hours; also HBM utilization and idle capacity %."
---

# Productive GPU Utilization

## Definition

Measures how effectively available GPU capacity is producing useful inference work — productive inference GPU-hours divided by available GPU-hours. It answers whether we are actually monetizing the fleet. Supporting measures include HBM utilization and idle capacity %, tracked by model and cluster across each [[Capacity Pool]] and [[GPU Node]].

## KPI Job

Serves internal operating decisions (feeds autoscaling, GPU reallocation, and the procurement trigger) and commercial/strategic positioning (fleet monetization) — jobs 1 and 3/4 per [[KPI Telemetry Target List]]. Raw GPU counters likely exist; the open question is reaching model/pool grain, whether from the producer or a downstream join to deployment metadata.

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

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Capacity Pool]] | → | Per pool |
| MEASURES | [[GPU Fleet]] | → | Against fleet capacity |
| DEPENDS_ON | [[Autoscaling]] | ← | Scaling signal |
| DEPENDS_ON | [[GPU Reallocation]] | ← | Utilization signal |
| CONSUMES | [[Procurement Trigger]] | ← | Sustained near-saturation input |
| GENERATES | [[Capacity Reallocation Triggered]] | → | Utilization crossing a threshold can fire the event |
| CONSTRAINS | [[OpenRouter Initial Market Share]] | ← | Low launch share limits utilization |
| SUPPORTS | [[OpenRouter Traffic Follows Performance]] | ← | Better performance → more routed traffic |

## Evidence

- Confidence rationale: `assumed` — direction (↑) is roadmap-mandated (KPI #1), but no measured Rack AI utilization exists yet. Feeds [[Autoscaling]], [[GPU Reallocation]], and [[Procurement Trigger]].

## See Also

- [[Operations Hub]]
