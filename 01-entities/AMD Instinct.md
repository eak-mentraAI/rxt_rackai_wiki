---
id: ent-gpu-amd-instinct
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [amd instinct, amd gpu, mi350p, rocm gpu]
related: [ent-gpu-node, ent-gpu-fleet, ent-serving-runtime, idx-fleet-inventory, idx-open-questions, asm-fleet-competitiveness, hub-entities]
source_docs: [openrouter_engineering_roadmap.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-entities
summary: "Incoming AMD Instinct MI350P (ROCm), 8-way pool, ETA ~Oct 2026; still PCIe, so same scaling limit as H100."
---

# AMD Instinct

## Definition

**AMD Instinct MI350P** is the incoming non-NVIDIA GPU capacity in Rack AI's fleet plan — a large order with an ETA of approximately **October 2026** per the [[Fleet Inventory]]. We can position it as an **8-way MI350P inference pool**, a genuine capacity step up. But it is a **PCIe accelerator**, so it carries the *same* limitation as the fleet's H100 NVL: it does **not** scale a workload horizontally across a large tightly-coupled group the way an SXM part (H200) or UBB8 platform (B300) does. It is also the first ROCm serving path in the fleet, which constrains engine choice (vLLM/SGLang, not TensorRT-LLM). Quantity is TBD.

## Layer

L1 — Entity Ontology. An incoming GPU type that will be realized by [[GPU Node]]s within the [[GPU Fleet]].

## Attributes

| Attribute | Value | Confidence |
|-----------|-------|:----------:|
| Vendor / stack | AMD Instinct MI350P / ROCm (not CUDA) | assumed |
| Form factor | PCIe accelerator (not SXM/UBB8) | assumed |
| Deployment | 8-way MI350P inference pool | assumed |
| Horizontal scaling | Limited — PCIe, no large tightly-coupled fabric domain | derived |
| Quantity | TBD | assumed |
| ETA | ~October 2026 | assumed |
| Serving stack | vLLM and SGLang run on ROCm; TensorRT-LLM does not | measured |

**What it unlocks — and what it doesn't.** The 8-way MI350P pool adds real inference capacity and lets us serve more concurrent demand than the H100 NVL fleet. But because it is a **PCIe** accelerator, it hits the **same horizontal-scaling wall** as the H100 NVL: it cannot assemble the large, tightly-coupled GPU group that frontier-class models need. It raises how much we can serve, not the ceiling on model size. That ceiling only moves with **SXM clusters or UBB8** platforms — see [[Fleet Competitiveness]].

## Serving Constraint (critical)

The AMD path changes the [[Serving Runtime]] picture:

- **Supported on ROCm:** vLLM and SGLang both have ROCm builds and run on AMD Instinct.
- **Not available on ROCm:** TensorRT-LLM and FlashAttention-3 are NVIDIA/CUDA-only — no ROCm equivalent. NVIDIA Dynamo's NVIDIA-specific paths do not apply.

This means priority-model deployments targeting AMD Instinct must use vLLM or SGLang, and any TensorRT-LLM-specific optimization in a model's performance profile will not port. Tracked in [[Open Questions]].

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| WILL_BE_REALIZED_BY | [[GPU Node]] | ← | Future nodes of AMD Instinct type |
| PART_OF | [[GPU Fleet]] | → | Incoming capacity |
| CONSTRAINS | [[Serving Runtime]] | → | ROCm-only: vLLM/SGLang, not TensorRT-LLM |
| CONSTRAINED_BY | [[Fleet Competitiveness]] | ← | PCIe form factor caps horizontal scaling |
| INVENTORIED_IN | [[Fleet Inventory]] | → | 8-way MI350P pool, ETA ~Oct 2026 |

## Evidence

- Order/ETA: operator-reported 2026-09-03 (see [[Fleet Inventory]]); class and quantity not yet confirmed → `assumed`.
- Class/deployment (MI350P, 8-way pool, PCIe): operator-reported 2026-09-03.
- ROCm engine support: [AMD ROCm vLLM docs](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html), [AMD ROCm SGLang docs](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/sglang.html); TensorRT-LLM / FlashAttention-3 have no ROCm equivalent per [ROCm vs CUDA 2026 analysis](https://www.spheron.network/blog/rocm-vs-cuda-gpu-cloud-2026/). Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Fleet Inventory]]
- [[GPU Type Compatibility Matrix]]
- [[Serving Runtime]]
- [[Open Questions]]
