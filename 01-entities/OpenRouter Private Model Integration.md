---
id: ent-openrouter-private-model
type: entity
status: draft
owner: product
domain: product
aliases: [openrouter private model, private model integration, private models, path a]
related: [ent-openrouter-integration, ent-model-deployment, ent-api-key, hub-openrouter, hub-entities]
source_docs: [openrouter_concepts_integration_provider, identity_access_spec]
confidence: derived
last_reviewed: 2026-09-04
parent: hub-entities
summary: "Canonical entity: registering a RackAI tenant deployment into OpenRouter as a restricted private model (Path A)."
---

# OpenRouter Private Model Integration

## Definition

An **OpenRouter Private Model Integration** registers a specific RackAI [[Model Deployment]] endpoint into OpenRouter as a **private model** — a restricted, non-public model callable only by approved users/organizations, routed through the same OpenAI-compatible API as any other OpenRouter model. It is the **Path A** entry to OpenRouter: a natural extension of the existing RackAI product rather than a new inference-as-a-service business.

This is distinct from the [[OpenRouter Provider Integration]] (Path B), which exposes Rackspace-operated public models to arbitrary marketplace traffic.

## Layer

L1 — Entity Ontology. Position in the abstraction chain:

**Demand (OpenRouter private-model callers) → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

Like the provider integration, it sits at the demand boundary and presents a Model endpoint, never GPU hardware.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Target deployment | The RackAI Model Deployment endpoint registered | ref | derived |
| Access control | Approved users/orgs allowed to call it | set | derived |
| API format | OpenAI-compatible chat-completions | enum | measured |
| Visibility | Not publicly listed / ranked / benchmarked | bool | measured |
| Enterprise plan | Requires an OpenRouter Enterprise plan | bool | measured |

## Dependencies

- **Primary dependency:** [[API Key]] support (Identity/Access workstream) to authenticate the registered endpoint.
- Assumes endpoint auth, OpenRouter's private-model validation, and Enterprise-plan mechanics are straightforward — currently unverified.
- Does **not** require RackAI-side [[Billing & Payment]] (usage bills to the tenant's own OpenRouter account).

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Requested | Enterprise setup requested via OpenRouter | Deployment endpoint exists | Approved |
| Registered | Private model configured with access rules | Approval + API key wired | Callable by approved users |
| Active | Serving approved private traffic | Registration complete | Deregistered |
| Deregistered | Removed from OpenRouter | Deployment retired or access revoked | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| REGISTERS | [[Model Deployment]] | → | Wraps a tenant deployment endpoint |
| DEPENDS_ON | [[API Key]] | → | Primary dependency for Path A |
| PEER_OF | [[OpenRouter Provider Integration]] | ↔ | The other OpenRouter integration path |

## Evidence

- Source: `OpenRouter provider reference` (Private Models section — near-term, needs API-key support + docs); `Identity and Access Control Spec` (API keys).
- Confidence rationale: `derived` — the capability building blocks (per-deployment endpoint) exist and shipped; the end-to-end private-model registration has not been validated. Exit criterion: an end-to-end private-model registration validated against OpenRouter onboarding.

## See Also

- [[Entity Ontology Hub]]
- [[OpenRouter Initiative]]
- [[OpenRouter Provider Integration]]
