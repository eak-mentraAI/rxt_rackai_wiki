---
id: evd-inference-serving-competitors
type: evidence
status: draft
owner: product
domain: strategy
aliases: [inference serving competitors, fireworks, fireworks ai, together, together ai, baseten, anyscale, ray, battleground b competitors]
related: [hub-evidence, hub-battlegrounds, hub-product, hub-rackai-platform, evd-erebine-competitive-analysis, evd-gpu-neocloud-competitors, evd-sovereign-governed-competitors]
source_docs: ["https://fireworks.ai/", "https://www.together.ai/", "https://www.baseten.co/", "https://www.anyscale.com/", "web research 2026-09-21"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-evidence
summary: "Battleground (b) inference competitors: Fireworks, Together, Baseten, Anyscale vs. RackAI."
---

# Inference Serving Competitors

Competitor profiles for **[[Three Battlegrounds|Battleground (b) — AI-native inference]]**: runtime muscle, orchestration, placement, and cost-effective serving of models and agents. Companion notes: [[GPU Neocloud Competitors]] (battleground a), [[Sovereign & Governed AI Competitors]] (battleground c), and [[Erebine Competitive Analysis]] (the one competitor validated against a live API).

> **Confidence discipline.** Hardware specs and dated funding events from official/reputable sources are `measured`. Funding valuations are press-reported (`derived`). Vendor security/compliance claims found only via third-party aggregators are `assumed` until confirmed on a vendor trust page. This note sits at `derived` overall. Content rephrased for compliance with licensing restrictions.

## Fireworks AI

- **Positioning.** The AI inference cloud / "platform for specialized intelligence"; automated product-and-model co-design for quality, speed, and cost. Founded 2022 by ex-Meta engineers ([Menlo VC](https://menlovc.com/perspective/menlos-investment-in-fireworks-the-runtime-for-specialized-intelligence/)).
- **Products.** Serverless per-token inference plus on-demand dedicated GPU deployments across open-weight families (Llama, Qwen, DeepSeek, GLM, Kimi); OpenAI- and Anthropic-compatible APIs ([OpenAI compatibility](https://fireworksai-docs.mintlify.app/tools-sdks/openai-compatibility)). Fine-tuning via SFT with LoRA/qLoRA, DPO, and RFT; up to 100 LoRA adapters on one dedicated deployment ([deploying LoRAs](https://docs.fireworks.ai/fine-tuning/deploying-loras)).
- **Differentiator.** Proprietary **FireAttention** kernels + disaggregated inference engine, claiming up to ~4x throughput vs. open-source alternatives with quality preserved ([FireAttention](https://fireworks.ai/blog/fire-attention-serving-open-source-models-4x-faster-than-vllm-by-quantizing-with-no-tradeoffs)) (vendor `assumed`).
- **Hardware.** Latest NVIDIA incl. B300/B200 ([Nemotron blog](https://fireworks.ai/blog/nemotron-3-ultra)). No AMD claim found (unverified).
- **Sovereign/compliance.** SOC 2 Type II / HIPAA / ISO 27001 / ISO 42001 cited only via an aggregator ([markaicode](https://markaicode.com/best/best-fireworks-ai-configuration-production-guide/)) — `assumed`, confirm on Fireworks' trust page. Dedicated deployments give single-tenant isolation.
- **Funding.** ~$1.5B Series D at ~$17.5B valuation with ~$1B ARR, reported 2026-07-16 ([Fortune/EZ Newswire](https://fortune.com/press-releases/fireworks-raises-1-5b-series-d-reaches-1b-arr-2026-07-16/)) (`derived`).
- **Battleground.** Primarily **(b)**, with a "own your specialized intelligence" tilt toward differentiated private deployment.

## Together AI

- **Positioning.** The "AI Acceleration Cloud" — make open-source models cheaper and easier to run at scale; also a neocloud renting NVIDIA clusters. Founded 2022 ([homepage](https://www.together.ai/)).
- **Products.** Serverless per-token inference across 200+ open-weight models, dedicated endpoints, GPU clusters, and fine-tuning ([dedicated endpoints](https://docs.together.ai/docs/dedicated-endpoints/v1/overview); [GPU clusters](https://www.together.ai/gpu-clusters)). OpenAI-compatible API (expected; exact wording not confirmed in this pass).
- **Differentiator.** Inference research led by Chief Scientist Tri Dao — the **FlashAttention** lineage, custom speculators, quantization; Together Inference Engine 2.0 with Turbo/Lite endpoints ([Inference Engine 2.0](https://www.together.ai/blog/together-inference-engine-2)).
- **Hardware.** NVIDIA neocloud: H100/H200/B200/GB200 clusters, bare-metal + InfiniBand ([GPU clusters](https://www.together.ai/gpu-clusters)).
- **Sovereign/compliance.** SOC 2 Type II controls on GPU clusters, customer retains data/weights ([B200 page](https://www.together.ai/gpu/nvidia-hgx-b200)). No explicit in-customer-datacenter on-prem claim found (unverified).
- **Funding.** $800M Series C at $8.3B post-money, announced 2026-07-01, led by Aramco Ventures with NVIDIA among investors ([BusinessWire](https://www.businesswire.com/news/home/20260701243402/en/)) (`derived`).
- **Battleground.** Straddles **(a)** raw capacity (neocloud clusters) and **(b)** AI-native inference. Less positioned on regulated/sovereign outcomes.

## Baseten

- **Positioning.** "The inference platform for AI-native products" — mission-critical, performant, cost-efficient inference and post-training. Founded 2019/2021 ([Series F blog](https://www.baseten.co/blog/announcing-our-series-f/)).
- **Products.** Cloud inference, dedicated deployments, **self-hosted in customer VPC**, and hybrid with overflow to Baseten Cloud; plus per-token Model APIs ([self-hosted](https://www.baseten.co/deployments/baseten-self-hosted/); [hybrid](https://www.baseten.co/solutions/baseten-hybrid/)). **Truss** is its open-source model packaging/deployment format (widely documented; not opened in this pass).
- **Differentiator.** Multi-Cloud Capacity Management (MCM) spanning cloud, self-hosted, and hybrid; autoscaling, fast cold starts, per-GPU efficiency ([MCM blog](https://www.baseten.co/blog/how-baseten-multi-cloud-capacity-management-mcm-powers-cloud-self-hosted-and-hybr/)).
- **Hardware.** NVIDIA T4 through B200 (aggregator rate cards). No AMD claim found (unverified).
- **Sovereign/compliance.** Strong: single-tenant, region-locked, and self-hosted (workload plane in customer infra, control plane at Baseten); **SOC 2 Type II, HIPAA, GDPR**; states it does not store model inputs/outputs ([dedicated](https://www.baseten.co/products/dedicated-deployments/)) (vendor-stated, `assumed`/`derived`).
- **Funding.** Series F ~$1.5B at up to ~$13B, reported June 2026 ([Series F blog](https://www.baseten.co/blog/announcing-our-series-f/); [SiliconANGLE](https://siliconangle.com/2026/06/18/ai-inference-provider-baseten-reportedly-raising-1-5b-funding/)) (`derived`; exact figures vary by source).
- **Battleground.** The closest of the four to **(c)** — self-hosted VPC + HIPAA/SOC 2/GDPR — combined with **(b)** inference performance. Not a raw-capacity neocloud.

## Anyscale

- **Positioning.** From the creators of **Ray**; a unified AI platform to run and scale ML/AI workloads (data, training, inference) around "AI-native computing" ([platform](https://www.anyscale.com/platform)).
- **Products.** Managed/serverless Ray, Ray Serve for online inference, native LLM APIs, Anyscale Endpoints + Private Endpoints (self-hosted LLMs) ([LLM APIs blog](https://www.anyscale.com/blog/llm-apis-ray-data-serve)).
- **Differentiator.** Ray itself — distributed compute scaling from laptop to thousands of heterogeneous CPU/GPU nodes; Anyscale adds optimized runtime, managed clusters, observability ([Runtime blog](https://www.anyscale.com/blog/announcing-anyscale-runtime-powered-by-ray)). More a compute/orchestration platform than a token-serving API.
- **Hardware.** Cloud-agnostic control plane running in the customer's environment or hosted by Anyscale, across GCP/Azure; first-party co-engineered Azure service announced 2025-11-04 ([Microsoft partnership](https://www.anyscale.com/press/anyscale-collaborates-with-microsoft-to-deliver-ai-native-computing-on-azure)). Doesn't primarily sell its own GPU fleet.
- **Sovereign/compliance.** In-tenant/VPC deployment is its data-residency story; explicit SOC 2 / HIPAA statements not found (unverified).
- **Funding.** No current 2026 round surfaced; historical ~$1B (2021) not confirmed here (unverified).
- **Battleground.** Primarily **(b)**, but broader than serving — competes on distributed compute/orchestration for the full AI lifecycle.

## How They Map Against RackAI

| Dimension | Fireworks | Together | Baseten | Anyscale | [[RackAI Platform\|RackAI]] |
|---|---|---|---|---|---|
| Core stance | Custom-kernel inference cloud | AI-native cloud + neocloud | Inference platform for AI-native products | Ray-based unified compute | K8s-native inference **+ fine-tuning** platform w/ tenancy + control plane |
| Inference engine edge | FireAttention (`assumed` 4x) | FlashAttention lineage | Perf + MCM | Ray Serve | vLLM/NIM via [[Serving Runtime]]; smart routing **planned** |
| Fine-tuning | SFT/LoRA/DPO/RFT | Yes | Growing post-training | Via Ray | [[Fine-Tuning Job]] → [[LoRA Adapter]] (SFT shipped) |
| Self-hosted / sovereign | Dedicated isolation | Bare-metal + SOC 2 | **Self-hosted VPC, HIPAA/SOC 2/GDPR** | In-tenant deploy | RackAI *is* the on-prem K8s platform; certs **planned** |
| Owned fleet | No (NVIDIA cloud) | Yes (neocloud) | No | No | Yes ([[GPU Fleet]], [[Accelerator Class]]) — topology-capped ~27B |
| Evidence posture | Vendor perf claims | Vendor perf claims | Vendor perf claims | Thin | No telemetry/benchmarks yet — all KPIs `assumed` |

## Threat Assessment

- **Ahead of us on (b) today:** Fireworks and Together on inference-engine performance and $/token; all four on orchestration/self-serve maturity. Our smart-routing gateway and harness runtime are `planned`, not shipped ([[Capability Gap Register]]).
- **Where we're differentiated:** first-class fine-tuning as a platform primitive, Kubernetes-native tenancy + control plane, and an owned fleet with an [[Accelerator Class]] abstraction. Fine-tuning → domain models is the wedge into [[Three Battlegrounds|Battleground (c)]].
- **The strategic read:** (b) is a well-funded race we can compete in but should not anchor identity on — fighting on $/token from a 27B-capped fleet is mid-pack. Baseten is the one to watch because it is drifting toward (c) via self-hosted VPC + HIPAA, the ground we intend to own.

## Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Confirm Fireworks' actual certification set (ISO 27001/42001, HIPAA) against its trust page | this note | Medium |
| Does Baseten's self-hosted VPC + HIPAA posture directly contest RackAI's sovereign wedge? | [[Three Battlegrounds]], [[Sovereign & Governed AI Competitors]] | High |
| Do we need a competing developer memory / agent surface (cf. Erebine)? | [[Erebine Competitive Analysis]] | Medium |

## See Also

- [[Three Battlegrounds]]
- [[Evidence Hub]]
- [[GPU Neocloud Competitors]]
- [[Sovereign & Governed AI Competitors]]
- [[Erebine Competitive Analysis]]
- [[Capability Gap Register]]
