---
id: src-metering-spec
type: source
status: reviewed
owner: platform-eng
domain: commercial
aliases: [metering spec, multi tenancy prd, metering tech spec, usage metering]
related: [hub-rackai-platform, hub-commercial, src-rackai-platform-prd]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI Multi-Tenancy & Metering PRD + technical spec (usage capture, quotas, tenant isolation)."
---

# Multi-Tenancy and Metering Spec

## Provenance

- Origin: `reference/rackai-platform/PRD - Multi Tenancy and Metering.docx`, `Multi_Tenants_Metering_TechSpec.docx`
- Status: Draft (spec v0.2)
- Classification: planning / architecture

## Summary

Defines tenant isolation, usage **metering** (capturing token/request usage per tenant), and **quotas**. Introduces Projects and UsageRecord concepts. All of this is **planned/draft**, not shipped.

> **Critical for the OpenRouter Initiative:** this spec explicitly lists **"defining pricing rates or billing logic" as a non-goal**. Metering ≠ billing. There is no billing/payment mechanism on the platform roadmap, which is the headline P0 gap for the OpenRouter public-provider path. Tracked as an open question and modeled in [[Billing & Payment]].

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Metering / usage capture | [[Metering]] | L2 |
| Billing gap (non-goal) | [[Billing & Payment]] | L3 |
| Multi-tenancy | [[Organization]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
- [[Open Questions]]
