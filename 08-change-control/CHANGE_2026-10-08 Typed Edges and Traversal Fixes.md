---
id: chg-2026-10-08-typed-edges
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [typed edges and traversal fixes, regression actions 1-3, post-fix regression change]
related: [chg-kg-test-results, pol-regression-suite, chg-2026-10-08-regression-baseline, ent-market-demand]
source_docs: [05-wiki/Knowledge Graph Acceptance Test Results.md, 08-change-control/REGRESSION_SUITE.md, "python3 scripts/kg.py post-fix run 2026-10-08"]
confidence: measured
last_reviewed: 2026-10-08
parent: hub-wiki
summary: "Typed Relationships on L2/L4 notes, Market Demand node, FP8→capacity edges; regression avg 3.71→4.21."
---

# 2026-10-08 — Typed Edges and Traversal Fixes

## Trigger

The baseline [[REGRESSION_SUITE]] run ([[CHANGE_2026-10-08 Regression Suite Baseline]]) scored an average of 3.71 (Warning). R-01, R-02 and R-03 were at 3.5, below their ≥ 4 minimum. This change applies the baseline's improvement actions 1–3, raises `related` reciprocity (part of action 7), and re-runs the suite. Results are in [[Knowledge Graph Acceptance Test Results]].

## Convention Used

Every new edge is a row in a `## Relationships` table (`| Relationship | Target | Direction | Notes |`) and uses **only the 18 canonical types**.

- `→` means this note is the subject.
- `←` means the target is the subject. For example, `CONSUMES ←` on a formula means "the target consumes this formula".

`kg.py in` shows the direction of the source row, so consumers and inputs can be told apart without reading the body. The original body tables (`Inputs`, `Coefficients Used`, `Consumed By`, `Used By`, `Measures`, `Governs`, `Impacts`, `Documents This Can Change`, `Dependencies`, `Events Emitted`) are kept as written.

## What Changed

| Area | Files | Change |
|---|---|---|
| New canonical node | `01-entities/Market Demand.md` (`ent-market-demand`, `derived`) | Head of the serving chain. Holds OpenRouter pool volume and direct-tenant demand per Model × [[Traffic Class]]. `ROUTES_TO` Model / DeepSeek / GLM, `USES` Traffic Class, `FORECASTS ←` Demand Forecasting, `CONSUMES ←` Model Radar. Pool volumes are cited as a measured 2026-09-03 snapshot. RackAI share, Traffic Class split and peak multiplier stay `assumed`. A check with `kg.py find` found no existing canonical home (Traffic Class, Demand Forecasting and Model Radar each cover only one facet) |
| Formulas (6) | Tokens per GPU-Second Formula, GPU-Hours per 1M Tokens, Cost per 1M Tokens, GPUs per Replica, Gross Margin per Model, Revenue per GPU-Hour | New Relationships tables built from Inputs, Coefficients Used and Consumed By (`CONSUMES` / `DERIVES` / `MEASURES` / `DEPENDS_ON`). Where an original row was transitive (Cost per 1M listed as a direct consumer of the tokens formula), it is modelled as transitive |
| Metrics (7) | Tokens per GPU-Second, TTFT, Output Throughput, Productive GPU Utilization, Availability, Model Launch Lag, Cost per Outcome | Relationships tables built from Measures, Source, Targets and Evidence. Removed TTFT's self-reference from `related` |
| Coefficients (6) | FP8 Throughput Factor, Model Weight Footprint, KV Cache Hit Rate, Speculative Decoding Acceptance Rate, Cost per GPU-Hour, OpenRouter Price | Relationships tables built from Used By and Evidence. **FP8**: the definition now spells out the memory path (Model Weight Footprint → GPUs per Replica → Capacity Pool / Model Portfolio Capacity). The `Used By` row "Quantization program (Milestone 3.6) / —" is now [[Quantization Program]] (`wf-quantization-program`), and a [[GPUs per Replica]] row was added |
| Events (5) | New Model Detected, Deployment Canary Passed, Performance Regression Detected, Capacity Reallocation Triggered, Demand Forecast Published | Emitted By became `GENERATES ←`. Consumed By became `CONSUMES ←`. Lifecycle hooks added (Canary Passed `SUPPORTS` the Model Deployment Canary → Production transition) |
| Policies (10) | Admission Control Policy, Capacity Reservation Policy, Performance Regression Gate, Procurement Trigger, Action Controls, Governable Self-Modification, Supply Chain Inventory, FITNESS_CHECKLIST, CHANGE_PACKET, REGRESSION_SUITE | `Governs` tables and Enforcement text converted |
| Assumptions (8) | all `asm-*` | `Impacts` converted, plus `VALIDATES ←` where a validation or program is the exit criterion |
| Validations (3) | all `val-*` | `Documents This Can Change` became `VALIDATES →` |
| Evidence (6) | Erebine, Inference Serving, Sovereign & Governed, GPU Neocloud, KPI Telemetry Target List, Sovereign Private Assistant | `SUPPORTS` / `USES` / `IMPLEMENTS` edges from stated mappings. The 3 `04-evidence/benchmarks/` notes were **not edited** (concurrent session) |
| Spine workflows (11) | Model Radar, Model Launch Factory, Standard Model Deployment, Canary & Rollback, Autoscaling, Admission Control, Request Routing, GPU Reallocation, Demand Forecasting, Quantization Program, Closed-Loop Optimization | Relationships tables built from Dependencies and Events Emitted. Non-canonical originals (`FEEDS`, `HANDS_OFF_TO`, `GOVERNED_BY`) are recorded in Notes. New edges: Launch Factory hardware-fit → GPUs per Replica / Model Weight Footprint; benchmark stage `PRODUCES` TTFT / throughput / cost baselines; Closed-Loop `PRODUCES` Serving Runtime configs |
| Spine entities (7) | Model, Model Deployment, Serving Runtime, Capacity Pool, Traffic Class, DeepSeek V4 Flash, GLM 5.3 Flash | Canonical rows appended (no renames). Serving Runtime `CONSUMES` Capacity Pool and Capacity Pool `ALLOCATES` GPU Fleet close the two forward-direction spine gaps. Model Deployment gains `MEASURES ←` metric/formula rows and workflow rows. DeepSeek and GLM link to Market Demand, their scorecards, Model Launch Factory, GPUs per Replica and Model Weight Footprint (GLM also to [[First Bet — GLM 5.3 Flash]]). 35 existing non-canonical rows got a `(canonical: …)` hint in Notes; the edge names are unchanged |
| Indexes / wiki | Model Portfolio Capacity, DeepSeek V4 Flash Scorecard, GLM 5.3 Flash Scorecard, Serving Platform MOC, Entity Ontology Hub, Entity Index, Source-to-Concept Crosswalk | Relationships tables on the 3 capacity/scorecard notes. Market Demand is linked as MOC chain step 1 and listed in the hub and index. A Crosswalk row was added for its sources |
| Reciprocity | 64 notes (27 changed in `related` only: API Key, Agent Identity, Dataset, Empirical Map, GPU Cluster, GPU Fleet, GPU Node, Governed Harness, Model Catalog Endpoint, Model Deployment Specification, Nemotron 3 Ultra, OpenRouter Private Model Integration, OpenRouter Provider Integration, Organization, Packaged Solution, RackAI Control Plane, Region, Solution Marketplace, Topology, Audit, Identity & Access Control, Loop Planning & Credit Assignment, Metering, Monitoring & Observability, Self-Improvement Loop, Verification, Billing & Payment) | Rule: if A.related contains B, B is a canonical-type note, and B lacks A, then add A to B. Exclusions: A is a hub/index/change/source/broad projection; B is protected (benchmarks, accelerator entities, Benchmark Run); B is a hub-like note with more than 8 candidates where A has no typed edge to or from B (37 skipped as noise). 236 back-references added |
| Regression | `05-wiki/Knowledge Graph Acceptance Test Results.md`, `08-change-control/REGRESSION_SUITE.md` | "Run 2026-10-08 (post-fix)" section added at the top, with the baseline kept below. Score History row added |

