---
id: prd-{slug}
type: prd
status: draft
owner: team-or-role
domain: product
aliases: [{name} prd]
related: [{canonical-note-id}]
source_docs: []
confidence: assumed
last_reviewed: YYYY-MM-DD
parent: hub-product
summary: "PRD for {thing}: {problem + what's proposed} — keep under 120 chars."
---

<!-- type: `prd` is a first-class note type (ID prefix `prd-`). See .kiro/steering/prd-standards.md. -->
<!-- related MUST include the canonical concept note's ID. summary MUST be <= 120 chars (Fitness S-16). -->
<!-- This template is a portable standard shared across sibling wiki repos — do not add product-specific content to the template itself. -->
<!-- Minimum viable set: a PRD is incomplete unless sections 2,3,4,6,7,8,9,10,12,13 are all answered (see prd-standards.md). Section 12 (kill criterion) is the one most often skipped and is required. -->


# {Thing} — PRD

> **Artifact type: Product Requirements Document.** This is an authored product spec, not a knowledge-graph definition. The canonical concept lives in [[{Canonical Note}]]; this PRD *projects* from it and must not re-define it (One-Concept Rule). If the two disagree, the canonical note wins and this PRD is stale.
>
> **Status banner.** State plainly whether this is a *draft PRD for a proposed initiative* (nothing built; requirements are intent, not commitments) or a PRD for a funded build. Carry the honest confidence: proposed capability is `assumed` until there is evidence.

## 1. Summary

Two or three sentences: what this is, who it's for, why now. Readable in isolation.

## 2. Problem / Opportunity

The user/business problem. What is broken or missing today, for whom, and what it costs. Ground it in evidence or name it as a hypothesis.

## 3. Goals & Non-Goals

**Goals** — what success looks like, as outcomes (not features).

**Non-Goals** — what this explicitly does *not* cover. The boundary is as important as the scope; name what belongs to another team/product/offer.

## 4. Users & Personas

Who uses or is affected by this. For a two-sided product, name both sides and what each needs.

## 5. User Journeys / Scenarios

The key flows, end to end, in prose or numbered steps. One worked example beats an abstract list.

## 6. Functional Requirements

Numbered, testable requirements grouped by area. Use **MUST / SHOULD / MAY**. Each should be verifiable. Mark anything unresolved as an Open Decision rather than inventing a spec.

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-1 | ... | MUST | |

## 7. Non-Functional Requirements

Security, isolation, performance, compliance, scale, observability. For regulated/sovereign contexts, state the control requirements explicitly.

## 8. Scope & Phasing

What ships in which phase. Tie to the roadmap/release stages where one exists.

## 9. Success Metrics

How we'll know it worked. Name the baseline (even if "none today") and the target *posture*, not asserted values. Prefer a small **ladder** of metrics over a single Goodhart-fragile number. Keep numbers traceable; do not assert a measured value that doesn't exist.

## 10. Dependencies

What this needs from other teams/products/capabilities, and what depends on it.

## 11. Risks & Mitigations

The things that could sink it, and the response to each.

## 12. Kill / Falsification Criterion

**Required.** What evidence would show this bet is wrong and we should stop or change course? State it concretely (e.g. "if metric X stays flat after N trials"). A PRD without a stop condition is a wish, not a plan.

## 13. Open Decisions

The unresolved questions that block adoption or scoping, each with an owner. Distinct from requirements. The gating one (if any) should be first.

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| D-1 | ... | | |

## See Also

- [[{Canonical Note}]] — the canonical concept this PRD builds on
- the product/roadmap hub for this repo
