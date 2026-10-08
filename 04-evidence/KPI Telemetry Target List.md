---
id: evd-kpi-telemetry-targets
type: evidence
status: draft
owner: product
domain: performance
aliases: [kpi telemetry targets, telemetry target list, measurement contract, telemetry gap review, metric provenance review]
related: [hub-evidence, idx-metrics, idx-kpi-hierarchy, met-ttft, met-output-throughput, met-tokens-per-gpu-second, met-gpu-utilization, met-availability, met-model-launch-lag, met-cost-per-outcome, ent-empirical-map, hub-operations, hub-commercial]
source_docs: ["repo review 2026-10-05 (TTFT/output-throughput telemetry gap)", "openrouter_engineering_roadmap.md", "openrouter_strategic_vision.md"]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-evidence
summary: "Product's measurement contract for the RackAI KPI model: the signals we need, why each matters, and how to review them."
---

# KPI Telemetry Target List

## Purpose

This isn't intended to prescribe the telemetry architecture. It's the set of signals Product believes we need to support the RackAI KPI model. Status reflects my understanding from the repo review and should be validated with the relevant component owners. For each signal, the review question is: **do we produce it, do we retain it at the required duration, and can we reliably attribute it at the grain the KPI requires?**

> **Confidence: `assumed` / to-validate.** This is a product review artifact, not canon. Statuses are my read from the 2026-10-05 repo review and must be confirmed with serving, infrastructure, and factory owners before any status flips to `measured`. It does not redefine the canonical metric notes it references.

## Why these signals — the product rationale

We're not collecting telemetry to have telemetry. Every metric on this list has to earn its place by serving a decision or an experience — something a human or a system acts on. If a signal doesn't change what someone does, what a customer sees, or what we can commit to contractually, it's cost without return and it shouldn't be a requirement.

Each signal we commit to should map to at least one of these four **jobs**. If it maps to none, we drop it.

**Job 1 — Internal operating decisions.** The signal drives an automated or human action inside the platform — autoscaling, admission control, canary gating, GPU reallocation, procurement triggers. These are the "keep the fleet healthy and efficient" metrics. They generally need service/model grain, not tenant grain, and operational retention is fine.

**Job 2 — Customer-facing experience.** The signal shows up in something a customer sees — a dashboard, a usage view, a model scorecard, a status page. The bar is higher: it has to be trustworthy, attributable to that customer, and retained long enough to be useful to them, not just to us.

**Job 3 — Commercial economics & commitments.** The signal backs something we promise, price against, or report as commercial performance — a latency SLA, an availability guarantee, a per-token rate, a margin target. Highest bar: durable, defensible, and measured against a baseline *before* we commit to a number. (The RACKAI-555 lesson lives here — a 500ms P95 committed, then missed 6-7x on first measurement. Don't promise a number we haven't measured.)

**Job 4 — Strategic / competitive positioning.** The signal validates whether the strategy is working — OpenRouter rank, competitive TTFT/throughput comparisons, cost-per-token trend. Informs roadmap and investment rather than day-to-day operations.

> **A signal may serve multiple jobs, but each use does not necessarily require the same measurement path.** TTFT for Job 1 (a canary guardrail) can be short-lived service/model telemetry; TTFT for Job 3 (an SLA) needs a durable, tenant-attributable record. That's effectively two measurement products from one underlying signal. We should build to the highest bar only where that use is actually committed — a Job 3 tag is a *potential* requirement, not a standing instruction to build SLA-grade persistence now.

### The test for each signal

- **Who or what consumes it, and what do they do differently because of it?** If the answer is "nobody yet," it's a candidate to defer, not build.
- **Which of the four jobs does it serve, and which of those are actually committed?** The committed jobs decide grain, retention, and attribution. An internal autoscaling signal and a customer-billed signal have very different bars; we shouldn't pay the high bar for a job we haven't committed to.
- **Can we reliably attribute it at the grain the committed job requires?** Nearly every KPI resolves to *measurement + dimensions + retention + a trustworthy join*. Attribution can happen at the producer or downstream, as long as the relationship is reliable and not lost.
- **What's the cost of being wrong or missing?** A metric backing an SLA failing silently is a very different risk than an internal efficiency dashboard being stale.

### Expected review outcome

Walking this list with engineering, each signal should leave with one of four dispositions:

