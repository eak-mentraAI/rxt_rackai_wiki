---
id: chg-kg-test-results
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [kg test results, regression suite results, graph acceptance test log, regression baseline 2026-10-08]
related: [pol-regression-suite, pol-fitness-checklist, chg-consistency-report, idx-moc-serving-platform, idx-open-questions, idx-benchmark-library]
source_docs: [08-change-control/REGRESSION_SUITE.md, "python3 .claude/tools/kg.py run 2026-10-08"]
confidence: measured
last_reviewed: 2026-10-08
parent: pol-regression-suite
summary: "First regression suite run (R-01 to R-07): avg 3.71/5, Warning; R-01 to R-03 below the 4/5 minimum."
---

# Knowledge Graph Acceptance Test Results

## Summary

This is the first full run of the [[REGRESSION_SUITE]] (R-01 to R-07) against the RackAI wiki. It sets the baseline. Each test was run the way a fresh agent would run it. The agent started from `kg.py` (`hubs`, `find`, `show`, `out`, `in`, `type`, `stats`, `broken`) and read only the note sections that `show` pointed to. It reasoned only from the wiki layer (`00-hub` to `06-sources`), never from `reference/`.

**Average: 3.71 / 5. Verdict: Warning (suite status: Conditional pass).** No test fell below the 3/5 hard stop. However, R-01, R-02 and R-03 scored 3.5, below the ≥ 4/5 minimum that [[FITNESS_CHECKLIST]] Section 3 sets for them. These must be fixed before the next release.

The graph is strong at the **entity layer**: 39 entities, all with typed Relationships tables, and 24/24 canonical Layer-1 objects present. It is honest about evidence: nothing is presented as measured. It is weak at the **operational layer**. None of the 36 formula, metric, coefficient, event, policy, assumption, validation and evidence notes has a typed Relationships table. Their dependencies sit in untyped `related` lists or in body tables (`Inputs`, `Consumed By`, `Used By`, `Measures`) that `kg.py` does not parse. Impact and reverse analysis therefore need section reads and judgement, and cannot be done by following edges mechanically.

---

## Run Details

| Item | Value |
|---|---|
| Run date | 2026-10-08 |
| Corpus | 244 notes (240 with frontmatter); 199 wiki-layer notes |
| Tool | `python3 .claude/tools/kg.py` (stdlib) + targeted section reads |
| Grader | Strict. The test definitions and pass criteria in [[REGRESSION_SUITE]] are applied as written. Having the tool is not a pass. |
| Scale | 0–5 per test, half points allowed |
| Efficiency measure | Number of `kg.py` calls plus the number of section reads or greps needed to answer the prompt |

## Method

1. Every test prompt was run exactly as written in [[REGRESSION_SUITE]]. Where the prompt lets the tester choose, these choices were made: R-01 used DeepSeek V4 Flash with long-context coding demand. R-03 changed the quantization coefficient ([[FP8 Throughput Factor]]). R-04 traced "cost/1M tokens for GLM 5.3 Flash". R-05 simulated a day-zero launch.
2. Traversal began at the navigation entry points (`kg.py hubs`, `find`). It followed typed edges (`out`/`in`) first, then `related` IDs, then wikilinks. A section was read only when `show` showed that it held needed content.
3. Each step was graded on whether it was **explicit in the graph** (a typed edge or a `related` ID) or **needed inference** (body prose, or a guess from naming).
4. R-06 health metrics came from `kg.py stats` and `broken`, plus a read-only scratch script that loads notes with `kg.py`'s own `load()` to count orphans, reciprocity, Relationships tables and lifecycles. `kg.py` has no `orphans` or `health` command.

---

## Scorecard

| Test | Name | Minimum | Score | Status | kg.py calls | Section reads / greps |
|------|------|:-------:|:-----:|:------:|:-----------:|:---------------------:|
| R-01 | Traversal: market demand → GPU topology | ≥ 4 | **3.5** | Below minimum | 31 | 2 |
| R-02 | Reverse traversal: fleet signal → business impact | ≥ 4 | **3.5** | Below minimum | 10 | 3 |
| R-03 | Impact analysis (FP8 / quantization coefficient) | ≥ 4 | **3.5** | Below minimum | 11 | 1 |
| R-04 | Evidence chain (cost/1M tokens, GLM 5.3 Flash) | ≥ 4 | **4.0** | Pass | 9 | 3 |
| R-05 | Digital twin (day-zero launch) | ≥ 3.5 | **3.5** | Pass (at floor) | 7 | 2 |
| R-06 | Graph health and completeness | ≥ 3.5 | **3.5** | Pass (at floor) | 27 | 1 script |
| R-07 | Multi-deliverable generation | ≥ 3.5 | **4.0** | Pass | 4 | 3 |
| | **Average** | ≥ 4.0 | **3.71** | **Warning** | **99** | **15** |

