---
id: pol-release-readiness
type: policy
status: draft
owner: rackai-product
domain: governance
aliases: [release readiness, implementation complete vs customer available, release gates, milestone readiness states]
related: [wiki-prd-coverage-plan, hub-roadmap, pol-verification-status, pol-failure-taxonomy, prd-concierge-engineer, prd-model-lifecycle, prd-inference-access-distribution, prd-customer-observability-evidence]
source_docs: ["Product-owner review disposition, PRD batch B–J, 2026-10-10 (finding S-6)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-governance
summary: "Four readiness states per milestone (implemented, integration ready, acceptance proven, customer available)."
---

# Release Readiness States

## Purpose

A milestone can deliver its own code and still not be releasable because a prerequisite from another PRD is missing. Examples: H v1 needs C Phase 2, F's canary needs A's candidate revisions, I's shared endpoint needs E's cache check, and D's report needs every contributor's coverage records. One "done" status hides those gaps. This note separates them.

## Rule

Every tech-spec milestone, and every acceptance criterion's release gate, is tracked through four states, in order:

| State | Means | Requires |
|---|---|---|
| **Implementation complete** | The milestone's own code, tests and docs are merged | The milestone's engineering checklist |
| **Integration ready** | Every cross-PRD prerequisite the milestone consumes is itself at least *implementation complete*, and the interfaces match | The milestone's named **release blockers** (below) are cleared |
| **Acceptance proven** | Each acceptance criterion the milestone carries has passed, with its evidence source recorded | AC results with evidence |
| **Customer available** | It is enabled for customers at its gate (MOE-n), with docs and support | Release checklist; product sign-off |

**Release blockers.** Each milestone lists its cross-PRD prerequisites as named blockers, in the form `blocked-by: <PRD> <milestone or item>`. A milestone may not be marked *integration ready* while a blocker is open. A blocker is never just a cross-reference.

**Acceptance criteria** each name an expected result, an evidence source and their milestone or release gate.

## Scope

Section 13 (Milestones) of every RackAI tech spec, and the [[PRD Coverage Plan]] delivery view.

## Governs

| Target | Relationship |
|--------|--------------|
| [[PRD Coverage Plan]] | CONSTRAINS → delivery-readiness reporting |
| [[Concierge Engineer Tech Spec]] | CONSTRAINS → v1 blocked by C Phase 2 |
| [[Model Lifecycle Tech Spec]] | CONSTRAINS → canary blocked by A candidate revisions |
| [[Inference Access & Distribution Tech Spec]] | CONSTRAINS → shared endpoint blocked by E M3 |

## Enforcement

Applied at review (Fitness T-06): every milestone lists its release blockers, and every acceptance criterion names its evidence source and gate.

## See Also

- [[Verification Status Vocabulary]]
- [[Failure Mode Taxonomy]]
- [[Governance Hub]]
