---
id: chg-2026-10-07-graph-link-integrity
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [graph link integrity, broken link repair 2026-10-07, unresolved reference cleanup]
related: [pol-fitness-checklist, pol-regression-suite, hub-ai-operations-product, src-rackai-org-design, hub-inference-optimization]
source_docs: ["python3 .claude/tools/kg.py broken run 2026-10-07"]
confidence: validated
last_reviewed: 2026-10-07
parent: hub-wiki
summary: "Repointed 30 unresolved graph refs to canonical IDs/titles; 2 aliases added, 3 false positives remain."
---

# 2026-10-07 — Graph Link Integrity

## Trigger

`python3 .claude/tools/kg.py broken` reported **33 unresolved references**. These were stale or misspelled frontmatter IDs in `related`, plus body wikilinks to titles that have no canonical note. Fitness checks S-03 (no broken backlinks) and S-01 (one canonical home) apply. No `id:` values were changed (S-14), and no aliases were removed (S-15).

## What Changed

| Unresolved ref | Where | Resolution |
|---|---|---|
| "Product Operations" wikilink (×7) | 6 pillar hubs in `00-hub/`, [[Pillar Working Model]] | Added alias `product operations` to [[AI Operations Product]] (`hub-ai-operations-product`). [[RackAI Organizational Design]] names pillar 6 "AI Operations Product (Product Operations)", so it is the canonical home and the alias is a true synonym. |
| `ent-nvidia-h100`, `ent-nvidia-l40s`, `ent-nvidia-a30`, `ent-amd-instinct` | [[Inference Optimization]] `related` | → `ent-gpu-h100`, `ent-gpu-l40s`, `ent-gpu-a30`, `ent-gpu-amd-instinct` |
| `met-productive-gpu-utilization` | [[Inference Optimization]] `related` | → `met-gpu-utilization` ([[Productive GPU Utilization]]) |
| `coef-fp8-throughput-factor`, `coef-kv-cache-hit-rate`, `coef-speculative-decoding-acceptance-rate` | [[Inference Optimization]] `related` | → `coeff-fp8-throughput`, `coeff-kv-cache-hit-rate`, `coeff-spec-decode-acceptance` |
| "RackAI Organizational Design (Source)" wikilink | [[RackAI Organizational Design]] (hub) | Added alias `rackai organizational design (source)` to `src-rackai-org-design`. The hub and the source share a filename, so the link uses this disambiguating name. |
| `ent-openrouter-provider-integration` (×4) | [[Model Launch Lag]], [[Availability]], [[Request Routing]], [[Billing & Payment]] | → `ent-openrouter-integration` ([[OpenRouter Provider Integration]]) |
| `oq-open-questions` | [[Billing & Payment]] | → `idx-open-questions` |
| `hub-openrouter-initiative` | [[Erebine Competitive Analysis]] | → `hub-openrouter` |
| `hub-commercial-capacity` (×2) | [[Erebine Competitive Analysis]], [[KPI Telemetry Target List]] | → `hub-commercial` |
| `hub-rackai-roadmap` (×2) | [[Uniphore Recovery Plan — RackAI Input]], [[CHANGE_2026-10-02 Uniphore Recovery Plan]] | → `hub-roadmap` |
| `wf-serving-lifecycle` | [[Uniphore Recovery Plan — RackAI Input]] `related` | → `hub-model-services`. No serving-lifecycle workflow exists. The note uses "lifecycle" to mean model onboarding → versioning → retirement, which [[Model Services]] owns. |
| `chg-kg-test-results` and the "Knowledge Graph Acceptance Test Results" wikilink | [[REGRESSION_SUITE]] | The note never existed. Repointed to `chg-consistency-report` ([[CONSISTENCY_REPORT]]), the existing run-output template. |
| "Metric" wikilink | [[CHANGE_2026-10-06 Solution Marketplace PRD v2 Eng Review]] | → [[Metric Index]] (display text "Metric"). There is no "Metric" type note; the Metric Index is the canonical register. |

Result: `kg.py broken` went from **33 to 3**. `./scripts/lint-frontmatter.sh` passes.

## Open items

- **False positives (left as-is):**
  - The double-bracketed word "wikilinks" is literal inline-code text in [[FITNESS_CHECKLIST]] (S-03 row) and in `05-wiki/changelogs/2026-09-03 Corpus Buildout.md`.
  - The CSV attachment link in [[Milestone Release Map]] is a valid Obsidian attachment link; the file exists at `05-wiki/RackaI Roadmap 10062026.csv`. `kg.py` indexes only `.md` files, so it flags attachment links. Recommendation: teach `kg.py broken` to skip links to existing non-`.md` files, or to skip inline code.
- [[REGRESSION_SUITE]] `source_docs` still names `05-wiki/Knowledge Graph Acceptance Test Results.md`, which does not exist. `source_docs` is not a graph edge. Recommendation: either create the test-run log when the suite is first run, or set `source_docs: []`.
- The body of [[CHANGE_2026-10-02 Uniphore Recovery Plan]] still lists `hub-rackai-roadmap` and `wf-serving-lifecycle` in a code span. It was left unchanged as a historical record; its frontmatter `related` is now correct.
