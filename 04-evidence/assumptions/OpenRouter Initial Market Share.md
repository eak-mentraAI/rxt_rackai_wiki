---
id: asm-openrouter-initial-share
type: assumption
status: draft
owner: product
domain: commercial
aliases: [openrouter initial market share, rackspace openrouter share, provider pool share assumption]
related: [hub-evidence, idx-assumption-register, idx-gpu-capacity-demand-rationale, asm-traffic-follows-performance, bench-openrouter-leaderboard-2026-09, idx-openrouter-integration-plan]
source_docs: ["reference/RackAI - GPU Capacity.xlsx"]
confidence: assumed
last_reviewed: 2026-09-24
parent: hub-evidence
summary: "RackAI will capture <1% of a model's OpenRouter pool volume at launch, growing to 15–25% base case."
---

# OpenRouter Initial Market Share

## Statement

At public provider launch (Phase 3), RackAI will capture **less than 1% of a given model's total OpenRouter token volume** across all providers. A base-case trajectory of 15–25% share is achievable within 3–6 months of sustained competitive performance.

## Rationale

OpenRouter routes proportionally to latency, throughput, uptime, and price within a provider pool. As a new entrant RackAI starts with no routing history and no uptime score (OpenRouter begins uptime scoring after 100+ requests, so score accumulates quickly, but rank is depressed until it does). The pool for GLM 5.3 Flash processes ~11.4T tokens/week across all providers; even a 1% share represents ~114B tokens/week, which at ~750 tok/GPU-sec on 10 GPUs exceeds the proposed launch capacity. The realistic starting position is therefore a fraction of 1%, with growth tracking rank improvement.

The three scenarios from [[GPU Capacity Demand Rationale]]:

| Scenario | Share | Condition |
|----------|:-----:|-----------|
| Conservative (launch) | <1% | New entrant, rank establishing, conformance ramp |
| Base (3–6 months) | 15–25% | Full conformance, competitive TTFT/throughput, good uptime |
| Optimistic (post-AMD) | 30–40% | AMD capacity live, pricing competitive, strong rank |

## Exit Criterion

Phase 3 live traffic telemetry showing actual RackAI share of the GLM provider pool over a 4-week window. Upgrades to `measured` once first traffic data is available.

## Impacts

| Impacted | Type |
|----------|------|
| [[GPU Capacity Demand Rationale]] | SUPPORTS |
| [[Demand Forecasting]] | CONSTRAINS |
| [[Productive GPU Utilization]] | CONSTRAINS |

## Status

- Confidence: `assumed`
- Owner: product
- Target resolution date: Phase 3 launch + 4 weeks

## See Also

- [[Assumption Register]]
- [[OpenRouter Traffic Follows Performance]]
- [[OpenRouter Leaderboard Snapshot]]
- [[GPU Capacity Demand Rationale]]
