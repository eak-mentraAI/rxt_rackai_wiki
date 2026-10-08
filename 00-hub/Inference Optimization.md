---
id: hub-inference-optimization
type: hub
status: draft
owner: product
domain: performance
aliases: [inference optimization, optimization pillar, serving efficiency, inference performance engineering, ai optimization and efficiency]
related: [hub-rackai-platform, hub-roadmap, hub-inference-serving, hub-model-services, hub-ai-harness, hub-commercial, hub-org-design, wiki-pillar-working-model, ent-accelerator-class, ent-gpu-h100, ent-gpu-l40s, ent-gpu-a30, ent-gpu-amd-instinct, ent-benchmark-run, met-ttft, met-output-throughput, met-gpu-utilization, fml-tokens-per-gpu-second, fml-cost-per-1m-tokens, fml-gpu-hours-per-1m-tokens, coeff-fp8-throughput, coeff-kv-cache-hit-rate, coeff-spec-decode-acceptance]
source_docs: ["reference/jd/EXTERNAL_PDM_Optimization_and_Efficiency_JD.md", "reference/RackAI - Roadmap.xlsx", "06-sources/Rack AI OpenRouter Engineering Roadmap.md"]
confidence: derived
last_reviewed: 2026-09-24
parent: hub-org-design
summary: "Pillar hub: serving efficiency, cost floor, benchmark harness, optimization levers, and the performance-regression gate."
---

# Inference Optimization

The **Inference Optimization** pillar owns *how well* RackAI serves its model portfolio — the economic and performance layer on top of the serving plane. The question this pillar answers is: given the hardware we have, are we serving each model as efficiently as it can be served, at a cost we can defend?

This is not the same as *running the serving infrastructure* (that is [[Inference and Serving Services]]) or *managing what models exist* (that is [[Model Services]]). Inference Optimization is the **measurement, improvement, and cost-floor** discipline that makes owned capacity worth having.

> **Today the cost floor is unestablished.** The cost-per-GPU-hour is not modeled; usage is metered but cost-per-1M-tokens is not yet a number RackAI can quote with confidence. Making it real is the first job of this pillar. See gap P-003 in the [[RackAI Roadmap]].

---

## Scope

| Area | What it includes |
|---|---|
| **Serving efficiency** | Tokens-per-GPU-second (throughput), TTFT (time-to-first-token), and cost-per-outcome across every model in the portfolio — on owned NVIDIA and maturing AMD hardware. |
| **Benchmark and measurement product** | The harness that establishes, per model and per hardware config, what the system can produce and what 1M tokens cost. The ground truth every pricing and placement decision reads from. |
| **Optimization levers** | Quantization (FP8, INT4/AWQ), KV and prefix caching, continuous batching, tensor and expert parallelism, speculative decoding — prioritized by measured impact on real arriving workloads, not by novelty. *(Many single-engine levers here are increasingly delivered by vendor engines — see **Two Layers of Optimization** below for what we own vs. commoditize.)* |
| **Cost-floor story** | Turning the fleet's measured cost-per-GPU-hour into a defensible cost-per-1M-tokens that underwrites pricing across every route to market (direct tenants, the app, OpenRouter, contracted capacity). |
| **AMD / ROCm efficiency bet** | Defining where serving economics must land for AMD hardware to broaden the model portfolio, and tracking progress against that bar. |
| **Performance-regression gate** | The bar a runtime, quantization, or config change must clear on latency, throughput, and quality before it reaches production. Owned by this pillar; enforced across [[Inference and Serving Services]] changes. |
| **Accelerator benchmarking** | Per-GPU-class performance baselines; [[Benchmark Run]] execution and evidence for every accelerator class in the fleet. |

---

## Two Layers of Optimization — what we commoditize vs. what we own

"Inference optimization" collapses two different things. Separating them answers the question *"if [[Serving Runtime|vendor engines]] (AIM on AMD, NIM on NVIDIA) become our inference optimization, where do we still add value?"* — the short answer being that vendor engines commoditize **Layer A**, which was never the moat, and leave **Layer B** — the higher-leverage layer — entirely to us.

