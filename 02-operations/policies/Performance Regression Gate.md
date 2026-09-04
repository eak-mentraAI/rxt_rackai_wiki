---
id: pol-performance-regression-gate
type: policy
status: draft
owner: performance-eng
domain: performance
aliases: [performance regression gate, performance ci/cd gate, regression policy]
related: [wf-closed-loop-optimization, evt-performance-regression-detected, met-ttft, met-tokens-per-gpu-second, met-output-throughput, ent-model-deployment, ent-benchmark-run]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-governance
summary: "No change reaches production if it materially worsens key performance signals; performance gates CI/CD."
---

# Performance Regression Gate

## Purpose

Make performance a CI/CD gate so no runtime or configuration change silently degrades the fleet. It protects the headline engineering signals as changes flow from lab to production. (Roadmap Milestone 6.2.)

## Rule

No runtime or configuration change reaches production if it materially worsens [[TTFT]], [[Tokens per GPU-Second]], error rate, quality, or cost/token relative to the current known-good baseline. A breach emits [[Performance Regression Detected]] and blocks promotion until the regression is resolved.

## Scope

Applies to every candidate change evaluated in [[Closed-Loop Optimization]] — runtime releases, kernels, quantization, batching, parallelism, and cache settings — for all production [[Model Deployment]]s.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Closed-Loop Optimization]] | GOVERNS → |
| [[Model Deployment]] | CONSTRAINS → |

## Enforcement

Enforced as an automated gate in the promotion path (lab → canary → production), comparing candidate configs against a reference [[Benchmark Run]]. Failing candidates are returned to the lab.

## See Also

- [[Governance Hub]]
