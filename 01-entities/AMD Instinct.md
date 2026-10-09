---
id: ent-gpu-amd-instinct
type: entity
status: draft
owner: infrastructure
domain: infrastructure
aliases: [amd instinct, amd gpu, mi350p, rocm gpu, amd mi350p]
related: [ent-gpu-node, ent-gpu-fleet, ent-serving-runtime, idx-fleet-inventory, idx-open-questions, asm-fleet-competitiveness, hub-entities, pol-benchmark-evidence-chain, bench-amd-mi350p-qualification, asm-mi350p-serving-competitive, val-mi350p-qualification, hub-why-now, evd-compute-supply-sovereign-demand-2026]
source_docs: [openrouter_engineering_roadmap.md, "AMD Instinct MI350P product page and brochure (launched 2026-05-07)"]
confidence: assumed
last_reviewed: 2026-10-09
parent: hub-entities
summary: "AMD Instinct MI350P (ROCm), 8-way pool, deployed Oct 2026; PCIe, so same scaling limit as H100; qualification pending."
---

# AMD Instinct

## Definition

**AMD Instinct MI350P** is the non-NVIDIA GPU capacity in Rack AI's fleet — a large order with an ETA of approximately **October 2026** per the [[Fleet Inventory]], reported **deployed** on 2026-10-07 (operator-reported; not yet reflected in Fleet Inventory ground truth). We can position it as an **8-way MI350P inference pool**, a genuine capacity step up. But it is a **PCIe accelerator**, so it carries the *same* limitation as the fleet's H100 NVL: it does **not** scale a workload horizontally across a large tightly-coupled group the way an SXM part (H200) or UBB8 platform (B300) does. It is also the first ROCm serving path in the fleet, which constrains engine choice (vLLM/SGLang, not TensorRT-LLM). Quantity is TBD.

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
| ETA / status | Deployed — operator-reported 2026-10-07 (order ETA was ~October 2026) | assumed |
| Qualification | Not started — B1→B5 per [[AMD MI350P Qualification Plan]] | assumed |
| Serving stack | vLLM and SGLang run on ROCm; TensorRT-LLM does not | measured |
| Vendor spec: power and cooling | 600 W TBP (cappable to 450 W), passively air-cooled, dual-slot PCIe 5.0 x16; up to 8 per server (AMD) | assumed (vendor) |
| Vendor spec: memory | 144 GB HBM3E (AMD lists this as an estimate), up to 4 TB/s; no on-card high-speed fabric (AMD) | assumed (vendor) |
| Vendor spec: compute | CDNA 4, 128 CUs; MXFP4/MXFP6 4.6 PF, MXFP8 2.3 PF, FP16 1.15 PF dense (AMD peak figures) | assumed (vendor) |

**What it unlocks — and what it doesn't.** The 8-way MI350P pool adds real inference capacity and lets us serve more concurrent demand than the H100 NVL fleet. But because it is a **PCIe** accelerator, it hits the **same horizontal-scaling wall** as the H100 NVL: it cannot assemble the large, tightly-coupled GPU group that frontier-class models need. It raises how much we can serve, not the ceiling on model size. That ceiling only moves with **SXM clusters or UBB8** platforms — see [[Fleet Competitiveness]].

## Serving Constraint (critical)

The AMD path changes the [[Serving Runtime]] picture:

- **Supported on ROCm:** vLLM and SGLang both have ROCm builds and run on AMD Instinct.
- **Not available on ROCm:** TensorRT-LLM and FlashAttention-3 are NVIDIA/CUDA-only — no ROCm equivalent. NVIDIA Dynamo's NVIDIA-specific paths do not apply.

This means priority-model deployments targeting AMD Instinct must use vLLM or SGLang, and any TensorRT-LLM-specific optimization in a model's performance profile will not port. Tracked in [[Open Questions]].

## Benchmarking and Claims

**Vendor specs are not measurements.** The rows above are AMD's published specifications, collected 2026-10-09 for the [[Why Now]] argument (air-cooled, 600 W cards fit existing racks where powered space is the scarce resource). B1 node acceptance confirms them on our hardware; no independent MI350P benchmark was found. Quantity and per-node topology remain open (D4).


No MI350P performance figure exists in the corpus. The pool is qualified tier by tier under the [[Benchmark Evidence Chain]] (B1 node → B2 cluster profile → B3 serving cards → B4 service qualification → B5 economics); the run plan is the [[AMD MI350P Qualification Plan]] and the competitiveness belief is tracked as [[MI350P Serving Competitive]]. Until B2 completes, the only claimable statement is that the capacity is deployed; until B3 cards exist, no inference-performance claim may be made about it.

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| WILL_BE_REALIZED_BY | [[GPU Node]] | ← | Future nodes of AMD Instinct type |
| PART_OF | [[GPU Fleet]] | → | Incoming capacity |
| CONSTRAINS | [[Serving Runtime]] | → | ROCm-only: vLLM/SGLang, not TensorRT-LLM |
| CONSTRAINED_BY | [[Fleet Competitiveness]] | ← | PCIe form factor caps horizontal scaling |
| INVENTORIED_IN | [[Fleet Inventory]] | → | 8-way MI350P pool, ETA ~Oct 2026 |
| MEASURED_BY | [[AMD MI350P Qualification Plan]] | ← | B1–B5 qualification runs (planned) |
| GOVERNED_BY | [[Benchmark Evidence Chain]] | ← | Claim rights per benchmark tier |

## Evidence

- Order/ETA: operator-reported 2026-09-03 (see [[Fleet Inventory]]); class and quantity not yet confirmed → `assumed`.
- Class/deployment (MI350P, 8-way pool, PCIe): operator-reported 2026-09-03.
- ROCm engine support: [AMD ROCm vLLM docs](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html), [AMD ROCm SGLang docs](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/sglang.html); TensorRT-LLM / FlashAttention-3 have no ROCm equivalent per [ROCm vs CUDA 2026 analysis](https://www.spheron.network/blog/rocm-vs-cuda-gpu-cloud-2026/). Content was rephrased for compliance with licensing restrictions.

## See Also

- [[Fleet Inventory]]
- [[GPU Type Compatibility Matrix]]
- [[Serving Runtime]]
- [[Open Questions]]
- [[Benchmark Evidence Chain]]
- [[AMD MI350P Qualification Plan]]
