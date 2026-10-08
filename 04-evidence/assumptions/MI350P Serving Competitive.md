---
id: asm-mi350p-serving-competitive
type: assumption
status: draft
owner: performance-eng
domain: performance
aliases: [mi350p serving competitive, mi350p competitive with h100, rocm serving parity, mi350p competitiveness]
related: [ent-gpu-amd-instinct, ent-gpu-h100, bench-amd-mi350p-qualification, val-mi350p-qualification, pol-benchmark-evidence-chain, asm-h200-sufficient, asm-fleet-competitiveness, met-goodput, fml-cost-per-1m-tokens, idx-assumption-register]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "critical review of benchmarking notes (2026-10-07)"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-evidence
summary: "For fitting priority models, optimized MI350P/ROCm serving is competitive with H100 on performance, operability, cost."
---

# MI350P Serving Competitive

## Statement

> For selected RackAI priority models that fit the deployed MI350P topology, an optimized ROCm serving configuration can deliver SLO-qualified inference performance and fully loaded cost efficiency competitive with the corresponding [[NVIDIA H100]] configuration under matched workload conditions.

The claim is **workload-specific**. A result for [[GLM 5.3 Flash]] does not establish MI350P competitiveness for other models, context lengths, or engines.

It is split into three clauses, each validated independently with **matched evidence from both platforms**:

| Clause | Claim | Validated at | Criterion (to be ratified) | Status |
|--------|-------|:------------:|----------------------------|:------:|
| **C1 Performance** | MI350P SLO-qualified goodput is competitive with H100 for the same model and profile | B3 (provisional) → B4 (qualified) | Competitive band not yet ratified — see [[Open Questions]] | assumed |
| **C2 Operability** | MI350P meets the same B4 service qualification categories as H100 (isolation, resilience, sovereignty) | B4 | Same SQR categories pass on both | assumed |
| **C3 Economics** | Fully loaded cost per 1M **successful** output tokens at the SLO-qualified point is competitive with H100 | B5 | Competitive band not yet ratified; capped by [[Cost per GPU-Hour]] confidence | assumed |

MI350P doesn't need to win all three. For example, lower goodput per GPU with better fully loaded economics and the same SLO could still make it the preferable platform. Higher peak throughput with worse p99 latency or unstable production behaviour isn't competitive.

## Comparison Views

Every comparison names its view:

| View | Question | Primary audience |
|------|----------|------------------|
| Per GPU | Which accelerator produces more useful work? | Engineering optimization |
| Per replica / node | Which deployed configuration delivers more capacity? | Infrastructure architecture |
| Per dollar at SLO | Which platform delivers better economics? | Customer positioning, pricing |

The GPUs differ in memory, platform, and acquisition cost, so the per-GPU view alone doesn't establish competitiveness.

## Rationale

MI350P is a newer generation, and vLLM/SGLang run on ROCm. If its per-GPU memory is larger than H100 NVL (to be confirmed in Pass 0), it may need a lower tensor-parallel degree on PCIe. Against that: no TensorRT-LLM or FlashAttention-3 on ROCm, a less mature kernel ecosystem, and the same PCIe horizontal-scaling limit ([[Fleet Competitiveness]]). The net effect is unknown.

## Exit Criterion

Each clause exits separately. Its evidence must match the [[Benchmark Evidence Chain]] cross-vendor rule: same model revision, quantization format, profile, load mode, harness version, and dated workload set, with both sides `current`.

- C1 — matched B3 cards, then matched B4 qualified goodput.
- C2 — B4 Service Qualification Records on both platforms.
- C3 — B5 Economics Sheets on both platforms using the same cost-model version.

Completing the [[AMD MI350P Qualification Plan]] alone resolves none of the clauses, because the H100 side must also exist.

## Impacts

| Impacted | Type |
|----------|------|
| [[AMD Instinct]] | SUPPORTS |
| [[Tokens per GPU-Second]] | SUPPORTS |
| [[Cost per 1M Tokens]] | SUPPORTS |
| Milestone Release Map T4.S5 (engine × accelerator selection) | SUPPORTS |

## Status

- Confidence: assumed (all three clauses)
- Owner: Inference Optimization (C1, C3); Inference and Serving Services (C2)
- Target resolution: per clause, on matched evidence; no date set

## See Also

- [[Evidence Hub]]
- [[Assumption Register]]
- [[Validate MI350P Qualification]]
