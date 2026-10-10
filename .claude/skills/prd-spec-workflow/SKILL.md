---
name: prd-spec-workflow
description: Run the wiki's PRD → tech spec → roadmap process end to end with the right stop points for product approval. Use when asked to draft or revise a PRD for a roadmap item, convert an approved PRD into a tech spec, record as-built drift from engineering, or update the roadmap's PRD/Tech spec links. Works in any wiki that carries the portable PRD + tech-spec standard (.kiro/steering/prd-standards.md, tech-spec-standards.md).
---

# PRD → Tech Spec → Roadmap Workflow

This skill is the **procedure**. The **rules** live in the repo's steering files; read them, don't restate them:

- `.kiro/steering/prd-standards.md` — PRD shape, minimum set, approval, divergence, confidence
- `.kiro/steering/tech-spec-standards.md` — spec shape, PRD→spec conversion, read-only code rule, as-built discipline
- `.kiro/steering/*operating-standards.md` — note types, frontmatter, **code repositories (read-only)**, **roadmap ↔ PRD/spec link columns**
- `08-change-control/FITNESS_CHECKLIST.md` — P-checks (PRD) and T-checks (spec)
- Templates: `templates/prd.md`, `templates/tech-spec.md`

Repo-specific facts (which code repos, where the roadmap table is, the console URL, which scripts exist) come from those files, never from this skill. If a step names a script the repo doesn't have, do the step by hand and say so.

## Non-negotiables (apply in every mode)

1. **Checks are not approval.** Lint and fitness passing means *review-ready*. Only the product owner approves; record their approval exactly as they gave it, never on their behalf.
2. **Stop at every ⛔ stop point.** Present what changed and what needs a decision, then wait. Never commit, push or publish past a stop point without an explicit instruction.
3. **Code repos are read-only.** Never write to, commit in, branch, push to, or open PRs/issues against them. Read only from local mirrors outside the wiki (or read-only API calls), pinned to a commit SHA.
4. **Canonical notes only when a concept is shared** across capabilities. Otherwise define it inside the PRD.
5. **Honest confidence.** `assumed` for unbuilt intent; `derived` for code/as-built evidence; `measured` only with cited test, benchmark or telemetry evidence.
6. **PRD ↔ spec is many-to-many.** Traceability in both directions; no forced one-to-one.

## Mode 1 — Draft or revise a PRD

1. **Locate the work.** Find the roadmap item(s) and their grouping in the coverage plan (e.g. `05-wiki/PRD Coverage Plan.md` if present): loop role, wave, gating decisions, shared interfaces. Query the graph (`scripts/kg.py find|show|in`) rather than reading whole files.
2. **Read context.** The canonical notes the PRD projects from, the relevant hubs, the ingested engineering sources, and any ownership rules between PRDs (e.g. which PRD owns a decision vs its execution).
3. **Survey current state (read-only), if the capability touches built code.** Refresh mirrors if the repo has a mirror script (e.g. `scripts/code-mirror.sh sync`). Delegate a read-only survey that returns facts with `owner/repo@sha:path` citations: what exists, what's missing, what fails today and how users see it. Use it in the PRD's Problem Statement; it is evidence, not design.
4. **Shared concepts.** If the PRD introduces a concept other PRDs will consume, write a thin canonical note in the same change. If only this PRD uses it, define it in the PRD (Core Entities).
5. **Draft from `templates/prd.md`.** Pay special attention to:
   - document control table: exact roadmap milestone names, `;`-separated; *Product approval* = not yet approved
   - scope line naming what this PRD does **not** own
   - Loop Role & Cross-PRD Interfaces: each shared interface defined in exactly one place
   - acceptance criteria: binary, testable, each traced to requirements, each reviewable on its own
   - proposed product decisions: each with alternatives and rationale, status *proposed*
   - kill/falsification criterion and owned open decisions
   - no invented numbers: targets are postures; no baseline means say so
