---
id: idx-capability-gap-register
type: index
status: draft
owner: product
domain: strategy
aliases: [capability gap register, capability gaps, gap register, capability-vs-goal matrix, missing capabilities]
related: [hub-evidence, hub-rackai-platform, hub-product, hub-roadmap, idx-open-questions, idx-validation-register, idx-kpi-hierarchy, src-strategic-vision, src-engineering-roadmap, src-rackai-delivery-roadmap]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md, rackai_platform_prd, rackai_release_1_0_0, metering_spec, identity_access_spec, monitoring_audit_spec, "reference/RackAI - Roadmap.xlsx"]
confidence: derived
last_reviewed: 2026-09-21
parent: hub-evidence
summary: "Capability-vs-goal matrix: the platform capabilities missing to reach the strategic project-level goals."
---

# Capability Gap Register

## Purpose

Maps the **strategic project-level goals** of the [[RackAI Platform]] to the capabilities required to reach them, and records which of those capabilities are missing today. This is a navigation and tracking index over the evidence layer: it does not redefine goals, metrics, or entities — it links to their canonical homes and to the [[Open Questions]] register where a gap is also a genuine unknown.

Scope is the **whole project**, not just the [[OpenRouter Initiative]]. The enduring goal (per [[Rack AI OpenRouter Strategic Vision]] and [[Rack AI OpenRouter Engineering Roadmap]]) is a repeatable operating system: *identify a model early → launch it in hours → optimize its performance → maximize fleet utilization → improve the economics of every token*, running on a multi-tenant inference + fine-tuning platform. OpenRouter rank is an outcome of that system, not the system itself (see [[KPI Hierarchy]]).

## How to Read This

- **Goal** — the strategic objective the capability serves.
- **Required capability** — what must exist to reach the goal.
- **State** — `shipped` (RackAI 1.0.0, `measured`), `partial`, `planned` (`assumed`/`derived`, not shipped), or `missing` (no plan / explicit non-goal).
- **Confidence** — the weakest truthful state per the [[Evidence Hub]] framework.
- **Open question** — link to the tracked unknown where one exists.

> Per the [[Evidence Hub]], no benchmark run or production telemetry exists yet, so even `shipped` capabilities are unproven against their targets. Every target number remains `assumed` until validated (see [[Validation Register]]).

## Gap Summary by Goal Area

| # | Goal Area | Net State |
|---|-----------|-----------|
| 1 | Commercial / unit economics | Largest hole — metering **now in progress** (M1), billing an open RXT question, cost model still absent |
| 2 | Performance & evidence (ground truth) | Telemetry now in progress (Platform M1–M2); benchmarks not started; targets still assumed |
| 3 | Model velocity (day-zero factory) | Manual today; radar and factory unbuilt |
| 4 | Dynamic fleet allocation | Inference routing (llm-d) in progress; admission control/reallocation planned |
| 5 | Platform-product completeness | Serving + **auth/RBAC/audit-API shipped** (IAC M1–M3); org-level RBAC dropped; tenant observability in progress |

## 1 — Commercial / Unit-Economics Goals