---

## R-01 — Traversal: Market Demand to GPU Topology — 3.5 / 5

**Prompt run:** DeepSeek V4 Flash sees rising OpenRouter demand for long-context coding traffic. Walk from demand to GPU topology.

**Path traversed:**

| Step | Node (ID) | Edge used | Owner | Explicit? |
|---|---|---|---|---|
| Demand | no canonical "Market Demand" node. Nearest: [[Traffic Class]] (`ent-traffic-class`, has "Long-context" and "Coding" classes), [[Demand Forecasting]] (`wf-demand-forecasting`), [[OpenRouter Provider Integration]] | `find "market demand"` returns only the MOC | performance-eng / finops | **No.** Demand is spread across 3 notes |
| Demand → Model | `ent-traffic-class` → [[Model]] | `CHARACTERIZES` (typed) | — | Yes |
| Model instance | [[DeepSeek V4 Flash]] (`ent-deepseek-v4-flash`) | `INSTANCE_OF Model` | model-enablement | Yes |
| Model → Deployment | [[Model Deployment]] (`ent-model-deployment`) | `SERVED_BY` / `SERVES` | platform-eng | Yes, both directions |
| Deployment → Runtime | [[Serving Runtime]] (`ent-serving-runtime`) | `RUNS_ON` / `RUNS` | performance-eng | Yes |
| Runtime → Capacity Pool | [[Capacity Pool]] (`ent-capacity-pool`) | wikilink only. Deployment `DRAWS_FROM` Pool skips over the runtime | finops | **Partial** |
| Pool → Fleet | [[GPU Fleet]] (`ent-gpu-fleet`), [[GPU Node]], [[GPU Cluster]] | Pool `ALLOCATES GPU Node`, `SPANS GPU Cluster`. Fleet `← ALLOCATED_BY Pool`, but the Pool has no outbound edge to the Fleet | infrastructure | Mostly |
| Fleet → Topology / DC | [[Topology]] (`ent-topology`), [[Region]] (`ent-region`) | Node `CONSTRAINED_BY Topology`, `BELONGS_TO Region` | infrastructure | Yes |
| Formulas | [[Tokens per GPU-Second Formula]], [[Cost per 1M Tokens]], [[TTFT]] (metric), [[Productive GPU Utilization]] (metric) | reached only through workflow `related` lists and `type formula`. No entity in the chain has a typed edge to a formula | performance-eng / finops | **Weak** |
| Workflows | [[Model Launch Factory]], [[Autoscaling]], [[Request Routing]], [[Admission Control]] | found with `type workflow` and MOC wikilinks. None has a typed Relationships table | model-enablement / infrastructure / platform-eng / reliability | Untyped |

**What worked:** The entity spine from Model to Deployment, Runtime, Pool, Node/Cluster, Topology and Region is fully typed and mostly bidirectional. [[Serving Platform MOC]] lists every spine node. Every node has an owner.

**Gaps:**
- There is no canonical **Market Demand / OpenRouter demand signal** node. The first hop ("demand is rising for model X in traffic class Y") cannot be traversed. It has to be assembled from Traffic Class, Demand Forecasting and the OpenRouter integration.
- [[DeepSeek V4 Flash]] has **no edges to any workflow, formula, scorecard or demand note**. Its only operational backlinks come from the scorecard and from evidence notes.
- Serving Runtime → Capacity Pool and Capacity Pool → GPU Fleet are not typed in the forward direction.
- Entities have no typed edges to formulas or workflows (for example, Model Deployment `MEASURED_BY` Tokens per GPU-Second). Formulas are linked only from the operational side, through untyped `related` IDs.
- **Edge vocabulary drift.** 54% of typed edges (116/213) use types outside the 18 canonical relationship types: `SERVED_BY`, `INSTANCE_OF`, `ASSIGNED_TO`, `VALIDATED_BY`, `RUNS_ON`, `INCLUDES_TYPE`, and others.
- `kg.py show` does not print `owner`. The ownership question needed a separate grep over 29 files.

