---
id: evd-gpu-neocloud-competitors
type: evidence
status: draft
owner: product
domain: capacity
aliases: [gpu neocloud competitors, neocloud, coreweave, lambda, lambda labs, capacity partners, battleground a competitors]
related: [hub-evidence, hub-battlegrounds, hub-commercial, hub-rackai-platform, evd-inference-serving-competitors, evd-sovereign-governed-competitors, asm-fleet-competitiveness]
source_docs: ["https://www.coreweave.com/", "https://lambda.ai/", "web research 2026-09-21"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-evidence
summary: "Battleground (a) capacity competitors: CoreWeave and Lambda, and why neither is a topology peer to RackAI."
---

# GPU Neocloud Competitors

Competitor profiles for **[[Three Battlegrounds|Battleground (a) — capacity partner]]**: providing the hardware and GPU-fleet economics. The key finding: both are **supply/partner relationships, not like-for-like rivals** — their fabric is optimized for the opposite end of the spectrum from RackAI's [[Fleet Competitiveness|topology-capped ~27B]] serving envelope.

> **Confidence discipline.** Hardware/interconnect specs from official docs are `measured`. Funding valuations and revenue figures are press-reported (`derived`). Point-in-time GPU-hour prices are `measured`-at-a-point but volatile — dated where cited. Sovereign/HIPAA posture for both is an open question. Content rephrased for compliance with licensing restrictions.

## CoreWeave

- **Positioning.** Self-styled "AI Hyperscaler" — a purpose-built GPU cloud for large-scale AI training and inference ([GB200 launch](https://www.coreweave.com/news/coreweave-launches-nvidia-gb200-grace-blackwell-systems-at-scale)).
- **What they sell.** Broad stack: raw GPU capacity, managed Kubernetes (CKS), Slurm-on-Kubernetes (SUNK), **and a real inference product family** — fully-managed Serverless, configurable Dedicated Inference, and self-managed on CKS ([Inference docs](https://docs.coreweave.com/products/inference); [Dedicated Inference](https://coreweave.com/products/dedicated-inference)). So CoreWeave competes as both a capacity partner *and* a serving-platform provider.
- **Fleet & interconnect.** Full NVIDIA high-end lineup; among the first CSPs on H100/H200 and first to GA on **GB200 NVL72** and **HGX B200** ([GB200 NVL72 GA](https://coreweave.com/blog/coreweave-becomes-the-first-cloud-provider-with-generally-available-nvidia-gb200-nvl72-instances); [HGX B200 GA](https://coreweave.com/blog/coreweave-expands-its-nvidia-blackwell-fleet-with-generally-available-nvidia-hgx-b200-instances)). Interconnect is **rack-scale NVLink (NVL72) + Quantum-2 InfiniBand**; benchmarked 800 TPS on Llama 3.1 405B on GB200 ([MLPerf v5.0](https://www.coreweave.com/news/coreweave-achieves-new-record-breaking-ai-inferencing-benchmark-with-nvidia-gb200-grace-blackwell-superchips)) (`measured`).
- **Sovereign/compliance.** Holds SOC 2 ([neocloud SOC 2 guide, 2026](https://www.spheron.network/blog/soc-2-compliant-gpu-cloud-providers-2026/)). Hybrid/on-prem via Red Hat AI + llm-d on CKS ([Red Hat AI on CKS](https://coreweave.com/blog/red-hat-ai-inference-on-cks-for-hybrid-inference)). Sovereign-region / HIPAA specifics unverified.
- **Pricing.** Per-GPU-hour + reserved capacity; >75% of revenue is contracted/committed ([Motley Fool, Sep 2026](https://www.fool.com/investing/2026/09/11/coreweave-is-my-top-ipo-pick-right-now-x-of-its-re/)).
- **Scale.** **IPO'd on Nasdaq 2025-03-28** at $40/share ([CNBC](https://www.cnbc.com/2025/03/28/coreweave-starts-trading-on-nasdaq-at-per-share.html)). FY2025 revenue ~$5.13B, up ~168% YoY; net loss ~$1.2B; significant debt-fueled capex ([FY2025 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results/default.aspx); [stockanalysis.com](https://stockanalysis.com/stocks/crwv/)) (`derived`).
- **Relevance to RackAI.** Architected for the opposite end of the spectrum — full-mesh NVLink/InfiniBand superclusters for frontier-scale training and 405B-class inference. A PCIe/NVLink-pair, ~27B-class platform does not compete head-on. CoreWeave is a **capacity/scale partner, not a same-tier rival**.

## Lambda (Lambda Labs / Lambda Cloud)

- **Positioning.** "The AI cloud company founded by AI engineers" — on-demand NVIDIA GPUs with transparent pricing and no egress fees; increasingly framing gigawatt-scale "AI factories" and single-tenant superclusters ([Lambda Cloud](https://lambdalabs.com/cloud); [Superintelligence](https://lambda.ai/superintelligence)).
- **What they sell.** On-demand GPU Instances, **1-Click Clusters**, and reserved Superclusters ([pricing](https://lambda.ai/pricing)), plus a **Lambda Inference API** — OpenAI-compatible token-billed endpoints for ~20 open models on dedicated GPU clusters. Nuance: Lambda no longer offers *serverless* BYO-model auto-scaling inference ([premai, 2026](https://www.premai.io/blog/serverless-llm-deployment-runpod-vs-modal-vs-lambda-2026/)), and it **shut down its on-prem workstation/server hardware business in Aug 2025** to redirect GPUs to rental ([Sacra](https://sacra.com/research/no-side-quests-for-lambda/)). Net: capacity-first with a bounded inference-API product — less of a full serving platform than CoreWeave.
- **Fleet & interconnect.** On-demand **H100, H200, B200** ([pricing](https://lambda.ai/pricing)). 1-Click Clusters: 16–512 H100/B200 **SXM** GPUs on NVIDIA Quantum-2 400 Gb/s **InfiniBand**, rail-optimized non-blocking fabric ([1CC docs](https://docs.lambda.ai/public-cloud/1-click-clusters/)); single-tenant clusters advertised up to ~165,000 GPUs ([Superintelligence](https://lambda.ai/superintelligence)) (`measured`).
- **Sovereign/compliance.** Holds SOC 2 ([neocloud SOC 2 guide](https://www.spheron.network/blog/soc-2-compliant-gpu-cloud-providers-2026/)). No verified sovereign-region or on-prem appliance offering after the Aug 2025 hardware shutdown (unverified / likely not offered).
- **Pricing.** Per-GPU-hour on-demand + reserved/committed; widely cited H100 SXM ~$2.49–3.99/GPU-hr, B200 ~$6.69/GPU-hr mid-2026 (drift; date-sensitive) ([markaicode](https://markaicode.com/pricing/lambda-labs-pricing/)).
- **Scale.** Series E ~$1.5B announced 2025-11-18, led by TWG Global, following a multibillion-dollar Microsoft deal; valuation undisclosed ([TechCrunch, Nov 2025](https://techcrunch.com/2025/11/18/ai-data-center-provider-lambda-raises-whopping-1-5b-after-multibillion-dollar-microsoft-deal/)). Still private; pre-IPO chatter cites ~$12B+ ([TechFundingNews](https://techfundingnews.com/lambda-eyes-12b-valuation-with-3b-pre-ipo-raise-as-ai-cloud-race-heats-up/)) (`derived`).
- **Relevance to RackAI.** Like CoreWeave, its cluster products are SXM + InfiniBand fabric optimized for large distributed training — orthogonal to a PCIe/NVLink-pair ~27B serving envelope. Its single on-demand instances are the closest analog to commodity capacity one might source from it. A **capacity partner, not a same-tier platform rival**.

## How They Map Against RackAI

| Dimension | CoreWeave | Lambda | [[RackAI Platform\|RackAI]] |
|---|---|---|---|
| Primary product | Hyperscale GPU capacity + managed inference | GPU capacity + bounded Inference API | K8s-native inference + fine-tuning platform |
| Interconnect | NVLink NVL72 + Quantum-2 InfiniBand (SXM) | Quantum-2 InfiniBand (SXM) | **NVL-PCIe, NVLink pairs, no clustering** ([[Fleet Competitiveness]]) |
| Serving envelope | Frontier / 405B-class | Large distributed training | **~27B class** |
| Owned inference platform | Yes (Serverless/Dedicated/CKS) | Bounded fixed-catalog API | Yes ([[Model Deployment]], [[Serving Runtime]]) |
| Fine-tuning primitive | Not a platform primitive | No | [[Fine-Tuning Job]] → [[LoRA Adapter]] |
| Relationship to us | Supply/scale partner | Supply partner | — |

## Threat Assessment

- **Not a topology peer.** Neither optimizes for RackAI's serving envelope; both target frontier training/inference at fabric scale we cannot match at ~16 usable [[NVIDIA H100|H100]]. Playing (a) as identity is playing a game our topology says we lose — see [[Three Battlegrounds]].
- **CoreWeave is the more direct overlap** because it ships a real managed-inference layer on top of capacity, but still at frontier scale.
- **Correct posture:** treat both as potential **capacity partners** that extend our supply, and let our [[Unit Economics Model|cost floor]] — once established — differentiate on economics rather than on raw fabric.

## Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| CoreWeave sovereign-region + HIPAA specifics | this note, [[Three Battlegrounds]] | Low |
| Lambda sovereign/on-prem availability after the Aug 2025 hardware shutdown | this note | Low |
| Should RackAI source overflow capacity from a neocloud partner rather than compete? | [[Commercial & Capacity Hub]], [[Capacity Pool]] | Medium |

## See Also

- [[Three Battlegrounds]]
- [[Evidence Hub]]
- [[Fleet Competitiveness]]
- [[Inference Serving Competitors]]
- [[Sovereign & Governed AI Competitors]]
- [[Commercial & Capacity Hub]]