Goal: close the loop *tokens/GPU-second → cost/token → price → traffic → utilization* (see [[Commercial & Capacity Hub]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| [[Billing & Payment]] (charge computation, payment) | missing | assumed | Billing/payment P0 blocker (open question to RXT in the [[RackAI Roadmap (Delivery Plan)\|delivery roadmap]]) |
| [[Metering]] — usage capture, `UsageRecord`, quotas | partial (in progress) | derived | Metering M1 pipeline **in progress** (RACKAI-352); M2–M4 (UsageRecord APIs, quotas, enforcement) not started — [[RackAI Roadmap (Delivery Plan)]] |
| [[Cost per GPU-Hour]] internal cost model | missing | assumed | Usage is metered, but cost/GPU-hour modeling is **absent from the delivery roadmap** — strategy gap (roadmap P-003) |
| [[Revenue per GPU-Hour]] / [[Gross Margin per Model]] inputs | planned | derived | Depends on cost model + metering above |
| [[Demand Forecasting]] as an operating system | planned | assumed | — |
| [[Fleet Yield Optimization]] / [[Procurement Trigger]] | planned | assumed | — |

The cost model is the foundational coefficient: without it, every downstream economic number is `assumed`. Roadmap Phase 0.3 (cost model) is unbuilt.

## 2 — Performance & Evidence Goals (Ground Truth)

Goal: treat every priority model as an optimization program measured against the fastest competitor (see [[KPI Hierarchy]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| Production telemetry / benchmark runs | missing | assumed | No [[Benchmark Run]] or telemetry exists yet |
| GPU telemetry (compute / HBM / bandwidth / power) | partial | derived | Platform Prometheus shipped; per-GPU KPI visibility unconfirmed |
| Benchmark harness + performance lab | planned | assumed | Optimal serving engine per model unknown |
| Fleet inventory / hardware-fit confirmation | partial | assumed | H100 sufficiency for large MoE; ~27B topology ceiling; L40S-vs-L40; A30 role |
| [[TTFT]] / [[Tokens per GPU-Second]] / [[Productive GPU Utilization]] measured | planned | assumed | All four headline KPIs sit at assumed |

## 3 — Model-Velocity Goals (Day-Zero Factory)

Goal: <24h median / <72h P90 launch lag, with day-zero readiness (see [[Model Launch Lag]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| Model Radar (Launch Now / Prepare Next / Watch pipeline) | missing | assumed | — |
| Day-Zero Launch Factory (automated intake→validate→fit→benchmark→canary→publish) | planned | assumed | — |
| Measured launch lag | missing | assumed | [[Validate Launch Lag Under 24h]] (open) |

## 4 — Dynamic Fleet Allocation Goals

Goal: capacity follows Demand × utilization × performance × revenue/GPU-hour × strategic importance.

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| Smart-routing gateway (hardware-aware + economic routing) | partial (in progress) | derived | Inference routing (llm-d, shared KV cache) **in progress** (RACKAI-311); evidence/economic-driven routing not yet — [[RackAI Roadmap (Delivery Plan)]] |
| [[Admission Control Policy]] enforcement | planned | assumed | — |
| [[GPU Reallocation]] / [[Capacity Pool]] dynamic allocation | planned | assumed | — |
| Warm pools | planned | assumed | — |

## 5 — Platform-Product Completeness Goals

Goal: a full multi-tenant inference + fine-tuning product, not just a serving backend (see [[RackAI Platform]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| Production [[Environment]] | planned | assumed | — |
| [[API Key]] (programmatic access) | shipped | measured | **Complete** — IAC M1 (APIKey CRD + Gateway auth, RACKAI-204); unblocks OpenRouter Path A — [[RackAI Roadmap (Delivery Plan)]] |
| Full RBAC roles / Projects | partial | derived | Platform RBAC **complete** (IAC M2, RACKAI-333); **org-level RBAC dropped** (IAC M4 "Won't Do") — strategy gap (roadmap P-006) |
| Tenant-facing observability + [[Audit]] | partial (in progress) | derived | Audit Log query API **complete** (IAC M3, RACKAI-351); Platform/Observability telemetry in progress; Auditing M1–M3 not started |
| Fine-tuning breadth: RL & DPO methods | partial (in progress) | derived | DPO fine-tuning **in progress** (RACKAI-252); SFT shipped; RL still not planned — [[RackAI Roadmap (Delivery Plan)]] |
| Runtime breadth (SGLang, TensorRT-LLM, NVIDIA Dynamo) | planned | assumed | Optimal engine per model unknown |
| Accelerator breadth (Intel Gaudi, CPU) | planned | assumed | — |
| Canonical deployment path resolved | partial | derived | Legacy Platform9 vs Docker+Helm+nginx |

## The Through-Line

RackAI can **serve** models today (org/namespace tenancy, control-plane CRDs, KServe deployments with OpenAI-compatible endpoints, KEDA autoscaling, Accelerator Class abstraction, LoRA serving, SFT fine-tuning, platform-level monitoring — all `measured` in 1.0.0). Per the [[RackAI Roadmap (Delivery Plan)|delivery roadmap]] (2026-09, `measured`), the CSP Platform Layer has since **shipped identity/auth, platform RBAC, and the audit-log query API** (IAC M1–M3), and has **metering, telemetry, and inference routing in progress**. What remains missing clusters in Layers 3–4 (commercial/capacity and evidence) plus the closed-loop parts of Layer 2 — and, from the operator strategy's view, the **cost model, the Empirical Map (moat), a governed harness, and a compliance attestation**. In one line: the platform can increasingly **meter and observe** models, but still cannot **know what they cost**, **prove how fast they are** against competitors, **decide from cross-workload evidence**, or **operate inside a certified enterprise boundary** — which is the enduring operating capability the strategy defines as the point of the project.

## Caveats

- No dedicated platform-whole OKR document exists; platform-level goals are inferred from [[RackAI Platform]] plus the initiative narratives ([[Rack AI OpenRouter Strategic Vision]], [[Rack AI OpenRouter Engineering Roadmap]]).
- Confidence is `derived`: the gaps are traced from shipped-vs-planned status and the [[Open Questions]] register, but no telemetry confirms the shipped side performs to goal.

## See Also

- [[Evidence Hub]]
- [[Open Questions]]
- [[Validation Register]]
- [[KPI Hierarchy]]
- [[RackAI Platform]]