**Efficiency:** 31 `kg.py` calls (1 `hubs`, 6 `find`, 18 `out`, 5 `type`, 1 `show`) plus 2 greps (owners; long-context coverage). A well-informed agent could do it in about 15. The demand hop and the formula/workflow layer are what drive the count up.

---

## R-02 — Reverse Traversal: Fleet Signal to Business Impact — 3.5 / 5

**Prompt run:** Tokens/GPU-second for a model dropped 11% overnight. Walk backwards and enumerate the causes.

**Path traversed:** [[Tokens per GPU-Second]] (`met-tokens-per-gpu-second`) `in`: 17 `related-by` and 14 backlinks. From there to [[Tokens per GPU-Second Formula]], then the coefficients ([[FP8 Throughput Factor]], [[KV Cache Hit Rate]], [[Speculative Decoding Acceptance Rate]]), then [[Closed-Loop Optimization]] and [[Performance Regression Detected]] (`evt-performance-regression-detected`) and [[Performance Regression Gate]]. Downstream to economics: [[GPU-Hours per 1M Tokens]], [[Cost per 1M Tokens]], [[Revenue per GPU-Hour]], [[Gross Margin per Model]], and [[Model Scorecard]] rows.

**Causes enumerable from the graph (7):**

1. Serving-runtime config change, including batching. Batching is an attribute of [[Serving Runtime]] in body text only. Path: [[Closed-Loop Optimization]], then [[Performance Regression Detected]].
2. Quantization or precision change ([[FP8 Throughput Factor]], [[Quantization Program]]).
3. KV/prefix cache hit-rate drop ([[KV Cache Hit Rate]]).
4. Speculative-decoding acceptance compressing under saturation ([[Speculative Decoding Acceptance Rate]]).
5. Traffic-mix shift ([[Traffic Class]] `CONSTRAINS` Model Deployment).
6. Topology placement ([[Topology]] `CONSTRAINS` Model Deployment, `INFORMS` Serving Runtime).
7. Utilization or scaling change ([[Autoscaling]], [[GPU Reallocation]], [[Productive GPU Utilization]]).

**Gaps:**
- The metric's `## Measures` table (`MEASURES → Model Deployment`) is not a `## Relationships` table, so `kg.py out` shows no typed edge. Reverse direction comes only from `related-by`, which is undirected and does not say whether a note is a cause or a consumer.
- There is **no production-telemetry anomaly event**. [[Performance Regression Detected]] is emitted only by the lab promotion gate in Closed-Loop Optimization, not by a live-fleet signal. The demand and routing layers have only 2 events ([[Demand Forecast Published]], [[Capacity Reallocation Triggered]]). The prompt asks for "events at each layer", and those events do not exist.
- Noisy neighbour / multi-tenant contention does not appear in the operational layer. `find "noisy neighbor"` and `find batching` both return nothing.
- No telemetry exists for the metric (`confidence: assumed`, "no measured baseline yet"). The reverse walk is structural only.

**Efficiency:** 10 `kg.py` calls plus 3 section reads or greps. The 31-entry `in` listing was the main cost: each cause had to be picked out by hand from an untyped list.

---

## R-03 — Impact Analysis: change the FP8 / quantization coefficient — 3.5 / 5

**Prompt run:** Change the quantization scheme. In the graph this is the [[FP8 Throughput Factor]] (`coeff-fp8-throughput`). Show everything impacted.

**Path traversed and impact set:**

