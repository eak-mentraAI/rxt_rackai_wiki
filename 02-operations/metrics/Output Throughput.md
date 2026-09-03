---
id: met-output-throughput
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [output throughput, output tokens per second, requests per second, prefill throughput]
related: [met-tokens-per-gpu-second, met-ttft, met-gpu-utilization, ent-model-deployment, ent-benchmark-run]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "How much useful inference work the fleet produces: output tokens/sec and related throughput measures."
---

# Output Throughput

## Definition

Measures how much useful inference work the fleet produces. The headline figure is output tokens/sec, with supporting measures for requests/sec, concurrent requests per GPU, and prefill throughput. It complements [[TTFT]] (latency) and [[Tokens per GPU-Second]] (efficiency), and it is optimized separately from TTFT because throughput and latency need different strategies.

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

## Evidence

- Confidence rationale: `assumed` — direction (↑) is roadmap-mandated, but no measured Rack AI throughput exists yet. Values become `measured` from production/benchmark telemetry.

## See Also

- [[Operations Hub]]