| | **Layer A — single-deployment engine tuning** | **Layer B — cross-deployment operating optimization** |
|---|---|---|
| **What it is** | Max tok/s from *one model on one GPU config*: kernels, quantization, attention backend, batch params | Optimizing *across* all models, engines, and hardware at once: which engine/model/accelerator, placed where, at what cost |
| **Who does it best** | The silicon vendor — **AIM / NIM** (and they will always out-resource us on their own hardware) | **RackAI** — the only party standing above all engines and all hardware |
| **Does it compound?** | No — a treadmill, re-tuned per model, per engine version, per ROCm/CUDA release | Yes — every workload improves the next one (the [[Empirical Map]] flywheel; K2) |
| **Verdict** | **Cede it — deliberately.** Running the vendor's blessed engine is a good trade, not a loss | **Own it.** This is the operator moat |

**Layer B is not one thing — it is four kinds of optimization no vendor engine can do, because none of them sit inside a single engine:**

1. **Engine/model/hardware *selection* (meta-optimization).** AIM optimizes *within* the AMD+GLM cell; NIM *within* the NVIDIA+Nemotron cell. Neither decides *which cell is right for this workload*. The [[Empirical Map]] + evidence-informed [[Request Routing]] optimize the **choice across cells** — a strictly higher-value optimization than tuning any one cell.
2. **Placement / topology / capacity optimization.** Which [[Capacity Pool]] a workload lands in, packing a heterogeneous fleet for [[Productive GPU Utilization]], reallocation under load ([[GPU Reallocation]]), [[Fleet Yield Optimization]]. Vendor engines run a container; they don't decide *where* it runs or how to pack the fleet.
3. **Cost optimization / the economics.** Per [[Three Battlegrounds]], supply is interchangeable but *the intelligence deciding how to consume it (placement + cost) is not commoditized*. NIM makes a model fast; it does nothing for cost/GPU-hour, utilization-adjusted cost, or [[Cost per Outcome]]. The [[AI FinOps]] / [[Unit Economics Model]] layer is optimization a vendor has no reason to build for us.
4. **Cross-engine optimizations that ride *on top of* any engine.** Semantic/prompt caching, in-path token compression (the `erepress`-style idea flagged in [[Erebine Competitive Analysis]]), request shaping, speculative-decoding *policy*, cross-request KV-reuse strategy — these live at the routing/gateway layer above the engine and apply whether the engine underneath is vLLM, AIM, or NIM. **These remain fully open to us to introduce.**

**The referee advantage (why using vendor engines makes Layer B *more* credible).** Because we run each vendor's *best* engine rather than a home-rolled stack, when the Empirical Map says "route this to AMD+AIM over NVIDIA+NIM," it is an honest verdict — we optimized each option to its vendor-blessed best and *then* chose. That neutral-referee position is one no silicon vendor can occupy. It also connects to why [[Three Battlegrounds|OpenRouter is the "gym"]]: we're not trying to own the best inference API, we're trying to make the best operating decision over whatever engines exist.

> **The conditional risk (the line to protect).** Layer B value is real **only if we actually build it.** If we run vendor engines *and* skip the Empirical Map / routing / economics layer, we are a passthrough with a nice UI — the fear is then justified. This is exactly why P-005 (Empirical Map) is the load-bearing center of the roadmap's D2. Ceding Layer A is safe *because* Layer B is funded; if Layer B slips, revisit the whole stance.

**In one line:** *the engine is the commodity; the operating decision over the engines is the moat.*

---

## Key Metrics and Formulas

| Metric / Formula | What it measures | Note |
|---|---|---|
| [[TTFT]] | Time to first token (latency experience) | Primary user-facing latency metric |
| [[Output Throughput]] | Tokens/second generated | System throughput |
| [[Tokens per GPU-Second Formula]] | Productive throughput per GPU | The efficiency numerator |
| [[Cost per 1M Tokens]] | Total cost / tokens served | The cost-floor anchor |
| [[GPU-Hours per 1M Tokens]] | GPU-time consumed per M tokens | Inputs to cost modeling |
| [[Productive GPU Utilization]] | Fraction of GPU time doing useful work | Utilization signal |
| [[FP8 Throughput Factor]] | Throughput multiplier from FP8 quantization | Key optimization coefficient |
| [[KV Cache Hit Rate]] | Prefix cache reuse rate | Caching optimization signal |
| [[Speculative Decoding Acceptance Rate]] | Fraction of speculative tokens accepted | Speculative decoding efficiency |