| Category | Impacted (found) | How found |
|---|---|---|
| Formulas | [[Tokens per GPU-Second Formula]] (direct). Transitively [[GPU-Hours per 1M Tokens]], [[Cost per 1M Tokens]], [[Revenue per GPU-Hour]], [[Gross Margin per Model]] | coefficient `Used By` section, then `in` on each formula |
| Metrics / KPIs | [[Tokens per GPU-Second]] (headline KPI), [[Output Throughput]], Cost/1M and Revenue/GPU-hour guardrails in [[KPI Hierarchy]] | `related`, backlinks |
| Scorecards | [[DeepSeek V4 Flash Scorecard]], [[GLM 5.3 Flash Scorecard]], [[Nemotron 3 Ultra Scorecard]], [[Model Scorecard]] | backlinks to Cost per 1M Tokens |
| Workflows | [[Quantization Program]], [[Request Routing]] (uses cost/1M), [[GPU Reallocation]] (uses gross margin) | `related-by` |
| Entities | [[Serving Runtime]], [[Benchmark Run]], [[Model Deployment]] | coefficient `related` |
| Evidence | [[FP8 Quality Neutral]] (assumption), [[Validate DeepSeek H100 FP8]], [[DeepSeek H100 FP8 Benchmark]], [[GPU Type Compatibility Matrix]] | backlinks |
| Commercial | [[Unit Economics Model]], [[OpenRouter Price]], [[AI FinOps]] | `related-by` on formulas |
| Confidence | Coefficient is `assumed`, so every downstream formula and scorecard row stays `assumed`. No upgrade path until the DeepSeek FP8 benchmark runs | `show` |

**Gaps (missed or non-mechanical dependencies):**
- **Memory path is missing.** The coefficient's own summary says FP8 changes *memory* as well as throughput. But it has no link to [[Model Weight Footprint]] or [[GPUs per Replica]], so the effect on replica size, then [[Capacity Pool]] sizing, then [[Model Portfolio Capacity]], cannot be found by traversal. This is a major dependency.
- The coefficient's `Used By` table lists "Quantization program (Milestone 3.6)" as plain text with ID "—", although [[Quantization Program]] exists.
- Formula `Inputs`, `Coefficients Used` and `Consumed By` tables are not parsed as edges. `related-by` mixes inputs and consumers. For example, Cost per 1M Tokens is "related-by" Tokens per GPU-Second Formula, which is an upstream input, not an impacted consumer. The tester has to read each formula to tell direction.
- No concrete Model Deployment or Capacity Pool instances exist, so "affected deployments/pools" can only be answered at class level.

**Efficiency:** 11 `kg.py` calls plus 1 section read. Fast, but the result over-includes (upstream mixed with downstream) and misses the memory/capacity branch.

---

## R-04 — Evidence Chain: "cost/1M tokens for GLM 5.3 Flash" — 4.0 / 5

**Path traversed:**

| Node | Confidence | Note |
|---|:---:|---|
| Claim: [[GLM 5.3 Flash Scorecard]] row "Cost per 1M Tokens" (`idx-scorecard-glm`) | assumed | "no run yet". Notes state all rows are assumed until a Benchmark Run is cited |
| Formula: [[Cost per 1M Tokens]] (`fml-cost-per-1m-tokens`) | assumed | Worked example labelled "assumed / illustrative" and "NOT a measured value" |
| Formula input: [[GPU-Hours per 1M Tokens]], from [[Tokens per GPU-Second Formula]] | assumed | |
| Coefficients: [[Cost per GPU-Hour]] (`coeff-cost-per-gpu-hour`) | assumed | Value "TBD". Exit criterion: Milestone 0.3 cost model |
| Coefficients: [[FP8 Throughput Factor]], [[KV Cache Hit Rate]], [[Speculative Decoding Acceptance Rate]] | assumed | |
| Benchmark Run / telemetry | **none** | [[Benchmark Library]]: "no measured results exist yet". No GLM benchmark definition exists; the only one is [[DeepSeek H100 FP8 Benchmark]] |
| Hardware / config | [[GLM 5.3 Flash]] → Serving Runtime, Capacity Pool; [[First Bet — GLM 5.3 Flash]] (NVL-PCIe topology fit); [[Inference Optimization]] "TTFT (H100, GLM 5.3 Flash): Not Started" | |

**Terminal point:** "Projected, not yet benchmarked". The chain ends honestly at an `assumed` placeholder. No roadmap target is presented as a measured result. This meets C-09.

**Gaps:**
- There is no planned Benchmark Run or Validation note for GLM 5.3 Flash, although it is the chosen first bet. DeepSeek has both.
- The [[GLM 5.3 Flash]] entity does not link to its scorecard or to [[First Bet — GLM 5.3 Flash]]. Hardware context comes from backlinks and a hub table.
- **ID/title mismatch:** `bench-deepseek-h200-fp8` and `val-deepseek-h200-fp8` are titled and described as **H100**. IDs are stable (S-14), so this needs an alias and an open question, not a rename.

