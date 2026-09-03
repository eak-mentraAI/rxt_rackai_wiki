---
id: chg-2026-09-03-corpus-buildout
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [corpus buildout, 2026-09-03 buildout, initial corpus change]
related: [hub-wiki, src-strategic-vision, src-engineering-roadmap]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Build-out of the supporting corpus from the Strategic Vision and Engineering Roadmap narratives."
---

# 2026-09-03 — Corpus Buildout

## Trigger

Build-out of the supporting documentation from the two source narratives: the [[Rack AI OpenRouter Strategic Vision]] and the [[Rack AI OpenRouter Engineering Roadmap]]. These provide the operating scorecard, KPI hierarchy, milestone sequence, and phased engineering plan from which the canonical corpus is extracted.

## Objects Changed

- Added:
  - **L1 entities (15):** the canonical semantic backbone — [[Model]], [[Model Deployment]], [[Model Deployment Specification]], [[Serving Runtime]], [[GPU Node]], [[GPU Cluster]], [[Capacity Pool]], [[Region]], [[Topology]], [[OpenRouter Provider Integration]], [[Benchmark Run]], [[Traffic Class]], and the three priority model instances [[DeepSeek V4 Flash]], [[GLM 5.3 Flash]], [[Nemotron 3 Ultra]].
  - **L2 operational notes (31):** 8 workflows, 4 events, 6 metrics, 5 formulas, 4 coefficients, and 4 policies covering launch, serving, scheduling, and optimization behavior.
  - **L3 commercial notes:** unit-economics, pricing, and capacity-pool notes derived from the cost model and revenue/GPU-hour logic.
  - **L4 evidence notes:** benchmark, assumption, validation, and open-question notes recording that performance/economic values are not yet measured.
  - **L5 wiki notes:** three model scorecards, the Metric Index, Entity Index, KPI Hierarchy, Glossary, Serving Platform MOC, and this changelog.

## Edges

- Added:
  - The **abstraction-chain edges** — Market Demand → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → GPU Fleet ([[GPU Node]]/[[GPU Cluster]]) → [[Topology]].
  - The **metric → formula → coefficient chains** — e.g. [[Tokens per GPU-Second]] and [[Cost per 1M Tokens]] linked to their calculation formulas and the coefficient inputs those formulas consume.
- Removed:
  - None.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| All performance metric notes | — | assumed | No benchmark runs yet; targets are strategy/roadmap intent, not measurements. |
| All economic notes (cost/1M tokens, revenue/GPU-hour) | — | assumed | No production telemetry or cost measurements captured yet. |
| Model scorecards (DeepSeek, GLM, Nemotron) | — | assumed | Summaries of not-yet-measured metrics; every "Current" is "no run yet". |
| Indexes / Glossary / MOC / this changelog | — | validated | Describe the corpus itself, which exists as authored. |

## Open Questions Created

| Question | Affected Docs |
|----------|---------------|
| See the open-questions register for the full list raised by this buildout. | [[Open Questions]] |

## Fitness / Consistency Result

- Structural checks: **Pass.** Frontmatter lint clean across all 101 notes (`scripts/lint-frontmatter.sh`). No duplicate canonical IDs (S-01, S-14). All `[[wikilinks]]` across the content layers resolve to existing notes (S-03). Every note carries owner, source_docs, and a confidence state (S-05/06/07).
- Consistency pass: **Pass.** Abstraction chain intact — Market Demand → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Topology (C-05). Layers kept distinct: L3/L4/L5 reference L1/L2 canonical homes and never redefine them (C-04). Targets vs. results distinct — all performance/economic values sit at `assumed`; no roadmap target is presented as measured (C-06/C-09).
- Diagrams: all Mermaid, no forced colors/styles.
- Regressions: not run (no release cut). Recommended next: seed the first Benchmark Run to begin upgrading `assumed` → `measured`.

## See Also

- [[Wiki Hub]]
- [[CHANGE_PACKET]]
