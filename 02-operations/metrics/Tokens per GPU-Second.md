---
id: met-tokens-per-gpu-second
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [tokens per gpu-second, tokens/gpu-second, tokens/sec/gpu, core efficiency metric]
related: [fml-tokens-per-gpu-second, fml-gpu-hours-per-1m-tokens, fml-cost-per-1m-tokens, met-output-throughput, met-ttft, ent-model-deployment, ent-benchmark-run]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Core infrastructure-efficiency metric: output tokens produced per GPU-second."
---

# Tokens per GPU-Second

## Definition

The core efficiency metric — how many output tokens the fleet produces per GPU-second of compute. It answers whether we are becoming better at producing inference from the hardware we own, and it is the primary internal lever behind cost/token. Track per [[Model Deployment]] and per [[Benchmark Run]].

## Unit

output tokens / GPU-second.

## Source or Formula

- Derived from: [[Tokens per GPU-Second Formula]] (`fml-tokens-per-gpu-second`) — output token count over GPU-seconds consumed.
- Measured from: production telemetry (token volume, GPU-hours consumed) once deployments exist.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | Maximize (no measured baseline yet) | Must not degrade [[TTFT]] beyond SLO |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — no measured Rack AI baseline exists yet. The direction (↑) is roadmap-mandated (KPI #2); actual values require a [[Benchmark Run]]. Throughput improvements must be traded off against [[TTFT]] per the roadmap's continuous-batching guidance.

## See Also

- [[Operations Hub]]
