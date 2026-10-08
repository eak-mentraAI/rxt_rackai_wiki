---
id: met-goodput
type: metric
status: draft
owner: performance-eng
domain: performance
aliases: [goodput, slo-compliant throughput, effective throughput, useful throughput]
related: [met-output-throughput, met-ttft, met-tpot, met-slo-attainment, met-tokens-per-gpu-second, ent-traffic-class, pol-benchmark-evidence-chain, hub-inference-optimization]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "https://mlcommons.org/benchmarks/inference-datacenter/"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-operations
summary: "Throughput counting only requests that met every SLO threshold for their profile — the honest capacity number."
---

# Goodput

## Definition

**Goodput** is the rate of requests (or output tokens) completed **while meeting every latency threshold** for their [[Traffic Class]] — [[TTFT]] and [[TPOT]] at the profile's percentile targets. Raw [[Output Throughput]] counts every token; goodput counts only tokens a customer would accept. Past saturation, throughput keeps rising while goodput falls — which is why the [[Benchmark Evidence Chain]] reports both and computes economics at the goodput-qualified point, not peak throughput.

**Provisional vs. qualified.** At B3, goodput is *provisional*: it must name the thresholds used, which are not yet ratified. *Qualified* goodput exists only in a B4 Service Qualification Record against ratified per-profile thresholds.

Relation to [[SLO Attainment]]: over a window, goodput ≈ request rate × attainment. Attainment is the *ratio*; goodput is the *rate*.

## KPI Job

Internal operating decision (sizing, SLO-qualified operating point) and commercial input (capacity per GPU that can actually be sold).

## Unit

requests/second (primary) or output tokens/second, within thresholds; per deployment or per GPU.

## Source or Formula

- Derived from: request-level TTFT/TPOT telemetry filtered by the profile's thresholds.
- `goodput = count(requests meeting all thresholds) / window`

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | None — undefined until per-profile thresholds are ratified | Never reported without the thresholds used |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |
| [[Capacity Pool]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — concept from serving-systems practice and MLPerf's latency-constrained throughput; depends on SLO thresholds that do not yet exist.

## See Also

- [[Operations Hub]] · [[SLO Attainment]] · [[Output Throughput]] · [[Benchmark Evidence Chain]]
