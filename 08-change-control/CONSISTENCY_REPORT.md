---
id: chg-consistency-report
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [consistency pass, consistency audit, cc-consistency-report]
related: [pol-fitness-checklist, pol-change-packet]
parent: hub-wiki
source_docs: []
confidence: validated
last_reviewed: 2026-09-03
summary: "Output template for a consistency pass in the Rack AI OpenRouter wiki."
---

# Consistency Report Template

## Purpose

Output of a consistency pass. Produced after every meaningful change. Records what was verified, what passed, and what needs attention.

---

## Report Structure

### Meta

- **Date:** YYYY-MM-DD
- **Scope:** (specific notes | layer | full corpus)
- **Trigger:** (change packet reference | periodic review | new source/benchmark incorporation)
- **Run by:** (agent | human)

---

### Structural Checks (Section 1)

| Check | Status | Notes |
|-------|:------:|-------|
| S-01 No duplicate concepts | ☐ Pass / ☐ Fail | |
| S-02 No orphan nodes | ☐ Pass / ☐ Fail | |
| S-03 No broken backlinks | ☐ Pass / ☐ Fail | Count: |
| S-04 No layer violations | ☐ Pass / ☐ Fail | |
| S-05 Owner assigned | ☐ Pass / ☐ Fail | Missing: |
| S-06 Source traceability | ☐ Pass / ☐ Fail | Missing: |
| S-07 Confidence declared | ☐ Pass / ☐ Fail | Missing: |
| S-08 Relationships explicit | ☐ Pass / ☐ Fail | Sparse: |
| S-09 Formulas resolve | ☐ Pass / ☐ Fail | Broken: |
| S-10 Coefficients resolve | ☐ Pass / ☐ Fail | Missing: |
| S-11 Assumptions linked | ☐ Pass / ☐ Fail | Orphaned: |
| S-12 Validations linked | ☐ Pass / ☐ Fail | Stale: |
| S-13 Benchmarks resolve | ☐ Pass / ☐ Fail | Unsourced numbers: |
| S-14 Stable IDs preserved | ☐ Pass / ☐ Fail | Changed: |
| S-15 Aliases preserved | ☐ Pass / ☐ Fail | Lost: |

---

### Story Consistency (Section 2)

| Check | Status | Notes |
|-------|:------:|-------|
| C-01 One coherent story | ☐ Pass / ☐ Fail | |
| C-02 Terminology stable | ☐ Pass / ☐ Fail | Drift detected: |
| C-03 Layer agreement | ☐ Pass / ☐ Fail | Conflict: |
| C-04 No silent redefinitions | ☐ Pass / ☐ Fail | Redefined: |
| C-05 Abstraction chain intact | ☐ Pass / ☐ Fail | Broken at: |
| C-06 Confidence propagation valid | ☐ Pass / ☐ Fail | Violations: |
| C-07 Graph invariants hold | ☐ Pass / ☐ Fail | Violated: |
| C-08 No hidden conflicts | ☐ Pass / ☐ Fail | New conflicts: |
| C-09 Targets vs. results distinct | ☐ Pass / ☐ Fail | Mislabeled: |

---

### Findings

#### Contradictions Detected

| # | Source A | Source B | Concept | Status |
|---|----------|----------|---------|--------|
| | | | | Open question created / resolved |

#### Terminology Drift

| Term | Expected | Found In | Action |
|------|----------|----------|--------|
| | | | |

#### Stale Assumptions

| ID | Last Reviewed | Exit Criteria Met? | Action |
|----|--------------|:------------------:|--------|
| | | | |

#### Unsourced Performance Claims

| Claim | Location | Missing Evidence | Action |
|-------|----------|------------------|--------|
| | | | |

#### New Regressions

| Test | Previous Score | Current Score | Δ | Action |
|------|:--------------:|:-------------:|:-:|--------|
| | | | | |

---

### Recommendations

1. 
2. 
3. 

---

### Sign-off

- **Consistency pass:** ☐ Pass / ☐ Conditional / ☐ Fail
- **Blocking issues:** (count)
- **Next review date:** YYYY-MM-DD

---

## See Also

- [[FITNESS_CHECKLIST]] — check definitions
- [[CHANGE_PACKET]] — triggering change
- [[REGRESSION_SUITE]] — acceptance tests
