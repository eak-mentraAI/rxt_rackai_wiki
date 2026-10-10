---
id: ent-authority-context
type: entity
status: draft
owner: governance
domain: governance
aliases: [authority context, authority principal, acting principal, represented customer, delegation chain]
related: [ent-agent-identity, pol-action-controls, ent-organization, ent-api-key, wf-identity-access, prd-governed-execution-authority, spec-governed-execution-authority, prd-workload-declaration-placement, prd-sovereign-isolation-assurance, prd-concierge-engineer, prd-customer-observability-evidence, hub-entities]
source_docs: ["05-wiki/Governed Execution & Delegated Authority PRD.md", "05-wiki/Governed Execution & Delegated Authority Tech Spec.md", "Product-owner review disposition 2026-10-10 (S-2, X-1)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: who is acting, for which customer, in which scope, on whose delegated authority, for which action."
---

# Authority Context

## Definition

An **Authority Context** is the single structure that says, for one action instance: **who is acting**, **which customer they act for**, **in which tenant scope**, **through which chain of delegation**, **on what authorisation basis**, and **until when**. It is produced by C ([[Governed Execution & Delegated Authority PRD]]) and travels with every governed action, decision and evidence record. Downstream capabilities consume it as given and never reconstruct it from headers, namespaces or installation layout.

> **Assumed confidence.** Proposed in PRD C v0.2 (product-owner review disposition 2026-10-10, ruling S-2). Nothing is built. Today's code carries only an identity and a tenant namespace (`X-RackAI-*` headers; [[Identity & Access Control]]).

## Layer

L1 — Entity Ontology. A governance entity, peer to [[Agent Identity]] (which it instantiates for one action) and scoped within an [[Organization]]. It sits beside the serving chain, not in it: every action on a [[Model Deployment]] or its declaration carries one.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Acting principal | The authenticated identity performing the action: user, operator, service, system controller, or agent (Phase 2). `{type, id, identityProvider}` | struct | assumed |
| Represented customer (authority principal) | The customer whose authority the action is exercised under: an Organization, or a CustomerOrg only when that CustomerOrg carries the validated single-customer attribute. Never the installation | ref | assumed |
| Tenant scope | `{customerOrg, organization, project}` the action applies to | struct | assumed |
| Delegation chain | Ordered grants from the authority principal to the acting principal (empty when acting on direct permission); `onBehalfOf` for agents | list | assumed |
| Action instance | `{actionId, class, subject {kind, uid, generation}, digest}` from C's action catalogue | struct | assumed |
| Authorisation basis | What made it authorised: a role binding, a grant, an authorisation reference, or a catalogued platform-safety or emergency path; plus whether separation of duties was met or a recorded exception applied | struct | assumed |
| Expiry | When the authority stops: the earliest of the authorisation's, grant's and credential's expiry | time | assumed |
| Attribution | `attributed`, `system`, `principal-not-captured` or `unknown-authority-source`. The last two are audit coverage gaps, never actors | enum | assumed |

## Invariant

*No customer can create, approve, weaken or inherit authority over another customer's workload through a shared parent.* The installation is never automatically a customer authority boundary.

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Resolved | Built by C for one request or decision | Authentication plus catalogue lookup | Used or expired |
| Authorised | Carries a valid basis for its action instance | `Decide` returns authorised | Consumed, expired or invalidated |
| Consumed | Used by the enforcing capability for one decision | `Consume` succeeds | Terminal (kept for audit) |
| Expired / Invalid | Basis lapsed or was withdrawn | Expiry passed, or grant/binding removed | Terminal |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| IMPLEMENTS | [[Agent Identity]] | → | One action's instance of identity plus delegated authority |
| BELONGS_TO | [[Organization]] | → | Scoped to one tenant; CustomerOrg only when single-customer |
| USES | [[API Key]] | → | A key may carry the credential; authority still comes from the chain |
| CONSTRAINS | [[Action Controls]] | → | Gating decisions read the context |

## Evidence

- Source: [[Governed Execution & Delegated Authority Tech Spec]] §4.5 (`Decide`, `Consume` and `For*` take and return it).
- Confidence rationale: `assumed`, a proposed design under product review.

## See Also

- [[Entity Ontology Hub]]
- [[Agent Identity]]
- [[Governed Execution & Delegated Authority PRD]]
