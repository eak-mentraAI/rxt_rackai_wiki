---
id: ent-api-key
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [api key, api credential, programmatic credential]
related: [ent-organization, wf-identity-access, ent-openrouter-private-model, hub-entities]
source_docs: [identity_access_spec]
confidence: assumed
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Planned entity: a programmatic credential for calling RackAI APIs and inference endpoints."
---

# API Key

## Definition

An **API Key** is a programmatic credential for calling RackAI's APIs and inference endpoints. It is part of the Identity/Access workstream and is the primary dependency for the OpenRouter Private Model path (which needs a stable, org-scoped credential to authenticate provider-routed traffic). **Status: planned** — API keys are described in the identity/access spec but are not confirmed shipped, so this entity carries `assumed` confidence.

## Layer

L1 — Entity Ontology. The API Key authenticates an Organization's programmatic access to Model endpoints:

**Consumer → API Key → [[Identity & Access Control]] → [[Organization]] → [[Model Deployment]] endpoint**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Key ID | Stable identifier | string | assumed |
| Scope | Org-scoped access to APIs/inference | enum | assumed |
| Secret material | The token used to authenticate | ref | assumed |
| Status | Planned — not confirmed shipped | enum | assumed |

## Lifecycle States

Not a stateful entity. (Planned; issuance/rotation/revocation lifecycle is not yet specified as shipped.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| AUTHENTICATES | [[Organization]] | → | Grants org-scoped programmatic access |
| DEPENDS_ON | [[Identity & Access Control]] | → | Issued/validated by the identity workstream |
| REQUIRED_BY | [[OpenRouter Private Model Integration]] | ← | Primary dependency for the private-model path |

## Evidence

- Source: `identity_access_spec`.
- Confidence rationale: `assumed` — API keys appear in the identity/access spec (PRD) but are not confirmed shipped. Planned capability carries `assumed` confidence and must not be asserted as present. Whether API keys ship, and in what form, is an open question.

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Organization]]
