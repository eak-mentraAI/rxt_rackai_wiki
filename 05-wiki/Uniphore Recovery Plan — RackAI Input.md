---
id: idx-uniphore-recovery-plan
type: index
status: draft
owner: product
domain: strategy
aliases: [uniphore recovery plan, uniphore rackai recovery, uniphore partnership recovery, uniphore battlecard map, customer zero recovery plan]
related: [hub-wiki, hub-rackai-roadmap, ent-model-deployment, ent-organization, wf-fine-tuning, wf-serving-lifecycle, idx-open-questions]
source_docs: [rackai_project_update_jun_2026, rackai_roadmap_master, rackai_roadmap_uniphore, rackai_m2_roadmap_csv, questions_to_uniphore_csv, uniphore_phase_1_csv, project_specific_rackai_docs, iaas_battlecard, ftaas_battlecard]
confidence: assumed
last_reviewed: 2026-10-02
parent: hub-wiki
summary: "Uniphore recovery-plan input: current roadmap, what we can offer and when, and battlecard-mapped capability status."
---

# Uniphore Recovery Plan — RackAI Input

**Owner:** Ed Kerr · **For:** Chetan Gupta / Gajen leadership review · **Status:** draft for discussion

**Scope:** the three RackAI deliverables assigned to Ed:
- **#2 — Current RackAI roadmap at a high level**
- **#3 — What we can offer Uniphore, and when**
- **#4 — Against the FTaaS + IaaS battlecards, what is already done** (mapped to the actual cards)

Amine owns **#1** (our understanding vs. Uniphore's); a short bridge is in the opening frame.

> **Sources:** June 2026 project update (`FW- RackAI Project Update - Jun 4 2026.eml`), current master roadmap (`RackAI-Roadmap 2.pptx`), Uniphore progress slide (`RackAI-Roadmap-Uniphore.pptx`), delivery plan CSVs (`rackai-m2.csv`, `rackai-2026-roadmap.csv`, `uniphore-phase-1.csv`), clarification Q&A (`questions-to-uniphore.csv`), environment inventory (`rackai-platform` docs), and the two battlecards (`IaaS Battlecard.pdf`, `FTaaS Battlecard.pdf`).

---

## Framing (read first — 60 seconds)

Our posture into this meeting is **recovery, not apology.** Three facts anchor it:

