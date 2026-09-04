---
id: ent-accelerator-class
type: entity
status: draft
owner: infra-eng
domain: infrastructure
aliases: [accelerator class, accelerator, gpu class]
related: [ent-model-deployment, ent-gpu-node, ent-serving-runtime, ent-gpu-fleet, hub-entities]
source_docs: [accelerator_selection_spec, rackai_release_1_0_0]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a cluster-scoped abstraction that selects GPU hardware for a deployment."
---

# Accelerator Class

## Definition

An **Accelerator Class** is a cluster-scoped abstraction that selects GPU hardware for a [[Model Deployment]]. It captures vendor selection (`nvidia` or `amd`), node affinity, and resource sizing, and it maintains an automated inventory of allocatable versus used capacity. It shipped in 1.0.0. The Accelerator Class is the layer that binds a deployment's runtime to concrete GPU nodes — consumers never address GPU hardware directly.

## Layer

L1 — Entity Ontology. Position in the abstraction chain, between the Serving Runtime and the GPU Fleet:

**[[Model Deployment]] → [[Serving Runtime]] → Accelerator Class → [[GPU Node]] → [[GPU Fleet]] → [[Topology]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Class ID | Stable identifier | string | measured |
| Vendor | `nvidia` or `amd` | enum | measured |
| Node affinity | Scheduling affinity to target nodes | struct | measured |
| Resource sizing | GPU count/resource request per unit | struct | measured |
| Allocatable capacity | Automated inventory of available capacity | int | measured |
| Used capacity | Automated inventory of consumed capacity | int | measured |
| Scope | Cluster-scoped | enum | measured |

## Lifecycle States

Not a stateful entity. (Allocatable/used capacity are continuously reconciled inventory counters, not a modeled lifecycle.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| USED_BY | [[Model Deployment]] | ← | A deployment selects an accelerator class |
| MAPS_TO | [[GPU Node]] | → | Resolves to concrete GPU nodes |
| DEPENDS_ON | [[Serving Runtime]] | ← | Runtime hardware stack bounds vendor choice |

## Evidence

- Source: `accelerator_selection_spec`, `rackai_release_1_0_0`.
- Confidence rationale: `measured` — cluster-scoped abstraction, vendor selection (`nvidia`/`amd`), affinity/sizing, and automated allocatable/used inventory shipped in 1.0.0.

## See Also

- [[Entity Ontology Hub]]
- [[Model Deployment]]
- [[GPU Node]]
