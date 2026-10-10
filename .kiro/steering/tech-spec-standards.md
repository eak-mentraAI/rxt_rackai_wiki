---
inclusion: fileMatch
fileMatchPattern: '*Tech Spec*'
---

# Tech Spec Authoring Standards (portable across wiki repos)

> **Portable standard — shared across sibling wiki repos.** Companion to `prd-standards.md`, same rules of propagation: canonical in **RackAI Wiki**, pushed to siblings with `scripts/sync-prd-standard.sh`, never forked per repo. Nothing in the **normative** sections names a specific product.

## Purpose

A PRD says *what* and *why*. A tech spec says *how*: the engineering design a team builds from. This standard gives specs the shape engineering already writes (overview → architecture → resources/APIs → lifecycle → failure handling → NFRs → milestones → open questions) and adds the three things past specs lacked or invented ad hoc: **requirement traceability to the PRD**, **explicit divergences**, and **dated as-built markers**.

## What a Tech Spec Is (and Isn't) Here

- An **authored engineering design** — a Layer-5 (`05-wiki/`) artifact, peer of the PRD it implements.
- **Not** a knowledge-graph definition. Concepts it builds have canonical notes; the spec links them and must not redefine them (One-Concept Rule).
- **Not** an ingested source. A spec written *outside* the wiki and dropped into `reference/` is ingested as a `source` note in `06-sources/`. A spec *authored here* is `type: spec`.

## Location, Naming, Type

- **Location:** `05-wiki/`. **Filename:** `<Thing> Tech Spec.md`. **ID:** `spec-<slug>`.
- **Note type:** `spec` — a **first-class canonical note type** (ID prefix `spec-`). A repo adopting this standard MUST list `spec` in its operating-standards type list and its frontmatter lint.
- **Template:** author from `templates/tech-spec.md`.

## Required Frontmatter

Standard 12-field frontmatter, plus:
- `type: spec`
- `related:` MUST include the ID of every PRD it implements (when any) and the canonical concept note's ID. PRD ↔ spec is many-to-many: a spec may implement several PRDs, and a PRD's requirements may be split across several specs
- `parent:` the product/platform hub the spec belongs to
- `summary:` ≤ 120 characters (Fitness S-16)
- `confidence:` `assumed` for a design not yet built; never higher than the evidence for what is built

## The Minimum Viable Set

A spec is incomplete without:

1. **Document control** — version, status, author, reviewers, date, **based-on PRD**, **roadmap items**, Jira epic(s).
2. **Goals and non-goals** (§1.1–1.2), with non-goals pointing at where the excluded work lives.
3. **Requirements traceability** (§1.3) — every functional requirement of every PRD it implements mapped to spec sections and a milestone, or marked deferred, divergent, or covered by a named sibling spec. No silent drops. With no PRD, the spec's own `R-n` requirements go here.
4. **Deliberate divergences from the PRD** (§1.4) — "none" is valid; undeclared divergence is not.
5. **Relationship to other specs** (§1.6) — dependencies and any change to another spec's contract, called out as an exception.
6. **Architecture** with a Mermaid dependency map and data flow.
7. **Data model and API surface** for every new or changed resource/endpoint.
8. **Platform integration contract** (§7) — identity/authz, tenancy, metering/quotas, audit, monitoring, tenant-visible fields, billing. Every row answered.
9. **Failure handling** — fail-open vs fail-closed, delivery guarantees, how loss is detected.
10. **NFRs** with each target labelled *target* or *measured (source)*.
11. **Milestones** — each with Jira epic, a breakdown table (item → requirement → Jira → estimate → priority), an engineering checklist, and a release checklist.
12. **Open questions** — numbered, with owner and what each blocks.
13. **Codebase grounding** (§3, read-only) — the repos and commit SHAs read; existing patterns followed; what is extended; standards to enforce; dependencies and fork prevention; improvement and modularity opportunities. See the conversion procedure below.
14. **Roadmap link-back** — the roadmap items named in the document control table, each carrying this spec's knowledge-console link in the roadmap table's *Tech spec* column.

