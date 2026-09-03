---
id: pol-capacity-reservation
type: policy
status: draft
owner: infrastructure
domain: capacity
aliases: [capacity reservation policy, warm pool policy, strategic reservation]
related: [wf-autoscaling, wf-gpu-reallocation, pol-procurement-trigger, met-gpu-utilization, ent-capacity-pool, ent-gpu-node]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-governance
summary: "Maintain a warm pool, never commit 100% of the fleet, and preserve strategic capacity reservations."
---

# Capacity Reservation Policy

## Purpose

Keep the fleet responsive to spikes, new-model launches, and failing deployments by never fully committing capacity, and preserve capacity for higher-value strategic workloads. (Roadmap Milestones 5.6 and 5.7.)

## Rule

A warm pool of rapidly reassignable capacity must be maintained at all times; the fleet is never 100% committed to production deployments. Strategic capacity reservations must be preserved even when short-term utilization or yield would favor reallocating them. Capacity-yield optimization maximizes productive utilization and gross contribution while maintaining performance SLOs and these reservations.

## Scope

Applies to every [[Capacity Pool]] and to fleet-level allocation across all [[GPU Node]]s, including launch/canary and reserve pools.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Autoscaling]] | CONSTRAINS → |
| [[GPU Reallocation]] | CONSTRAINS → |
| [[Capacity Pool]] | GOVERNS → |

## Enforcement

Enforced as a floor within [[Autoscaling]] (minimum warm capacity) and as a reservation constraint within [[GPU Reallocation]]. Sustained inability to hold the warm pool while meeting demand escalates to [[Procurement Trigger]].

## See Also

- [[Governance Hub]]
