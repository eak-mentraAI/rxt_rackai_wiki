---
id: met-tpot
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [tpot, time per output token, itl, inter-token latency, decode latency, token latency]
related: [met-ttft, met-output-throughput, met-goodput, met-slo-attainment, ent-traffic-class, ent-benchmark-run, pol-benchmark-evidence-chain, hub-inference-optimization]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "https://docs.vllm.ai/en/latest/", "https://mlcommons.org/benchmarks/inference-datacenter/"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-operations
summary: "Time per output token after the first (TPOT) and its per-gap distribution (ITL): streaming smoothness."
---

# TPOT

## Definition

**Time per output token** — the decode-phase latency a user experiences once streaming has started. This is the canonical note for both reporting forms:

- **TPOT** (per request): `(end-to-end latency − TTFT) / (output tokens − 1)`. One value per request.
- **ITL — inter-token latency** (per gap): the time between consecutive streamed tokens. A distribution over every gap; exposes stalls that a per-request mean hides.

TPOT is measured separately from [[TTFT]] because prefill and decode are bound by different resources (compute vs. memory bandwidth) and are optimized differently. Together they describe interactive experience; neither alone does.

## KPI Job

Internal operating decision (regression gate, profile tuning) and customer-facing experience (streaming smoothness). Candidate SLA input once per-profile thresholds are ratified — see [[SLO Attainment]].

## Unit

milliseconds per token; reported as p50 / p95 / p99 (TPOT over requests, ITL over gaps).

## Source or Formula

- Measured from: request-level serving telemetry (token emission timestamps) or the benchmark harness (vLLM serving benchmark, AIPerf).
- TPOT formula as above; ITL is measured directly.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↓ | No ratified threshold per [[Traffic Class]] yet (see [[Open Questions]]) | Reported at every concurrency rung on a Benchmark Card ([[Benchmark Evidence Chain]]) |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |
| [[Serving Runtime]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — definition adopted from common serving-benchmark practice (vLLM, MLPerf Inference); no RackAI measurement exists. Not in the [[KPI Telemetry Target List]] yet; vLLM exposes per-token latency natively (to validate as a scraped signal).

## See Also

- [[Operations Hub]] · [[TTFT]] · [[Goodput]] · [[Benchmark Evidence Chain]]
