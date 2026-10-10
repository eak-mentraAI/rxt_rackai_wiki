---
id: chg-2026-10-10-prd-a-workload-declaration
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd a draft, workload declaration prd draft, approval and divergence rules]
related: [prd-workload-declaration-placement, ent-workload-declaration, ent-model-deployment-spec, wiki-prd-coverage-plan, wiki-milestone-release-map, hub-roadmap, pol-fitness-checklist, chg-2026-10-10-tech-spec-prd-v2]
source_docs: ["PM direction 2026-10-10: start PRD A; refinements on approval, divergence, measured confidence, canonical notes", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD A and the Workload Declaration note; added approval, divergence-review and measured-confidence rules."
---

# CHANGE 2026-10-10 — PRD A Draft and Approval Rules

## Trigger

The product owner approved the PRD grouping and workflow, asked for PRD A to be drafted, and added five refinements. Work stops before publishing or committing so the product decisions, scope and acceptance criteria can be reviewed.

## What Changed

**Standards (the product owner's refinements):**
1. **Canonical notes are created when a concept must be shared across capabilities**, not as a documentation prerequisite (`prd-standards.md`, PRD template §6).
2. **Checks are not approval.** New section in `prd-standards.md`. PRD template v2 gains a *Product approval* row, **§15 Acceptance Criteria** (binary, testable) separated from success metrics, and **§20 Proposed Product Decisions** (each reviewable on its own). `status: reviewed` requires recorded product approval. Fitness **P-11**. The tech-spec standard states the same for specs.
3. **Material as-built divergence needs product review.** A divergence is material if it changes a requirement, an acceptance criterion, a hard-constraint guarantee, a boundary or customer-visible behaviour. It is marked *divergent: pending product review* in the PRD, with an open decision owned by the product owner (`prd-standards.md`, `tech-spec-standards.md`). Fitness **T-11**.
4. **Many-to-many PRD ↔ spec** is kept (no change needed).
5. **`measured` is allowed when test, benchmark or production-telemetry evidence is cited**; `derived` when the only evidence is code or as-built annotations (both standards).

**Corpus:**
- New canonical entity [[Workload Declaration]] (`ent-workload-declaration`). It was needed because six PRDs consume it. Supply target / accelerator pool / execution location stay inside PRD A until G consumes them.
- New [[Workload Declaration & Placement PRD]] (`prd-workload-declaration-placement`, v0.1 draft). Its current-state section draws on a read-only code survey at the cited commits.
- Roadmap CSV: the **PRD** column now links PRD A for *Supply-abstraction interface*, *Workload declaration (intent + constraints)*, *Supply abstraction v1 - second impl (AMD/partner)* and *Heterogeneous supply*.
- Propagation:
  - [[Model Deployment Specification]]: DERIVES ← Workload Declaration edge.
  - [[Milestone Release Map]]: "Empirical Map owns the placement decision" corrected to the ratified A/G rule (the Map recommends; T1.S2 executes).
  - [[RackAI Roadmap]]: the same correction in the placement-principle text, plus links to the new note and PRD from P-004.
  - [[PRD Coverage Plan]]: A marked as drafted.

## v0.2 — Product-Owner Review (same day)

PRD A was directionally approved (structure, scope, A/G/C boundaries). **Approved:** PD-1, PD-3, PD-5, PD-6, PD-7, PD-8, PD-9.

**Revised, pending final approval:**
- **PD-2:** known infeasibility is now separate from *feasible, performance unverified*. Operator acknowledgment never implies verified SLO attainment, and *unverified* is no longer an infeasibility category.
- **PD-4:** authorized operators approve initial realizations and material changes to a *placement envelope*; routine operations inside an approved envelope run under policy set by C.
- **PD-10:** the falsification test is now genuine customer rejection of managed placement (performance, economics or control); pin frequency is diagnostic only.

**Acceptance criteria updated:** AC-3, AC-5, AC-7, AC-14.

**Clarified:**
- Feasibility is revalidated at deployment commitment (FR-7).
- A runtime constraint violation is detected, contained and evidenced (FR-10, §12, AC-5c).
- *Placement envelope* is defined locally in §6.

**Phase 1 scope unchanged**; no new initiatives. [[Workload Declaration]] lifecycle and invariants were aligned. Checks pass.

## v1.0 — Approved (same day)

The product owner approved PD-2, PD-4, PD-10 as revised and the acceptance criteria. AC-8 was extended to check that the specification records the approved placement envelope and whether performance was verified at approval. PRD status → `reviewed` (approved product contract; nothing built). Open decisions D-1 to D-8 remain open.

## Checks

Frontmatter lint, PRD/spec lint (P-09 link-back) and broken-link check all pass. Checks P-01 to P-11 were reviewed by hand. **This is review-readiness, not approval.** As of v1.0 all product decisions and acceptance criteria are approved by the product owner.

## Open Questions

- PRD A §19 holds eight open decisions (D-1 to D-8). D-1 (per-profile service-level thresholds, roadmap row 11) is the gating one.
- Committed locally after approval; not pushed until knowledge-platform supports the `spec` type.
