---
id: ent-capacity-pool
type: entity
status: draft
owner: finops
domain: capacity
aliases: [capacity pool, pool, gpu pool, capacity allocation]
related: [ent-gpu-node, ent-gpu-cluster, ent-model, ent-model-deployment, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a logical, software-controlled pool of GPU capacity assigned to a model or purpose."
---

# Capacity Pool

## Definition

A **Capacity Pool** is a logical, software-controlled pool of GPU capacity mapped onto [[GPU Node]]s and [[GPU Cluster]]s and assigned to a [[Model]] or a purpose. It is the abstraction that decouples deployments from raw hardware: a [[Model Deployment]] draws its capacity from exactly one pool, never from individual nodes directly. Pools include per-model pools (e.g., DeepSeek, GLM, Nemotron) plus purpose pools such as Launch/canary, Reserve, Warm, and Unallocated/spot.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → Capacity Pool → [[GPU Fleet]] → [[Topology]]**

The Capacity Pool is the software-controlled layer that maps deployments onto the physical GPU Fleet.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Pool identity | Stable pool identifier | string | validated |
| Purpose/assignment | Model or purpose the pool serves | enum | validated |
| Mapped capacity | Nodes/clusters and GPU capacity mapped into the pool | struct | validated |
| Committed capacity | Capacity committed to active deployments | struct | derived |
| Available capacity | Free capacity available for new/scaled deployments | struct | derived |
| Pool class | Per-model, Launch/canary, Reserve, Warm, or Unallocated/spot | enum | validated |
| Elasticity policy | Rules for expanding/contracting the pool | ref | derived |

## Pool Classes

| Class | Purpose | Notes |
|-------|---------|-------|
| Per-model (DeepSeek, GLM, Nemotron) | Dedicated capacity for a specific Model | One pool per priority model |
| Launch / canary | Capacity for new launches and canary traffic | Isolates launch risk |
| Reserve | Held-back capacity for burst and failover | Not routinely allocated |
| Warm | Pre-warmed capacity for fast scale-up | Reduces cold-start latency |
| Unallocated / spot | Idle or spot-eligible capacity | Reclaimable, lowest priority |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Defined | Pool created and mapped to capacity | Purpose assigned | Capacity activated |
| Active | Serving one or more deployments | Capacity mapped and healthy | Rebalanced or dissolved |
| Rebalancing | Capacity being shifted in/out | Demand or policy change | New allocation settled |
| Dissolved | Pool retired, capacity returned | Purpose ended | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| ALLOCATES | [[GPU Node]] | → | Maps node/cluster capacity into the pool |
| DRAWN_FROM_BY | [[Model Deployment]] | ← | Each deployment draws from exactly one pool (invariant) |
| ASSIGNED_TO | [[Model]] | → | Per-model pools are assigned to a Model |
| SPANS | [[GPU Cluster]] | → | Capacity may span clusters within the fleet |

## Graph Invariants

- Every Model Deployment draws from exactly one Capacity Pool.
- Commercial objects reference Capacity Pools and Models, never individual GPU nodes.

## Evidence

- Source: roadmap Milestone 5.1 / 5.6 (software-controlled capacity pools mapped to hardware; per-model and purpose pools).
- Confidence rationale: pool structure, classes, and the single-pool-per-deployment invariant are `validated` by the roadmap; committed/available capacity is `derived` from live allocation state.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Node]]
- [[Model Deployment]]
