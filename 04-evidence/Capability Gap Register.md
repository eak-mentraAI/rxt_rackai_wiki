---
id: idx-capability-gap-register
type: index
status: draft
owner: product
domain: strategy
aliases: [capability gap register, capability gaps, gap register, capability-vs-goal matrix, missing capabilities]
related: [hub-evidence, hub-rackai-platform, hub-product, idx-open-questions, idx-validation-register, idx-kpi-hierarchy, src-strategic-vision, src-engineering-roadmap]
source_docs: [openrouter_strategic_vision.md, openrouter_engineering_roadmap.md, rackai_platform_prd, rackai_release_1_0_0, metering_spec, identity_access_spec, monitoring_audit_spec]
confidence: derived
last_reviewed: 2026-09-04
parent: hub-evidence
summary: "Capability-vs-goal matrix: the platform capabilities missing to reach the strategic project-level goals, not just the OpenRouter initiative."
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
| 1 | Commercial / unit economics | Largest hole — metering planned, billing missing, cost model absent |
| 2 | Performance & evidence (ground truth) | No telemetry or benchmarks yet; all targets assumed |
| 3 | Model velocity (day-zero factory) | Manual today; radar and factory unbuilt |
| 4 | Dynamic fleet allocation | Static today; routing/admission/reallocation planned |
| 5 | Platform-product completeness | Serving substrate shipped; tenancy features thin |

## 1 — Commercial / Unit-Economics Goals

Goal: close the loop *tokens/GPU-second → cost/token → price → traffic → utilization* (see [[Commercial & Capacity Hub]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| [[Billing & Payment]] (charge computation, payment) | missing | assumed | Billing/payment P0 blocker (explicit non-goal of metering spec) |
| [[Metering]] — usage capture, `UsageRecord`, quotas | planned | assumed | When metering ships / how quotas enforce |
| [[Cost per GPU-Hour]] internal cost model | missing | assumed | Internal cost per GPU-hour not established |
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
| Smart-routing gateway (hardware-aware + economic routing) | planned | assumed | Whether prefill/decode disaggregation is justified |
| [[Admission Control Policy]] enforcement | planned | assumed | — |
| [[GPU Reallocation]] / [[Capacity Pool]] dynamic allocation | planned | assumed | — |
| Warm pools | planned | assumed | — |

## 5 — Platform-Product Completeness Goals

Goal: a full multi-tenant inference + fine-tuning product, not just a serving backend (see [[RackAI Platform]]).

| Required capability | State | Confidence | Open question |
|---------------------|-------|:----------:|---------------|
| Production [[Environment]] | planned | assumed | — |
| [[API Key]] (programmatic access) | planned | assumed | API Key ship status (blocks OpenRouter Path A) |
| Full RBAC roles / Projects | planned | assumed | — |
| Tenant-facing observability + [[Audit]] | planned | derived | Platform monitoring shipped; per-tenant view planned |
| Fine-tuning breadth: RL & DPO methods | planned | assumed | RL/DPO "Coming Soon" — only SFT shipped |
| Runtime breadth (SGLang, TensorRT-LLM, NVIDIA Dynamo) | planned | assumed | Optimal engine per model unknown |
| Accelerator breadth (Intel Gaudi, CPU) | planned | assumed | — |
| Canonical deployment path resolved | partial | derived | Legacy Platform9 vs Docker+Helm+nginx |

## The Through-Line

RackAI can **serve** models today (org/namespace tenancy, control-plane CRDs, KServe deployments with OpenAI-compatible endpoints, KEDA autoscaling, Accelerator Class abstraction, LoRA serving, SFT fine-tuning, platform-level monitoring — all `measured` in 1.0.0). What is missing is almost all of Layers 3–4 (commercial/capacity and evidence) plus the automation and closed-loop parts of Layer 2. In one line: the platform cannot yet **meter** models, **bill** for them, **know what they cost**, **prove how fast they are**, **launch them in hours**, or **move capacity toward the best ones** — which is exactly the enduring operating capability the strategy defines as the point of the project.

## Caveats

- No dedicated platform-whole OKR document exists; platform-level goals are inferred from [[RackAI Platform]] plus the initiative narratives ([[Rack AI OpenRouter Strategic Vision]], [[Rack AI OpenRouter Engineering Roadmap]]).
- Confidence is `derived`: the gaps are traced from shipped-vs-planned status and the [[Open Questions]] register, but no telemetry confirms the shipped side performs to goal.

## See Also

- [[Evidence Hub]]
- [[Open Questions]]
- [[Validation Register]]
- [[KPI Hierarchy]]
- [[RackAI Platform]]
