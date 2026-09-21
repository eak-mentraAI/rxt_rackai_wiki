---
id: ent-api-key
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [api key, api credential, programmatic credential]
related: [ent-organization, wf-identity-access, ent-openrouter-private-model, hub-entities]
source_docs: [identity_access_spec, "reference/RackAI - Roadmap.xlsx"]
confidence: measured
last_reviewed: 2026-09-21
parent: hub-entities
summary: "Entity: a programmatic credential for calling RackAI APIs and inference endpoints (shipped, IAC M1)."
---

# API Key

## Definition

An **API Key** is a programmatic credential for calling RackAI's APIs and inference endpoints. It is part of the Identity/Access workstream and is the primary dependency for the OpenRouter Private Model path (which needs a stable, org-scoped credential to authenticate provider-routed traffic). **Status: shipped** — delivered as part of IAC M1 (APIKey CRD + JWT/API-key validation + Gateway auth, RACKAI-204, Complete) per the [[RackAI Roadmap (Delivery Plan)|delivery roadmap]], so this entity now carries `measured` confidence. This unblocks OpenRouter Path A.

## Layer

L1 — Entity Ontology. The API Key authenticates an Organization's programmatic access to Model endpoints:

**Consumer → API Key → [[Identity & Access Control]] → [[Organization]] → [[Model Deployment]] endpoint**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Key ID | Stable identifier | string | measured |
| Scope | Org-scoped access to APIs/inference | enum | measured |
| Secret material | The token used to authenticate | ref | measured |
| Status | Shipped (IAC M1, RACKAI-204) | enum | measured |

## Lifecycle States

APIKey CRD with lifecycle events (issuance/revocation logged via the audit-log API, IAC M3). Rotation specifics beyond the shipped CRD are not yet detailed.

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| AUTHENTICATES | [[Organization]] | → | Grants org-scoped programmatic access |
| DEPENDS_ON | [[Identity & Access Control]] | → | Issued/validated by the identity workstream |
| REQUIRED_BY | [[OpenRouter Private Model Integration]] | ← | Primary dependency for the private-model path |

## Evidence

- Source: `identity_access_spec`; delivery status from the [[RackAI Roadmap (Delivery Plan)]] (`reference/RackAI - Roadmap.xlsx`).
- Confidence rationale: `measured` — shipped as IAC M1 (RACKAI-204, Complete): APIKey CRD, JWT/API-key validation, Gateway auth. Upgraded from `assumed` on 2026-09-21 per the delivery roadmap (shipped-beats-planned).

## See Also

- [[Entity Ontology Hub]]
- [[Identity & Access Control]]
- [[Organization]]
