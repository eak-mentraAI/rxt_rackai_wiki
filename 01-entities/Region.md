---
id: ent-region
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [region, geography, datacenter region, location]
related: [ent-gpu-node, ent-gpu-cluster, ent-topology, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: a datacenter geography that a GPU Node belongs to exactly once."
---

# Region

## Definition

A **Region** is a datacenter geography — a bounded physical location in which GPU capacity resides. It is the coarsest physical grouping in the fleet: every [[GPU Node]] belongs to exactly one Region, and every [[GPU Cluster]] resides within one. Regions carry latency, data-residency, and availability characteristics that inform placement and routing decisions.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A Region bounds the physical GPU Fleet — clusters and nodes live inside exactly one Region.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Region identity | Stable region identifier/name | string | validated |
| Geography | Physical location / jurisdiction | string | validated |
| Datacenter(s) | Datacenter facilities within the region | set | measured |
| Data residency | Applicable data-residency constraints | enum | derived |
| Latency profile | Baseline network latency characteristics | struct | measured |
| Availability posture | Redundancy / availability characteristics | enum | derived |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Planned | Region identified for expansion | Demand or strategy driven | Capacity installed |
| Active | Serving live capacity | Clusters online | Draining begins |
| Draining | Capacity being migrated out | Decommission decision | Emptied |
| Retired | Region decommissioned | Draining complete | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONTAINS | [[GPU Cluster]] | → | Clusters reside within the region |
| CONTAINS | [[GPU Node]] | → | Each node belongs to exactly one region (invariant) |
| CONSTRAINS | [[Model Deployment]] | → | Residency/latency constrain placement |

## Graph Invariants

- Every GPU Node belongs to exactly one Region.
- Every GPU Cluster resides within exactly one Region.

## Evidence

- Source: roadmap hardware topology (nodes and clusters bounded by datacenter geography).
- Confidence rationale: the region grouping and the one-region-per-node invariant are `validated` by the roadmap; latency and residency attributes are `measured`/`derived` from operational data.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Node]]
- [[GPU Cluster]]
