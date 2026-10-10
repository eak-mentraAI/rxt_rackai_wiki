---
id: wf-quantization-program
type: workflow
status: draft
owner: performance-eng
domain: performance
aliases: [quantization program, quantization evaluation, precision program]
related: [coeff-fp8-throughput, asm-fp8-quality-neutral, wf-closed-loop-optimization, hub-operations, pol-performance-regression-gate, fml-gpus-per-replica, coeff-model-weight-footprint, idx-gpu-compatibility-matrix]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-operations
summary: "Evaluates model-specific quantization as a controlled engineering decision, not a deployment switch."
---

# Quantization Program

## Purpose

The Quantization Program treats precision selection as a controlled engineering decision rather than a deployment switch (roadmap Milestone 3.6). For each priority [[Model]] it evaluates candidate precisions and benchmarks every configuration against the combined objective **quality × throughput × GPU memory × cost/token**.

## Trigger

Runs per priority model in the Performance Lab (Phase 3), and again when a new runtime version, hardware type, or model architecture could shift the precision/quality tradeoff.

## Candidate Precisions

- BF16 — reference quality baseline
- FP8 — reported effectively lossless across model scales (see [[FP8 Quality Neutral]])
- FP4 — evaluated where viable (e.g., NVFP4 / MXFP4 on Blackwell-class hardware)
- INT8 / other supported approaches

## State Machine

```mermaid
stateDiagram-v2
    [*] --> Candidate
    Candidate --> Benchmarked: run quality x throughput x memory x cost
    Benchmarked --> Approved: meets quality bar and improves economics
    Benchmarked --> Rejected: quality regression or no economic gain
    Approved --> [*]: promoted via regression gate
    Rejected --> [*]
```

## Steps

1. Select candidate precisions per model — performance-eng.
2. Benchmark each — record quality, throughput, GPU memory, and cost/token via the benchmark harness.
3. Score against the combined objective — quality × throughput × GPU memory × cost/token.
4. Promote or reject — approved configurations pass through the [[Performance Regression Gate]] before production.

## Dependencies

| Depends On | Type | Notes |
|------------|------|-------|
| [[FP8 Throughput Factor]] | PRODUCES | Program measures and updates this coefficient |
| [[Performance Regression Gate]] | DEPENDS_ON | Approved configs must clear the gate |
| [[Closed-Loop Optimization]] | FEEDS | Quantization is one experimentation axis in the loop |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| PRODUCES | [[FP8 Throughput Factor]] | → | Measures and updates the coefficient |
| DEPENDS_ON | [[Performance Regression Gate]] | → | Approved configs must clear the gate |
| SUPPORTS | [[Closed-Loop Optimization]] | → | One experimentation axis (original: FEEDS) |
| VALIDATES | [[FP8 Quality Neutral]] | → | Quality benchmark per precision |
| DEPENDS_ON | [[GPUs per Replica]] | ← | Precision sets bytes/param |
| DEPENDS_ON | [[Model Weight Footprint]] | ← | Precision sets footprint |
| CONSTRAINS | [[GPU Type Compatibility Matrix]] | ← | Precision support per GPU type |

## Ownership

Inference Performance Engineering owns the program. Results upgrade the confidence of quantization coefficients from `assumed` to `measured`.

## See Also

- [[Operations Hub]]
- [[FP8 Throughput Factor]]
- [[FP8 Quality Neutral]]
