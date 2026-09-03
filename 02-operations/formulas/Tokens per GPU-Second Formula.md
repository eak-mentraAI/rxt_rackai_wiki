---
id: fml-tokens-per-gpu-second
type: formula
status: draft
owner: performance-eng
domain: performance
aliases: [tokens per gpu-second formula, tokens/gpu-second formula]
related: [met-tokens-per-gpu-second, fml-gpu-hours-per-1m-tokens, fml-cost-per-1m-tokens, coeff-fp8-throughput, coeff-spec-decode-acceptance, coeff-kv-cache-hit-rate, ent-benchmark-run, ent-model-deployment]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Computes output tokens produced per GPU-second from token count and GPU-seconds consumed."
---

# Tokens per GPU-Second Formula

## Purpose

Computes the core efficiency metric [[Tokens per GPU-Second]] from a measured workload or [[Benchmark Run]]. It is the foundation for GPU-hours per 1M tokens and, downstream, cost per 1M tokens.

## Definition

```
tokens_per_gpu_second = output_tokens / (gpu_count × wall_clock_seconds)
```

Runtime optimizations (FP8, speculative decoding, KV/prefix cache) act as multiplicative modifiers on effective throughput via their coefficients.

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| output_tokens | Serving telemetry / benchmark | [[Output Throughput]] | assumed |
| gpu_count | Deployment spec | [[Model Deployment]] | assumed |
| wall_clock_seconds | Benchmark harness | [[Benchmark Run]] | assumed |
| fp8 modifier (optional) | Quantization program | [[FP8 Throughput Factor]] | assumed |
| spec-decode modifier (optional) | Runtime config | [[Speculative Decoding Acceptance Rate]] | assumed |
| cache modifier (optional) | Cache telemetry | [[KV Cache Hit Rate]] | assumed |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| [[FP8 Throughput Factor]] | coeff-fp8-throughput | assumed |
| [[Speculative Decoding Acceptance Rate]] | coeff-spec-decode-acceptance | assumed |
| [[KV Cache Hit Rate]] | coeff-kv-cache-hit-rate | assumed |

## Consumed By

| Consumer | Type |
|----------|------|
| [[Tokens per GPU-Second]] | CONSUMES |
| [[GPU-Hours per 1M Tokens]] | CONSUMES |
| [[Cost per 1M Tokens]] | CONSUMES |

## Worked Example

Illustrative only (assumed inputs, no measured Rack AI value):

- output_tokens = 1,800,000
- gpu_count = 8
- wall_clock_seconds = 300

tokens_per_gpu_second = 1,800,000 / (8 × 300) = 1,800,000 / 2,400 = **750 tokens/GPU-second (assumed / illustrative)**.

## See Also

- [[Operations Hub]]
