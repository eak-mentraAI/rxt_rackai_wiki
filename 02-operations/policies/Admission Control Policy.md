---
id: pol-admission-control
type: policy
status: draft
owner: reliability
domain: reliability
aliases: [admission control policy, overload protection policy]
related: [wf-admission-control, met-ttft, met-availability, ent-model-deployment, ent-traffic-class]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-10-08
parent: hub-governance
summary: "Under overload, protect TTFT and availability rather than letting saturated GPUs collapse endpoint performance."
---

# Admission Control Policy

## Purpose

Protect [[TTFT]] and [[Availability]] under overload. Saturated GPUs that admit everything degrade every request; this policy mandates shaping or shedding excess load so admitted traffic keeps its SLO. (Roadmap Milestone 5.4.)

## Rule

When a [[Model Deployment]] approaches saturation, the serving layer must enforce limits on maximum concurrency, context-heavy requests, queue length, burst traffic, and large-output jobs. Excess requests are throttled, deferred, or rejected (capacity rejection) before TTFT or availability guardrails are breached. Protecting the SLO for admitted traffic takes precedence over admitting all traffic.

## Scope

Applies to every production [[Model Deployment]] and is differentiated by [[Traffic Class]].

## Governs

| Target | Relationship |
|--------|--------------|
| [[Model Deployment]] | GOVERNS → |
| [[Admission Control]] | CONSTRAINS → |
| [[Traffic Class]] | CONSTRAINS → |

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| GOVERNS | [[Model Deployment]] | → | Every production deployment |
| CONSTRAINS | [[Admission Control]] | → | Overload rule the workflow enforces |
| IMPLEMENTS | [[Admission Control]] | ← | Workflow implements this policy |
| CONSTRAINS | [[Traffic Class]] | → | Shaping differentiated by class |
| DEPENDS_ON | [[TTFT]] | → | Protected guardrail |
| DEPENDS_ON | [[Availability]] | → | Protected guardrail |

## Enforcement

Enforced at the serving layer by the [[Admission Control]] workflow, using [[TTFT]] and [[Availability]] as the protected guardrails. Sustained shedding escalates to [[Autoscaling]] / [[GPU Reallocation]].

## See Also

- [[Governance Hub]]
