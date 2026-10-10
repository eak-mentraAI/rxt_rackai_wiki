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
<!-- Template v2 (2026-10-10): aligned to the section vocabulary engineering already uses in PRDs (Vision, Problem Statement, Product Principles, Scope, Core Entities, Platform Integration, Failure Handling, Success Criteria), while keeping the ten-item minimum set. -->
<!-- Minimum viable set: a PRD is incomplete unless sections 2, 4, 5, 6, 8, 9, 14, 15, 16, 18, 19, 20 are all answered (see prd-standards.md). Section 18 (kill criterion) is the one most often skipped and is required. Sections 3, 10, 11, 12, 13 are standard; write "n/a — reason" rather than deleting them. -->


# {Thing} — PRD

| Field | Value |
|:--|:--|
| Version | v0.1 |
| Status | Draft / In review / Approved / Superseded |
| Owner | |
| Reviewers | |
| Product approval | not yet approved — recorded by the product owner only (who, date, version); passing checks is not approval |
| Date | YYYY-MM-DD |
| Roadmap items | Milestone names exactly as they appear in the canonical roadmap table, separated by `;` — every PRD names the roadmap item(s) it is written for, and each listed row's *PRD* column must link this note (Fitness P-09) |
| Tech spec(s) | [[{Thing} Tech Spec]] — one or more; a spec may also serve other PRDs. Or "not yet written" |

> **Artifact type: Product Requirements Document.** This is an authored product spec, not a knowledge-graph definition. The canonical concept lives in [[{Canonical Note}]]; this PRD *projects* from it and must not re-define it (One-Concept Rule). If the two disagree, the canonical note wins and this PRD is stale.
>
> **Status banner.** State plainly whether this is a *draft PRD for a proposed initiative* (nothing built; requirements are intent, not commitments) or a PRD for a funded build. Carry the honest confidence: proposed capability is `assumed` until there is evidence.
>
> **Scope line (read first).** One sentence on what this PRD covers and — critically — what it does **not** (the ownership boundary).

## 1. Summary / Vision

Two or three sentences: what this is, who it's for, why now. Readable in isolation. The vision is the end state this moves toward, not a feature list.

## 2. Problem Statement

The user/business problem. What is broken or missing today, for whom, and what it costs. Ground it in evidence or name it as a hypothesis.

## 3. Product Principles

Three to seven principles that settle trade-offs when the requirements don't (e.g. "least privilege by default", "everything is attributed", "fail closed"). Each one line plus why.

## 4. Scope: Goals & Non-Goals

**Goals** — what success looks like, as outcomes (not features).

**Non-Goals / Out of Scope** — what this explicitly does *not* cover. The boundary is as important as the scope; name what belongs to another team/product/offer, and what is deferred to a later phase.

## 5. Users & Personas

Who uses or is affected by this. For a two-sided product, name both sides and what each needs. Include operators/admins, not only end users.

## 6. Core Entities

The domain objects this PRD acts on, each **linked to its canonical note** with one line on the role it plays here. Do not redefine them. Create a canonical note only when a concept must be shared across capabilities: if a concept this PRD introduces is consumed elsewhere and has no canonical note, write a thin one **in the same change**. A concept used only here is defined in this PRD until a second consumer appears.

## 7. User Journeys / Scenarios

The key flows, end to end, in prose or numbered steps. One worked example beats an abstract list. Where requests cross systems, show the lifecycle (authenticate → authorize → admit/quota → execute → meter → audit → report).

## 8. Functional Requirements

Numbered, testable requirements grouped by area. Use **MUST / SHOULD / MAY**. Each should be verifiable. Mark anything unresolved as an Open Decision rather than inventing a spec.

| # | Requirement | Priority | Notes |
|---|-------------|:--------:|-------|
| FR-1 | ... | MUST | |

## 9. Non-Functional Requirements

Security, isolation, performance, compliance, scale, observability. For regulated/sovereign contexts, state the control requirements explicitly. Targets are postures until measured.

## 10. Platform Integration

What this needs from, and gives to, the shared platform systems. Answer every row, even with "none"; this is the section engineering most often has to reconstruct.

| System | Needs from it | Provides to it |
|---|---|---|
| Identity & access (authn/authz, roles) | | |
| Tenancy & isolation | | |
| Metering, quotas & billing | | |
| Audit | | |
| Monitoring & observability | | |

## 11. Loop Role & Cross-PRD Interfaces

Which step of the operating loop this PRD owns (*declare* / *stay inside your boundaries* / *deliver the how* / *prove it*), and which promise it serves (operator, sovereign, or the contract between them). Then the interfaces it **provides to** and **consumes from** other PRDs. A shared interface is defined in exactly one PRD (or its canonical note) and referenced everywhere else. This is what stops related PRDs from becoming silos.

| Interface | Direction | Other PRD | Defined where |
|---|---|---|---|
| e.g. workload declaration | consumes | {other PRD} | [[{canonical note}]] |

## 12. Failure Handling

Expected behaviour when dependencies fail or degrade: what fails closed vs open, what the user sees, what is guaranteed not to happen (e.g. no cross-tenant access, no unmetered usage).

## 13. Data Retention & Compliance

What data this creates or holds, how long it is kept, who can see or delete it, and any compliance obligation it serves. "n/a" if it holds no data.

## 14. Scope & Phasing

What ships in which phase, tied to the roadmap items in the header and release stages where they exist. Prefer prototype-first sequencing where the shape is uncertain.

## 15. Acceptance Criteria & Success Metrics

**Acceptance criteria** decide whether what was built meets this PRD. Each is binary and testable, traces to requirements, and is reviewable on its own.

| # | Criterion (observable, pass/fail) | Verifies | How tested |
|---|---|---|---|
| AC-1 | ... | FR-1 | |

**Success metrics** decide whether the bet is working once it is live. Name the baseline (even if "none today") and the target *posture*, not asserted values. Prefer a small **ladder** of metrics over a single Goodhart-fragile number. Keep numbers traceable; do not assert a measured value that doesn't exist.

## 16. Dependencies

What this needs from other teams/products/capabilities, and what depends on it.

## 17. Risks & Mitigations

The things that could sink it, and the response to each.

## 18. Kill / Falsification Criterion

**Required.** What evidence would show this bet is wrong and we should stop or change course? State it concretely (e.g. "if metric X stays flat after N trials"). A PRD without a stop condition is a wish, not a plan.

## 19. Open Decisions

The unresolved questions that block adoption or scoping, each with an owner. Distinct from requirements. The gating one (if any) should be first.

| # | Decision | Owner | Blocks |
|---|----------|-------|--------|
| D-1 | ... | | |

## 20. Proposed Product Decisions

The decisions this PRD *takes* (as distinct from §19, which lists decisions still open). Each is listed separately so the product owner can accept, change or reject it. None is final until approved.

| # | Decision | Alternatives considered | Why this one | Status |
|---|---|---|---|---|
| PD-1 | ... | | | proposed |

## See Also

- [[{Canonical Note}]] — the canonical concept this PRD builds on
- [[{Thing} Tech Spec]] — the engineering design that implements it (when written)
- the product/roadmap hub for this repo
