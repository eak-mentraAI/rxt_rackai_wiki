---
id: met-tokens-per-gpu-second
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [tokens per gpu-second, tokens/gpu-second, tokens/sec/gpu, core efficiency metric]
related: [fml-tokens-per-gpu-second, fml-gpu-hours-per-1m-tokens, fml-cost-per-1m-tokens, met-output-throughput, met-ttft, ent-model-deployment, ent-benchmark-run, fml-revenue-per-gpu-hour, ent-serving-runtime, wf-closed-loop-optimization, evt-performance-regression-detected, asm-spec-decode-beneficial, val-deepseek-h200-fp8, val-erebine-inference-claims, wf-model-launch-factory, pol-performance-regression-gate, idx-scorecard-glm, idx-scorecard-deepseek, evd-kpi-telemetry-targets]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Core infrastructure-efficiency metric: output tokens produced per GPU-second."
---

# Tokens per GPU-Second

## Definition

The core efficiency metric — how many output tokens the fleet produces per GPU-second of compute. It answers whether we are becoming better at producing inference from the hardware we own, and it is the primary internal lever behind cost/token. Track per [[Model Deployment]] and per [[Benchmark Run]].

## KPI Job

Serves internal operating decisions (the primary efficiency lever behind the scheduler and cost/token) and strategic positioning (jobs 1 and 4, per [[KPI Telemetry Target List]]). Requires two feeds to meet at deployment grain: the serving output-token count and GPU-seconds consumed — the join point is the open question, not the raw signals.

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

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model Deployment]] | → | Tracked per deployment |
| DERIVES | [[Tokens per GPU-Second Formula]] | ← | Formula computes this metric |
| PRODUCES | [[Benchmark Run]] | ← | Benchmark runs produce values (none yet) |
| CONSTRAINS | [[Serving Runtime]] | ← | Batching, kernels, parallelism and cache config set achievable throughput |
| CONSUMES | [[GPU-Hours per 1M Tokens]] | ← | Downstream cost chain |
| CONSUMES | [[Revenue per GPU-Hour]] | ← | Downstream yield |
| DEPENDS_ON | [[Closed-Loop Optimization]] | ← | Primary efficiency signal of the loop |
| CONSTRAINS | [[TTFT]] | ← | Throughput gains must not breach the TTFT SLO |
| GENERATES | [[Performance Regression Detected]] | → | A material drop in a candidate config fires the event (lab gate only) |
| SUPPORTS | [[Speculative Decoding Beneficial]] | ← | Assumed throughput gain |
| VALIDATES | [[Validate DeepSeek H100 FP8]] | ← | Would set the first measured baseline |
| VALIDATES | [[Validate Erebine Inference Claims]] | ← | External competitive datapoint |

## Evidence

- Confidence rationale: `assumed` — no measured Rack AI baseline exists yet. The direction (↑) is roadmap-mandated (KPI #2); actual values require a [[Benchmark Run]]. Throughput improvements must be traded off against [[TTFT]] per the roadmap's continuous-batching guidance.

## See Also

- [[Operations Hub]]
