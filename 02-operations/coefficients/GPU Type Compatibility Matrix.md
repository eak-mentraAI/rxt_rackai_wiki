---
id: idx-gpu-compatibility-matrix
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [gpu compatibility matrix, gpu type compatibility, hardware compatibility matrix, engine hardware matrix]
related: [hub-operations, ent-serving-runtime, ent-gpu-fleet, idx-fleet-inventory, ent-gpu-amd-instinct]
source_docs: [openrouter_engineering_roadmap.md]
confidence: derived
last_reviewed: 2026-09-03
parent: hub-operations
summary: "Maps fleet GPU types to supported serving engines, precisions, and suitability for the priority models."
---

# GPU Type Compatibility Matrix

## Purpose

Maps the GPU types actually in Rack AI's fleet (see [[Fleet Inventory]]) to the [[Serving Runtime]] engines and precisions they support, and to their suitability for the large MoE priority models. This extends the roadmap's Architecture Compatibility Matrix (Milestone 4.2) from model architectures to the specific hardware Rack AI operates. Placement decisions and the [[Model Deployment Specification]] must respect this matrix.

## Engine × GPU Type

| GPU Type | vLLM | SGLang | TensorRT-LLM | NVIDIA Dynamo | Stack |
|----------|:----:|:------:|:------------:|:-------------:|-------|
| [[NVIDIA H100]] | ✅ | ✅ | ✅ | ✅ | CUDA |
| [[NVIDIA L40S]] | ✅ | ✅ | ✅ | ✅ | CUDA |
| [[NVIDIA A30]] | ✅ | ✅ | ✅ | ✅ | CUDA |
| [[AMD Instinct]] | ✅ | ✅ | ❌ | ❌ | ROCm |

**Key constraint:** TensorRT-LLM and FlashAttention-3 are CUDA-only and have no ROCm equivalent. On [[AMD Instinct]], serving must use vLLM or SGLang, and any TensorRT-LLM-specific optimization in a model's performance profile will not port.

## Precision × GPU Type

| GPU Type | BF16/FP16 | FP8 | INT8 | FP4 |
|----------|:---------:|:---:|:----:|:---:|
| [[NVIDIA H100]] | ✅ | ✅ (Transformer Engine) | ✅ | ❌ (no native FP4) |
| [[NVIDIA L40S]] | ✅ | ✅ (Transformer Engine) | ✅ | ❌ |
| [[NVIDIA A30]] | ✅ | ❌ (no FP8) | ✅ | INT4 weight-only |
| [[AMD Instinct]] | ✅ | ✅ (MI300-class) | ✅ | class-dependent |

The [[FP8 Throughput Factor]] coefficient and [[Quantization Program]] apply only where FP8 is supported — notably **not** on the A30.

## Suitability for Priority Models

| GPU Type | Memory | Interconnect | Large MoE suitability |
|----------|--------|--------------|------------------------|
| [[NVIDIA H100]] | 80 GB HBM3 | NVLink/NVSwitch | Best current fit; multi-GPU tensor/expert parallelism |
| [[AMD Instinct]] | high (MI300-class) | Infinity Fabric | Promising once online (vLLM/SGLang); pending fit |
| [[NVIDIA L40S]] | 48 GB GDDR6 | no NVLink (PCIe) | Limited: FP8 single-GPU / staging / smaller models |
| [[NVIDIA A30]] | 24 GB HBM2 | NVLink (200 GB/s) | Weak for large MoE; better for small/quantized/MIG |

## Implications

- The priority MoE models ([[DeepSeek V4 Flash]], [[Nemotron 3 Ultra]]) target **H100** first, and **AMD Instinct** once it lands (vLLM/SGLang only).
- **No H200s exist** in the fleet — earlier illustrative H200 references have been retargeted to H100.
- L40S and A30 are staging/dev/small-model capacity, not the primary home for large MoE serving.

## Evidence

- GPU presence: [[Fleet Inventory]] (operator-reported 2026-09-03).
- Engine/precision support: NVIDIA and AMD ROCm documentation; ROCm engine gaps per published 2026 analysis. Values are `derived` from vendor capability docs, not from Rack AI benchmark runs — hardware-fit remains an [[Open Questions|open question]].

## See Also

- [[Serving Runtime]]
- [[Fleet Inventory]]
- [[Operations Hub]]
