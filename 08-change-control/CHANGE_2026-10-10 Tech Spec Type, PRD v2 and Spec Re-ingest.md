---
id: chg-2026-10-10-tech-spec-prd-v2
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [tech spec note type, spec first-class type, prd template v2, prd coverage plan change, as-built re-ingest 2026-10-10]
related: [pol-fitness-checklist, chg-2026-10-07-prd-first-class-type, chg-2026-10-06-prd-standard-pack, wiki-prd-coverage-plan, src-identity-access-spec, src-metering-spec, src-monitoring-audit-spec, hub-roadmap]
source_docs: ["reference/PRD/", "PM request 2026-10-10: use filed PRDs/tech specs as template basis; spec as first-class type; PRD coverage plan"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "spec type, PRD v2 + tech-spec templates, code grounding + roadmap link lint; 5 newer specs re-ingested; PRD plan."
---

# CHANGE 2026-10-10 — Tech Spec Type, PRD v2 and Spec Re-ingest

## Trigger

The product owner added `reference/PRD/` (11 engineering PRDs and tech specs) on 2026-10-10. They asked for three things: use it to shape PRD and tech-spec templates that match what the developers expect, make tech specs a first-class note type, and produce a plan for which PRDs the roadmap still needs (without writing those PRDs).

## What Changed

**Intake finding.** `reference/PRD/` mostly duplicates `reference/rackai-platform/` (ingested 2026-09-04). The five PRDs and the Accelerator Selection spec are unchanged. The IAC, Multi-Tenancy & Metering, Platform Monitoring, In-Tenant Observability and Auditability specs are newer: same version headers, plus dated AS BUILT / PROPOSED, NOT BUILT annotations (2026-09-11 → 2026-10-08).

**Standards (portable pack).**
- New note type `spec` (ID prefix `spec-`): added to `rackai-operating-standards.md` (type list and frontmatter enum) and `scripts/lint-frontmatter.sh`.
- New `.kiro/steering/tech-spec-standards.md` and `templates/tech-spec.md`. The template is based on the engineering design-doc shape (document control table → overview/goals/non-goals → architecture → resources/APIs → lifecycle → failure → NFR → milestones with engineering and release checklists → open questions). It adds:
  - requirement traceability to the PRD
  - declared divergences from the PRD
  - a platform integration contract
  - dated as-built markers as a formal convention
- `templates/prd.md` v2:
  - a document control table that includes **roadmap items**
  - the engineering team's section names (Vision, Problem Statement, Product Principles, Core Entities, Platform Integration, Failure Handling, Data Retention), on top of the ten-item minimum set
  - renumbered: kill criterion is now §17, open decisions §18
- `prd-standards.md`: section numbers updated; new sections on Standard Sections, Roadmap Traceability, and PRD → Tech Spec. v1 PRDs stay valid until their next substantive revision.
- `FITNESS_CHECKLIST.md`: new Section 2c, T-01…T-08.
- `scripts/sync-prd-standard.sh`: now carries both packs and reports the type/lint and T-check actions siblings need.

**Corpus.**
- Source notes re-ingested with an "As-Built Deltas" section: [[Identity and Access Control Spec]], [[Multi-Tenancy and Metering Spec]], [[Monitoring and Auditability Spec]].
- Downstream propagation of those deltas: see Impact.
- New [[PRD Coverage Plan]] (`wiki-prd-coverage-plan`), linked from [[RackAI Roadmap]].

## Why

The engineering PRDs are narrative: no requirement IDs, no owners, success criteria that can't be measured, no kill criterion. They do carry sections developers rely on, which our v1 template lacked. The engineering tech specs had already invented as-built annotation and PRD-divergence sections on their own, but had no requirement traceability. Formalising both shapes means wiki-authored PRDs and specs look familiar to engineering while being stricter.

## Impact

- **Knowledge-platform:** `spec` is not yet in its ingestion schema. No `type: spec` note exists yet, so nothing breaks today. **Before the first spec note is pushed, knowledge-platform must accept `spec` / `spec-`**, otherwise the note becomes a shadow node.
- **Sibling wikis (AIOS Wiki, VCFRaxWiki):** not yet synced. Before running `scripts/sync-prd-standard.sh --apply`, add `spec` to their type lists and merge Section 2c by hand.
- **Existing PRD:** [[Solution Marketplace PRD]] stays on v1 numbering until its next substantive revision.

## Addendum — Code Grounding and Roadmap Links (same day)

Product-owner follow-up: tech specs must be grounded in the existing code, read-only, and the roadmap table must link the PRD/spec for each item.

- **Read-only code rule + conversion procedure** (`tech-spec-standards.md`): converting a PRD to a spec now requires a read-only investigation of `RSS-Engineering/rackai` (backend), `rackai-ui` (frontend) and `rackai-docs` (docs). The spec must answer: fit with existing patterns, what is extended, standards to enforce, dependency management and fork prevention, and modularity improvements. These repos are never written to, pushed to or PR'd from wiki work. The repo list is in `rackai-operating-standards.md`.
- **Template:** tech-spec §3 is now *Codebase Grounding (read-only)*, with six subsections and citations in the form `owner/repo@sha:path`.
- **Roadmap table:** `05-wiki/RackAI Roadmap.csv` gained **PRD** and **Tech spec** columns (knowledge-console links). They are filled for the 20 rows covered today. Only the two columns were appended; no other cell changed. [[Solution Marketplace PRD]] gained a document control table naming its eight roadmap items.
- **Fitness:** P-09 (PRD roadmap link-back), T-09 (codebase grounding), T-10 (spec roadmap link-back).
- **Lint:** new `scripts/lint-prd-spec.py`, wired into the pre-commit hook (`install-git-hooks.sh`, re-installed). It passes on the current corpus, and a deliberately bad probe note confirmed it catches each failure.
- **Local guard (git-excluded, not committed):** `.claude/hooks/code-repo-guard.sh` denies agent writes, commits, pushes, branches and PR/issue creation against the code repos or the clone directory `~/Projects/rackai-code/`.

## Addendum — PRD Grouping Ratified (same day)

The product owner reviewed the proposed groupings, asked for a critical review, and accepted eight changes, now applied to [[PRD Coverage Plan]] and the templates.

1. **Wave 1 is now A, B, C, J, plus D-0.** J (Fine-Tuning Operations) moved up because the partner build is already moving; wave 1 covers only its product boundary. D-0 is a sketch of the evidence contract so wave-1 PRDs contribute evidence in one shape.
2. **Row 21** (evidence-informed accelerator selection) moved from A to G, as a later phase. It is a recommendation, not a placement mechanism.
3. **Renames.** C becomes **Governed Execution & Delegated Authority** (`prd-governed-execution-authority`): "control envelope" is the name of decision D3 as a whole, which also covers E. I becomes **Inference Access & Distribution** (`prd-inference-access-distribution`), framed as the access surfaces for the Level 0 shared-endpoint offer. It consumes the platform contracts rather than re-specifying them, and row 78 stays an open decision.
4. **Two ownership rules:**
   - **C vs E.** C owns who may act and enforcement; E owns where execution happens and what may cross the boundary. E's boundary rules are enforced by C. Both serve the sovereign promise, and both contribute to D's evidence.
   - **A vs G.** A owns the placement contract and its execution; G owns recommendations, and only ranks options that already satisfy A's hard constraints, never relaxing one.
5. **Delivery column.** Specification coverage and delivery readiness are now reported separately; every plan table has a Delivery column taken from the roadmap's Status field.
6. **Loop role section.** PRD template v2 gains **§11 Loop Role & Cross-PRD Interfaces**; later sections are renumbered to §12–§19, and fitness check **P-10** is added. The plan maps each PRD onto the existing operating loop rather than a new grouping scheme.
7. **Many-to-many PRD ↔ spec.** A PRD may be implemented by several specs and a spec may implement several PRDs. Updated: the spec template ("Based on PRD(s)", PRD-prefixed traceability), `tech-spec-standards.md`, and checks T-01 and T-02.
8. **Canonical notes.** A shared concept's canonical note is written in the same change as the PRD that introduces it, not as a separate gate beforehand. A concept used by only one PRD may live in that PRD until a second consumer appears (`prd-standards.md`, template §6).

**Code access.** `scripts/code-mirror.sh` keeps read-only copies of the three RackAI code repos in `~/Projects/rackai-code/`, read with a second `gh` account (the work account). The wiki's push account is unchanged.

## Propagation (as-built deltas)

Corrected for as-built state, each citing its source note:
- 01-entities: [[Organization]]
- 02-operations workflows: [[Audit]], [[Identity & Access Control]], [[Metering]]
- 03-commercial: [[Billing & Payment]]
- 04-evidence: [[Capability Gap Register]], [[KPI Telemetry Target List]], Open Questions register
- Hubs and wiki: [[RackAI Platform]], [[Milestone Release Map]], Glossary
- 06-sources: [[Source-to-Concept Crosswalk]]

Confidence on built items is `derived`, never `measured`. Three conflicts were surfaced, not resolved:
- end-to-end latency recording rule ("confirmed" in the KPI list vs no PrometheusRule shipped)
- `usage_records` retention (13 months vs per-install, default 365 days)
- org-level RBAC ("dropped" vs built but gated off)

## Open Questions

- Approve the PRD groupings and wave order in [[PRD Coverage Plan]].
- Access: the current GitHub login (`eak-mentraAI`) cannot see the RSS-Engineering repos. Grounding needs an account with read access, or read-only clones in `~/Projects/rackai-code/`.
- Console links follow the knowledge-platform route `/browse/<corpus>/<id>` with corpus `rackai`. This is read from the console code, not yet checked against the live site.
- `spec` must be added to the knowledge-platform schema before the first spec note is pushed.
- Org-level RBAC: the roadmap says IAC M4 was dropped, but the as-built IAC has org-scoped RoleBindings (gated off). Recorded in the open questions register.
