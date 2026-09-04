---
id: ent-organization
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [organization, org, tenant, tenant workspace]
related: [ent-model-deployment, ent-dataset, ent-fine-tuning-job, ent-lora-adapter, ent-model, ent-registry-credential, wf-identity-access, hub-entities]
source_docs: [rackai_console_docs, rackai_api_reference, identity_access_spec]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: the tenant workspace that scopes all RackAI resources and maps to a Kubernetes namespace."
---

# Organization

## Definition

An **Organization** is the tenant workspace in RackAI. It is the top-level ownership boundary: every resource on the platform — models, deployments, datasets, fine-tuning jobs, adapters, and credentials — is org-scoped. Each Organization maps to a dedicated Kubernetes namespace, so tenancy isolation is enforced at the cluster level. Organizations are provisioned by Rackspace via Auth0 (there is no self-service signup path); a user is associated with one or more Organizations through the identity plane.

## Layer

L1 — Entity Ontology. The Organization is the ownership root of the serving chain:

**Organization → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Accelerator Class]] → [[GPU Fleet]] → [[Topology]]**

Consumers see Model endpoints scoped to their Organization; they never address GPU hardware directly.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Org ID | Stable identifier for the tenant | string | measured |
| Namespace | Kubernetes namespace the org maps to | string | measured |
| Display name | Human-readable organization name | string | measured |
| Members | Users associated via the identity plane | set | measured |
| Provisioning source | Created by Rackspace via Auth0 (no self-service) | enum | measured |

## Lifecycle States

Not a stateful entity. (Provisioning and deprovisioning are administrative operations, not modeled lifecycle states on the CRD.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| OWNS | [[Model Deployment]] | → | All deployments are org-scoped |
| OWNS | [[Dataset]] | → | Training data is org-scoped |
| OWNS | [[Fine-Tuning Job]] | → | Jobs run within the org namespace |
| OWNS | [[LoRA Adapter]] | → | Adapters are org-scoped |
| OWNS | [[Model]] | → | Model definitions are org-scoped |
| OWNS | [[Registry Credential]] | → | Credentials for pulling weights/images |
| GOVERNED_BY | [[Identity & Access Control]] | → | Auth, RBAC, and namespace scoping |
| MAPS_TO | Kubernetes namespace | → | One namespace per organization |

## Evidence

- Source: `rackai_console_docs`, `rackai_api_reference`, `identity_access_spec`.
- Confidence rationale: `measured` — org-as-namespace tenancy and Rackspace/Auth0 provisioning are shipped and documented in the console docs and API reference. Self-service signup is explicitly absent.

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Model Deployment]]
