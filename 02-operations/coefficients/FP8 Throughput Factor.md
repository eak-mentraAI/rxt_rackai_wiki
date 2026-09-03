---
id: coeff-fp8-throughput
type: coefficient
status: draft
owner: performance-eng
domain: performance
aliases: [fp8 throughput factor, fp8 vs bf16, fp8 benefit]
related: [fml-tokens-per-gpu-second, met-tokens-per-gpu-second, coeff-spec-decode-acceptance, coeff-kv-cache-hit-rate, ent-benchmark-run, ent-serving-runtime]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Relative throughput and memory benefit of serving in FP8 versus BF16."
---

# FP8 Throughput Factor

## Definition

The relative throughput and GPU-memory benefit of serving a model in FP8 versus BF16. Applied as a multiplicative modifier on effective throughput in the [[Tokens per GPU-Second Formula]] and used to steer the quantization program. FP8 reduces weight/activation memory and can raise achievable throughput, subject to per-model quality validation.

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
| Quantization program (Milestone 3.6) | — |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Initial note; cites FP8 losslessness research as rationale | — → assumed |

## See Also

- [[Operations Hub]]
