---
id: pol-regression-suite
type: policy
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [acceptance tests, regression tests, graph tests, cc-regression-suite]
related: [pol-fitness-checklist, chg-kg-test-results, chg-consistency-report]
parent: hub-wiki
source_docs: [05-wiki/Knowledge Graph Acceptance Test Results.md]
confidence: validated
last_reviewed: 2026-10-08
summary: "Regression test suite for Rack AI OpenRouter knowledge graph invariants."
---

# Regression Suite

## Purpose

Formal acceptance tests that verify the knowledge graph can reason over the Rack AI inference operating system. Run periodically and before any release. These tests validate traversal, impact analysis, simulation, and completeness — capabilities that plain document search cannot provide.

---

## Cadence

| Trigger | Tests Run |
|---------|-----------|
| Monthly (active development) | Full suite (all 7 tests) |
| New source material or benchmark incorporated | Tests R-01 through R-04 |
| Coefficient, formula, or economics change | Tests R-03, R-04 |
| Before release/milestone | Full suite + scoring |

---

## Pass Criteria

| Score | Status | Action |
|:-----:|--------|--------|
| ≥ 4.0 avg | **Pass** | Corpus is healthy |
| 3.5–4.0 avg | **Conditional pass** | Known gaps documented; schedule fixes |
| < 3.5 avg | **Fail** | Must be remediated before proceeding |

**Individual test hard stops:** Any single test below 3/5 is a blocking failure regardless of average.

---

## Test Definitions

### R-01 — Traversal: Market Demand to GPU Topology

**Prompt:** A priority model (e.g., DeepSeek V4 Flash) is seeing rising OpenRouter demand for long-context coding traffic. Walk from market demand to GPU topology. At every step, name canonical objects, formulas evaluated, workflows involved, and team ownership.

**Expected behavior:**
- Complete chain: Market Demand → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Datacenter/Topology
- Every relevant formula referenced (tokens/GPU-second, cost/1M tokens, TTFT, utilization)
- Workflows named (Model Launch Factory, Autoscaling, Routing, Admission Control)
- Ownership identified at each layer (Platform, Performance Eng, Model Enablement, Infra, SRE, FinOps)

**Pass criteria:** ≥ 4/5 — full chain traversable with explicit graph edges, no gaps requiring inference from source docs.

---

### R-02 — Reverse Traversal: Fleet Signal to Business Impact

**Prompt:** Tokens/GPU-second for a model dropped 11% overnight. Walk backwards through the ontology and identify every operational and business cause that could explain it.

**Expected behavior:**
- Reverse chain: Telemetry/GPU signal → Serving Runtime config → Model Deployment → Capacity Pool → Routing/Admission → Demand/Workload mix → Economics (cost/token, revenue/GPU-hour)
- Multiple plausible causes enumerated (batching change, cache hit-rate drop, traffic-mix shift, topology placement, quantization change, noisy neighbor)
- Formulas referenced in reverse
- Events at each layer identified

**Pass criteria:** ≥ 4/5 — reverse path explicit; at least 5 distinct causes enumerated from graph.

---

### R-03 — Impact Analysis

**Prompt:** I want to change [a coefficient / a runtime version / a quantization scheme / a capacity-pool allocation]. Show everything impacted.

**Expected behavior:**
- All consuming formulas listed
- All dependent metrics, KPIs, scorecards, dashboards
- All affected workflows (deployment, routing, autoscaling)
- All affected entities (deployments, pools)
- All affected assumptions/validations/benchmarks
- All affected commercial objects (unit economics, pricing)
- Confidence impact assessed

**Pass criteria:** ≥ 4/5 — mechanical traversal possible through explicit edges; no major dependency missed.

---

### R-04 — Evidence Chain Tracing

**Prompt:** Show me the evidence chain behind [a specific performance or cost claim, e.g., "cost/1M tokens for GLM 5.3 Flash"].

**Expected behavior:**
- Trace: Claim → Formula → Coefficient → Benchmark Run / telemetry → hardware & config
- Confidence at each node stated
- Terminal point (where evidence ends — e.g., "projected, not yet benchmarked") clearly identified
- Distinction between roadmap target and measured result made explicit

**Pass criteria:** ≥ 4/5 — chain terminates with honest confidence assessment; no roadmap target presented as a measured result.

---

