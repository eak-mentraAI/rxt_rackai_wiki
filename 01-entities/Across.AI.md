---
id: ent-across-ai
type: entity
status: draft
owner: rackai-product
domain: strategy
aliases: [across.ai, across ai, partner candidate]
related: [ent-empirical-map, wf-verification, wf-self-improvement-loop, hub-enterprise-ai, src-rackai-dev-plan, hub-load-bearing-bets]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-entities
summary: "Canonical entity: Across.AI, the candidate partner (pending diligence) that could accelerate the moat's harness/orchestration/loop machinery."
---

# Across.AI

## Definition

**Across.AI** is the **partner candidate** identified in the [[RackAI Enterprise AI Development Plan]] to potentially accelerate the long-term "moat" work — the harness, orchestration, and loop machinery around the [[Empirical Map]], [[Verification]], routing, and the [[Self-Improvement Loop]]. It is the "A" in the plan's `L+A` (long-term, partner-accelerable) coverage marks.

> **Assumed confidence, pending diligence.** Across.AI is a *candidate*, not a signed partner; a similar partner could fill the same role. Its coverage marks in the plan are explicitly "early and unproven." This note exists so the partner reference is not an orphan and so the diligence status is tracked.

## Layer

L1 — Entity Ontology. An external partner/vendor entity, referenced by the portfolio and the coverage view; it does not sit in the serving chain and never references GPUs.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Role | Accelerate moat machinery (harness/orchestration/loop) | text | assumed |
| Status | Candidate, pending due diligence | enum | assumed |
| Substitutability | A similar partner could fill the same role | text | assumed |
| Boundary constraint | Perimeter & data-rights terms must be held; moat stays in-house | policy | assumed |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SUPPORTS | [[Empirical Map]] | → | Could accelerate, but ownership stays in-house |
| SUPPORTS | [[Verification]] | → | `L+A` — partner-accelerable long-term work |
| SUPPORTS | [[Self-Improvement Loop]] | → | `L+A` |
| CONSTRAINS | [[Enterprise AI Portfolio]] | ← | Perimeter/data-rights terms gate any engagement |

## Open Questions

- Due diligence on Across.AI is unresolved. What are the specific perimeter and data-rights terms required before any moat work is shared?
- Which `L+A` items, if any, would actually be handed to a partner vs. kept fully in-house?

## Evidence

- Source: dev plan Table 2 (L+A marks), "Owned in-house" and "Staffing" sections.
- Confidence rationale: `assumed` — candidate pending diligence; marks are early and unproven per the source.

## See Also

- [[Entity Ontology Hub]]
- [[Enterprise AI Portfolio]]
- [[Load-Bearing Bets]]
- [[RackAI Enterprise AI Development Plan]]
