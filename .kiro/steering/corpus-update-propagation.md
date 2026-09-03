---
inclusion: auto
---

# Corpus Update Propagation Skill

## When This Applies

This skill MUST be used whenever:
- New information, corrections, or source updates are introduced into the repository
- The user asks to update documentation, revise the corpus, incorporate new findings, or reconcile new source material
- A validation item is resolved, a benchmark result arrives, a coefficient value changes, or a competitive datapoint is captured
- Any source document is added or modified that affects canonical concepts

## Required Behavior

### Step 1 — Identify Affected Concepts

Before editing anything:
1. Identify the canonical concept(s) affected by the new information
2. Locate their canonical home in the appropriate layer folder (01-entities/, 02-operations/, 03-commercial/, 04-evidence/)
3. Determine the change type: new object | object modification | relationship change | evidence update | validation update | deprecation

### Step 2 — Impact Scan

Map all downstream objects that may be impacted:
- Entities (01-entities/): models, deployments, runtimes, GPU fleet, capacity pools
- Workflows, events, metrics, formulas, coefficients, policies (02-operations/)
- Commercial objects (03-commercial/): unit economics, pricing, allocation, forecasting
- Assumptions, validations, benchmarks (04-evidence/)
- Hub pages, indexes, glossary, scorecards (00-hub/, 05-wiki/)
- Source inventory, crosswalk (06-sources/)

Use the typed relationship edges (SERVES, USES, ALLOCATES, ROUTES_TO, PRODUCES, MEASURES, etc.) on entity pages to trace dependencies. Use the "Used By" fields on coefficients and "Dependencies" sections on workflows.

### Step 3 — Update in Layer Order

Propagate changes through layers in this sequence:

```
1. Source note / provenance (06-sources/)
2. Canonical entity or operational note (01-entities/ or 02-operations/)
3. Dependent operational notes (formulas, workflows, metrics, coefficients)
4. Evidence layer (benchmarks, assumptions, validations, confidence states)
5. Commercial layer (if unit economics, pricing, or allocation affected)
6. Hub pages, indexes, and model scorecards (00-hub/, 05-wiki/indexes/)
7. Crosswalk and source inventory (06-sources/)
8. Changelog entry (05-wiki/changelogs/)
```

### Step 4 — Preserve Identity

During all edits:
- Never change canonical IDs (ent-xxx, wf-xxx, fml-xxx, coeff-xxx, met-xxx, etc.)
- Preserve aliases — move deprecated terms to aliases, don't delete them
- Maintain source traceability in `source_docs` frontmatter
- Keep confidence states honest — never upgrade confidence without evidence. A projected number stays `assumed` until a benchmark run or telemetry supports it.

### Step 5 — Consistency Pass

After edits, verify:
- Terminology is consistent across all affected notes
- No definitions contradict each other
- Commercial, operational, and capacity layers still agree
- No dependency was missed
- No open question is being treated as resolved
- Confidence propagation rule holds (downstream ≤ weakest upstream)
- No performance number appears without a benchmark or telemetry source

### Step 6 — Surface Uncertainty

- If the new information creates ambiguity, record it as an open question in 04-evidence/open-questions/
- If sources disagree (e.g., roadmap target vs. measured benchmark), create a contradiction entry — never smooth it over
- If confidence cannot be determined, use `assumed` and document exit criteria

### Step 7 — Change Summary

Produce a concise summary listing:
- Objects changed / added
- Edges added or removed
- Documents impacted
- Assumptions / validations / benchmarks impacted
- Open questions created
- Confidence states changed

## Execution Rules

1. **Never make a silent update** that changes meaning without surfacing the propagation impact.
2. **Always update the canonical source-of-truth note first** before updating dependent notes.
3. **Always check the Coefficient Catalog and Formula Library** when capacity, cost, or performance concepts change — formulas have explicit dependency chains (e.g., tokens/GPU-second → cost/1M tokens → revenue/GPU-hour → gross margin).
4. **Always check the Assumption Register** when confidence or evidence changes.
5. **Always update the Source-to-Concept Crosswalk** when new source material is incorporated.
6. **Always update the affected Model Scorecard** when a benchmark, deployment, or metric for a priority model changes.
7. **Reference the FITNESS_CHECKLIST** at `08-change-control/FITNESS_CHECKLIST.md` for the full gate criteria.

## Example Execution Flow

```
User: "DeepSeek V4 Flash benchmarked at 3,200 output tokens/sec/GPU on H200 at FP8"

Agent execution:
1. Identify: This affects the DeepSeek V4 Flash model note, its Model Deployment,
   the Benchmark Run entity, met-tokens-per-gpu-second, CAL cost formulas,
   CF-fp8-throughput coefficient, and the relevant validation item.
2. Impact scan: Benchmark Run → Model Deployment → Serving Runtime config →
   Capacity Pool economics → cost/1M tokens → revenue/GPU-hour → DeepSeek scorecard.
3. Update canonical notes:
   - Benchmark Run: record run, hardware, config, result
   - met-tokens-per-gpu-second: upgrade confidence assumed → measured for DeepSeek
   - cost formulas: recompute cost/1M tokens with measured throughput
   - CF-fp8-throughput: upgrade confidence, record evidence source
   - validation item: mark Validated
4. Propagate:
   - Coefficient Catalog: update confidence distribution
   - DeepSeek Model Scorecard: update throughput and cost rows
   - Evidence & Confidence Framework: update corpus confidence table
5. Consistency pass: verify no contradictions, update Performance/Commercial hubs
6. Summary: "Recorded DeepSeek H200 FP8 benchmark. tokens/GPU-second upgraded to
   measured. cost/1M tokens recomputed. 6 notes updated. No new open questions."
```

## Anti-Patterns

- Editing a hub page or scorecard without updating the canonical note it summarizes
- Changing a coefficient value without updating the Assumption Register
- Adding a new concept without checking for an existing canonical home first
- Updating a throughput formula without checking which cost/economics metrics consume it
- Recording a benchmark without updating downstream confidence states
- Presenting a roadmap target as a measured result
- Creating a new document that redefines an existing concept instead of linking to it
