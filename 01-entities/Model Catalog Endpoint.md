---
id: ent-model-catalog-endpoint
type: entity
status: draft
owner: platform-eng
domain: platform
aliases: [model catalog endpoint, /models endpoint, models endpoint, catalog api]
related: [ent-openrouter-integration, ent-model, ent-billing-payment, hub-openrouter, hub-entities]
source_docs: [openrouter_concepts_integration_provider, rackai_api_reference]
confidence: assumed
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: the OpenRouter-schema /models catalog endpoint a public provider must publish (a P0 gap today)."
---

# Model Catalog Endpoint

## Definition

The **Model Catalog Endpoint** is the machine-readable `/models` catalog a public OpenRouter provider must publish, describing every served model in **OpenRouter's typed schema** — pricing, context window, maximum output tokens, supported parameters, capacity limits, and datacenter locations, with per-modality pricing/capacity. It is a **P0** requirement for the [[OpenRouter Provider Integration]] (public-provider path).

## Layer

L1 — Entity Ontology. It is the published description of the [[Model]] catalog exposed to OpenRouter; it sits at the demand boundary alongside the provider integration.

## Status

- **Not shipped in OpenRouter's schema.** RackAI exposes a Kubernetes-style resource listing (Model / Model Class / Model Deployment CRDs) and the serving engine's `/v1/models`, but **not** an OpenRouter-schema catalog with pricing, capacity, and datacenter per modality.
- Confidence `assumed` (gap): the requirement is documented; the conforming endpoint does not exist.

## Dependencies

- **Pricing** — depends on [[Billing & Payment]] / pricing definition (which is itself a gap).
- **Capacity declarations** — depends on published per-model capacity limits.
- **Datacenter/region** — single-region today (see [[Environment]]); limits geo declarations.

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| PUBLISHED_BY | [[OpenRouter Provider Integration]] | ← | The provider integration must expose it |
| DESCRIBES | [[Model]] | → | Catalog of served models |
| DEPENDS_ON | [[Billing & Payment]] | → | Needs pricing to populate |

## Evidence

- Source: `OpenRouter provider reference` (P0 `/models` typed-schema requirement); `RackAI API Reference` (current CRD listing + engine `/v1/models`, not OpenRouter-schema).
- Confidence rationale: `assumed` — modeled as a known gap. Exit criterion: a `/models` endpoint conforming to OpenRouter's schema, populated with real pricing and capacity.

## See Also

- [[Entity Ontology Hub]]
- [[OpenRouter Initiative]]
- [[OpenRouter Provider Integration]]
