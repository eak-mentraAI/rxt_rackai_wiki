---
id: ent-topology
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [topology, interconnect topology, fabric topology, numa topology]
related: [ent-gpu-node, ent-gpu-cluster, ent-model-deployment, ent-serving-runtime, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Canonical entity: the interconnect structure that constrains placement of performance-sensitive deployments."
---

# Topology

## Definition

A **Topology** is the interconnect structure of GPU capacity — NVLink and NVSwitch within a node, RDMA over InfiniBand or Ethernet across nodes, and NUMA boundaries on the host. It describes how tightly GPUs can communicate, which directly constrains where performance-sensitive [[Model Deployment]]s (tensor-parallel, expert-parallel, or multi-node) can be placed. Topology is the terminal layer of the abstraction chain: it bounds what the physical [[GPU Fleet]] can actually deliver — and on Rack AI's current fleet it is the **binding competitive constraint** (see [[Fleet Competitiveness]]).

## Coupling Classes (why this is the ceiling)

The number of GPUs that can act as **one tightly-coupled unit** sets the largest model a node can serve:

| Class | Coupling | Coupled group | Largest model band |
|-------|----------|---------------|--------------------|
| PCIe + NVLink pairs (fleet H100 NVL, AMD MI350P) | pairwise bridges | 2 coupled, 4/node | ~27B class |
| SXM + NVSwitch (H200, HGX) | full 8-GPU node | 8 coupled | frontier |
| UBB8 / full fabric (B300-class) | large fabric domain | 8+ coupled | frontier+ |

More GPUs of a PCIe class add capacity but do not enlarge the coupled group, so they do not raise the model-size ceiling. That only moves by delivering SXM or UBB8 topology.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → Topology**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Intra-node interconnect | NVLink / NVSwitch layout between GPUs in a node | struct | validated |
| Inter-node fabric | RDMA over InfiniBand or Ethernet across nodes | enum | validated |
| Fabric bandwidth | Achievable interconnect bandwidth | struct | measured |
| NUMA boundaries | Host NUMA domains affecting CPU/GPU affinity | struct | validated |
| Locality group | Set of GPUs that can be treated as tightly coupled | struct | derived |
| Placement constraints | Rules a deployment must satisfy given the topology | ref | derived |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Characterized | Interconnect measured and modeled | Cluster fabric wired | Model published |
| Active | Constraining live placement decisions | Model available to scheduler | Fabric changed |
| Revised | Re-characterized after fabric change | Hardware/fabric update | New model published |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSTRAINS | [[Model Deployment]] | → | Placement of performance-sensitive deployments |
| DESCRIBES | [[GPU Node]] | → | Intra-node NVLink/NVSwitch and NUMA layout |
| DESCRIBES | [[GPU Cluster]] | → | Inter-node fabric across the cluster |
| INFORMS | [[Serving Runtime]] | → | Parallelism config must respect topology |

## Graph Invariants

- Topology constrains placement but never exposes hardware to OpenRouter consumers.

## Evidence

- Source: roadmap Milestone 3.10 (topology-aware placement of performance-sensitive deployments).
- Confidence rationale: the interconnect structure and its role as a placement constraint are `validated` by the roadmap; bandwidth and locality figures are `measured`/`derived` from fabric characterization.

## See Also

- [[Entity Ontology Hub]]
- [[GPU Node]]
- [[Model Deployment]]
