---
id: idx-open-questions
type: index
status: draft
owner: performance-eng
domain: performance
aliases: [open questions, open questions register, unknowns register]
related: [hub-evidence, idx-validation-register, idx-benchmark-library]
source_docs: [openrouter_engineering_roadmap.md, openrouter_strategic_vision.md]
confidence: assumed
last_reviewed: 2026-09-03
parent: hub-evidence
summary: "Register of genuine unknowns and surfaced source conflicts affecting the evidence layer."
---

# Open Questions

## Purpose

The register of genuine unknowns and any surfaced conflicts between sources. Items here are questions the evidence layer cannot yet answer; each points at the documents it affects and closes when resolved by evidence or a decision. This index is `assumed` because it records open questions, not conclusions.

## Entries

| Question | Affected Docs | Status |
|----------|---------------|--------|
| Exact parameter counts, active parameters, and context length for the V4 / 5.3 / 3-generation priority models are not yet confirmed. | [[DeepSeek V4 Flash]], [[GLM 5.3 Flash]], [[Nemotron 3 Ultra]] (all marked assumed) | open |
| Which serving engine (vLLM vs SGLang vs TensorRT-LLM vs Dynamo disaggregated) is optimal per priority model. | [[Serving Runtime]], [[Benchmark Library]] | open |
| Internal cost per GPU-hour is not yet established. | [[Cost per GPU-Hour]], and all downstream economics | open |
| Whether prefill/decode disaggregation is economically justified for these workloads. | [[Request Routing]] | open |
| Can the current [[NVIDIA H100]] fleet (80GB HBM3, 20 in SPOT) serve the large MoE priority models at competitive TTFT/throughput without H200/Blackwell-class memory? Competitors may run newer hardware. | [[Available Hardware Sufficient for Priority Models]], [[DeepSeek H100 FP8 Benchmark]] | open |
| AMD MI350P order: confirm quantity and ETA (~Oct 2026); confirm 8-way PCIe pool config. | [[AMD Instinct]], [[Fleet Inventory]] | open |
| ROCm serving constraint: TensorRT-LLM and FlashAttention-3 have no ROCm equivalent, so AMD Instinct is limited to vLLM/SGLang. Does any priority model's optimal config depend on a CUDA-only path, and what is the throughput penalty on ROCm? | [[AMD Instinct]], [[Serving Runtime]], [[GPU Type Compatibility Matrix]] | open |
| Topology ceiling: NVL-PCIe pairs (and MI350P PCIe) cap servable models at ~27B class. When/whether do we invest in SXM clusters or UBB8 to reach frontier models and top-10? | [[Fleet Competitiveness]], [[Topology]], [[Model Portfolio Capacity]] | open |
| OpenRouter API conformance: which capability/provider requirements are we short on, and how much will they down-rank us until met? | [[OpenRouter Provider Integration]], [[Fleet Competitiveness]] | open |
| Price competitiveness (routing gate G3): can projected GLM 5.3 Flash cost/token on SPOT H100 FP8 land within the competitive band of live GLM providers on OpenRouter? Price routes before performance, so this gates the public launch. | [[OpenRouter Integration Plan]], [[Cost per 1M Tokens]], [[Cost per GPU-Hour]], [[GLM 5.3 Flash]] | open |
| SPOT-capacity reliability: can public OpenRouter traffic meet the >99.9% availability target while served on preemptible SPOT H100 capacity? | [[OpenRouter Integration Plan]], [[Availability]], [[Fleet Inventory]] | open |
| Confirm GLM 5.3 Flash's actual footprint fits 2–4 H100 at FP8 (first-bet dependency). | [[First Bet — GLM 5.3 Flash]], [[GLM 5.3 Flash]], [[GPUs per Replica]] | open |
| Proof-point model: roadmap says DeepSeek first, fit analysis says GLM first. | [[DeepSeek-First vs GLM-First Sequencing]] | resolved (GLM-first) |
| Is "i40's" in staging confirmed to be [[NVIDIA L40S]] (vs L40)? Affects FP8 capability assumptions. | [[NVIDIA L40S]], [[Fleet Inventory]] | open |
| Exact RackAI dev A30 count is TBD. | [[NVIDIA A30]], [[Fleet Inventory]] | open |
| The A30 has no FP8 and only 24GB — likely unsuitable for large MoE serving. Confirm its role (small models / quantized / MIG / dev only). | [[NVIDIA A30]], [[GPU Type Compatibility Matrix]] | open |
| Billing/payment gap: RackAI has no billing mechanism, and defining pricing/billing logic is an explicit non-goal of the metering spec. This is a P0 blocker for the OpenRouter public-provider path. Who owns/funds it? | [[Billing & Payment]], [[OpenRouter Provider Integration]], [[Metering]] | open |
| Fine-Tuning methods: the data model advertises supervised / reinforcement / dpo, but only Supervised is wired/shipped (RL & DPO marked "Coming Soon"). Confirm roadmap/ETA for RL and DPO. | [[Fine-Tuning Job]], [[Fine-Tuning]] | open |
| Dual deployment paths in the codebase: legacy Platform9 (RPM/scp) vs current Docker+Helm+nginx. Confirm which is canonical and whether the legacy path is deprecated. | [[RackAI Control Plane]], [[RackAI Deployment and Environments]] | open |
| API Key ship status: is programmatic API-key support shipped or still planned? It is the primary dependency for the OpenRouter Private Model path (Path A). | [[API Key]], [[OpenRouter Private Model Integration]] | open |

The register extends as new unknowns or source conflicts surface.

## See Also

- [[Evidence Hub]]
- [[Validation Register]]
- [[Benchmark Library]]