| Disposition | Meaning |
|---|---|
| **Sufficient** | Existing measurement path supports the intended job |
| **Gap** | Required for a committed use, but the measurement path is insufficient |
| **Defer** | Valuable, but no current product/operating need justifies the work |
| **Investigate** | We don't yet understand the existing implementation well enough to decide |

The goal is to leave the review knowing which gaps become roadmap work — not just a list of interesting findings.

### Why this matters for the review

The point of walking the list with engineering isn't just "what's missing." It's to make sure the *grain and durability we ask for match the job the metric actually serves* — so we don't over-build operational telemetry into a billing pipeline it doesn't need, or under-build a customer-facing number into 90-day operational storage it will outlive. The job sets the requirement, not the metric. It also sequences the work: Job 1 signals are more likely to already exist in operational telemetry; Job 3 signals require the most discipline, because durability, attribution, and defensibility raise the measurement bar — and that's where a missing or untrustworthy signal becomes a broken promise.

**Status legend:** *Confirmed* = verified in the repo during review; *To validate* = my read, needs an owner to confirm.

## 1. Serving latency & throughput

| Signal | Job | Source / producer | Retained? | Attributable at KPI grain? |
|---|:---:|---|---|---|
| Time to first token (P50/P95/P99) | 1,2,3,4 | vLLM exposes native metric (confirmed) | Not scraped today (to validate) | Not at tenant/model grain today (to validate) |
| Output tokens/sec | 1,2,3,4 | vLLM exposes native metric (confirmed) | Not scraped today (to validate) | Not at tenant/model grain today (to validate) |
| Queueing delay | 1 | vLLM queue metrics (to validate) | Not scraped today (to validate) | Service grain likely fine; tenant grain to validate |
| End-to-end request latency | 1,2 | vLLM native metric (confirmed) | Partially wired — recording rule + panels (confirmed) | Service grain today; tenant grain to validate |
| Requests waiting / running | 1 | vLLM native metric (confirmed) | Consumed by autoscaling (confirmed) | Service grain — sufficient for its use (confirmed) |
| KV cache usage % | 1 | vLLM native metric (confirmed) | Consumed by autoscaling (confirmed) | Service grain — sufficient (confirmed) |
| Request success / error rate | 1,2 | vLLM `request_success_total` (confirmed) | Consumed today (confirmed) | Service grain today; tenant grain to validate |

**For discussion:** my read is that TTFT and output tokens/sec are the clearest gaps — the metrics exist but don't appear to be scraped or retained. I'd like to validate with the serving owners whether enabling collection is sufficient or whether anything else is required. The grain question is separate: these are useful for fleet/service SLOs (Job 1) as-is; the tenant/model dimension only matters for the Job 2/3 uses.

## 2. Durable usage-grade serving records

| Signal | Job | Source / producer | Retained? | Attributable? |
|---|:---:|---|---|---|
| input / output / cached tokens | 2,3 | usage_records (confirmed) | 13-month window (confirmed) | Tenant-attributed (confirmed) |
| queue_secs / latency_secs / compute_secs | 2,3 | Columns exist but read as 0 — no producer writes them (confirmed) | Persisted but unpopulated (confirmed) | — (no producer) |
| TTFT as a durable/customer-reporting dimension | 2,3 | No producer today (to validate) | Would need a persisted record (to validate) | Tenant grain (to validate) |
| Output-token throughput as durable dimension | 2,3 | No producer today (to validate) | Needs a trustworthy duration to pair with tokens (to validate) | Tenant grain (to validate) |

**For discussion:** for billing or durable customer reporting, my assumption is we need a persisted usage-grade record rather than relying on 90-day operational telemetry. I'm treating TTFT and tokens/sec as durable/customer-reporting dimensions, not billing dimensions — important for SLA/product/commercial reporting, but I'm not assuming we price on them unless there's intent to. Worth confirming where that line sits. One caveat the existing `*_secs` columns surface: a column that defaults to 0 can't distinguish "not collected" from a real zero — worth representing absence explicitly if we add fields here.

## 3. GPU / fleet telemetry

| Signal | Job | Source / producer | Retained? | Attributable at KPI grain? |
|---|:---:|---|---|---|
| GPU-hours available vs consumed | 1 | To validate | To validate | Needs to reach model/pool grain (to validate) |
| HBM utilization % | 1 | To validate | To validate | Needs model/pool grain (to validate) |
| Idle capacity % | 1 | To validate | To validate | Needs pool grain (to validate) |
| GPU-seconds consumed per deployment | 1,3 | To validate | To validate | Needs deployment grain (to validate) |

