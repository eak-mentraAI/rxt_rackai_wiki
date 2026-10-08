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
last_reviewed: 2026-10-07
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
| AMD MI350P order: confirm quantity and ETA (~Oct 2026); confirm 8-way PCIe pool config. Now reported deployed (2026-10-07): confirm quantity, per-GPU HBM, and node topology — required for the B2 Validated Cluster Profile. | [[AMD Instinct]], [[Fleet Inventory]], [[AMD MI350P Qualification Plan]] | open |
| No per-profile SLO thresholds (TTFT/TPOT percentile limits, attainment target) are ratified, so B4 service qualification, [[Goodput]], and [[SLO Attainment]] cannot be scored. Owner: Product (PM Inference/Serving). | [[Benchmark Evidence Chain]], [[SLO Attainment]], [[Goodput]], [[Traffic Class]] | open |
| Standard benchmark profile shapes (input/output length distributions, arrival processes, prefix/cache-hit assumptions per Interactive / Throughput / Long Context profile) are not defined; until they are, cards across runs are not comparable. | [[Benchmark Evidence Chain]], [[Traffic Class]] | open |
| Who runs the B2 vendor-reference reproduction (AMD ROCm vLLM container on the bare cluster): Infra, as part of the Validated Cluster Profile, or Inference Optimization on Infra's cluster? The Kubernetes-line rule puts it with Infra; the skills sit with Inference Optimization. | [[Benchmark Evidence Chain]], [[AMD MI350P Qualification Plan]], [[Pillar Working Model]] | open |
| MI350P reference model and reproduction contract: Llama-70B class vs gpt-oss class, which named AMD published result, which matching conditions and permitted deviations, what tolerance. Must be fixed before B2. | [[AMD MI350P Qualification Plan]], [[Benchmark Evidence Chain]] | open |
| What should MI350P evidence prove first: technical competitiveness with NVIDIA, enterprise production readiness, or better economics for specific workloads? All three are needed eventually; the order sets initial scope and what goes to market first. Leadership decision. | [[AMD MI350P Qualification Plan]], [[MI350P Serving Competitive]] | open |
| Should vendor-reference reproduction gate **infrastructure acceptance** (B2) or only **serving qualification**? The policy now records "infrastructure accepted" and "reference performance validated" as separate outcomes; AMD's published configuration may differ from ours in topology, software or settings. | [[Benchmark Evidence Chain]], [[AMD MI350P Qualification Plan]] | open |
| What existing MI350P evidence (AMD, engineering, earlier internal tests) can be reused at its tier, and what is genuinely missing? | [[AMD MI350P Qualification Plan]], [[Benchmark Library]] | open |
| Competitive band for [[MI350P Serving Competitive]]: what counts as a "win" — performance parity, better economics at the same SLO, or supporting workloads that would otherwise need more NVIDIA GPUs — and what counts as "competitive" for C1 performance (a proposal on the table: SLO-qualified goodput per GPU ≥ 90% of H100 — illustrative, not ratified) and for C3 economics (cost per 1M successful tokens vs H100). Product decision. | [[MI350P Serving Competitive]] | open |
| User model for capacity claims: what arrival rate per user, think time, active fraction, and token distributions turn "concurrent requests" into "users supported"? Required before any user-count claim. | [[Benchmark Evidence Chain]], [[AMD MI350P Qualification Plan]], [[Traffic Class]] | open |
| Power telemetry at deployment grain: can Infra's GPU telemetry (`amd-smi` / DCGM) be co-sampled with serving runs so [[Energy per Token]] is measurable? | [[Energy per Token]], [[KPI Telemetry Target List]] | open |
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
| Should RackAI adopt VMware Avi's (Broadcom) AI Gateway / multi-cluster load-balancing services to close the global-front-door gap? Adoption is an open evaluation; the shared architectural baseline is captured in the partner brief. Decision turns on the identity hand-off and Avi's answers to the questions in the partner brief. | [[Multi-Cluster Governance Brief (Partner)]] | open |
| Identity hand-off to a partner AI Gateway (e.g. Avi's): how would an edge tier consume a trusted RackAI tenant identity? This is the one governance layer a load balancer cannot supply on its own and the input to every other layer — the decisive item for any adoption decision. | [[Multi-Cluster Governance Brief (Partner)]], [[Identity & Access Control]] | open |
| Uniphore delivery-status conflict: the Jun 2026 project update reports NIM inference, SFT, and LoRA as *completed* and shared in staging, while the Uniphore progress slide colors the same capabilities "Milestone 2 — Target May 15" (not yet in production). Likely delivered to staging but not promoted to Uniphore production. Engineering must confirm before any "in production" claim to Uniphore. | [[Uniphore Recovery Plan — RackAI Input]], [[Model Deployment]], [[Fine-Tuning]] | open |
| Uniphore engagement gap: a dedicated Uniphore production environment (DFW3 undercloud, 8× H100) is Active, but no Uniphore acceptance, production feedback, or current (post-Jun 2026) priorities/success-definition are on record. Is Uniphore still engaged on the production ("DFW Prod") track? | [[Uniphore Recovery Plan — RackAI Input]], [[Environment]], [[Organization]] | open |
| Uniphore requirement currency: the strongest "Uniphore requirements" we hold (OpenAI-only API, SFT-first, file-upload data, single-cluster, private-registry ask) are secondhand (attributed to Paavan during MVP planning, several flagged "assuming… need clarification"), not direct Uniphore statements. Which still hold? | [[Uniphore Recovery Plan — RackAI Input]] | open |

| Telemetry provenance for the headline KPIs: TTFT and output-token throughput are declared in the roadmap and canon but appear not to be scraped, retained, or attributed per tenant/model today — and every headline metric sits at `assumed` with no confirmed producer. Which signals are collected, at what grain, and where do they live (operational vs. durable usage-grade)? Needs validation with serving, infrastructure, and factory owners. | [[KPI Telemetry Target List]], [[TTFT]], [[Output Throughput]], [[Tokens per GPU-Second]], [[Productive GPU Utilization]], [[Model Launch Lag]] | open |

The register extends as new unknowns or source conflicts surface.

## See Also

- [[Evidence Hub]]
- [[Validation Register]]
- [[Benchmark Library]]
