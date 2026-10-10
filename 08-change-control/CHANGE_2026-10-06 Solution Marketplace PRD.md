---
id: chg-2026-10-06-solution-marketplace-prd
type: change
status: draft
owner: product
domain: product
aliases: [solution marketplace prd change, prd template change]
related: [prd-solution-marketplace, ent-solution-marketplace, ent-packaged-solution, hub-roadmap, hub-eac-product-model]
source_docs: ["01-entities/Solution Marketplace.md", "PM/leadership marketplace discussion 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Added a reusable PRD template and the draft Solution Marketplace PRD scoping the RackAI-owned rails."
---

# 2026-10-06 — Solution Marketplace PRD + PRD Template

## Trigger

Follow-up to the [[Solution Marketplace]] modeling: the user wanted a **PRD** for the marketplace initiative (distinct from the canonical entity note). The corpus recognizes PRDs as an artifact type (the roadmap flags "sunsetting a model has no PRD yet"; source PRDs live in `06-sources/`) but had **no PRD template** and no authored-here PRD. Chose to create a reusable template first, then write the marketplace PRD against it.

## Objects Changed

- **Added — `templates/prd.md`:** reusable PRD house format. Uses `type: index` (no `prd` type exists in the frontmatter schema; PRD-ness is carried in title/body/banner). Sections 1–12 (Summary, Problem, Goals/Non-Goals, Users, Journeys, Functional Reqs, NFRs, Scope/Phasing, Success Metrics, Dependencies, Risks, Open Decisions) + a mandatory banner distinguishing *proposed* from *funded* and pointing at the canonical note.
- **Added — `05-wiki/Solution Marketplace PRD.md`** (`prd-solution-marketplace`, `assumed`): the PRD. Scopes the **rails only** (SDK, submission→certification gate, catalog/instantiation, metering/attribution); explicitly non-goals the solution authoring, a public app store, billing implementation, and GPU exposure. Two-sided users (authors / consuming customers); worked journey via [[Sovereign Private Assistant]]; 15 functional requirements (MUST/SHOULD/MAY) grouped by rail; isolation as the load-bearing NFR; phasing tied to the release-map stages MK.S1–S5; success metrics (re-instantiation ratio, workloads/FTE, Empirical-Map instrumentation) with zero/none baselines; dependencies; risks + a falsification/kill criterion; 5 Open Decisions (commercial model, certification bar, SDK surface, corpus binding, sequencing).
- **Changed — [[Solution Marketplace]]:** See Also → [[Solution Marketplace PRD]].
- **Changed — [[RackAI Roadmap]]:** marketplace subsection now points to the PRD alongside the entity.
- **Deprecated:** none.

## Edges

- **Added:** [[Solution Marketplace]] ↔ [[Solution Marketplace PRD]]; PRD → [[Packaged Solution]], [[Sovereign Private Assistant]], [[Enterprise AI Cloud Product Model]], [[AI Operations Product]], [[Milestone Release Map]], [[Metering]], [[Agent Identity]], [[AI Governance and Assurance]], [[Multi-Cluster Governance Brief (Partner)]], [[Billing & Payment]], [[Dataset]] — all verified to resolve.
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| prd-solution-marketplace | — | assumed | PRD for a proposed, unbuilt initiative; requirements are intent, not commitments. Banner states this explicitly. |
| templates/prd.md | — | n/a (template) | Reusable scaffold; carries placeholder `assumed`. |

No performance numbers asserted. Success metrics carry **zero/none baselines** and target *postures*, not measured values. All requirements point to the `assumed` rails; the PRD does not upgrade any capability.

## Open Questions / Decisions

The PRD **surfaces** (does not create new beyond) the five Open Decisions already tracked on [[Solution Marketplace]]: commercial/rev-share model (D-1), sovereign-tenant certification bar (D-2), SDK surface (D-3), corpus-binding primitive (D-4), and proving-ground sequencing (D-5). These are now enumerated with owners and what each blocks.

## Downstream Propagation Check

- **Dependent notes updated?** Entity ↔ PRD linked both ways; roadmap points to the PRD. No canonical *definition* changed — the PRD projects from [[Solution Marketplace]] / [[Packaged Solution]] and does not redefine them (One-Concept Rule stated in the PRD banner).
- **Canonical IDs/aliases preserved?** Yes — new IDs only (`prd-solution-marketplace`, `prd-{slug}` template).
- **Formulas/metrics/coefficients/scorecards?** None introduced; the PRD references workloads/FTE and the Empirical Map as consumers, not new definitions.
- **Source-to-Concept Crosswalk?** No new source — the PRD is an authored projection of the already-registered 2026-10-06 marketplace discussion; logged here.
- **Layer purity?** Held — PRD is a Layer-5 authored artifact linking down to L1 entities; the template is a scaffold under `templates/`.

## Fitness / Consistency Result

- Structural: **Pass** — all PRD wikilinks resolve (0 missing).
- Consistency: **Pass** — PRD scope (rails only) matches the [[Enterprise AI Cloud Product Model]] boundary and the [[Solution Marketplace]] entity; phasing matches the [[Milestone Release Map]] MK.S1–S5; billing framed as a dependency/non-goal consistent with the [[Billing & Payment]] gap; nothing re-defined.
- Confidence propagation: **Pass** — `assumed` throughout; baselines zero/none; no capability upgraded.
- Regressions: none.

## See Also

- [[Solution Marketplace PRD]] · [[Solution Marketplace]] · [[Packaged Solution]]
- `templates/prd.md` — the reusable PRD format
- [[Wiki Hub]] · [[CHANGE_PACKET]]
