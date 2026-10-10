---
id: ent-evidence-report
type: entity
status: draft
owner: rackai-product
domain: product
aliases: [evidence report, moe-1 evidence report, customer evidence report, recurring evidence report, acceptance artifact 4, prove-it report]
related: [ent-customer-observability, prd-customer-observability-evidence, spec-customer-observability-evidence, ent-workload-declaration, ent-organization, met-slo-attainment, pol-benchmark-evidence-chain, pol-action-controls, ent-agent-identity, wf-audit, hub-minimum-operable-estate, hub-battlegrounds, pol-sovereignty-levels]
source_docs: ["00-hub/Minimum Operable Estate.md", "05-wiki/RackAI Roadmap.csv", "00-hub/Three Battlegrounds.md"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-entities
summary: "Canonical entity: the recurring, reviewed report proving a customer's outcome was met and their declared envelope held."
---

# Evidence Report

## Definition

An **Evidence Report** is the recurring, customer-facing report that proves, for one customer and one period, the **realisation outcome** RackAI delivered: performance against the declared service levels, usage and charges, the policy decisions taken (admitted, rejected, escalated, infeasible), the actions taken and by whom (including agents acting for a user), whether every declared hard constraint and boundary held, and incidents. It is MOE-1 acceptance artifact 4 ([[Minimum Operable Estate]]).

It is built **only from evidence records** in the shared evidence contract (D-0), defined in [[Customer Observability & Evidence Report PRD]] §1.2 and formalised in its tech spec. Every statement links to the records behind it. Each section states its coverage, for collection and observation separately. A section with no positive evidence reads *not evidenced*, never *held* or *met*, and no SLO is declared met without measured joint attainment. It proves the realisation outcome, not the business result of the customer's application (outcome boundary, [[Three Battlegrounds]]).

> **Status: proposed, not built.** No evidence store or report exists today. Audit records what happened ([[Audit]]) but cannot show an outcome was met. Everything below is `assumed`; the product contract is [[Customer Observability & Evidence Report PRD]].

## Layer

L1 — Entity Ontology. It sits at the end of the operating loop (*prove it*), downstream of every decision it reports:

**[[Workload Declaration]]** (what was promised) → decisions and telemetry from every capability → evidence records (D-0) → **Evidence Report**

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Scope | The customer's authority principal (C's [[Authority Context]]): the CustomerOrg only where it is validated as controlled by one customer, otherwise the [[Organization]]; with per-organisation and per-project sections | ref | assumed |
| Period | Half-open interval the report covers; cadence agreed per customer | interval | assumed |
| Performance vs SLO | Canonical joint [[SLO Attainment]] per declared workload against the ratified thresholds, or `not_measured`, with any lower bound and per-threshold estimates labelled as such and never shown as met; the typed `performance` status ([[Verification Status Vocabulary]]) | section | assumed |
| Usage and charges | Metered consumption and what the customer is charged; never internal cost | section | assumed |
| Policy decisions | Admitted, rejected, escalated and infeasible decisions, with reasons ([[Action Controls]]) | section | assumed |
| Actions | Who or what acted, and for agents, on whose behalf ([[Agent Identity]]) | section | assumed |
| Envelope held | Hard constraints held at commit and at runtime; violations and containment; boundary held and exceptions ([[Sovereignty Levels]]) | section | assumed |
| Incidents | Operator-asserted incidents and their impact | section | assumed |
| Coverage | Per section, typed `coverage` status (`complete`, `incomplete`, `unknown`), stated separately for collection of available records and observation of the system; distinct from the section's outcome (e.g. *not evidenced*) | enum | assumed |
| Version and digest | Issued versions are immutable; a correction issues a new version that supersedes the old | int / hash | assumed |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Draft | Generated from the records for the period; visible to operators only | Operator generates it for a closed period | Issued, or regenerated |
| Issued | Reviewed and issued by an authorised operator; immutable, with a digest; visible to the customer | Issue bound to the reviewed draft's digest | Superseded |
| Superseded | A later version corrects it; still retrievable and marked | A correction is issued | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Workload Declaration]] | → | Outcomes are judged against the declaration version in force |
| USES | [[SLO Attainment]] | → | Performance section |
| USES | [[Audit]] | → | Records reference audit events; the report does not replace audit |
| CONSUMES | [[Customer Observability]] | → | Telemetry-derived values, recorded as evidence |
| BELONGS_TO | [[Organization]] | → | Scoped to one customer |
| VALIDATES | [[Minimum Operable Estate]] | → | Acceptance artifact 4 for MOE-1 |

## Graph Invariants

- Every issued Evidence Report belongs to exactly one authority principal and one period, and is never changed after issue.
- No customer receives another customer's evidence through a shared CustomerOrg or other parent.
- Every statement in a report traces to at least one evidence record; every record traces to its sources.
- No section states *held* or *met* without positive evidence for the whole period.
- No operator-only evidence (internal cost, suspected violations) appears in a customer report.

## Evidence

- Source: `source_docs` (acceptance definition and roadmap; no shipped implementation).
- Confidence rationale: `assumed`. A proposed deliverable (roadmap row *MOE-1 evidence report*); the four evidence groups come from the minimum evidence contract in [[Minimum Operable Estate]] (2026-10-08).

## See Also

- [[Customer Observability & Evidence Report PRD]]: the product contract, including the evidence contract (D-0)
- [[Customer Observability & Evidence Report Tech Spec]]: the proposed design (draft)
- [[Customer Observability]]: the always-on half of *prove it*
- [[Minimum Operable Estate]]: MOE-1 acceptance artifacts
- [[Entity Ontology Hub]]
