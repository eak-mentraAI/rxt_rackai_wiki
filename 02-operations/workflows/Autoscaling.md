---
id: wf-autoscaling
type: workflow
status: draft
owner: infrastructure
domain: capacity
aliases: [autoscaling, replica scaling, elastic capacity]
related: [wf-gpu-reallocation, wf-admission-control, pol-capacity-reservation, met-gpu-utilization, met-ttft, ent-model-deployment, ent-capacity-pool, ent-gpu-node, ent-topology]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Add or remove serving replicas while respecting load time, topology, warm capacity, and latency SLO."
---

# Autoscaling

## Purpose

Automatically add or remove serving replicas or capacity for a [[Model Deployment]] to track demand, without violating latency SLOs or the minimum warm-capacity floor. (Roadmap Milestone 5.3.)

## Trigger

- Demand forecast or live utilization/queue-depth signal crosses a scale threshold.
- [[Capacity Reallocation Triggered]] delegating replica adjustment.

## State Machine

```mermaid
stateDiagram-v2
    [*] --> Steady
    Steady --> ScaleOut: demand rising, SLO at risk
    Steady --> ScaleIn: demand falling, headroom high
    ScaleOut --> Warming: replica requested
    Warming --> Steady: weights transferred, replica warm
    ScaleIn --> Draining: replica selected for removal
    Draining --> Steady: in-flight complete, capacity released
    ScaleOut --> Steady: GPU unavailable, hold
```

## Steps

1. Evaluate — capacity/infrastructure; read demand signals against [[Productive GPU Utilization]] and [[TTFT]] SLO.
2. Scale-out decision — respect model load time, weight transfer time, [[Topology]], and GPU availability before requesting a replica from the [[Capacity Pool]].
3. Warming — infrastructure; new replica loads weights and passes health checks before receiving traffic.
4. Scale-in decision — remove replicas only while preserving minimum warm capacity and the latency SLO.
5. Draining — infrastructure; selected replica finishes in-flight requests, then releases [[GPU Node]] capacity.

Constraints respected: **model load time, weight transfer time, topology, GPU availability, minimum warm capacity, latency SLO**. The warm-capacity floor is set by [[Capacity Reservation Policy]].

## Events Emitted

| Event | When | Consumers |
|-------|------|-----------|
| [[Capacity Reallocation Triggered]] | Scaling need exceeds pool headroom | [[GPU Reallocation]], capacity |

## Dependencies

| Depends On | Type | Notes |
|------------|------|-------|
| [[Capacity Reservation Policy]] | CONSTRAINED_BY | Minimum warm capacity floor |
| [[Productive GPU Utilization]] | DEPENDS_ON | Scaling signal |
| [[TTFT]] | CONSTRAINED_BY | Latency SLO guardrail |
| [[Topology]] | CONSTRAINED_BY | Placement of new replicas |

## Ownership

GPU / Infrastructure Engineering owns replica scaling; Capacity/FinOps informs thresholds.

## See Also

- [[Operations Hub]]
