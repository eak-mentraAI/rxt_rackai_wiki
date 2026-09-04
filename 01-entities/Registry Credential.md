---
id: ent-registry-credential
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [registry credential, registry secret, pull credential]
related: [ent-model, ent-organization, hub-entities]
source_docs: [rackai_console_docs]
confidence: measured
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: a credential used to fetch model weights and container images."
---

# Registry Credential

## Definition

A **Registry Credential** is a stored secret that RackAI uses to fetch model weights and container images from external registries. There are three types: `modelPull` (for example, a HuggingFace token used to pull weights), `license`, and `imagePull`. A [[Model]] uses a Registry Credential to pull its weights, and every credential belongs to exactly one [[Organization]].

## Layer

L1 — Entity Ontology. The credential is a supporting entity that enables the Model to acquire weights before deployment:

**[[Organization]] → Registry Credential → [[Model]] (weight pull) → [[Model Deployment]]**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Credential ID | Stable identifier | string | measured |
| Type | `modelPull`, `license`, `imagePull` | enum | measured |
| Registry target | Registry the credential authenticates against | string | measured |
| Secret ref | Reference to the stored secret material | ref | measured |

## Lifecycle States

Not a stateful entity. (A credential is a stored secret; it is created, rotated, and deleted administratively rather than moving through a modeled lifecycle.)

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| USED_BY | [[Model]] | ← | A model uses it to pull weights/images |
| BELONGS_TO | [[Organization]] | → | Org-scoped, stored in the org namespace |

## Evidence

- Source: `rackai_console_docs`.
- Confidence rationale: `measured` — the three credential types (`modelPull`, `license`, `imagePull`) and the HuggingFace token usage are shipped and documented in the console docs.

## See Also

- [[Entity Ontology Hub]]
- [[Model]]
- [[Organization]]