6. **Link the roadmap.** Add the PRD's console link to the *PRD* column of every named roadmap row (append with `; ` if the cell has links). Change no other cell; verify that only that column changed.
7. **Propagate.** Back-links on canonical notes the PRD relies on; fix any note the PRD's ownership rules contradict; update the coverage plan's status for this PRD.
8. **Change record** in `08-change-control/` (date, trigger, what changed, propagation, open items).
9. **Run checks:** frontmatter lint, PRD/spec link lint (if present), broken-link check, then the P-checks by hand. Also verify internal IDs: every `FR-n`, `AC-n`, `D-n`, `PD-n` used is defined.
10. ⛔ **Stop for product review.** Report: what was drafted, current-state findings, the proposed decisions (PD-n) and acceptance criteria (AC-n) to decide, the most contestable ones, and open decisions. Ask which to approve or revise.
11. **Apply review.** Revise only what was asked; don't expand scope. Mark approved decisions with the date, revised ones *pending approval*. Re-run checks. ⛔ Return the updated decisions and acceptance criteria for final approval.
12. **On final approval:** record it in the *Product approval* row and the change record, set `status: reviewed`, rerun checks. ⛔ Commit only when told to; push only when told to.

## Mode 2 — Convert an approved PRD into a tech spec

Precondition: the PRD (or PRDs) is approved, and the knowledge platform accepts `type: spec` (if it doesn't, stop and say so: a pushed spec would become an unstructured shadow node).

1. **Scope.** Decide with the user whether this is a new spec, an extension of an existing engineering spec, or one spec serving several PRDs.
2. **Ground in the code (read-only; mandatory).** Refresh mirrors, pin SHAs, and answer the six parts of the spec's *Codebase Grounding* section: repos & revisions read; existing patterns; extension points (additive vs breaking); standards to enforce; dependencies & fork prevention across backend/UI/docs and environments; improvement & modularity opportunities (in scope vs follow-up). Delegate wide surveys; cite `owner/repo@sha:path`; never copy code.
3. **Design from `templates/tech-spec.md`:** requirements traceability (every FR of every implemented PRD: covered / partial / deferred / divergent / sibling spec), declared divergences from the PRD, the platform integration contract (every row), failure handling, NFRs labelled target vs measured, milestones with epic, breakdown, engineering checklist and release checklist.
4. **Link both ways:** `related` lists every PRD; each PRD's *Tech spec(s)* row links the spec; the roadmap *Tech spec* column gets the spec's console link for each named row.
5. **Change record, checks** (T-checks by hand plus the lints; the grounding lint needs real `owner/repo@sha` citations).
6. ⛔ **Stop for engineering and product review.** A divergence from the PRD that is *material* (changes a requirement, acceptance criterion, hard-constraint guarantee, boundary, or customer-visible behaviour) needs product approval before the spec is approved.

## Mode 3 — Record as-built drift

1. Gather the evidence (engineering spec revisions, release notes, code at a pinned SHA, tests, telemetry).
2. Record drift **inline** in the spec with dated markers (`AS BUILT (date, ticket)`, `PROPOSED, NOT BUILT (date)`, `RETAINED FOR THE RECORD`). Never rewrite the original design.
3. **Classify each item.** *Material* → mark the PRD requirement **divergent: pending product review** with a product-owner open decision, and ⛔ raise it with the product owner. *Non-material* → the spec marker is enough.
4. **Propagate in layer order** (sources → entities → operations → commercial → evidence → hubs/indexes → crosswalk). Use `measured` only with cited test/telemetry evidence. Surface conflicts as open questions rather than resolving them silently.
5. Update roadmap status columns from the delivery source of record, change record, checks. ⛔ Stop before commit.

## Reporting style

Lead with what changed and what needs the user's decision. Keep decisions and acceptance criteria individually addressable (by ID). Say plainly what was not done or not verified.
