---
id: chg-2026-10-09-smp-prd-v3
type: change
status: draft
owner: product
domain: product
aliases: [solution marketplace prd v3, prd fde review incorporation]
related: [prd-solution-marketplace, ent-solution-marketplace, ent-packaged-solution, wiki-milestone-release-map, hub-ai-operations-product]
source_docs: ["05-wiki/Solution Marketplace PRD.md", "PM/FDE-perspective PRD review 2026-10-09"]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-wiki
summary: "Folded FDE-perspective review into the Solution Marketplace PRD: operating modes, dev workflow, handoff contract."
---

# 2026-10-09 — Solution Marketplace PRD v3 (FDE Review Incorporation)

## Trigger

An FDE-perspective review scored the PRD 9/10 on architecture, trust model, and strategy, but only 5–6/10 on FDE authoring experience, development speed, and operational handoff. Its main point was that the PRD specified the factory before defining the developer experience. The reviewer said to make targeted refinements, not a rewrite, and to keep four decisions: rails vs. solution-logic ownership, prototype-first (MK.S0), separate package certification and estate validation, and delivery leverage as the headline metric. All four are kept. All five refinements and the eight expected FDE questions are incorporated.

## Objects Changed — [[Solution Marketplace PRD]]

1. **Design stance** (after the scope line): the rails are an *accelerator*, not a framework; we are not asking FDEs to change how they invent solutions.
2. **Goals / Non-Goals:** new goal "make FDE delivery faster, not slower." New non-goals: productizing every engagement, dictating the authoring framework, and becoming a full app-dev platform.
3. **§5 Operating modes** (Experiment / Customer deployment / Reusable Packaged Solution). These are three ways of using the same rails, and certification applies only to the third. **§5 FDE developer workflow** covers build → test → package → deploy → operate, and the SDK is accountable for the whole workflow.
4. **New FRs (no renumbering):**
   - FR-1a: manifest mostly generated, plus validation of undeclared access
   - FR-3a: extension path and exception process
   - FR-5a: framework-agnostic SDK with minimum integration points
   - FR-6a: dev/test loop in a customer-like sandbox
   - FR-6b: experiment → deployment → package without a rewrite
   - FR-9a: certification gates only reusable publication; customer deployments still get estate validation
   - FR-13a: customization through config, extension points, or an estate-scoped layer; editing the artifact is a fork
   - FR-18b: maintaining owner plus a responsibility split, with a **proposed default operating-contract table** (marked as a hypothesis for D-7) and the 12-estate API-break worked case
5. **§8 phasing:** MK.S0 must use a realistic FDE workflow (not a demo) and baseline FDE hours. MK.S1 adds the dev loop, manifest generation, and promotion path. The FR ranges in the S1–S4 rows are updated.
6. **§9 metrics:** FDE delivery leverage now counts integration and customization work. New rung: **authoring overhead** (packaging/certification hours ÷ build hours), baselined at MK.S0.
7. **§11 risks:** added process tax, orphaned solutions, and customization sprawl.
8. **§12 kill criterion:** now has two tests, technical portability **and** effort saved. Portability without effort saved does not count as leverage.
9. **§13 Open Decisions:** added D-7 (operating contract / maintaining owner), D-8 (partner-framework scope: Palantir, Uniphore), and D-9 (exception process). Added the reviewer's central question to FDE leadership as a discovery input to D-0.
10. **§14 FDE Review Map** (new): maps the eight expected FDE questions to the sections that answer them.
11. **Fix:** a stale v2 reference "metering/attribution (FR-13–15)" in §11 now reads FR-22–24.

- **Also changed:** [[Milestone Release Map]] — MK.S0, S1, and S3 stage rows synced (realistic workflow + effort baseline; framework-agnostic SDK, dev loop, generated manifest, promotion path; operating contract + handoff).

## Edges

- **Added:** PRD → [[Load-Bearing Bets]] (partner platforms); stronger links to [[AI Operations Product]] (FR-18b, D-7) and [[Three Battlegrounds]].
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| prd-solution-marketplace | assumed | assumed | Deeper spec for a proposed initiative; nothing built. |

No performance numbers are asserted. The reviewer's 1–10 scores are qualitative review judgments and are **not** recorded in the PRD. The operating-contract table is labeled as a hypothesis.

## Open Questions / Decisions

- **Created:** D-7, D-8, D-9. **Sharpened:** D-0 (now includes the extension-point contract and the FDE leadership discovery question).

## Downstream Propagation Check

- **Dependent notes updated?** The release map is re-synced. The [[Packaged Solution]] and [[Solution Marketplace]] entities were checked, and their definitions still hold. Operating modes describe how the rails are *used*; a Packaged Solution is still only the reusable unit (mode 3). The entity's "Authored" lifecycle state is consistent with this because experiments and deployments come before a solution enters that lifecycle. No entity edit was required.
- **Canonical IDs/aliases preserved?** Yes.
- **Formulas/metrics/scorecards?** "Authoring overhead" is a PRD-local success measure, not a canonical Metric note.
- **Source-to-Concept Crosswalk?** No new source concept; the review is logged here.
- **One-Concept / layer purity?** Held.

## Fitness / Consistency Result

- Structural: **Pass** — `kg.py broken`: 0 unresolved; frontmatter lint: all 250 files pass.
- PRD checks P-01…P-08: **Pass** — canonical link kept; all ten items present (kill criterion strengthened); new D-7…D-9 each have an owner and a "blocks" entry; FR cross-references (FR-1a…FR-18b, S-row ranges) are consistent; `assumed` throughout.
- Regressions: none.

## See Also

- [[Solution Marketplace PRD]] · [[Solution Marketplace]] · [[Packaged Solution]]
- [[CHANGE_2026-10-06 Solution Marketplace PRD v2 Eng Review]]
- [[Milestone Release Map]] · [[Wiki Hub]]
