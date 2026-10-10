---
id: chg-2026-10-08-regression-baseline
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [regression suite baseline, first regression run, regression baseline 2026-10-08 change]
related: [pol-regression-suite, pol-fitness-checklist, chg-kg-test-results, chg-2026-10-07-graph-link-integrity]
source_docs: [05-wiki/Knowledge Graph Acceptance Test Results.md, "python3 .claude/tools/kg.py run 2026-10-08"]
confidence: measured
last_reviewed: 2026-10-08
parent: hub-wiki
summary: "First regression suite run: baseline avg 3.71 (Warning); results note created; REGRESSION_SUITE scored."
---

# 2026-10-08 — Regression Suite Baseline

## Trigger

[[REGRESSION_SUITE]] was defined on 2026-09-03 but never scored. Its Baseline Scores table said "TBD". The 2026-10-07 link cleanup ([[CHANGE_2026-10-07 Graph Link Integrity]]) had temporarily pointed it at [[CONSISTENCY_REPORT]] because the test-run log did not exist. Now that the entity and operational layers are populated, the suite was run in full (R-01 to R-07) for the first time.

## What Changed

| File | Change |
|---|---|
| `05-wiki/Knowledge Graph Acceptance Test Results.md` (`chg-kg-test-results`) | **New.** Run log: method, a section per test (score, path traversed, gaps, efficiency), scorecard, verdict, and 10 prioritized improvement actions. |
| `08-change-control/REGRESSION_SUITE.md` (`pol-regression-suite`) | Filled in Baseline Scores and added a 2026-10-08 Score History row. Restored `chg-kg-test-results` in `related` and [[Knowledge Graph Acceptance Test Results]] in See Also. Kept [[CONSISTENCY_REPORT]] as the template link. `source_docs` already named the results note and now resolves. `last_reviewed` set to 2026-10-08. |

No IDs were changed (S-14). No aliases were removed (S-15). No content gaps were fixed in this change. All gaps are recorded as actions only.

## Results

| R-01 | R-02 | R-03 | R-04 | R-05 | R-06 | R-07 | Average |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3.5 | 3.5 | 3.5 | 4.0 | 3.5 | 3.5 | 4.0 | **3.71** |

**Verdict:** Warning (FITNESS_CHECKLIST thresholds); Conditional pass (REGRESSION_SUITE). R-01, R-02 and R-03 are below their ≥ 4/5 minimum. No test is below the 3/5 hard stop.

## Downstream Impact

- None to canonical content. The run is observational.
- The confidence of [[REGRESSION_SUITE]] is unchanged.
- The results note is `measured`: it records an observed run, not a projection.

## Open Items

- Improvement actions 1–3 (typed Relationships on formula, metric, coefficient and event notes; a canonical demand node; FP8 → memory → capacity edges) are needed to bring R-01 to R-03 up to ≥ 4 before the next release.
- Two questions should be added to [[Open Questions]]: (a) the `bench-/val-deepseek-h200-fp8` IDs describe **H100**; (b) does `confidence` refer to the definition or to the value? (C-06.)
- `kg.py` gaps (no `owner` in `show`, no `orphans`/`health` command, body dependency tables not parsed as edges) are recorded for the tool owner. The tool was not changed here.

## Verification

- `./scripts/lint-frontmatter.sh`: pass.
- `python3 .claude/tools/kg.py broken`: 0 unresolved references.