---

## Current State vs. Target

| Metric | Baseline (today) | Target | Status |
|---|---|---|---|
| Cost-per-GPU-hour (internal) | Unknown | Modeled and defensible | **Gap → P-003** |
| Cost-per-1M-tokens per model | Unknown | Per-model floor established | **Gap → P-003** |
| Benchmark harness | None | Per-model/hardware baseline | Not Started (M2 AI Perf Benchmarks) |
| TTFT (H100, GLM 5.3 Flash) | Assumed competitive | Measured | Not Started |
| Speculative decoding (Refrag) | In progress (RACKAI-374) | Shipped | In Progress |
| DPO / optimization-aware fine-tuning | — | — | Separate (Model Services) |
| AMD AIM engine serving | In progress (RACKAI-347) | AMD models served at target econ | In Progress |

---

## Key Entities and Notes

- [[Benchmark Run]] — the canonical record of a measurement event
- [[Accelerator Class]] — the hardware classes benchmarks target
- [[NVIDIA H100]], [[NVIDIA L40S]], [[NVIDIA A30]], [[AMD Instinct]] — the GPU classes in scope
- [[GPU Fleet]] — the fleet being optimized
- [[FP8 Throughput Factor]], [[KV Cache Hit Rate]], [[Speculative Decoding Acceptance Rate]] — the key optimization coefficients
- [[Model Weight Footprint]] — memory constraint input to placement and quantization decisions
- [[GPU Type Compatibility Matrix]] — the compatibility matrix this pillar maintains

---

## Relationships to Other Pillars

```mermaid
flowchart LR
    IO[Inference Optimization]
    ISS[Inference and Serving Services] -->|serving plane to optimize| IO
    MS[Model Services] -->|models to benchmark at launch| IO
    IO -->|cost floor + efficiency gates| PO[Product Operations]
    IO -->|benchmark evidence| GOV[AI Governance & Assurance]
    IO -->|feeds Empirical Map| HAR[AI Harness]
```

- [[Inference and Serving Services]] — the plane being optimized; serving config changes must pass the performance-regression gate this pillar owns.
- [[Model Services]] — every model entering the catalog must pass through the benchmark harness before launch; optimization clears the gate.
- [[Product Operations]] — the cost-floor number feeds pricing inputs and launch-readiness decisions.
- [[AI Harness]] — the [[Empirical Map]] (harness-adjacent) is fed by the cross-workload performance evidence this pillar produces.

---

## Roadmap Proof Alignment

| Proof | Inference Optimization contributions |
|---|---|
| **Proof 1 — Observe** | Establish benchmark harness; produce the first cost-per-GPU-hour number; close gap P-003 |
| **Proof 2 — Decide** | Evidence-informed placement (model/hardware match); AMD economics decision; performance engineering system |
| **Proof 3 — Assume Responsibility** | Performance-regression gate enforced at every deployment change; per-model cost evidence for MOE pricing |
| **Proof 4 — Operate** | Closed-loop optimization (automate what the efficiency data teaches); heterogeneous-supply economics |

---

## Open Questions

| Question | Priority |
|---|---|
| Who owns the benchmark harness execution — Inference Optimization or SRE/Reliability? | High |
| What is the first cost-per-GPU-hour number and who ratifies it as the pricing input? | High |
| What is the AMD/ROCm serving economics target before AMD is considered viable for production workloads? | Medium |
| Does the performance-regression gate block deployments automatically or require manual sign-off from this pillar? | Medium |

---

## See Also

- [[EXTERNAL_PDM_Optimization_and_Efficiency_JD]] — the PDM role definition for this pillar
- [[Inference and Serving Services]] — the serving plane this pillar measures and improves
- [[Model Services]] — the model launch gate this pillar co-owns
- [[Commercial & Capacity Hub]] — pricing and unit economics that depend on the cost floor
- [[RackAI Roadmap]] — gap P-003 (cost model), M2 AI Performance Benchmarks
- [[RackAI Organizational Design]] — pillar structure and team boundaries
