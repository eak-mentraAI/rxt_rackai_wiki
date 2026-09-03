---
id: pol-change-packet
type: policy
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [change packet, change request, edit plan, cc-change-packet]
related: [pol-fitness-checklist, chg-consistency-report]
parent: hub-wiki
source_docs: [init/agent_guide.md]
confidence: validated
last_reviewed: 2026-09-03
summary: "Template for structured change proposals in the Rack AI OpenRouter wiki."
---

# Change Packet Template

## Purpose

Required before any meaningful corpus edit. Forces explicit impact assessment before changes are made. Prevents drift from becoming hidden debt.

---

## Rule

> **No change is complete until the affected canonical notes, dependent notes, and regression checks have been updated and re-passed.**

---

## Change Packet Structure

Complete this template before editing:

### 1. Source of Change

- **Trigger:** (new source document | correction | benchmark result | production telemetry | competitive datapoint | business decision | architecture update)
- **Source reference:** (document, benchmark run ID, dashboard, ticket)
- **Date:** YYYY-MM-DD
- **Requester/Owner:**

### 2. Affected Concept(s)

- **Primary concept:** (canonical name + ID)
- **Layer:** (L1 Entity | L2 Operations | L3 Commercial | L4 Evidence | L5 Wiki)
- **Change type:** (new object | modification | relationship change | evidence update | deprecation)

### 3. Impact Scan

| Category | Impacted Items |
|----------|---------------|
| Entities (models, deployments, runtimes, GPU fleet, pools) | |
| Workflows | |
| Formulas | |
| Coefficients | |
| Metrics / KPIs | |
| Benchmark Runs | |
| Assumptions | |
| Validations | |
| Events | |
| Policies | |
| Model Scorecards | |
| Hub pages | |
| Indexes | |
| Crosswalk | |

### 4. Propagation Plan

Order of updates (follow this sequence):

1. Source note / provenance update
2. Canonical entity or operational note
3. Dependent operational notes (formulas, workflows, metrics, coefficients)
4. Evidence layer (benchmarks, assumptions, validations, confidence)
5. Commercial layer (if unit economics/pricing/allocation affected)
6. Hub pages, indexes, and model scorecards
7. Crosswalk and source inventory
8. Changelog entry

### 5. Confidence Assessment

- **Confidence of new information:** (assumed | derived | measured | validated)
- **Confidence change on existing notes:** (upgrade | downgrade | unchanged)
- **Weakest link in chain:** (which upstream dependency caps confidence)

### 6. Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| | | |

### 7. Contradictions Surfaced

| Contradiction | Source A | Source B | Resolution |
|--------------|----------|----------|------------|
| | | | Open question / validation item created |

### 8. Change Summary (completed after edits)

- **Objects changed:**
- **Objects added:**
- **Edges added:**
- **Edges removed:**
- **Notes requiring review:**
- **Open questions created:**
- **Assumptions impacted:**
- **Validations impacted:**
- **Benchmarks impacted:**
- **Downstream documents affected:**

---

## Execution Sequence

```
Change request
  → Impact scan (this template)
  → Edit canonical note
  → Propagate dependent updates
  → Run fitness checks
  → Run consistency pass
  → Record regressions or close them
  → Produce changelog entry
```

---

## See Also

- [[FITNESS_CHECKLIST]] — gates that must pass
- [[CONSISTENCY_REPORT]] — output template
- [[REGRESSION_SUITE]] — acceptance tests
