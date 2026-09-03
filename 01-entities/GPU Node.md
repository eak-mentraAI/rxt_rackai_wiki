---
id: ent-gpu-node
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [gpu node, node, gpu host, server]
related: [ent-gpu-cluster, ent-region, ent-topology, ent-capacity-pool, ent-model-deployment, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a physical host of GPUs belonging to one cluster and one region."
---

# GPU Node

## Definition

A **GPU Node** is a physical host containing one or more GPUs, together with its host CPU, memory, interconnect, network, storage, and power envelope. It is the lowest-level physical unit on which a [[Model Deployment]] is placed. A GPU Node belongs to exactly one [[GPU Cluster]] and exactly one [[Region]]. Nodes are aggregated into logical [[Capacity Pool]]s; consumers never address a node directly.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A GPU Node is a member of the GPU Fleet, grouped by [[GPU Cluster]] and bounded by [[Region]] and [[Topology]].

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| GPU type/generation | GPU model and generation (e.g., [[NVIDIA H100]]) | enum | validated |
| GPU count | Number of GPUs in the node | int | validated |
| GPU memory | Per-GPU memory and bandwidth (e.g., H100 = 80GB HBM3 @ ~3.35 TB/s) | struct | validated |
| Host CPU | Host processor configuration | struct | measured |
| Host RAM | Host system memory | int | measured |
| NVLink/NVSwitch topology | Intra-node GPU interconnect layout | struct | validated |
| Network fabric | Inter-node fabric (RDMA, InfiniBand/Ethernet) | enum | validated |
| Storage | Local/attached storage for weights and cache | struct | measured |
| Power envelope | Power draw / thermal budget | struct | measured |
| Committed capacity | Capacity committed to pools/deployments | struct | derived |
| Available capacity | Free capacity available for allocation | struct | derived |
| Maintenance state | Operational/maintenance status of the node | enum | measured |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Provisioning | Node being racked and brought online | Hardware installed | Health checks pass |
| Available | Healthy and eligible for allocation | Passes bring-up | Allocated or drained |
| Allocated | Committed to a Capacity Pool / deployment | Assigned capacity | Released |
| Maintenance | Drained for service or repair | Fault or scheduled work | Returned to Available |
| Retired | Decommissioned | End of life or removal | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| BELONGS_TO | [[GPU Cluster]] | → | Exactly one cluster (invariant) |
| BELONGS_TO | [[Region]] | → | Exactly one region (invariant) |
| CONSTRAINED_BY | [[Topology]] | → | Interconnect and NUMA constrain placement |
| ALLOCATED_TO | [[Capacity Pool]] | → | Node capacity mapped into pools |
| HOSTS | [[Model Deployment]] | ← | Deployments placed on one or more nodes |

## Graph Invariants

- Belongs to exactly one GPU Cluster.
- Belongs to exactly one Region.
- Exposed to consumers only through Capacity Pools and Model endpoints, never directly.

## Evidence

- Source: roadmap Milestone 0.1 (hardware inventory attributes: GPU type/generation, count, memory, host CPU/RAM, interconnect topology, fabric, storage, power, committed vs available capacity, maintenance state).
- Confidence rationale: node structure and mandatory relationships are `validated` by the roadmap; per-node runtime values (capacity, maintenance) are `measured`/`derived` from inventory telemetry. Fleet GPU types are catalogued in the [[Fleet Inventory]] — currently [[NVIDIA H100]], [[NVIDIA A30]], and [[NVIDIA L40S]], with [[AMD Instinct]] incoming. No H200s are in the fleet.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Cluster]]
- [[Topology]]
