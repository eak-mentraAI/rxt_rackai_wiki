---
id: hub-wiki
type: hub
status: draft
owner: knowledge-graph-steward
domain: platform
aliases: [wiki hub, L5 hub, navigation hub]
related: [hub-root, hub-governance]
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Layer 5 navigation hub for indexes, scorecards, changelogs, and glossary."
---

# Wiki Hub

Layer 5 — the human navigation layer. Indexes, MOCs, model scorecards, changelogs, and the glossary that expose the underlying graph.

## Sections

| Section | Folder | Template |
|---------|--------|----------|
| Indexes | `05-wiki/indexes/` | `templates/index.md` |
| MOCs | `05-wiki/mocs/` | — |
| Model Scorecards | `05-wiki/scorecards/` | see below |
| Changelogs | `05-wiki/changelogs/` | `templates/change.md` |
| Glossary | `05-wiki/glossary/` | `templates/glossary.md` |

## Model Scorecards

Every priority model gets a continuously updated scorecard tracking the operating metrics from the strategy: GPU utilization, tokens/sec/GPU, output throughput, TTFT, queueing delay, availability, error rate, launch lag, capability coverage, cost/1M tokens, revenue/GPU-hour. Each row must cite a benchmark run or telemetry source and carry a confidence state.

- [[Model Scorecard]] — scorecard concept + index
- [[DeepSeek V4 Flash Scorecard]]
- [[GLM 5.3 Flash Scorecard]]
- [[Nemotron 3 Ultra Scorecard]]

## Indexes, Glossary & MOCs

- [[Entity Index]] · [[Metric Index]] · [[KPI Hierarchy]]
- [[Glossary]]
- [[Serving Platform MOC]]
- [[2026-09-03 Corpus Buildout]] — buildout changelog

## Change Control

- [[FITNESS_CHECKLIST]]
- [[REGRESSION_SUITE]]
- [[CONSISTENCY_REPORT]]
- [[CHANGE_PACKET]]

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[Governance Hub]]