**Efficiency:** 9 `kg.py` calls plus 3 section reads.

---

## R-05 — Digital Twin: Day-Zero Launch — 3.5 / 5

**Path traversed:** [[Model Radar]] (`wf-model-radar`) emits [[New Model Detected]]. Then [[Model Launch Factory]] (`wf-model-launch-factory`) runs its `State Machine` and `Steps`: Radar → Intake → Functional Validation → Hardware Fit → Benchmark → Canary → Publication, with a Blocked exit. It hands off to [[Canary & Rollback]], which emits [[Deployment Canary Passed]], and then to [[OpenRouter Provider Integration]] for publication. In parallel, [[Model Deployment]] `Lifecycle States` runs Provisioning → Internal → Canary → Production → Draining → Retired. [[Standard Model Deployment]] provides the deploy path.

**Simulation result:** A coherent end-to-end walkthrough is possible from the wiki alone. It has state transitions with conditions, an owner per step, milestones 4.1–4.8, and a launch-lag target of <24h median / <72h P90, correctly marked as an assumed roadmap target.

**Gaps:**
- **Events:** only 2 of about 7 transitions emit a defined event. Intake complete, hardware-fit decided, benchmark completed, published and rollback have no event notes.
- **Capacity decision has no formula link.** The hardware-fit step describes minimum GPU count and topology, but the launch factory does not link [[GPUs per Replica]] or [[Model Weight Footprint]]. Capacity Pool allocation for the new model is implicit.
- **Economics:** cost/1M tokens appears as prose in the Benchmark step. There is no edge to [[Cost per 1M Tokens]] or [[Revenue per GPU-Hour]].
- **Telemetry emissions:** none are defined per stage.
- The Model Deployment lifecycle and the launch-factory state machine are not cross-referenced (which factory state creates the Provisioning deployment).

**Efficiency:** 7 `kg.py` calls plus 2 section reads. This was the most efficient test, because the launch factory note is well sectioned.

---

## R-06 — Graph Health and Completeness — 3.5 / 5