**Totals:** typed edges went from 213 to 671. Canonical edges went from 97 (46%) to 555 (83%). The 116 legacy non-canonical edges are unchanged. `related` reciprocity went from 34% to 64%. No IDs were changed and no aliases were removed. `last_reviewed` was set to 2026-10-08 on notes whose content changed.

## Confidence

No confidence state was raised. Market Demand is new at `derived`. Its pool volumes cite a measured snapshot, and everything RackAI-specific is `assumed`. Every formula, coefficient and scorecard value is still `assumed`. No performance number was added without its source.

## Downstream Impact

- R-01 3.5 → 4.5, R-02 3.5 → 4.0, R-03 3.5 → 4.5, R-04 4.0 → 4.5, R-05 3.5 → 4.0, R-06 3.5 → 4.0, R-07 4.0 → 4.0. **Average 3.71 → 4.21 (Pass).**
- Efficiency: 99 → 58 `kg.py` calls, and 15 → 8 section reads.

## Open Items (follow-ups)

- **Edge normalization (action 6):** 116 legacy non-canonical edges on entities and 5 older workflow tables still need mapping. Spine entities now carry `(canonical: …)` hints to use as the mapping seed.
- **Out of scope because of the concurrent benchmarking session:** Relationships tables for `04-evidence/benchmarks/*` (DeepSeek H100 FP8 Benchmark, OpenRouter Leaderboard Snapshot, AgentX Benchmark Standard); reverse edges on [[Benchmark Run]], [[AMD Instinct]] and the NVIDIA accelerator entities; a GLM 5.3 Flash benchmark definition; the `bench-/val-deepseek-h200-fp8` ID open question.
- Event catalog, including a production anomaly event and noisy-neighbour / batching concepts (action 4). Reciprocity from 64% to ≥ 80%. Actions 8–10 as listed in the results note.

## Verification

- `./scripts/lint-frontmatter.sh`: pass.
- `python3 scripts/kg.py broken`: 0 unresolved references.
