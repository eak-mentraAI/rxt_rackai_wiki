---
id: ent-agent-identity
type: entity
status: draft
owner: governance
domain: governance
aliases: [agent identity, delegated authority, agent identity and delegated authority, scoped tokens, service identity]
related: [ent-organization, ent-api-key, ent-governed-harness, wf-identity-access, pol-action-controls, wf-perimeter-info-flow, hub-entities, src-rackai-dev-plan, hub-ai-governance-assurance, hub-ai-harness]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-entities
summary: "Canonical entity: the identity an agent acts under and the delegated, task-scoped authority it carries per run."
---

# Agent Identity

## Definition

An **Agent Identity** is the identity an agent acts under, together with the **delegated authority** it carries. Unlike a person — who has a stable identity and a role — an agent acts *on behalf of* a user, often several hops deep, spawns sub-agents, and calls tools with borrowed credentials. At each step the system must know **who is acting** and **whose authority they carry**, with permissions scoped down to the task rather than inherited whole.

This sits **upstream** of agentic security and information-flow control: you cannot authorize by intent ([[Perimeter Information-Flow Control]]) or gate outbound actions ([[Action Controls]]) until you know the acting identity.

> **Assumed confidence.** Program 2 thread 2.5. The baseline (service identities, scoped tokens, tenant isolation) is a near-term build consuming [[Identity & Access Control]] where it exists (`~R/U` today); delegation-to-sub-agents and intent-scoped authority are long-term research.

## Layer

L1 — Entity Ontology. A tenancy/identity entity, peer to [[Organization]] and [[API Key]], scoped within an Organization.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Acting identity | Who is acting at this step | ref | assumed |
| Delegation chain | Whose authority is carried, across hops | struct | assumed |
| Scope | Permissions scoped to the task, not inherited whole | struct | assumed |
| Revocation | Authority revoked when the task ends | policy | assumed |
| Attribution | After-the-fact proof of which identity did what | record | assumed |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| BELONGS_TO | [[Organization]] | → | Scoped within a tenant |
| USES | [[API Key]] | → | Scoped tokens/credentials |
| IMPLEMENTS | [[Identity & Access Control]] | → | Consumes baseline IAM where it exists |
| CONSTRAINS | [[Action Controls]] | → | Authorization by identity is upstream of blast-radius gating |
| CONSTRAINS | [[Perimeter Information-Flow Control]] | → | Data-flow control depends on knowing the actor |
| USED_BY | [[Governed Harness]] | ← | The harness acts under a scoped identity |

## Evidence

- Source: dev plan Program 2 thread 2.5 (operations plane; the one genuine research thread in operations).
- Confidence rationale: `assumed` — baseline is a near-term build on existing IAM; the delegation/intent-scope research is open.

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Action Controls]]
- [[Perimeter Information-Flow Control]]
