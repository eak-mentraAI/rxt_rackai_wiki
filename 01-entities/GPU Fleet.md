---
id: ent-gpu-fleet
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [gpu fleet, fleet, gpu inventory]
related: [ent-gpu-node, ent-gpu-cluster, ent-capacity-pool, ent-region, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: the aggregate of all GPU Nodes and Clusters Rack AI can allocate to inference."
---

# GPU Fleet

## Definition

The **GPU Fleet** is the aggregate of every [[GPU Node]] and [[GPU Cluster]] Rack AI can allocate to inference, across all [[Region]]s. It is the physical substrate of the platform — the pool of raw capacity that [[Capacity Pool]]s draw from and map onto [[Model Deployment]]s. Phase 0 of the roadmap ("Establish Ground Truth") is about knowing this fleet precisely: its inventory, telemetry, and cost economics.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → GPU Fleet → [[Topology]]**

The GPU Fleet is the physical layer that Capacity Pools allocate against. Consumers never reference the fleet directly.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Total GPU count | Count of GPUs across all clusters | int | derived |
| GPU generations | Mix of GPU types/generations (H100, A30, L40S; AMD Instinct incoming) | set | derived |
| Available capacity | GPU-hours available vs committed | struct | derived |
| Geographic spread | Regions the fleet spans | set | derived |
| Maintenance state | Fraction of fleet under maintenance | struct | derived |
| Committed capacity | Capacity currently mapped to pools/deployments | struct | derived |

## Lifecycle States

The fleet is not a lifecycle object; its capacity moves between committed, available, warm, and maintenance states, tracked per [[GPU Node]] and aggregated into [[Capacity Pool]]s.

## Current Composition (2026-09-03)

Ground truth is recorded in the [[Fleet Inventory]]. Summary:

| Environment ([[GPU Cluster]]) | GPUs |
|-------------------------------|------|
| SPOT | 20× [[NVIDIA H100]], 40× [[NVIDIA A30]] |
| RackAI — staging | 4× [[NVIDIA H100]], 6× [[NVIDIA L40S]] |
| RackAI — dev | some [[NVIDIA A30]] (count TBD) |
| Incoming (~Oct 2026) | [[AMD Instinct]] (class/qty TBD) |

No H200s are in the fleet; the current flagship is the [[NVIDIA H100]]. Engine/precision support per type is in the [[GPU Type Compatibility Matrix]].

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| COMPRISES | [[GPU Cluster]] | → | The fleet is the set of all clusters |
| COMPRISES | [[GPU Node]] | → | And all nodes within them |
| INCLUDES_TYPE | [[NVIDIA H100]] | → | Current flagship (SPOT + staging) |
| INCLUDES_TYPE | [[NVIDIA A30]] | → | High-count (SPOT + dev) |
| INCLUDES_TYPE | [[NVIDIA L40S]] | → | Staging |
| INCLUDES_TYPE | [[AMD Instinct]] | → | Incoming ~Oct 2026 (ROCm) |
| ALLOCATED_BY | [[Capacity Pool]] | ← | Pools map fleet capacity to deployments |
| SPANS | [[Region]] | → | Distributed across regions |
| MEASURED_BY | [[Productive GPU Utilization]] | ← | Utilization measured against fleet capacity |

## Graph Invariants

- The GPU Fleet is composed of GPU Clusters and GPU Nodes; it does not itself belong to any higher physical object.
- Commercial and capacity objects reference the fleet through Capacity Pools, never individual GPUs.

## Evidence

- Source: roadmap Phase 0 (fleet inventory, telemetry, cost model) and Phase 5 (dynamic fleet management).
- Confidence rationale: the fleet as a canonical layer is `validated` by the roadmap's Phase 0 mission; specific counts and available capacity are `derived` from live inventory/telemetry once Phase 0 completes.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Node]]
- [[Capacity Pool]]
