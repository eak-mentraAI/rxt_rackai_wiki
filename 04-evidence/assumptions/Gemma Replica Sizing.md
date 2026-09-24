---
id: asm-gemma-replica-sizing
type: assumption
status: draft
owner: performance-eng
domain: capacity
aliases: [gemma replica sizing, gemma 4 31b gpu per replica, gemma hardware fit]
related: [hub-evidence, idx-assumption-register, idx-gpu-capacity-demand-rationale, fml-gpus-per-replica, ent-gpu-node, asm-fleet-competitiveness]
source_docs: ["reference/RackAI - GPU Capacity.xlsx"]
confidence: assumed
last_reviewed: 2026-09-24
parent: hub-evidence
summary: "Gemma 4 31B at BF16 with 262k context requires 2× H100 per serving replica."
---

# Gemma Replica Sizing

## Statement

A single serving replica of **Gemma 4 31B at BF16 with 262k context length** requires **2× H100 NVL PCIe (80 GB)** to hold weights plus KV cache reserve without memory pressure.

## Rationale

Applying [[GPUs per Replica]] to the proposed Gemma 4 31B deployment:

```
weight_bytes        = 31B params × 2 bytes (BF16) = ~62 GB
h100_usable_mem     = 80 GB × 0.88             = ~70 GB
```

Weights alone fit in a single H100 (62 GB < 70 GB). However, at 262k context length the KV cache reserve becomes significant:

- A rough estimate for a 31B transformer at 262k context: KV cache ≈ 2 × n_layers × n_heads × head_dim × seq_len × bytes_per_element. For a typical 31B architecture (e.g. ~48 layers, GQA) this can add 10–30 GB depending on the GQA configuration.
- Adding KV reserve to weights exceeds a single H100's usable memory for any configuration with substantial concurrency.

Therefore **2× H100 per replica** is the working assumption for prod sizing. The proposed 26× H100 (min 20) per prod site accommodates ~10 replicas with redundancy overhead.

> This is analytical reasoning from the formula, not a measured benchmark. The actual requirement depends on Gemma 4 31B's confirmed architecture (n_layers, GQA config), which is `assumed`.

## Exit Criterion

A hardware-fit benchmark running Gemma 4 31B BF16 at 262k context on H100 NVL PCIe, measuring actual peak GPU memory consumption and confirming (or correcting) the 2-GPU-per-replica figure. Upgrades to `measured` once the benchmark run exists.

## Impacts

| Impacted | Type |
|----------|------|
| [[GPU Capacity Demand Rationale]] | SUPPORTS |
| [[GPUs per Replica]] | SUPPORTS |

## Status

- Confidence: `assumed`
- Owner: performance-eng
- Target resolution date: M2 AI Performance Benchmark (Gemma 4 31B hardware-fit run)

## See Also

- [[Assumption Register]]
- [[GPUs per Replica]]
- [[GPU Capacity Demand Rationale]]
- [[Fleet Competitiveness]]
