---
id: wf-model-launch-factory
type: workflow
status: draft
owner: model-enablement
domain: model-enablement
aliases: [model launch factory, day-zero factory, launch pipeline]
related: [wf-model-deployment, wf-canary-rollback, evt-new-model-detected, evt-deployment-canary-passed, met-model-launch-lag, ent-model, ent-benchmark-run, wf-model-radar, fml-gpus-per-replica, coeff-model-weight-footprint, met-ttft, met-tokens-per-gpu-second, fml-cost-per-1m-tokens, val-launch-lag-24h, met-output-throughput, idx-phase1-execution-glm, ent-deepseek-v4-flash, ent-glm-5-3-flash]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-09
parent: hub-operations
summary: "Day-zero factory that moves a new model from radar detection to OpenRouter publication in a repeatable pipeline."
---

# Model Launch Factory

> **Roadmap status (2026-10-09).** The full factory is a roadmap gap, rated `Won't (this horizon)`. Its middle (intake → functional validation → benchmark → canary, human-gated, known architectures) is pulled forward as **model onboarding pipeline v0** (RACKAI-354, MOE-1), plus a **model version upgrade** row that reuses [[Canary & Rollback]]. Model Radar and automated OpenRouter publication stay deferred. See [[Roadmap Narratives]] (N5).

## Purpose

Turn model launches from bespoke engineering projects into a repeatable pipeline. The factory carries a newly available [[Model]] from radar detection through automated intake, validation, hardware fit, benchmarking, canary, and OpenRouter publication so that a known architecture can reach production without a cross-functional war room. (Roadmap Phase 4.)

## Trigger

- [[New Model Detected]] emitted by Model Radar when a strategically relevant model appears.
- Operator-initiated launch candidate for a pre-announced model (day-zero readiness).

## State Machine

```mermaid
stateDiagram-v2
    [*] --> Radar
    Radar --> Intake: strategically relevant model detected
    Intake --> FunctionalValidation: arch/params/context/tokenizer/precision/capabilities extracted
    FunctionalValidation --> HardwareFit: functional tests pass
    FunctionalValidation --> Blocked: capability failure
    HardwareFit --> Benchmark: candidate config selected
    Benchmark --> Canary: meets performance thresholds
    Benchmark --> Blocked: below threshold
    Canary --> Publication: canary gate passed
    Canary --> Blocked: rollback triggered
    Publication --> [*]: published to OpenRouter
    Blocked --> [*]
```

## Steps

1. Model Radar — model-enablement; continuously tracks model labs, Hugging Face, GitHub, NVIDIA, OpenRouter, and research. Emits [[New Model Detected]] for strategically relevant models. (Milestone 4.1.)
2. Automated intake — model-enablement; auto-extracts architecture, parameter count, active parameter count, context length, tokenizer, precision, multimodal/tool capabilities, and memory requirements; produces a preliminary deployment recommendation. (Milestone 4.3.)
3. Functional validation — model-enablement; standardized tests for loading, generation, streaming, tokenization, long context, tools, structured output, reasoning controls, multimodal, and concurrency. Failures identify the blocking capability. (Milestone 4.4.)
4. Hardware fit testing — performance-eng / infrastructure; runs candidate configs against available hardware to determine minimum GPU count, preferred GPU type, memory headroom, [[Topology]] requirement, and initial parallelism profile. (Milestone 4.5.)
5. Benchmark stage — performance-eng; generates baseline [[TTFT]], [[Output Throughput]], [[Tokens per GPU-Second]], memory use, concurrency scaling, and cost/1M tokens via a [[Benchmark Run]], comparing against established thresholds. (Milestone 4.6.)
6. Canary — reliability; hands off to [[Canary & Rollback]] for internal → canary → limited external → production promotion. (Milestone 4.7.)
7. OpenRouter publication — platform-eng; once gates pass, automatically prepares endpoint, metadata, pricing, supported parameters, context, and routing via the [[OpenRouter Provider Integration]]. (Milestone 4.8.)

Target: **<24h median / <72h P90** launch lag, measured as [[Model Launch Lag]]. These targets are roadmap targets (assumed) until measured.

## Events Emitted

| Event | When | Consumers |
|-------|------|-----------|
| [[New Model Detected]] | Radar flags a strategically relevant model | Intake stage, model-enablement |
| [[Deployment Canary Passed]] | Canary gate cleared | Publication stage, reliability |

## Dependencies

| Depends On | Type | Notes |
|------------|------|-------|
| [[Standard Model Deployment]] | DEPENDS_ON | Uses the standard deployment contract for placement |
| [[Canary & Rollback]] | DEPENDS_ON | Promotion and rollback gate |
| [[Benchmark Run]] | DEPENDS_ON | Performance evidence before canary |
| [[OpenRouter Provider Integration]] | DEPENDS_ON | Final publication surface |
| [[Model Launch Lag]] | MEASURED_BY | Headline KPI for the factory |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| CONSUMES | [[New Model Detected]] | → | Trigger: starts intake |
| GENERATES | [[New Model Detected]] | → | Via its Radar step ([[Model Radar]]) |
| DEPENDS_ON | [[Model Radar]] | → | Supplies launch candidates |
| CONSUMES | [[Model Weight Footprint]] | → | Intake extracts memory requirements |
| CONSUMES | [[GPUs per Replica]] | → | Hardware-fit step: minimum GPU count |
| DEPENDS_ON | [[Topology]] | → | Hardware-fit step: topology requirement |
| DEPENDS_ON | [[Standard Model Deployment]] | → | Standard deployment contract for placement |
| DEPENDS_ON | [[Benchmark Run]] | → | Performance evidence before canary |
| PRODUCES | [[TTFT]] | → | Benchmark stage baseline |
| PRODUCES | [[Output Throughput]] | → | Benchmark stage baseline |
| PRODUCES | [[Tokens per GPU-Second]] | → | Benchmark stage baseline |
| PRODUCES | [[Cost per 1M Tokens]] | → | Benchmark stage baseline |
| DEPENDS_ON | [[Canary & Rollback]] | → | Promotion and rollback gate |
| CONSUMES | [[Deployment Canary Passed]] | → | Proceeds to publication |
| DEPENDS_ON | [[OpenRouter Provider Integration]] | → | Final publication surface |
| MEASURES | [[Model Launch Lag]] | ← | Headline KPI |
| VALIDATES | [[Validate Launch Lag Under 24h]] | ← | Open validation |

## Ownership

Model Enablement owns the factory end to end; Performance Engineering owns the hardware-fit and benchmark stages; SRE/Reliability owns the canary gate.

## See Also

- [[Operations Hub]]
