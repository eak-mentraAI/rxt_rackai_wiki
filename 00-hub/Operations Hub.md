---
id: hub-operations
type: hub
status: draft
owner: platform-eng
domain: platform
aliases: [operations hub, L2 hub, digital twin hub]
related: [hub-root, hub-entities, hub-commercial]
source_docs: [openrouter_engineering_roadmap.md]
confidence: validated
last_reviewed: 2026-09-03
parent: hub-root
summary: "Layer 2 navigation hub for the serving-platform operational ontology."
---

# Operations Hub

Layer 2 — the operational ontology / digital twin. How the platform behaves at runtime: serving lifecycle, workflows, events, metrics, formulas, coefficients, and policies.

## Workflows

| Workflow | ID |
|----------|----|
| [[Model Radar]] | wf-model-radar |
| [[Model Launch Factory]] (day-zero) | wf-model-launch-factory |
| [[Standard Model Deployment]] | wf-model-deployment |
| [[Canary & Rollback]] | wf-canary-rollback |
| [[Autoscaling]] | wf-autoscaling |
| [[Admission Control]] | wf-admission-control |
| [[Request Routing]] | wf-request-routing |
| [[GPU Reallocation]] | wf-gpu-reallocation |
| [[Quantization Program]] | wf-quantization-program |
| [[Closed-Loop Optimization]] | wf-closed-loop-optimization |
| [[Demand Forecasting]] | wf-demand-forecasting |
| [[Fine-Tuning]] | wf-fine-tuning |
| [[Identity & Access Control]] | wf-identity-access |
| [[Metering]] | wf-metering |
| [[Monitoring & Observability]] | wf-monitoring |
| [[Audit]] | wf-audit |

Serving/scheduling and optimization workflows serve the whole platform; **Fine-Tuning**, **Identity & Access Control**, **Metering**, **Monitoring & Observability**, and **Audit** are the platform-operations workflows added with the RackAI-platform rescope. Metering and Audit are planned (`assumed`); platform monitoring is shipped.

## Events

| Event | ID |
|-------|----|
| [[New Model Detected]] | evt-new-model-detected |
| [[Deployment Canary Passed]] | evt-deployment-canary-passed |
| [[Performance Regression Detected]] | evt-performance-regression-detected |
| [[Capacity Reallocation Triggered]] | evt-capacity-reallocation-triggered |
| [[Demand Forecast Published]] | evt-demand-forecast-published |

## Metrics

| Metric | ID |
|--------|----|
| [[Tokens per GPU-Second]] | met-tokens-per-gpu-second |
| [[TTFT]] (P50/P95/P99) | met-ttft |
| [[Output Throughput]] | met-output-throughput |
| [[Productive GPU Utilization]] | met-gpu-utilization |
| [[Availability]] | met-availability |
| [[Model Launch Lag]] | met-model-launch-lag |

See the [[Metric Index]] for the full listing.

## Formulas

| Formula | ID |
|---------|----|
| [[Tokens per GPU-Second Formula]] | fml-tokens-per-gpu-second |
| [[GPU-Hours per 1M Tokens]] | fml-gpu-hours-per-1m-tokens |
| [[Cost per 1M Tokens]] | fml-cost-per-1m-tokens |
| [[Revenue per GPU-Hour]] | fml-revenue-per-gpu-hour |
| [[Gross Margin per Model]] | fml-gross-margin-per-model |
| [[GPUs per Replica]] | fml-gpus-per-replica |

## Coefficients

| Coefficient | ID |
|-------------|----|
| [[Cost per GPU-Hour]] | coeff-cost-per-gpu-hour |
| [[FP8 Throughput Factor]] | coeff-fp8-throughput |
| [[Speculative Decoding Acceptance Rate]] | coeff-spec-decode-acceptance |
| [[KV Cache Hit Rate]] | coeff-kv-cache-hit-rate |
| [[Model Weight Footprint]] | coeff-model-weight-footprint |
| [[GPU Type Compatibility Matrix]] | idx-gpu-compatibility-matrix |

## Policies

| Policy | ID |
|--------|----|
| [[Admission Control Policy]] | pol-admission-control |
| [[Performance Regression Gate]] | pol-performance-regression-gate |
| [[Capacity Reservation Policy]] | pol-capacity-reservation |
| [[Procurement Trigger]] | pol-procurement-trigger |

## Related Hubs

- [[Entity Ontology Hub]]
- [[Commercial & Capacity Hub]]