**For discussion:** GPU counters likely exist in some form (DCGM/node-level); the open question is whether they reach the model/pool/deployment grain the utilization and tokens/GPU-second KPIs need — and whether that grain comes from the producer or a downstream join to deployment metadata. Both are fine; the requirement is that the path is reliable. Most of these are internal operating signals (Job 1); only GPU-seconds-per-deployment carries a Job 3 tag, and only because it feeds cost/token — the rest are inputs to internal economics, not commercial commitments in their own right. Tokens/GPU-second specifically needs this feed and the serving token feed to meet, so the join point matters.

## 4. Model lifecycle timestamps

| Signal | Job | Source / producer | Retained? | Attributable? |
|---|:---:|---|---|---|
| Weights-available timestamp (`New Model Detected`) | 1,4 | Event defined; producer to validate | To validate | Per-model (to validate) |
| Canary-passed timestamp (`Deployment Canary Passed`) | 1,4 | Event defined; producer to validate | To validate | Per-model (to validate) |
| Production-publish timestamp | 1,4 | To validate | To validate | Per-model (to validate) |

**For discussion:** different in kind from the vLLM signals — this needs the launch pipeline to stamp lifecycle events, not a metrics scrape. The events are defined as concepts; what I can't confirm is whether anything stamps them today. One for the factory owner.

## 5. Economic / FinOps inputs (derived)

| Signal | Job | Depends on | Status |
|---|:---:|---|---|
| Cost per 1M tokens | 3,4 | output tokens + GPU-seconds + cost/GPU-hour | Inherits §1 and §3 gaps |
| Revenue per GPU-hour | 3,4 | revenue + GPU-hours at model grain | Inherits §3 grain question |
| Gross margin per model | 3,4 | the two above | Fully derived — only as reliable as its inputs |
| Cost per Outcome | 3,4 | Empirical Map cost dimension (runtime instrumentation) | Planned, not confirmed shipped (to validate) — pricing-relevant, outside current OpenRouter PRD |

**For discussion:** these are formulas, so they can't be more trustworthy than their weakest input (per the Confidence Propagation rule). One important scope boundary: these KPIs depend on both *telemetry inputs* (tokens, GPU-seconds) and *business-system inputs* (revenue, contracted rates, allocated infrastructure cost from systems outside the inference stack). This review only evaluates the telemetry side — fixing GPU attribution does **not** by itself complete gross margin/model, which also needs trustworthy commercial allocation. The Cost-per-Outcome / [[Empirical Map]] line is worth raising on its own — a separate measurement surface tied to pricing, and it isn't in the OpenRouter PRD.

## 6. KPI-definition gaps surfaced by this review

These are **not telemetry asks.** The review surfaced that the [[KPI Hierarchy]] references these without a sufficiently defined measurement contract: error rate (partially covered by `request_success_total`), queueing delay, capability coverage, gross margin/model. Product should resolve the metric definition — what it means, what it's measured against — before Engineering is asked for any instrumentation. This is a Product action item, not an engineering gap.

## The cross-cutting question: attribution

Across serving, GPU, and economic telemetry, we need a reliable way to associate measurements with the dimensions the KPI requires: model, deployment/pool, tenant/project, and ultimately revenue/cost where applicable.

My assumption is that attribution should happen as close to the producer as practical, particularly where later joins would be ambiguous, but I'd like engineering to validate the right boundary for each producer. The requirement is less "every metric needs tenant_id" and more **"we cannot lose the ability to reliably attribute usage and performance at the grain required by the KPI."**

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| SUPPORTS | [[TTFT]] | → | Measurement contract |
| SUPPORTS | [[Output Throughput]] | → | Measurement contract |
| SUPPORTS | [[Tokens per GPU-Second]] | → | Measurement contract |
| SUPPORTS | [[Productive GPU Utilization]] | → | Measurement contract |
| SUPPORTS | [[Availability]] | → | Measurement contract |
| SUPPORTS | [[Model Launch Lag]] | → | Measurement contract |
| SUPPORTS | [[Cost per Outcome]] | → | Measurement contract |
| SUPPORTS | [[KPI Hierarchy]] | → |  |

## See Also

- [[Evidence Hub]]
- [[Metric Index]]
- [[KPI Hierarchy]]
- [[Empirical Map]]
