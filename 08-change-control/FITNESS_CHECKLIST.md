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
last_reviewed: 2026-10-10
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
| S-03 | No broken backlinks | All in-body `[[wikilinks]]` and relative `.md` links resolve to a Knowledge Object (`./scripts/lint-links.sh` reports 0 unresolved) |
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
| S-16 | Summary within limit | Every note's `summary` frontmatter is ≤ 120 characters. Over-length summaries are **blocked** by knowledge-platform ingestion and silently downgrade the note to an unstructured shadow node (searchable but not a proper object in the browse tree). Enforced by `./scripts/lint-frontmatter.sh`. |

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

## Section 2b — PRD Checks

Run on any PRD (`05-wiki/<Thing> PRD.md`, `type: prd`). Governed by `.kiro/steering/prd-standards.md` (a portable standard shared across sibling wiki repos). A PRD is not review-ready until all applicable checks pass.

| # | Check | Pass Criteria |
|---|-------|---------------|
| P-01 | Canonical link | The PRD links to the canonical concept note and does **not** redefine it (projection, not definition); the canonical ID is in `related` |
| P-02 | Minimum viable set | All ten required items are answered: problem/hypothesis, users, goals+non-goals, functional reqs, non-functional reqs, scope/phasing, success metrics, kill criterion, open decisions, dependencies |
| P-03 | Boundary stated | A scope line names what the PRD covers **and** what it explicitly does not (the ownership boundary) |
| P-04 | Requirements testable | Functional reqs are numbered and verifiable, prioritized MUST/SHOULD/MAY; no stale internal cross-references (e.g. dangling `FR-x`) |
| P-05 | Kill criterion present | There is an explicit kill/falsification criterion — what evidence would stop or redirect the initiative |
| P-06 | Open decisions owned | Each open decision is numbered with an owner and what it blocks; unresolved specifics are decisions, not invented requirements |
| P-07 | Confidence honesty | A proposed/unbuilt PRD is `confidence: assumed` with a status banner; it does not read as a committed build or assert unbuilt capability; metric targets are postures, not measured values (ties S-13) |
| P-08 | Shape compliance | Authored from `templates/prd.md`; frontmatter complete; `summary` ≤ 120 chars (S-16); located in `05-wiki/` with a `prd-` ID |
| P-09 | Roadmap link-back | The document control table names its roadmap items (milestone names exactly as in `05-wiki/RackAI Roadmap.csv`, `;`-separated), and each of those rows' **PRD** column contains this PRD's knowledge-console link (`https://knowledge.rackspace-cloud.com/browse/rackai/<id>`). Enforced by `scripts/lint-prd-spec.py` |
| P-10 | Loop role & interfaces | §11 names the loop step owned and the promise served, and lists each cross-PRD interface it provides or consumes, with exactly one defining location; shared concepts have a canonical note written no later than the PRD itself |
| P-11 | Reviewable decisions, not auto-approval | Proposed product decisions (§20) and acceptance criteria (§15) are listed individually so each can be accepted or changed; `status` is `reviewed` only with a recorded *Product approval* (who, date, version). Passing checks is never approval. Material as-built divergence is marked *divergent: pending product review* with a product-owner open decision |

---

## Section 2c — Tech Spec Checks

Run on any tech spec (`05-wiki/<Thing> Tech Spec.md`, `type: spec`). Governed by `.kiro/steering/tech-spec-standards.md` (portable, companion to the PRD standard). A spec is not review-ready until all applicable checks pass.

| # | Check | Pass Criteria |
|---|-------|---------------|
| T-01 | PRD + canonical link | The ID of every PRD it implements (PRD ↔ spec is many-to-many) and the canonical concept ID are in `related`; the spec links concepts instead of redefining them |
| T-02 | Requirements traced | Every functional requirement of each implemented PRD appears in the §1.3 table as covered / partial / deferred / divergent / in a named sibling spec; no silent drops |
| T-03 | Divergences declared | Every departure from the PRD is listed in §1.4 with its justification ("none" is valid) |
| T-04 | Integration contract complete | Every row of the platform integration contract (identity, tenancy, metering/quotas, audit, monitoring, tenant-visible fields, billing) is answered |
| T-05 | Failure behaviour explicit | Fail-open vs fail-closed, delivery guarantees, and loss detection are stated for each event/request class |
| T-06 | Milestones actionable | Each milestone has an epic, a breakdown mapped to requirement IDs, an engineering checklist and a release checklist |
| T-07 | Confidence + as-built honesty | Unbuilt design is `assumed`; drift is recorded with dated AS BUILT / PROPOSED, NOT BUILT markers; NFR targets are labelled target vs measured with a source (ties S-13) |
| T-08 | Shape compliance | Authored from `templates/tech-spec.md`; frontmatter complete; `summary` ≤ 120 chars (S-16); located in `05-wiki/` with a `spec-` ID; open questions numbered with owners |
| T-09 | Codebase grounding (read-only) | §3 cites at least one product code repo at a commit SHA (`owner/repo@sha`) and answers all six subsections: repos & revisions, existing patterns, extension points, standards to enforce, dependencies & fork prevention, improvement & modularity opportunities. No code repo was written to, pushed to, or PR'd from this work. Enforced by `scripts/lint-prd-spec.py` |
| T-10 | Roadmap link-back | The document control table names its roadmap items, and each of those rows' **Tech spec** column contains this spec's knowledge-console link. Enforced by `scripts/lint-prd-spec.py` |
| T-11 | Divergence escalated | Every AS BUILT marker that is material to an implemented PRD (changes a requirement, acceptance criterion, hard-constraint guarantee, boundary or customer-visible behaviour) has a matching *divergent: pending product review* item in that PRD; built claims cite evidence (`measured` needs test/benchmark/telemetry) |

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

Link resolution (same rules as the Knowledge Console — id, aliases, file name, H1 title; must report 0 unresolved):

```bash
./scripts/lint-links.sh
```

---

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| DEPENDS_ON | [[REGRESSION_SUITE]] | → | Section 3 runs the acceptance tests |
| PRODUCES | [[CONSISTENCY_REPORT]] | → | Output of the consistency pass |
| DEPENDS_ON | [[CHANGE_PACKET]] | ← | A change packet must pass these gates |

## See Also

- [[REGRESSION_SUITE]] — full acceptance test definitions
- [[CHANGE_PACKET]] — required before edits
- [[CONSISTENCY_REPORT]] — output of consistency pass