| Metric | Value | Assessment |
|---|---|---|
| Notes / with frontmatter | 244 / 240. The 4 without are `CLAUDE.md` and `reference/` files, which are excluded by design | Pass |
| Broken refs (`kg.py broken`) | **0** | Pass |
| Canonical Layer-1 coverage | **24/24** entity types from the operating standards exist (plus GPU Fleet and model and hardware instances) | Pass |
| Orphans (no inbound, wiki layer) | **10**: 5 folder READMEs and 5 changelogs in `05-wiki/changelogs/` | Minor |
| Dead ends (no outbound) | 0 | Pass |
| Entities with Relationships table | 39/39 | Pass (S-08) |
| Entities with lifecycle states | 30/39. Missing: NVIDIA A30, H100, L40S, AMD Instinct, Across.AI, Empirical Map, Model Catalog Endpoint, Agent Identity, Billing & Payment | 9 missing |
| Workflows with State Machine | 16/21 | 5 missing |
| L2/L4 notes with typed Relationships tables | **0/36** formulas, metrics, coefficients, events, policies, assumptions, validations, evidence; 5/21 workflows | **Major gap** |
| `related` reciprocity (bidirectional completeness, standard #5) | **35%** (485/1403 pairs) | Weak |
| Typed edges on canonical vocabulary | 46% (97/213); 74 distinct edge types | Weak (standard #3) |
| Notes without `source_docs` (excluding `source` type) | 10: [[OpenRouter Leaderboard Snapshot]] (evidence), [[Wiki Hub]], [[Source Inventory]], [[Source-to-Concept Crosswalk]], 1 changelog and 5 READMEs | Minor (S-06) |
| Missing owner | 0 | Pass |
| Confidence distribution | assumed 80, validated 73, derived 48, measured 28 (corpus-wide) | See below |
| Events | 5 in total | Thin for a digital twin |

**Confidence observation (C-06 / C-09 risk):** [[Benchmark Library]] states that no measured results exist. Yet 13 entities and 5 source notes are `measured`, and 19 operational notes are `validated`. Example: [[Performance Regression Detected]] is `validated`, and the [[Traffic Class]] attribute profiles are `measured`. Most of these probably mean "the definition is confirmed by a shipped spec" rather than "the value is measured". But the standard does not tell definition confidence apart from value confidence, so a reader cannot check C-06 mechanically. This is recorded as an open question, not as a defect.

**Gaps documented elsewhere:** [[Open Questions]], [[Capability Gap Register]], [[Assumption Register]] and [[Validation Register]] all exist and are linked from the hubs.

**Tooling gaps:** `kg.py stats` gives counts by type, domain and confidence only. Orphans, reciprocity, lifecycle coverage and Relationships-table coverage needed a custom script. Without one, a fresh agent would need about 200 `in` calls for orphan detection alone.

**Efficiency:** 2 `kg.py` calls (`stats`, `broken`), 25 `show` calls for entity coverage, and 1 scratch script.

---

## R-07 — Multi-Deliverable Generation — 4.0 / 5

Three deliverables were drafted from graph content alone, starting from [[KPI Hierarchy]], [[Inference Optimization]] and [[Unit Economics Model]].

1. **Exec scorecard.** Four headline KPIs from [[KPI Hierarchy]]: [[Productive GPU Utilization]], [[Tokens per GPU-Second]], [[TTFT]], [[Model Launch Lag]]. All are `assumed` with "no run yet" on all three model scorecards. Guardrails: [[Availability]] >99.9%, Cost/1M ↓, Revenue/GPU-hour ↑. Message: the first bet is GLM 5.3 Flash because of topology fit ([[DeepSeek-First vs GLM-First Sequencing]]), and no KPI has a measured baseline yet.
2. **Performance-engineering optimization brief.** Levers: FP8 ([[FP8 Throughput Factor]]), KV cache ([[KV Cache Hit Rate]]), speculative decoding ([[Speculative Decoding Acceptance Rate]]; Refrag in progress), and the AMD AIM engine (in progress). Gate: [[Performance Regression Gate]] via [[Closed-Loop Optimization]]. Gap: benchmark harness "Not Started". The current state and gaps come directly from the [[Inference Optimization]] "Current State vs. Target" table.
3. **FinOps unit-economics summary.** Economic loop and formula chain: [[Tokens per GPU-Second Formula]] → [[GPU-Hours per 1M Tokens]] → [[Cost per 1M Tokens]] (with [[Cost per GPU-Hour]] = TBD) → [[Gross Margin per Model]] with [[OpenRouter Price]]. Commercial objects reference Models and Pools, never GPUs (invariant holds). Blocker: the Milestone 0.3 cost model.

**Assessment:** All three are coherent, scoped to their audience, traceable to canonical notes, and do not contradict the ontology.

**Gaps:**
- There are no numbers anywhere, which the criterion allows while benchmarks are pending.
- In the [[KPI Hierarchy]] guardrails table, "Gross margin / model" shows "—" although [[Gross Margin per Model]] exists.
- Error rate, queueing delay and capability coverage are guardrails with no canonical metric note.

**Efficiency:** 4 `kg.py` calls plus 3 section reads. This was the most efficient test, because the hubs and indexes already act as projections.

---

## Verdict

| Threshold ([[FITNESS_CHECKLIST]]) | Result |
|---|---|
| Stable (5/5) | No |
| Acceptable (4/5) | No |
| **Warning (3.5–4/5)** | **Yes: average 3.71.** Must be addressed before the next release |
| Hard stop (< 3.5 avg, or any test < 3/5) | No. The lowest test score is 3.5 |

Suite status ([[REGRESSION_SUITE]] Pass Criteria): **Conditional pass**. R-01, R-02 and R-03 are each below their individual ≥ 4/5 minimum (FITNESS_CHECKLIST Section 3). R-05 and R-06 are exactly at their 3.5 floor.

**What the graph does well:** a typed, bidirectional entity spine; complete Layer-1 coverage; zero broken references; honest confidence (no target presented as a measurement); well-sectioned workflow notes with state machines; hubs that work as ready-made projections.

**What holds it back:** the operational layer (formulas, metrics, coefficients, events) is connected by untyped `related` lists, so impact and reverse traversal are not mechanical. There is no demand node at the head of the spine. Few events are defined. Edge-type vocabulary has drifted.

---

## Prioritized Improvement Actions

These are recorded, not applied. Each action names the tests it should raise.

| # | Action | Notes / edges to add | Raises |
|---|---|---|---|
| 1 | **Add typed Relationships tables to all formula, metric, coefficient and event notes.** Convert the existing `Inputs`, `Coefficients Used`, `Consumed By`, `Used By` and `Measures` tables into a `## Relationships` table (`CONSUMES` / `PRODUCES` / `MEASURES` / `DERIVES`) so `kg.py out`/`in` shows direction. | 6 `fml-*`, 7 `met-*`, 6 `coeff-*`, 5 `evt-*` | R-02, R-03, R-01 |
| 2 | **Create a canonical demand node** (for example `ent-market-demand` or a "Model Demand Signal" metric fed by OpenRouter token share per Traffic Class). Link it with `FORECASTS` / `GENERATES` to [[Traffic Class]], [[Model]], [[Demand Forecasting]] and [[Model Radar]]. Add operational edges from [[DeepSeek V4 Flash]] and [[GLM 5.3 Flash]] to their scorecards and workflows. | new entity or metric; edits to 2 model instances | R-01, R-02 |
| 3 | **Link FP8 / quantization to memory and capacity.** Add edges from [[FP8 Throughput Factor]] to [[Model Weight Footprint]] and [[GPUs per Replica]]. Replace the plain-text "Quantization program" row with [[Quantization Program]]. Link [[GPUs per Replica]] to [[Capacity Pool]] / [[Model Portfolio Capacity]]. | 3–4 notes | R-03, R-05 |
| 4 | **Fill out the event catalog.** Add events for Model Intake Completed, Hardware Fit Decided, Benchmark Run Completed, Model Published, Deployment Rolled Back, and a **production** throughput/latency anomaly event (separate from the lab regression gate). Link each to its workflow state and to the [[Model Deployment]] lifecycle. | about 6 `evt-*` notes | R-02, R-05 |
| 5 | **Add a GLM 5.3 Flash benchmark definition and validation item** (H100, matching the DeepSeek pair). Link [[GLM 5.3 Flash]] to its scorecard and to [[First Bet — GLM 5.3 Flash]]. Add `h100` aliases and an open question for the `bench-/val-deepseek-h200-fp8` ID/title mismatch. | 2 new evidence notes; alias edits | R-04, R-07 |
| 6 | **Normalize the edge vocabulary.** Map the 74 edge types onto the 18 canonical types, or formally extend the canonical list (for example, accept `RUNS_ON`, `INSTANCE_OF` and `*_BY` inverses as documented aliases). | `.kiro/steering` relationship list plus 39 entity tables | R-01, R-06 |
| 7 | **Raise `related` reciprocity** from 35% toward ≥ 80% (standard #5), starting with the spine, formulas and workflows. | bulk frontmatter pass | R-02, R-03, R-06 |
| 8 | **Separate definition confidence from value confidence** (C-06). Review the 13 `measured` entities and the `validated` operational notes against [[Benchmark Library]]. | entity attribute tables | R-04, R-06 |
| 9 | **Close small completeness gaps:** lifecycles for the 9 entities without them, state machines for the 5 workflows without them, `source_docs` for [[OpenRouter Leaderboard Snapshot]], links from the hub or changelog index to the 5 orphan changelogs, and the "Gross margin / model" link plus canonical metric notes for error rate, queueing delay and capability coverage in [[KPI Hierarchy]]. | various | R-06, R-07 |
| 10 | **Tooling (outside this repo's content scope):** make `kg.py show` print `owner`; add `orphans` / `health` commands; parse `Inputs`/`Consumed By`/`Measures` tables as edges; split `in` into typed-edge and untyped sections. This would roughly halve the R-01 and R-06 call counts. | `.claude/tools/kg.py` | efficiency, all tests |

Re-run R-01 to R-03 after actions 1–3. Re-run the full suite before the next release.

---

## See Also

- [[REGRESSION_SUITE]] — test definitions, baseline and score history
- [[FITNESS_CHECKLIST]] — Section 3 minimums and thresholds
- [[CONSISTENCY_REPORT]] — consistency-run template
- [[Serving Platform MOC]] — the spine traversed in R-01
- [[Open Questions]] — where the confidence-semantics and H100/H200 ID questions belong
- [[CHANGE_2026-10-08 Regression Suite Baseline]] — change record for this run
