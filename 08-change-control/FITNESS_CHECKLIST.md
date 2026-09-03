---
id: pol-fitness-checklist
type: policy
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [fitness checks, structural checks, quality gate, cc-fitness-checklist]
related: [pol-regression-suite, pol-change-packet, chg-consistency-report]
parent: hub-wiki
source_docs: [init/init.md, init/agent_guide.md]
confidence: validated
last_reviewed: 2026-09-03
summary: "Gate criteria checklist for corpus changes in the Rack AI OpenRouter wiki."
---

# Fitness Checklist

## Purpose

Required gate for every corpus change. No change is complete until all applicable checks pass. Run on every meaningful edit to canonical notes, operational ontology, commercial model, or evidence layer.

---

## When to Run

- **Every change:** Structural checks (Section 1)
- **After meaningful updates:** Story consistency checks (Section 2)
- **Before merge/release:** Full regression (Section 3 → see [[REGRESSION_SUITE]])

---

## Section 1 — Structural Fitness Checks

Run on every change.

| # | Check | Pass Criteria |
|---|-------|---------------|
| S-01 | No duplicate canonical concepts | Every concept has exactly one canonical home in the correct layer folder |
| S-02 | No orphan nodes | Every important entity has inbound links, outbound links, owner, source, and confidence |
| S-03 | No broken backlinks | All `[[wikilinks]]` in wiki layer (00-hub through 06-sources) resolve to existing .md files |
| S-04 | No layer violations | Entities in 01-entities/, operations in 02-operations/, commercial in 03-commercial/, evidence in 04-evidence/ |
| S-05 | Owner assigned | Every canonical note has a non-empty `owner` field in frontmatter |
| S-06 | Source traceability | Every canonical note has at least one entry in `source_docs` frontmatter |
| S-07 | Confidence declared | Every canonical note has a valid `confidence` state (assumed, derived, measured, validated) |
| S-08 | Relationships explicit | Every entity has a Relationships table with typed edges |
| S-09 | Formulas resolve | Every formula reference (CAL-xxx / fml-xxx) points to an existing formula catalog note |
| S-10 | Coefficients resolve | Every coefficient reference (CF-xxx / coeff-xxx) exists in the Coefficient Catalog or as a standalone note |
| S-11 | Assumptions linked | Every assumption (ASS-xxx / asm-xxx) exists in the Assumption Register with exit criteria |
| S-12 | Validations linked | Every validation item (VAL-xxx / val-xxx) exists in the Validation Register with status |
| S-13 | Benchmarks resolve | Every performance number traces to a Benchmark Run note or a named production-telemetry source |
| S-14 | Stable IDs preserved | No canonical ID was changed or recycled |
| S-15 | Aliases preserved | Deprecated terms moved to aliases, not deleted |

---

## Section 2 — Story Consistency Checks

Run after any meaningful update.

| # | Check | Pass Criteria |
|---|-------|---------------|
| C-01 | One coherent story | The corpus tells one consistent narrative about what Rack AI is on OpenRouter, how it serves models, and how its economics work |
| C-02 | Terminology stable | No concept has been casually renamed without alias preservation and dependent-note updates |
| C-03 | Layer agreement | Commercial, operational, capacity, and evidence layers describe the same reality |
| C-04 | No silent redefinitions | No new document quietly redefines an existing canonical concept |
| C-05 | Abstraction chain intact | Market Demand → Model → Model Deployment → Serving Runtime → Capacity Pool → GPU Fleet → Topology — no layer bypassed |
| C-06 | Confidence propagation valid | No downstream node has higher confidence than its weakest upstream dependency |
| C-07 | Graph invariants hold | All invariants from INIT.md verified (e.g., "Every Model Deployment serves exactly one Model") |
| C-08 | No hidden conflicts | Any source disagreement (roadmap target vs. measured benchmark, competing datapoints) is surfaced as an open question, not smoothed over |
| C-09 | Targets vs. results distinct | Roadmap/strategy targets are never presented as measured results; confidence states reflect this |

---

## Section 3 — Regression Acceptance Checks

Run periodically and before release. See [[REGRESSION_SUITE]] for full test definitions.

| # | Check | Minimum Score |
|---|-------|:-------------:|
| R-01 | Traversal: market demand → GPU topology | ≥ 4/5 |
| R-02 | Reverse traversal: fleet/telemetry signal → business impact | ≥ 4/5 |
| R-03 | Impact analysis for a changed node | ≥ 4/5 |
| R-04 | Evidence chain tracing (performance claim → benchmark) | ≥ 4/5 |
| R-05 | Digital twin simulation (model launch / traffic scenario) | ≥ 3.5/5 |
| R-06 | Graph health/completeness scoring | ≥ 3.5/5 |
| R-07 | Multi-deliverable generation from graph only | ≥ 3.5/5 |

---

## Thresholds

| Score | Status | Action |
|:-----:|--------|--------|
| 5/5 | Stable | No action required |
| 4/5 | Acceptable | Monitor; schedule improvement |
| 3.5–4/5 | Warning | Must be addressed before next release |
| < 3.5/5 | **Hard stop** | Must be fixed before merge |

---

## Verification Command (Manual)

Frontmatter compliance:

```bash
./scripts/lint-frontmatter.sh
```

Quick structural check for broken links in wiki layer:

```bash
# Find wikilinks that don't resolve to existing .md files
grep -roh '\[\[[^]|]*' 00-hub/ 01-entities/ 02-operations/ 03-commercial/ 04-evidence/ 05-wiki/ 06-sources/ | \
  sed 's/\[\[//' | sort -u > /tmp/targets.txt
find . -name "*.md" -not -path "./.kiro/*" -not -path "./templates/*" -exec basename {} .md \; | sort -u > /tmp/files.txt
comm -23 /tmp/targets.txt /tmp/files.txt
```

---

## See Also

- [[REGRESSION_SUITE]] — full acceptance test definitions
- [[CHANGE_PACKET]] — required before edits
- [[CONSISTENCY_REPORT]] — output of consistency pass
