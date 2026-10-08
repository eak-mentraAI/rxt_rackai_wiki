---
id: met-slo-attainment
type: metric
status: draft
owner: reliability
domain: reliability
aliases: [slo attainment, slo compliance, slo hit rate, percent within slo]
related: [met-goodput, met-ttft, met-tpot, met-availability, wf-admission-control, ent-traffic-class, ent-capacity-pool, pol-benchmark-evidence-chain, hub-inference-serving]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-operations
summary: "Share of requests in a window meeting all latency thresholds for their workload profile; the B4 qualification test."
---

# SLO Attainment

## Definition

**SLO attainment** is the percentage of requests in a measurement window that met **every** latency threshold defined for their [[Traffic Class]] (e.g. [[TTFT]] p95 and [[TPOT]] p95 limits). It is not a B3 Benchmark Card field. It is the pass/fail measure of the B4 tier in the [[Benchmark Evidence Chain]]: the **SLO-qualified operating point** is the highest concurrency per replica at which attainment stays at or above its target.

Distinct from [[Availability]] (was the endpoint up?) and from [[Goodput]] (the *rate* of compliant requests). A system can be 100% available with poor attainment.

## KPI Job

Internal operating decision (qualification, admission control, autoscaling triggers) and commercial commitment (the measure any latency SLA would be written against).

## Unit

percent of requests, per profile, per window.

## Source or Formula

- Derived from: request-level TTFT/TPOT telemetry and the ratified per-profile thresholds.
- `attainment = requests meeting all thresholds / total requests` (failed requests count as misses).

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↑ | Thresholds and attainment target **not yet ratified** — see [[Open Questions]] | B4 cannot be scored until defined |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |
| [[Capacity Pool]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — metric definition only; no thresholds, no telemetry.

## See Also

- [[Operations Hub]] · [[Goodput]] · [[Availability]] · [[Admission Control]] · [[Benchmark Evidence Chain]]
