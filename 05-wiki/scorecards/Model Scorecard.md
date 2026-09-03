---
id: idx-model-scorecards
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [model scorecard, model scorecards, scorecard index, operating scorecard]
related: [hub-wiki, idx-scorecard-deepseek, idx-scorecard-glm, idx-scorecard-nemotron]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Index of the per-model operating scorecards and the metric rows every scorecard tracks."
---

# Model Scorecard

## Purpose

Every priority [[Model]] has a continuously visible **operating scorecard** (strategy: "The Operating Scorecard"). This index defines the concept and lists the per-model scorecards. Each scorecard summarizes the canonical Layer-2 metrics for one model; it does not redefine them. OpenRouter rank is treated as an outcome of these metrics, never a directly optimized target.

## Per-Model Scorecards

| Model | Scorecard | Role |
|-------|-----------|------|
| [[DeepSeek V4 Flash]] | [[DeepSeek V4 Flash Scorecard]] | Win now — benchmark |
| [[GLM 5.3 Flash]] | [[GLM 5.3 Flash Scorecard]] | Win now — growth |
| [[Nemotron 3 Ultra]] | [[Nemotron 3 Ultra Scorecard]] | Bet ahead |

## Tracked Metrics

Every scorecard tracks these rows, each linked to its canonical metric note, each carrying a confidence state and a benchmark/telemetry source:

| Metric | Target Direction | Canonical Note |
|--------|:----------------:|----------------|
| GPU utilization | ↑ | [[Productive GPU Utilization]] |
| Tokens/sec/GPU | ↑ | [[Tokens per GPU-Second]] |
| Output throughput | ↑ | [[Output Throughput]] |
| P50 / P95 TTFT | ↓ | [[TTFT]] |
| Queueing delay | ↓ | [[TTFT]] |
| Availability | ↑ | [[Availability]] |
| Error rate | ↓ | [[Availability]] |
| Model launch lag | ↓ | [[Model Launch Lag]] |
| Capability coverage | ↑ | — |
| Cost / 1M tokens | ↓ | [[Cost per 1M Tokens]] |
| Revenue / GPU-hour | ↑ | [[Revenue per GPU-Hour]] |

## See Also

- [[Wiki Hub]]
- [[Metric Index]]
- [[KPI Hierarchy]]
