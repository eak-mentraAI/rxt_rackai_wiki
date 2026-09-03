---
id: idx-metrics
type: index
status: draft
owner: knowledge-graph-steward
domain: performance
aliases: [metric index, metrics index, L2 metric listing]
related: [hub-wiki, hub-operations, idx-kpi-hierarchy]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-wiki
summary: "Index of the canonical Layer-2 operating metrics for the Rack AI inference platform."
---

# Metric Index

## Purpose

Lists the canonical Layer-2 (L2) operational metrics that define how the Rack AI inference platform is measured. Each metric is defined once, in its canonical note; this index only points to those homes and records their current graph status. It is kept current as metric notes are created and their confidence changes.

## Entries

| Item | ID | Type | Status | Confidence |
|------|----|------|--------|:----------:|
| [[Tokens per GPU-Second]] | met-tokens-per-gpu-second | metric | draft | assumed |
| [[TTFT]] | met-ttft | metric | draft | assumed |
| [[Output Throughput]] | met-output-throughput | metric | draft | assumed |
| [[Productive GPU Utilization]] | met-gpu-utilization | metric | draft | assumed |
| [[Availability]] | met-availability | metric | draft | assumed |
| [[Model Launch Lag]] | met-model-launch-lag | metric | draft | assumed |

## Notes

- Individual metric values are `assumed` until a [[Benchmark Run]] or production telemetry supports them. This index describes the corpus of metric notes and is itself `validated`.

## See Also

- [[Wiki Hub]]
- [[KPI Hierarchy]]
