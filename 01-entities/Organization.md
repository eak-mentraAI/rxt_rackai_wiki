---
id: ent-organization
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [organization, org, tenant, tenant workspace]
related: [ent-model-deployment, ent-dataset, ent-fine-tuning-job, ent-lora-adapter, ent-model, ent-registry-credential, wf-identity-access, hub-entities, wf-audit, wf-metering, ent-api-key, ent-rackai-control-plane, ent-market-demand, ent-agent-identity]
source_docs: [rackai_console_docs, rackai_api_reference, identity_access_spec, "06-sources/rackai-platform/Identity and Access Control Spec.md"]
confidence: measured
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: the tenant workspace, namespaced under a CustomerOrg, that maps to a Kubernetes namespace."
---

# Organization

## Definition

An **Organization** is the tenant workspace in RackAI. It is the tenant ownership boundary: every resource on the platform — models, deployments, datasets, fine-tuning jobs, adapters, and credentials — is org-scoped. Each Organization maps to a dedicated Kubernetes namespace, so tenancy isolation is enforced at the cluster level. Organizations are provisioned by Rackspace (there is no self-service signup path); a user is associated with one or more Organizations through the identity plane (per-realm Keycloak; Auth0 is the legacy provider being cut over — see [[Identity & Access Control]]).

**Parent tier — CustomerOrg (as built 2026-09-14, per [[Identity and Access Control Spec]]).** The scope hierarchy is four-tier: platform → **CustomerOrg** → Organization (tenant) → Project. The Organization CRD is *namespaced* in its owning CustomerOrg's namespace (`metadata.namespace` is the ownership record; the earlier `spec.orgRef` was removed). Because the tenant name derives the workload namespace and Keycloak realm, tenant names are **globally unique** across CustomerOrgs (webhook-enforced). Deleting a CustomerOrg **cascades** to each of its tenants (finalizers emit audit, deprovision realm and namespace), stamped with one deleter/request ID. Multiple CustomerOrgs per install are gated off by default (`rbac.multiOrg.enabled`).

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
| Provisioning source | Created by Rackspace (no self-service); identity via Keycloak, Auth0 legacy | enum | derived |
| Parent CustomerOrg | Owning CustomerOrg = the namespace the Organization CRD lives in | ref | derived |
| Name uniqueness | Tenant name globally unique across CustomerOrgs | constraint | derived |

## Lifecycle States

Not a stateful entity. (Provisioning and deprovisioning are administrative operations, not modeled lifecycle states on the CRD.) Deprovisioning also occurs by cascade when the parent CustomerOrg is deleted; a stuck tenant finalizer hangs the CustomerOrg, and force-removing it skips the audit event and leaks the realm.

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
| BELONGS_TO | CustomerOrg | → | Namespaced under its owning CustomerOrg (as built) |
| MAPS_TO | Kubernetes namespace | → | One namespace per organization |

## Evidence

- Source: `rackai_console_docs`, `rackai_api_reference`, `identity_access_spec`.
- Source (as built): [[Identity and Access Control Spec]] — CustomerOrg parent tier, global name uniqueness, cascade delete.
- Confidence rationale: `measured` — org-as-namespace tenancy and Rackspace provisioning are shipped and documented in the console docs and API reference. Self-service signup is explicitly absent. The CustomerOrg parent tier, name uniqueness and cascade delete are `derived` (engineering spec annotations, not console docs); the earlier "provisioned via Auth0" detail is superseded by the Keycloak cutover.

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Model Deployment]]
