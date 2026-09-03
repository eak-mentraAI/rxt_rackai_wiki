---
id: coeff-kv-cache-hit-rate
type: coefficient
status: draft
owner: performance-eng
domain: performance
aliases: [kv cache hit rate, prefix cache hit rate, cache hit rate]
related: [fml-tokens-per-gpu-second, met-tokens-per-gpu-second, coeff-fp8-throughput, coeff-spec-decode-acceptance, ent-benchmark-run, ent-serving-runtime]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Fraction of prefix/KV cache lookups that hit, translating into prefill GPU work avoided."
---

# KV Cache Hit Rate

## Definition

The fraction of prefix / KV cache lookups that hit rather than requiring recomputation, and the GPU work thereby avoided. Applied as a modifier on effective throughput in the [[Tokens per GPU-Second Formula]] and exposed alongside "GPU work avoided" per roadmap Milestone 3.5. Hit rate depends heavily on the actual workload's prompt repetition and cacheability.

## Value

| Value | Unit | Confidence | As Of |
|-------|------|:----------:|-------|
| TBD (workload-dependent placeholder) | ratio / % | assumed | 2026-09-03 |

## Evidence

- Benchmark run / source: roadmap Milestone 3.5 (KV / Prefix Cache Optimization) mandates cache hit-rate telemetry and a "GPU work avoided" measure; Milestone 3.3 characterizes prompt repetition and cacheability. No measured Rack AI hit rate exists yet.
- Exit criterion to upgrade confidence: a Rack AI [[Benchmark Run]] or production telemetry sample reporting cache hit rate and GPU work avoided on characterized workloads, upgrading confidence from `assumed` to `measured`.

## Used By

| Formula | ID |
|---------|----|
| [[Tokens per GPU-Second Formula]] | fml-tokens-per-gpu-second |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Initial note; workload-dependent, awaiting telemetry | — → assumed |

## See Also

- [[Operations Hub]]
