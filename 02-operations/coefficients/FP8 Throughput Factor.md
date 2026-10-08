---
id: coeff-fp8-throughput
type: coefficient
status: draft
owner: performance-eng
domain: performance
aliases: [fp8 throughput factor, fp8 vs bf16, fp8 benefit]
related: [fml-tokens-per-gpu-second, met-tokens-per-gpu-second, coeff-spec-decode-acceptance, coeff-kv-cache-hit-rate, ent-benchmark-run, ent-serving-runtime, hub-inference-optimization, fml-gpus-per-replica, coeff-model-weight-footprint, wf-quantization-program, asm-fp8-quality-neutral, val-deepseek-h200-fp8, idx-gpu-compatibility-matrix]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Relative throughput and memory benefit of serving in FP8 versus BF16."
---

# FP8 Throughput Factor

## Definition

The relative throughput and GPU-memory benefit of serving a model in FP8 versus BF16. Applied as a multiplicative modifier on effective throughput in the [[Tokens per GPU-Second Formula]] and used to steer the quantization program. FP8 reduces weight/activation memory and can raise achievable throughput, subject to per-model quality validation. The memory side matters for capacity: FP8 halves bytes/param versus BF16, which shrinks the [[Model Weight Footprint]], which lowers [[GPUs per Replica]], which in turn sets [[Capacity Pool]] sizing and how many models fit ([[Model Portfolio Capacity]]). The [[Quantization Program]] owns the precision decision.

## Value

| Value | Unit | Confidence | As Of |
|-------|------|:----------:|-------|
| TBD (placeholder multiplier vs BF16; per model/hardware) | ratio (×) | assumed | 2026-09-03 |

## Evidence

- Benchmark run / source: research reports FP8 (W8A8) is effectively lossless across model scales — see [Give Me BF16 or Give Me Death (arXiv 2411.02355), Red Hat AI](https://arxiv.org/abs/2411.02355). This supports FP8 as a quality-safe efficiency lever but does not provide a Rack AI throughput multiplier. (Content rephrased for compliance with licensing restrictions.)
- Exit criterion to upgrade confidence: a Rack AI [[Benchmark Run]] measuring FP8-vs-BF16 throughput and memory on target hardware, upgrading confidence from `assumed` to `measured`.

## Used By

| Formula | ID |
|---------|----|
| [[Tokens per GPU-Second Formula]] | fml-tokens-per-gpu-second |
| [[GPUs per Replica]] (memory: bytes/param) | fml-gpus-per-replica |
| [[Quantization Program]] (Milestone 3.6) | wf-quantization-program |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMES | [[Tokens per GPU-Second Formula]] | ← | Throughput modifier |
| CONSUMES | [[GPUs per Replica]] | ← | Memory modifier: bytes/param at FP8 |
| DEPENDS_ON | [[Model Weight Footprint]] | ← | Footprint = params × bytes/param(precision) |
| PRODUCES | [[Quantization Program]] | ← | Program measures and updates this coefficient |
| DEPENDS_ON | [[Serving Runtime]] | → | Engine must support FP8 kernels |
| CONSTRAINS | [[GPU Type Compatibility Matrix]] | ← | FP8 only where supported (not on A30) |
| SUPPORTS | [[FP8 Quality Neutral]] | ← | Quality-neutral assumption behind using FP8 |
| VALIDATES | [[Validate DeepSeek H100 FP8]] | ← | Open validation: assumed → measured |
| MEASURES | [[DeepSeek H100 FP8 Benchmark]] | ← | Planned run (not executed) |
| MEASURES | [[Benchmark Run]] | ← | Exit criterion: FP8-vs-BF16 run on target hardware |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Initial note; cites FP8 losslessness research as rationale | — → assumed |

## See Also

- [[Operations Hub]]
