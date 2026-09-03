---
id: ent-gpu-cluster
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [gpu cluster, cluster, gpu fleet segment]
related: [ent-gpu-node, ent-region, ent-topology, ent-capacity-pool, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a set of GPU Nodes with shared fabric and ownership within a datacenter."
---

# GPU Cluster

## Definition

A **GPU Cluster** is a set of [[GPU Node]]s that share a common fabric and ownership boundary within a single datacenter. It is the unit of physical aggregation between an individual node and the [[Region]] — the scope within which nodes are wired together for multi-node serving. Every GPU Node belongs to exactly one GPU Cluster.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A GPU Cluster groups nodes within the GPU Fleet and lives inside exactly one [[Region]].

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Cluster identity | Stable cluster identifier | string | validated |
| Region | The Region this cluster resides in | ref | validated |
| Node set | GPU Nodes that belong to the cluster | set | validated |
| Shared fabric | Common interconnect fabric across the cluster | ref | validated |
| Ownership boundary | Ownership/administrative domain | enum | validated |
| Aggregate capacity | Total GPU capacity across member nodes | struct | derived |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Building | Cluster being stood up | Nodes racked, fabric wiring | Fabric validated |
| Active | Serving allocations across member nodes | Bring-up complete | Draining begins |
| Draining | Migrating workloads off the cluster | Decommission or major service | Emptied |
| Retired | Decommissioned | Draining complete | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONTAINS | [[GPU Node]] | → | Set of member nodes; each node belongs to exactly one cluster |
| BELONGS_TO | [[Region]] | → | Resides in exactly one region |
| SHAPED_BY | [[Topology]] | → | Shared fabric defines the cluster's interconnect topology |
| ALLOCATED_TO | [[Capacity Pool]] | → | Cluster capacity mapped into pools |

## Graph Invariants

- Belongs to exactly one Region.
- Every member GPU Node belongs to exactly one GPU Cluster.

## Evidence

- Source: roadmap hardware topology (nodes grouped by shared fabric and ownership within a datacenter).
- Confidence rationale: cluster structure and its containment of nodes within a region are `validated` by the roadmap; aggregate capacity is `derived` from member-node inventory.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Node]]
- [[Region]]