## PRD → Tech Spec Conversion Procedure

Converting a PRD into a spec follows these steps, in order. Step 2 cannot be skipped: a spec that does not show how it fits the existing code is not review-ready (T-09, enforced by lint).

1. **Scope from the PRD.** List the PRD's functional requirements (§1.3 skeleton) and the roadmap items it serves.
2. **Ground in the code (read-only).** Find the parts of the product's code repositories (backend, UI, docs; listed in the repo's operating standards) that the requirements touch. Record the commit SHA read. Answer, in §3:
   - How does the new code fit the existing patterns?
   - What, if anything, is extended, and is the extension additive or breaking?
   - Which standards must the implementation enforce?
   - How are shared dependencies managed so backend, UI, docs and environments don't fork or drift?
   - Where should the code be made more modular, now or as a follow-up, so future changes are easier?
3. **Design** (§4–§12) on top of what step 2 found: extend before adding, reuse before duplicating.
4. **Plan milestones** (§13), including docs and UI work in the repos that own them.
5. **Link back.** Put the spec's knowledge-console link in the roadmap table's *Tech spec* column for every roadmap item it names, and link the PRD ↔ spec both ways.

## Read-Only Code Rule (non-negotiable)

The product code repositories are **read-only from this wiki and from any agent working in it**:
- Never write to, commit in, branch, push to, or open/merge PRs or issues against them as part of wiki work. Proposed code changes live in the spec as design; engineering implements them in their own workflow.
- Read through local clones kept **outside** the wiki repo (the wiki is ingested wholesale; code must never land in it) with pushing disabled, or through read-only API calls. Never copy code into notes: cite `owner/repo@sha:path`, quote at most short signatures.
- Pin every reading to a commit SHA so the grounding can be re-checked later and drift detected.

## As-Built Discipline

Specs stay live after build. Drift is recorded **inline**, never by silently rewriting the design:

- `**AS BUILT (YYYY-MM-DD, TICKET):**` — what shipped where it differs from the text above it.
- `**PROPOSED, NOT BUILT (YYYY-MM-DD):**` — designed, not implemented.
- `**RETAINED FOR THE RECORD:**` — rejected or replaced design kept for the decision record.

Shipped beats planned: when an as-built marker contradicts a canonical note, update the canonical note (layer order) and record the change.

**Material divergence goes to product review.** If the as-built departure changes a PRD functional requirement, an acceptance criterion, a hard-constraint guarantee, a product boundary or customer-visible behaviour, it is *material*: flag it in the implementing PRD as **divergent: pending product review** with a product-owner open decision (see `prd-standards.md`). Documenting it here is necessary but not sufficient.

## Confidence Discipline

- Design text is intent: `assumed` until built. A spec must not read as shipped capability.
- Built behaviour can be `measured` when test results, benchmarks or production telemetry are cited for it; `derived` when the evidence is code or as-built annotations alone.
- Passing the T-checks makes a spec review-ready, not approved. Engineering and product approval is recorded in the document control table and a change record; an agent never records it on their behalf.
- **No invented numbers.** NFR targets are postures; a measured value cites its benchmark or telemetry source (Fitness S-13).
- Unresolved specifics are Open Questions, never invented requirements.

## Shape Discipline

- A spec is for the engineers building it: precise, complete on contracts, terse elsewhere. Long schemas, manifests and alert rules go in the appendix.
- Do not re-argue the PRD. If the *why* is wrong, fix the PRD.
- Keep internal cross-references (`FR-x`, `R-x`, `§n`, `Q-n`) consistent.

## Fitness

Subject to [[FITNESS_CHECKLIST]] plus the **tech-spec checks (T-01 … T-11)** in that file.

## Propagation

Canonical source: **RackAI Wiki** `.kiro/steering/tech-spec-standards.md` + `templates/tech-spec.md` + the T-checks (T-01 … T-10) in `08-change-control/FITNESS_CHECKLIST.md`. Push to siblings with `scripts/sync-prd-standard.sh` (the script carries both packs).
