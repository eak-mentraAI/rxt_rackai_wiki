---
id: met-cost-per-outcome
type: metric
status: draft
owner: rackai-product
domain: commercial
aliases: [cost per outcome, cost-per-outcome, token cost per outcome]
related: [ent-empirical-map, wf-request-routing, wf-loop-planning, fml-cost-per-1m-tokens, met-tokens-per-gpu-second, hub-operations, hub-commercial, src-rackai-dev-plan]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-operations
summary: "Metric: the cost to produce a completed outcome (not a token), attributed by workload, tenant, and result — the unit routing and FinOps reason about."
---

# Cost per Outcome

## Definition

**Cost per Outcome** measures the cost to produce a **completed outcome** — a finished task or result — rather than the cost of a token or a single request. It is the unit the [[RackAI Enterprise AI Development Plan|dev plan]]'s cost loop and economics thread (5.1) reason about, because a system's cost per run **varies by design**: one edge case can cost many times a normal run. It is read from the [[Empirical Map]]'s cost dimension and consumed by [[Request Routing]], [[Loop Planning & Credit Assignment]], and [[AI FinOps]].

> **Assumed confidence.** Program 5 thread 5.1 (build the FinOps platform; near-term research to reason about cost per outcome from the map). Distinct from the shipped-family metric [[Cost per 1M Tokens]], which measures token production cost, not outcome cost.

## Unit

Currency per completed outcome (e.g. $/outcome), attributable by workload, tenant, and result.

## Source or Formula

- Derived from: measured token cost recorded as the cost dimension of the [[Empirical Map]] (instrumented in the runtime, thread 1.3).
- Relates to: [[Cost per 1M Tokens]] (token-level) aggregated over the steps of an outcome.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↓ | Lower cost per outcome that clears the reliability bar | Reliability bar (from [[Verification]]) must still be met |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Governed Harness]] | MEASURES → cost to complete a workload |
| [[Model]] | MEASURES → per-workload outcome cost |

## Evidence

- Source: dev plan cost loop ("reason": turn metered data into cost-per-outcome and pricing); thread 5.1.
- Confidence rationale: `assumed` — no measured cost-per-outcome yet; depends on the map's `assumed` cost dimension. Downstream confidence (FinOps, pricing) may not exceed this.

## See Also

- [[Operations Hub]]
- [[Commercial & Capacity Hub]]
- [[AI FinOps]]
- [[Empirical Map]]
