---
id: chg-2026-10-06-milestone-release-map
type: change
status: draft
owner: product
domain: strategy
aliases: [milestone release map change, release map projection change 2026-10-06]
related: [wiki-milestone-release-map, hub-roadmap, hub-product, hub-minimum-operable-estate, wiki-pillar-working-model]
source_docs: ["00-hub/RackAI Roadmap.md", "05-wiki/Pillar Working Model.md", "00-hub/Three Battlegrounds.md"]
confidence: derived
last_reviewed: 2026-10-06
parent: hub-wiki
summary: "Added the Milestone Release Map: Layer-5 projection of the four-proof roadmap into releases across five tracks."
---

# 2026-10-06 — Milestone Release Map

## Trigger

Request to **map the existing roadmap into major milestone releases** to simplify market and internal messaging, grouped across five functional areas: the core platform, the governance/assurance planes around it, the learning loop that measures and improves the system, a longer-term bet on the model and inference layer, and efficiency (what the system costs and what it's worth).

The canonical [[RackAI Roadmap]] is organized on a *temporal* axis — the four proofs (Observe → Decide → Control → Operate) — which is correct for sequencing and gating but hard to communicate. This change adds a *functional* axis projection without altering the canonical plan.

## Objects Changed

- **Added:** `05-wiki/Milestone Release Map.md` (`wiki-milestone-release-map`, type `index`, confidence `derived`). A Layer-5 communication projection, not a new source. Contents:
  - **Five tracks**, each anchored to its canonical pillar: **T1 Core Platform** ([[Inference and Serving Services]]), **T2 Governance & Assurance** ([[AI Governance and Assurance]] + [[AI Harness]] runtime), **T3 Learning Loop** ([[AI Harness]] / [[Empirical Map]], fed by [[Inference Optimization]] + Serving), **T4 Model & Inference Bet** ([[Model Services]] + [[Inference Optimization]]), **T5 Efficiency & Economics** ([[Inference Optimization]] FinOps / [[AI FinOps]]).
  - Each track expressed as a sequence of **major releases** `T<track>.R<n>`, each with a theme, deliverables, the roadmap items it absorbs, a **proof tag**, and a state marker (🟢 shipped / 🟡 in progress / 🔴 gap→P-00x / ⚪ sequenced later).
  - **Two headline cross-track releases** — MOE-0 (rehearsal) and MOE-1 (paid identity proof) — tied to [[Minimum Operable Estate]] and kill criteria K1.
  - A **Track × Proof crosswalk** proving the two axes are the same plan, and a **D1–D4 executive-decision** mapping.
  - A "how to use" section separating the external (market) read from the internal planning read.
- **Changed:** [[RackAI Roadmap]] — one *See Also* link added to [[Milestone Release Map]] (no meaning change). [[Product Hub]] — one sentence in *Market Positioning* pointing to the release view (no meaning change).
- **Deprecated:** none.

## Edges

- **Added:** [[RackAI Roadmap]] → [[Milestone Release Map]] (See Also); [[Product Hub]] → [[Milestone Release Map]] (Market Positioning). The new note links **down/across** to ~30 pre-existing canonical homes (roadmap, pillars, Empirical Map, Minimum Operable Estate, Pillar Working Model, formulas/coefficients, benchmark standard, model notes) — all verified to resolve. No new concept defined.
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| wiki-milestone-release-map | — | derived | Re-projection of existing `derived`/`gap` roadmap content; no capability upgraded to shipped. State markers mirror the roadmap's own confidence (🔴 items trace to P-00x gaps). |

No performance numbers were introduced. All quantitative framing (margin, cost/token, utilization) is carried by reference to the canonical formulas/coefficients and remains `assumed`/`gap` exactly as in the roadmap. The 🟢/🟡/🔴 markers defer to the [[Capability Gap Register]] as the authority on live state.

## Downstream Propagation Check

- **Dependent notes updated?** The two notes that should surface the new view ([[RackAI Roadmap]], [[Product Hub]]) now link to it. No canonical *definition* changed, so no entity/metric/formula/coefficient/scorecard required edits.
- **Canonical IDs/aliases preserved?** Yes — `hub-roadmap`, `hub-product`, and all referenced IDs unchanged. The new note uses a fresh ID (`wiki-milestone-release-map`).
- **Formulas/metrics/coefficients/scorecards affected?** None — the note references them, does not redefine or alter them.
- **Source-to-Concept Crosswalk?** No row required — no new *source* concept was extracted; this is an internal re-projection of the existing [[RackAI Roadmap]], logged here and in the note's `source_docs`.
- **One-Concept Rule?** Held — the release view is a *projection*; MOE-0/MOE-1 still point to [[Minimum Operable Estate]], the Empirical Map to [[Empirical Map]], etc. No parallel definitions created.
- **Layer purity?** Held — Layer-5 wiki/index note; links down to canonical homes, defines nothing canonical.

## Open Questions Created

None new. The note surfaces the roadmap's existing open questions (release numbering is capability-based because dates live in Craft.io; 🔴 releases depend on the unresolved P-003/P-004/P-005/P-006 proposals) but does not create new ones.

## Fitness / Consistency Result

- Structural checks: **Pass** — all wikilink targets introduced verified to resolve (file_search sweep across Action Controls, Request Routing, AI FinOps, Capability Gap Register, Multi-Cluster Governance Brief, AgentX Benchmark Standard, Gross Margin per Model, Revenue per GPU-Hour, Cost per GPU-Hour, OpenRouter Integration Plan — 0 missing).
- Consistency pass: **Pass** — track→pillar mapping matches [[Pillar Working Model]]; proof tags match the [[RackAI Roadmap]] proof assignments; state markers consistent with the roadmap's gap/P-00x labels; no contradiction with the canonical plan.
- Confidence propagation: **Pass** — `derived`, nothing upgraded, no numbers asserted.
- Regressions: none.

## See Also

- [[Milestone Release Map]]
- [[RackAI Roadmap]]
- [[Wiki Hub]]
- [[CHANGE_PACKET]]
