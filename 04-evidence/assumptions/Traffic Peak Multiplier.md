---
id: asm-traffic-peak-multiplier
type: assumption
status: draft
owner: product
domain: capacity
aliases: [traffic peak multiplier, peak to average ratio, peak traffic multiplier, 3x peak assumption]
related: [hub-evidence, idx-assumption-register, idx-gpu-capacity-demand-rationale, wf-demand-forecasting, asm-openrouter-initial-share]
source_docs: ["reference/RackAI - GPU Capacity.xlsx"]
confidence: assumed
last_reviewed: 2026-09-24
parent: hub-evidence
summary: "Inference traffic peaks at 3× the daily average; used to size GPU capacity floor for prod deployments."
---

# Traffic Peak Multiplier

## Statement

Inference traffic for OpenRouter-routed workloads peaks at approximately **3× the daily average throughput**. GPU capacity must be sized to serve the peak, not the average, to maintain uptime scoring and avoid queue depth growth that degrades rank.

## Rationale

Agentic and coding workloads (the primary GLM 5.3 Flash use case) follow user activity patterns — morning/afternoon business-hours peaks, with troughs overnight. A 3× peak-to-average ratio is a conservative industry estimate for API-driven AI inference workloads; the real ratio for RackAI's specific traffic pattern is unknown until Phase 1 telemetry is available.

Used in [[GPU Capacity Demand Rationale]] to derive the peak GPU requirement from an average throughput estimate:

```
peak_tok_per_sec = avg_tok_per_sec × 3
gpus_required    = peak_tok_per_sec / tokens_per_gpu_second
```

## Exit Criterion

Phase 1 private-model telemetry showing the hourly request distribution over at least a 2-week window. Upgrades to `measured` once an empirical peak-to-average ratio is observed. If the measured ratio differs materially from 3×, [[GPU Capacity Demand Rationale]] and the prod capacity proposal should be revisited.

## Impacts

| Impacted | Type |
|----------|------|
| [[GPU Capacity Demand Rationale]] | SUPPORTS |
| [[Demand Forecasting]] | CONSTRAINS |

## Status

- Confidence: `assumed`
- Owner: product
- Target resolution date: Phase 1 telemetry (4+ weeks of private model traffic)

## See Also

- [[Assumption Register]]
- [[GPU Capacity Demand Rationale]]
- [[Demand Forecasting]]
