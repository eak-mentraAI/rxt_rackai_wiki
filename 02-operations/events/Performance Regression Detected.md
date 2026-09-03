---
id: evt-performance-regression-detected
type: event
status: draft
owner: performance-eng
domain: performance
aliases: [performance regression detected, regression alert, promotion blocked]
related: [wf-closed-loop-optimization, pol-performance-regression-gate, met-ttft, met-tokens-per-gpu-second, met-output-throughput, ent-model-deployment, ent-benchmark-run]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Signals that a config change worsened a performance metric beyond threshold and must block promotion."
---

# Performance Regression Detected

## Definition

Signals that a candidate runtime or configuration change materially worsened [[TTFT]], [[Tokens per GPU-Second]], error rate, quality, or cost/token beyond an allowed threshold. The event blocks promotion of that change to production. Emitted during [[Closed-Loop Optimization]] and enforced by [[Performance Regression Gate]]. (Roadmap Milestone 6.2.)

## Payload

| Field | Type | Description |
|-------|------|-------------|
| candidate_id | string | The experimental config under evaluation |
| model | ref | Model affected |
| metric | enum | Which signal regressed (ttft / tokens-per-gpu-second / error-rate / quality / cost-per-token) |
| baseline_value | float | Prior known-good value |
| observed_value | float | Regressed value |
| threshold | float | Materiality threshold breached |
| benchmark_ref | ref | [[Benchmark Run]] providing the comparison |
| detected_at | timestamp | When the regression was detected |

## Emitted By

| Source | Workflow | Condition |
|--------|----------|-----------|
| Regression gate | [[Closed-Loop Optimization]] | Candidate breaches a materiality threshold on any tracked signal |

## Consumed By

| Consumer | Action Taken |
|----------|--------------|
| [[Performance Regression Gate]] | Blocks promotion to production |
| [[Closed-Loop Optimization]] | Returns candidate to lab for rework |
| Performance-eng dashboards | Records regression against the candidate |

## See Also

- [[Operations Hub]]
