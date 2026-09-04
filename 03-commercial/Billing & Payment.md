---
id: ent-billing-payment
type: entity
status: draft
owner: commercial
domain: commercial
aliases: [billing, payment, billing and payment, payout, invoicing]
related: [wf-metering, hub-commercial, hub-openrouter, ent-openrouter-provider-integration, oq-open-questions]
source_docs: [metering_spec, openrouter_concepts_integration_provider]
confidence: assumed
last_reviewed: 2026-09-04
parent: hub-commercial
summary: "Canonical concept: the (currently absent) billing and payment capability — a headline gap for the OpenRouter public-provider path."
---

# Billing & Payment

## Definition

**Billing & Payment** is the capability to convert metered usage into money movement — pricing usage, generating invoices or account top-ups, and receiving/reconciling payout. It is distinct from [[Metering]] (which only captures usage). **This capability does not exist in RackAI today**, and defining pricing/billing logic is an explicit non-goal of the metering specification.

> **Metering ≠ Billing.** Metering answers "how much was used." Billing answers "what does it cost and how do we get paid." RackAI has planned metering; it has no billing.

## Layer

L3 — Commercial and Capacity Model. Downstream of [[Metering]]; consumed by initiatives that require money movement.

## Status

- **Not shipped. Not on the platform roadmap.** Billing/pricing logic is a declared non-goal of the [[Multi-Tenancy and Metering Spec]].
- Confidence `assumed` (gap): there is no artifact describing a billing system, only its absence.

## Why It Matters

Becoming an OpenRouter **public provider** (Path B) is a hard **P0** on automated billing — OpenRouter requires a way to pay providers via automatic top-ups or monthly invoices. Without it, RackAI cannot complete the provider application. This is the single highest-impact gap for the [[OpenRouter Initiative]] public-provider path.

The **Private Models** path (Path A) does not require RackAI-side billing (usage bills to the tenant's own OpenRouter account), which is part of why Path A is the faster entry.

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| DEPENDS_ON | [[Metering]] | → | Billing consumes metered usage |
| CONSTRAINS | [[OpenRouter Provider Integration]] | → | P0 blocker for the public-provider path |
| DERIVES | [[Unit Economics Model]] | → | Pricing must reflect cost/token to preserve margin |

## Evidence

- Source: `Multi-Tenancy and Metering Spec` (billing = explicit non-goal); `OpenRouter provider reference` (automated billing is P0 for providers).
- Confidence rationale: `assumed` — modeled as a known gap, not a built capability. Exit criterion: a funded billing/payout design accepted by OpenRouter onboarding would move dependent concepts off `assumed`.

## See Also

- [[Commercial & Capacity Hub]]
- [[Metering]]
- [[OpenRouter Initiative]]
- [[Open Questions]]