1. **We built what we committed to as Customer 0.** The June milestone represented the scope Rackspace had aligned on with Uniphore: robust inference (vLLM + NIM, runtime-optimized) plus a defined fine-tuning capability — completed and validated in a shared environment. *(The fuller comparison of Rackspace's understanding vs. Uniphore's is Amine's #1; this note does not make a categorical claim about Uniphore's understanding.)*
2. **The requirements and priorities evolved during the engagement, including changes to the originally agreed roadmap.** (Amine, #1.) The core challenge has been maintaining a stable, mutually-agreed direction — not a failure to deliver the agreed thing.
3. **We have continued to invest heavily since.** The platform is materially stronger than what Uniphore last evaluated, and much of what a Fireworks-style buyer asks for is now built or in flight.

Per Joseph Vito's framing: we believe **we met their cost requirements** and should review that openly, and the productive next step is to put a concrete capability map in front of Uniphore and **use it to have them identify specifically what is insufficient** — on use cases, performance, and cost.

**The one thing we need from Uniphore** is a current, concrete definition of success — the priority workloads/models, performance targets, and acceptance criteria — so the next phase is sequenced against the problems that matter most to them rather than a shifting list.

---

## Recommended meeting narrative (the spine — 5–6 sentences)

> We delivered the initial RackAI capability agreed for Customer 0, including the core inference and fine-tuning foundation. Since that milestone, the platform has continued to expand across performance, accelerator flexibility, automation, observability, and broader model support. We can walk through what is available today and what is already in flight. Where we need alignment is on what Uniphore considers insufficient today, because our last detailed definition of success dates to June and the requirements have evolved since then. We would like to agree on the priority workloads, performance targets, and acceptance criteria that should govern the next phase.

Everything below is the evidence underneath this narrative. Lead with these sentences; use the tables to support them, not to replace them.

---

## #2 — Current RackAI Roadmap (high level)

| Horizon | Theme | What it delivers | Representative items |
|---|---|---|---|
| **Q3 '26** | **Foundation** | Platform/API + multi-tenant base; accelerator breadth; FT depth; operational readiness | MSP/multi-tenant controls, routing, API-layer validation, KServe upgrade, AMD+NVIDIA node support, accelerator selection, AMD AIM engine, speculative decoding, context-parallel FT, DPO, SLM, OpenCenter upgrades, repeatable performance benchmarks |
| **Q4 '26** | **Optimization** | Efficiency + maturity | GPU-memory defragmentation (density/utilization), dataset-mgmt + synthetic data, end-to-end deployment automation, inference observability (latency/throughput/health/utilization) |
| **Q1 '27** | **Expansion** | Model choice + consumption | BYOM / import model, serverless (consumption-based) inference, additional runtimes (SGLang, llama.cpp), standardized benchmarking |
| **Q2 '27** | **Enterprise scale** | Advanced inference + governance + developer experience | Batch inference, evaluation framework, experiment tracking, quantization, custom containers; tool-calling + VLM fine-tuning; embeddings/reranking, guardrails, model lifecycle, endpoint-health mgmt; tracing, private endpoints, structured output, checkpoints, API/token management |

**Exec lifecycle framing:** *Build → Fine-tune → Evaluate → Deploy → Observe → Govern* — RackAI as inferencing & fine-tuning as a service.

**Two honesty flags (internal only):** multi-region and GPU-node-access support are **backlogged (Priority 6, unscheduled)**; org-level RBAC integration ("IAC M4") is marked **"Won't Do."**

---

## #3 — What We Can Offer Uniphore, and When

"When" uses roadmap horizons, not delivery commitments — directional until Uniphore re-confirms priorities.

### A. Available now / near-term (directly relevant to the agreed scope)
| Capability | Uniphore relevance | Status |
|---|---|---|
| vLLM + NIM inference, runtime-optimized | Core "displace Fireworks" inference surface; runs Uniphore's own optimized NIM models | **Delivered** (June) |
| OpenAI-compatible API + CLI | Only API surface Uniphore flagged; automation-friendly | **Delivered**, hardened |
| Supervised fine-tuning + LoRA adapter management | Defined FT capability in agreed scope | **Delivered** (status caveat below) |
| Dataset management (file upload) | FT data workflow Uniphore scoped | **Delivered**, improving |
| Accelerator selection | Match workloads to the right GPU | **Delivered** (phase 3) |
| Autoscaling + scale-to-zero | Cost control on fixed fleet | **Delivered** |
| Gateway auth + API keys/tokens, RBAC, audit logging | Enterprise/multi-tenant operability | **Complete** |

### B. In flight — platform maturation that improves Uniphore's experience
| Capability | Uniphore need it serves | Status |
|---|---|---|
| Inference routing + shared KV cache | Throughput + utilization on H100 fleet | In progress (due 30 Oct 2026) |
| Speculative decoding, Refrag (GPU-memory defrag) | Lower latency, higher model density | Planned (Q4 2026) |
| DPO; context-parallel FT | Preference-tuned + longer-context training | In progress (due 30 Oct 2026) — context-parallel FT already complete (RACKAI-340) |
| End-to-end deployment automation (IaC) | Repeatable, faster deployments | In progress (due 30 Oct 2026) |
| Inference observability + repeatable benchmarking | Objective latency/throughput/cost evidence | Planned (Q4 2026) |
| AMD inference + AMD AIM engine | Accelerator choice beyond NVIDIA | AMD inference **Complete**; AMD AIM engine **Backlog (partnership-dependent)** |

### C. Future alignment — valuable, needs Uniphore validation first
| Capability | Possible Uniphore fit | Horizon |
|---|---|---|
| Private inference endpoints / BYOM w/ governance | Possible answer to private-registry ask | Q1–Q2 '27 |
| Serverless / consumption-based inference | Consumption model vs. Fireworks | Q1 '27 |
| Embeddings & reranking, guardrails, model lifecycle | Fuller enterprise service layer | Q2 '27 |
| Tracing, structured output, token management | Developer-experience + governance parity | Q2 '27 |

**Message pattern per item:** *Uniphore need → RackAI capability → expected impact* — not a date commitment.

---

## #4 — Battlecard Feature/Function Map (what's already done)

Vito's instruction: build a feature/function map from the FTaaS and IaaS battlecards and mark where Rackspace has delivered, where Uniphore has given feedback, and use the map to have Uniphore identify what's insufficient.

> ### ⚠️ Important framing — what the battlecards are, and what they are not
>
> Both cards (`IaaS Battlecard.pdf`, `FTaaS Battlecard.pdf`) are marked **"CONFIDENTIAL — INTERNAL USE ONLY"** (dated April 2025 / June 2026) and are authored as **sales-enablement collateral** — persona maps, discovery questions, use-case fit, and CIO/CFO value props. They were built to *position and sell* RackAI to the market generally (offering manager: Amine; product marketing: Sharon Varalli).
>
> They are genuinely useful here as a **capability checklist and shared vocabulary**, and are mapped below. But we should be clear and respectful on one point so they are not misused:
>
> - **Uniphore has never seen these cards.** They are not a Uniphore artifact and were never shared with or validated by Uniphore.
> - **They are not a requirements document, an SLA, or an acceptance framework.** They contain no performance targets, no cost thresholds, and no Uniphore-specific criteria — by design they describe an idealized product, not a measured one.
> - Therefore they **cannot serve as a proxy for Uniphore feedback**, and delivery "success" should not be measured against them. Doing so would substitute our internal marketing framing for the customer's actual expectations — the very gap this recovery plan exists to close.
>
> **Right use:** the cards are the *structure* that prompts Uniphore to tell us, capability by capability, what matters and what is insufficient. **Wrong use:** treating a green check against a battlecard row as evidence we met Uniphore's bar. The only valid yardstick is a current, Uniphore-stated definition of success (see §Ask).

**Legend:** ✅ Delivered · 🔄 In progress · 📋 Planned · ⚪ Backlog/not planned · ⚠️ Status conflict (resolve internally)
*The "Documented Uniphore feedback?" column is intentionally sparse — that emptiness is the finding. We hold almost no documented Uniphore feedback against these capabilities.*

### Inferencing-as-a-Service — mapped to the actual IaaS battlecard
*Battlecard "Inference Capabilities" + "Key Differentiators" lines, matched to RackAI status.*

| Battlecard capability | RackAI status | Evidence | Documented Uniphore feedback? |
|---|---|---|---|
| OpenAI-compatible APIs | ✅ | June + API-layer validation complete | Scoped as the relevant API; no detail captured |
| Open-source LLMs | ✅ | June (vLLM) | — |
| Streaming responses | ✅ (via OpenAI-compat) | Not separately documented | — |
| Dedicated inference environments | ✅ | DFW3 undercloud dedicated to Uniphore | — |
| Shared inference environments | 📋 | Multi-tenant on slide; "shared infra" scope flagged *needs clarification* | — |
| Dynamic autoscaling | ✅ | June (scale-to-zero) | Flagged "out of scope phase 1?" — unconfirmed |
| Multi-model serving | 📋 | Milestone 3+ | — |
| High-throughput workloads (GPU alloc, throughput, queue mgmt, concurrency, scheduling) | 🔄 | Routing + KV cache + speculative decoding + Refrag in progress | **No throughput target on record** |
| GPU-backed inference across NVIDIA **and** AMD | ✅ NVIDIA / ✅ AMD inference | AMD inference complete; AMD AIM engine backlog (partnership-dependent) | — |
| Integrated observability / monitoring | 🔄 | Platform monitoring in progress | **The data that would let Uniphore articulate "insufficient"** |
| Operational automation | 🔄 | e2e deployment automation (RACKAI-224) | — |
| Enterprise security controls | ✅/🔄 | Gateway auth, API keys, RBAC, audit complete; quotas building | — |
| Private / on-prem / air-gapped deployment | ✅ private / 📋 air-gapped | Runs on Rackspace undercloud; air-gapped not documented | — |
| NIM model serving *(June scope, not a card line)* | ✅ / ⚠️ | June complete; Uniphore slide marks Milestone 2 | Resolve before stating "in prod" |

### Fine-Tuning-as-a-Service — mapped to the actual FTaaS battlecard
*Battlecard "Key Capabilities" + "Key Differentiators" lines, matched to RackAI status.*

| Battlecard capability | RackAI status | Evidence | Documented Uniphore feedback? |
|---|---|---|---|
| LoRA and QLoRA fine-tuning | ✅ LoRA / 🔄 QLoRA | LoRA in June (⚠️ slide marks Milestone 2); QLoRA in flight | LoRA/QLoRA named as desired methods |
| Supervised fine-tuning (SFT) *(June scope)* | ✅ / ⚠️ | June complete; slide Milestone 2 | Resolve before stating "in prod" |
| Dataset upload and management | ✅ | June; URL-download improvement in flight | File-upload confirmed as ingestion path |
| Distributed training orchestration | ✅/🔄 | Context-parallel FT complete (RACKAI-340) | — |
| Experiment tracking | 📋 | Q2 '27 roadmap | — |
| Model versioning & lifecycle management | 🔄 | Model registry delivered; sunsetting/lifecycle in flight | — |
| GPU-aware training optimization | ✅/🔄 | Accelerator selection complete; Refrag in flight | — |
| NVIDIA **and** AMD GPU support | ✅ NVIDIA / ⚪ AMD FT | AMD inference complete, but AMD *fine-tuning* depends on the AMD AIM engine, which is backlog (partnership-dependent) | — |
| Kubernetes-native training infra | ✅ | KServe-based, upgraded | — |
| Dedicated / isolated training environments | ✅ | Dedicated Uniphore cluster | — |
| Secure model artifact management | ✅/🔄 | Local model registry; **private registry requested, priority unset** | Private registry asked for — priority not set |
| DPO *(roadmap, not a card line)* | 🔄 | RACKAI-252 | — |
| SLM support *(roadmap, "relevant to Uniphore")* | 📋 | Not started | — |

**How to use this with Uniphore:** present the two tables as *our* view of the capability surface, be explicit that it is our framing rather than their requirements, and invite Uniphore to mark — capability by capability — what matters and what is insufficient against their **use cases, performance, and cost requirements.** That anchors the next phase in *their* words, not our battlecards.

---

## The two caveats to know before the room

> ### 🛑 STATUS-CONFLICT RULE — read before writing anything customer-facing
>
> **Never resolve a status conflict by inference.** When one source says a capability is "delivered/completed" and another says "milestone/target/not yet," **preserve both statements verbatim and flag the item for internal engineering confirmation before generating any customer-facing language.** Do not promote "delivered to staging" into "production capability," and do not quietly pick the more favorable source. The affected items today are **NIM inference, SFT, and LoRA** (see caveat 1). Until engineering confirms, these are described only as *delivered to the shared/staging environment* — never as "in production" for Uniphore.

1. **Status conflict on NIM / SFT / LoRA (⚠️).** The June update (4 Jun 2026) states these were **completed and shared**; the Uniphore progress slide colors the same capabilities **"Milestone 2 — Target May 15" (not yet in production).** Both statements are preserved here on purpose — this is unresolved, not reconciled. The most plausible reading is that they reached the shared/staging environment but were not promoted to Uniphore's DFW production cluster, but that is an inference and must not be stated as fact. **Action: engineering confirms actual production status before any "in production" claim reaches Uniphore.** Also logged in [[Open Questions]].

2. **Engagement gap, not just a feature gap.** A dedicated Uniphore production environment is Active (DFW3 undercloud, 8× H100), but across all materials there is **no record of Uniphore acceptance, production feedback, or current priorities since June.** The relationship risk extends beyond the RackAI roadmap and delivery — Uniphore appears disengaged on the production ("DFW Prod") track as well. Re-establishing engagement and a current success definition is the primary objective; the capability map is the vehicle to open that conversation, not the end goal.

---

## Recommended ask of Uniphore

Five, prioritized by what changes engineering decisions:
1. What does **"production ready"** mean to you now, and which capabilities are mandatory vs. desirable?
2. For your priority workloads/models, what **latency, throughput, concurrency, and p95/p99** targets should we design and benchmark against?
3. Are the **originally scoped models and the OpenAI-compatible API** still the right reference set?
4. Against the capability map, **which specific items are insufficient** — on use cases, performance, and cost?
5. What **test cases and sign-off** constitute acceptance?

*(Cost note per Vito: we believe we met the cost requirement — bring that evidence and ask Uniphore to confirm or challenge it directly.)*