### R-05 — Digital Twin Simulation

**Prompt:** Simulate a day-zero launch of a newly released model through the model factory, or a demand spike on a live model, from start to finish.

**Expected behavior:**
- Events fired in sequence (intake → hardware-fit → benchmark → canary → publish, or spike → admission control → autoscale → reallocate)
- State transitions with conditions
- Capacity/routing decisions with formula references
- Telemetry emissions
- Economic implications (cost/token, revenue/GPU-hour)
- Entity lifecycle progression (Model Deployment states)

**Pass criteria:** ≥ 3.5/5 — coherent simulation possible from wiki layer alone; timing and tooling specifics may be absent.

---

### R-06 — Graph Health & Completeness

**Prompt:** Evaluate the health of the ontology.

**Expected behavior:**
- Coverage percentage
- Orphan count
- Broken link count
- Missing lifecycles count
- Confidence distribution (how much is assumed vs. measured/validated)
- Layer integrity assessment
- Overall structural rating

**Pass criteria:** ≥ 3.5/5 — quantitative health metrics derivable from graph; known gaps explicitly documented.

---

### R-07 — Multi-Deliverable Generation

**Prompt:** From graph alone, produce N deliverables for different audiences (e.g., an exec scorecard, a performance-eng optimization brief, a FinOps unit-economics summary).

**Expected behavior:**
- Each deliverable is coherent and factually grounded in graph content
- No claims made that contradict the ontology
- Different audiences get appropriately scoped information
- Sources traceable to canonical notes and benchmark runs

**Pass criteria:** ≥ 3.5/5 — deliverables are useful and graph-grounded; may lack numeric specifics where benchmarks are pending.

---

## Baseline Scores

Baseline set on the first full run, 2026-10-08. Full evidence, traversal paths and efficiency counts are in [[Knowledge Graph Acceptance Test Results]].

| Test | Baseline Score | Minimum | Notes |
|------|:--------------:|:-------:|-------|
| R-01 | 3.5 | ≥ 4 | Entity spine fully typed; no canonical demand node; entities have no typed edges to formulas or workflows; 54% of edge types are non-canonical |
| R-02 | 3.5 | ≥ 4 | 7 causes enumerable, but the reverse walk uses untyped `related-by`; no production-telemetry anomaly event; noisy neighbour not modelled |
| R-03 | 3.5 | ≥ 4 | Formula/scorecard/commercial impact traversable; FP8 → Model Weight Footprint → GPUs per Replica → Capacity Pool branch missing; inputs and consumers not distinguished |
| R-04 | 4.0 | ≥ 4 | Chain ends honestly at `assumed` (Cost per GPU-Hour TBD, no benchmark run); no GLM benchmark/validation note; H100/H200 ID mismatch |
| R-05 | 3.5 | ≥ 3.5 | Launch Factory state machine and Model Deployment lifecycle work together; only 2 of ~7 transitions emit events; no formula links for capacity or economics |
| R-06 | 3.5 | ≥ 3.5 | 0 broken refs, 24/24 entity coverage, 10 minor orphans; 0/36 L2/L4 notes have typed edges; 35% `related` reciprocity |
| R-07 | 4.0 | ≥ 3.5 | Exec, perf-eng and FinOps deliverables coherent and traceable; no measured numbers yet; KPI Hierarchy guardrail links incomplete |
| **Average** | **3.71** | **≥ 4.0** | **Warning / Conditional pass**: R-01 to R-03 below their minimum; no hard stop |

---

## Score History

| Date | Average | Δ from Previous | Notes |
|------|:-------:|:---------------:|-------|
| 2026-09-03 | — | — | Suite defined; corpus not yet populated |
| 2026-10-08 | 3.71 | — (first scored run) | Baseline. Warning: R-01, R-02, R-03 at 3.5 (minimum 4). Top fixes: typed Relationships on formulas/metrics/coefficients/events; canonical demand node; FP8 → memory → capacity edges. See [[Knowledge Graph Acceptance Test Results]] |

---

## See Also

- [[Knowledge Graph Acceptance Test Results]] — detailed test run log (baseline 2026-10-08)
- [[CONSISTENCY_REPORT]] — output template for a consistency run
- [[FITNESS_CHECKLIST]] — structural and consistency checks
- [[CHANGE_PACKET]] — required before edits
