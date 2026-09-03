---
id: coeff-spec-decode-acceptance
type: coefficient
status: draft
owner: performance-eng
domain: performance
aliases: [speculative decoding acceptance rate, draft token acceptance, spec decode gain]
related: [fml-tokens-per-gpu-second, met-tokens-per-gpu-second, coeff-fp8-throughput, coeff-kv-cache-hit-rate, ent-benchmark-run, ent-serving-runtime]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Draft-token acceptance rate and the throughput gain it yields, which compresses under saturation."
---

# Speculative Decoding Acceptance Rate

## Definition

The rate at which draft tokens proposed by a smaller draft model (or self-speculation) are accepted by the target model, and the resulting throughput gain. Applied as a modifier on effective throughput in the [[Tokens per GPU-Second Formula]]. The gain is largest at low-to-medium concurrency and compresses toward zero as the system saturates, because spare compute for verification disappears under load.

## Value

| Value | Unit | Confidence | As Of |
|-------|------|:----------:|-------|
| TBD (acceptance rate placeholder; gain ~2–3× at low/medium concurrency, →~0 at saturation) | ratio / × speedup | assumed | 2026-09-03 |

## Evidence

- Benchmark run / source: NVIDIA NIM [speculative decoding documentation](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html) describes the draft-verify mechanism; 2026 production benchmarks from [traversaal.ai](https://traversaal.ai/) indicate gains concentrate at lower concurrency and shrink under saturation. EAGLE-style speculation is reported as lossless. (Content rephrased for compliance with licensing restrictions.)
- Exit criterion to upgrade confidence: a Rack AI [[Benchmark Run]] measuring acceptance rate, throughput gain, added memory, and TTFT impact per model/runtime, upgrading confidence from `assumed` to `measured`.

## Used By

| Formula | ID |
|---------|----|
| [[Tokens per GPU-Second Formula]] | fml-tokens-per-gpu-second |

## Change History

| Date | Old Value | New Value | Reason | Confidence Δ |
|------|-----------|-----------|--------|--------------|
| 2026-09-03 | — | TBD (placeholder) | Initial note; cites NVIDIA NIM + traversaal.ai as rationale | — → assumed |

## See Also

- [[Operations Hub]]
