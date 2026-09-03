---
id: fml-gpus-per-replica
type: formula
status: draft
owner: performance-eng
domain: capacity
aliases: [gpus per replica, replica gpu count, model footprint, replica sizing]
related: [hub-operations, coeff-model-weight-footprint, ent-gpu-h100, ent-gpu-amd-instinct, fml-cost-per-1m-tokens, idx-gpu-compatibility-matrix]
source_docs: [openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Minimum GPUs needed to hold one replica of a model, from weight + KV-cache footprint and per-GPU memory."
---

# GPUs per Replica

## Purpose

Computes the minimum number of GPUs required to hold **one serving replica** of a model on a given GPU type. This is the hard capacity gate that per-GPU memory size imposes before any performance tuning: a model that needs N GPUs per replica consumes N GPUs whether it serves one request or a thousand. It drives replica cost, how many replicas fit on the fleet, and therefore competitive concurrency. Consumed by [[Cost per 1M Tokens]] (replica cost) and the capacity-aware [[Fleet Competitiveness]] analysis.

## Definition

```
gpus_per_replica = ceil( (weight_bytes + kv_cache_reserve_bytes + overhead_bytes)
                         / usable_memory_per_gpu )
```

where, approximately:

```
weight_bytes        = active_or_total_params * bytes_per_param(precision)
kv_cache_reserve    = per_token_kv_bytes * max_context * target_concurrent_seqs
usable_memory_per_gpu = gpu_memory * utilization_headroom   (~0.85–0.90)
```

For dense-loaded MoE, `weight_bytes` uses **total** parameters (all experts must be resident even if only some activate per token). `bytes_per_param`: BF16 = 2, FP8 = 1, FP4 ≈ 0.5.

## Inputs

| Input | Source | Coefficient/Metric | Confidence |
|-------|--------|--------------------|:----------:|
| Model weight footprint | model card / [[Model]] | [[Model Weight Footprint]] | assumed |
| Precision (bytes/param) | deployment spec | [[Quantization Program]] | derived |
| Per-GPU memory | GPU type | [[GPU Type Compatibility Matrix]] | measured |
| KV-cache reserve | workload profile | [[KV Cache Hit Rate]] / [[Traffic Class]] | assumed |

## Coefficients Used

| Coefficient | ID | Confidence |
|-------------|----|:----------:|
| [[Model Weight Footprint]] | coeff-model-weight-footprint | assumed |

## Consumed By

| Consumer | Type |
|----------|------|
| [[Cost per 1M Tokens]] | CONSUMES (replica cost = gpus_per_replica × cost/GPU-hour) |
| [[Fleet Competitiveness]] | CONSUMES (replicas that fit on the fleet) |
| [[Standard Model Deployment]] | CONSUMES (placement / min GPU count) |

## The Interconnect Ceiling (read this first)

`gpus_per_replica` computes how many GPUs a replica *needs*. But on the current fleet the harder limit is how many GPUs can act as **one tightly-coupled unit**. The H100s are **NVL PCIe** — NVLink pairs only (2 coupled, 4/node, no clustering) — so the *usable* group for a single replica is realistically **2–4 GPUs at FP8**, not "however many fit." A model whose `gpus_per_replica` exceeds the coupled-group size cannot be served competitively at all, regardless of total fleet count. This is the binding constraint in [[Fleet Competitiveness]]; the memory math below is secondary to it.

## Worked Example (illustrative — assumed inputs)

Two regimes:

**A) A fitting model (~27B class, FP8)** ≈ ~27 GB weights → fits in **1–2 H100** within an NVLink pair. Servable competitively today. This is the target band (e.g., [[GLM 5.3 Flash]]).

**B) A large MoE (~671B total, FP8)** ≈ **~671 GB weights** before KV cache:

| GPU type | Usable mem/GPU (~0.88) | GPUs for weights only | Fits current coupling? |
|----------|-----------------------:|----------------------:|------------------------|
| [[NVIDIA H100]] NVL PCIe (80 GB) | ~70 GB | ceil(671/70) = **10** | **No** — needs 10 coupled, fleet couples 2 |
| NVIDIA H200 SXM (141 GB) — *not in fleet* | ~124 GB | **6** | Yes (NVSwitch 8-way) |
| [[AMD Instinct]] MI350P (PCIe) | — | (memory helps, coupling doesn't) | **No** — PCIe, same wall as H100 |

**Read-through:** the large MoE needs ~10 GPUs acting as one — impossible on NVL-PCIe pairs and not fixed by the MI350P (also PCIe). It only becomes servable on **SXM/UBB8**. So the fleet's realistic band is regime A (~27B-class fitting models), which is exactly why the first bet is a fitting model — see [[First Bet — GLM 5.3 Flash]]. Numbers illustrative pending confirmed params and hardware-fit — see [[Fleet Competitiveness]] and [[Open Questions]].

## See Also

- [[Model Weight Footprint]]
- [[Fleet Competitiveness]]
- [[GPU Type Compatibility Matrix]]
- [[Operations Hub]]
