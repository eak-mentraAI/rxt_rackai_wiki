---
id: ent-rackai-control-plane
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [rackai control plane, control plane, aggregated api]
related: [ent-organization, ent-model, ent-model-deployment, ent-accelerator-class, wf-identity-access, hub-entities]
source_docs: [rackai_api_reference, rackai_release_1_0_0, rackai_ui_architecture]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: the Kubernetes aggregated API and operators that reconcile RackAI CRDs."
---

# RackAI Control Plane

## Definition

The **RackAI Control Plane** is the Kubernetes aggregated API plus the operators that reconcile RackAI's custom resources (CRDs). It comprises `rackai-manager`, `organizer`, `apiserver`, and `frontproxy`. It exposes two API planes: the resource plane at `/apis/rackai.rackspace.com/v1alpha1` (models, deployments, datasets, jobs, adapters, accelerator classes) and the identity plane at `/apis/auth.rackai.io/v1`. The control plane governs every platform entity and owns the reconciliation loops that drive desired state to actual state.

## Layer

L1 — Entity Ontology. The control plane is the governing substrate beneath the whole serving chain:

**RackAI Control Plane ⟶ governs ⟶ [[Organization]] → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Accelerator Class]] → [[GPU Fleet]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Components | `rackai-manager`, `organizer`, `apiserver`, `frontproxy` | set | measured |
| Resource plane | `/apis/rackai.rackspace.com/v1alpha1` | string | measured |
| Identity plane | `/apis/auth.rackai.io/v1` | string | measured |
| CRD model | Objects follow metadata/spec/status/conditions | struct | measured |
| Reconciliation | Operators drive desired → actual state | process | measured |

## Lifecycle States

Not a stateful entity. (The control plane is infrastructure; its components are long-running services rather than a modeled lifecycle.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GOVERNS | [[Organization]] | → | Reconciles all org-scoped resources |
| GOVERNS | [[Model Deployment]] | → | Drives deployment desired state |
| GOVERNS | [[Accelerator Class]] | → | Reconciles cluster-scoped hardware inventory |
| OWNS | Reconciliation loops | → | Owns desired-state reconciliation |
| IMPLEMENTS | [[Identity & Access Control]] | → | Exposes the identity plane |

## Evidence

- Source: `rackai_api_reference`, `rackai_release_1_0_0`, `rackai_ui_architecture`.
- Confidence rationale: `measured` — component names, the two API plane paths, and CRD-based reconciliation are shipped in 1.0.0 and documented in the API reference.

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Organization]]
