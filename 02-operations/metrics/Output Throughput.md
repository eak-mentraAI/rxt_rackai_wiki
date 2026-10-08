---
id: met-output-throughput
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [output throughput, output tokens per second, requests per second, prefill throughput]
related: [met-tokens-per-gpu-second, met-ttft, met-gpu-utilization, ent-model-deployment, ent-benchmark-run, hub-inference-optimization, fml-tokens-per-gpu-second, wf-model-launch-factory, wf-closed-loop-optimization, pol-performance-regression-gate, evt-performance-regression-detected, evd-kpi-telemetry-targets, val-erebine-inference-claims]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "How much useful inference work the fleet produces: output tokens/sec and related throughput measures."
---

# Output Throughput

## Definition

Measures how much useful inference work the fleet produces. The headline figure is output tokens/sec, with supporting measures for requests/sec, concurrent requests per GPU, and prefill throughput. It complements [[TTFT]] (latency) and [[Tokens per GPU-Second]] (efficiency), and it is optimized separately from TTFT because throughput and latency need different strategies.

## KPI Job

Serves all four jobs (per [[KPI Telemetry Target List]]): internal operating decision, customer-facing experience, commercial commitment (durable record required before pricing or an SLA), and strategic positioning (competitive throughput rank). Rides the same serving-telemetry collection and attribution path as [[TTFT]].

## Unit

output tokens / second (primary); also requests/second, concurrent requests/GPU, prefill tokens/second.

## Source or Formula

- Measured from: serving telemetry per [[Model Deployment]] (streamed output tokens over wall-clock, request counts, concurrency) and from each [[Benchmark Run]].
- Related efficiency view derived via [[Tokens per GPU-Second Formula]].

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | Maximize (no measured baseline yet) | Must not push [[TTFT]] past SLO |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| MEASURES | [[Model Deployment]] | → | Per deployment |
| PRODUCES | [[Benchmark Run]] | ← | Benchmark runs produce values (none yet) |
| CONSUMES | [[Tokens per GPU-Second Formula]] | ← | `output_tokens` input |
| CONSTRAINS | [[TTFT]] | ← | Must not push TTFT past SLO |
| PRODUCES | [[Model Launch Factory]] | ← | Benchmark stage produces the baseline |

## Evidence

- Confidence rationale: `assumed` — direction (↑) is roadmap-mandated, but no measured Rack AI throughput exists yet. Values become `measured` from production/benchmark telemetry.

## See Also

- [[Operations Hub]]
