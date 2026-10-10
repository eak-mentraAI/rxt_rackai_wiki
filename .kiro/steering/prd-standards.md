---
inclusion: fileMatch
fileMatchPattern: '*PRD*'
---

# PRD Authoring Standards (portable across wiki repos)

> **Portable standard — shared across sibling wiki repos.** This file is **not RackAI-specific**. The same copy is intended to live in every knowledge-wiki that shares the `00-hub … 08-change-control` + `.kiro` + `templates` structure. Current target repos:
> - **RackAI Wiki** (canonical source of this standard)
> - **AIOS Wiki** (`github.com/eak-mentraAI/aios-wiki`)
> - **VCFRaxWiki** (`github.com/eak-mentraAI/RXT-Cloud-Wiki`)
>
> When you change this standard, change it in the canonical source (RackAI Wiki) and re-propagate with `scripts/sync-prd-standard.sh`. Do not fork it per-repo. Nothing in the **normative** sections below names a specific product — keep it that way so the file is drop-in identical everywhere.

## Purpose

PRDs are a recurring deliverable in these repos. This standard gives every PRD a **consistent shape** and a **minimum viable set** of questions it must answer, so a reader (and an engineering/architecture audience) can trust that any PRD here is complete and honestly scoped — regardless of which repo or product it covers.

## What a PRD Is (and Isn't) Here

- A PRD is an **authored product specification** — a Layer-5 (`05-wiki/`) artifact.
- It is **not** a knowledge-graph definition. The concept it specs has a **canonical note** elsewhere (an `entity`/`hub`); the PRD **projects from** that note and **must not redefine it** (One-Concept Rule).
- If the PRD and the canonical note disagree, the **canonical note wins** and the PRD is stale.
- **Canonical notes are created when a concept must be shared across capabilities, not as a documentation prerequisite.** If a concept the PRD introduces is consumed by other PRDs or capabilities, write a thin canonical note in the same change as the PRD. A concept only this PRD uses lives in the PRD until a second consumer appears; then it moves to a canonical note.

## Location, Naming, Type

- **Location:** `05-wiki/`. (Not `06-sources/` — that is for ingested *external* docs. A PRD authored here is not a source.)
- **Filename:** `<Thing> PRD.md`.
- **ID:** `prd-<slug>`.
- **Note type:** `prd` — a **first-class canonical note type** across this repo family and in knowledge-platform ingestion (ID prefix `prd-`). A repo adopting this standard MUST list `prd` in its operating-standards type list and in its frontmatter lint (if it has one). Do not use `index` as a stand-in.
- **Template:** author from `templates/prd.md` (v2). PRDs written on template v1 remain valid; adopt v2 numbering on their next substantive revision.

## Required Frontmatter

Standard note frontmatter applies, plus:
- `type: prd`
- `parent:` the canonical concept note's hub (usually `hub-product`)
- `related:` MUST include the canonical concept note's ID
- `summary:` ≤ 120 characters (hard limit — over-length summaries break ingestion; see Fitness S-16)
- `confidence:` honest per the discipline below

## The Minimum Viable Set (a PRD is incomplete without all ten)

Every PRD MUST answer these. Section numbers follow `templates/prd.md` (template v2, 2026-10-10).

1. **Why it exists** (§2) — problem/opportunity. If evidence is thin, state it as an explicit **hypothesis**, not a fact.
2. **Who it's for** (§5) — users/personas. If two-sided, name both sides and what each needs.
3. **What's in and explicitly out** (§4) — **goals and non-goals.** The boundary (what belongs to another team/product/offer) is as important as the scope.
4. **What it must do** (§8) — functional requirements, **testable**, prioritized **MUST / SHOULD / MAY**.
5. **What must be true non-functionally** (§9) — security, isolation, compliance, performance, scale.
6. **How it becomes real** (§14) — scope & phasing. Prefer **prototype-first** sequencing where the shape is uncertain (build one real instance → extract the general contract → productize), consistent with the "operate before automate" principle.
7. **How we'll know it worked** (§15) — **acceptance criteria** (binary, testable, each traced to requirements) and success metrics with **honest baselines** (state "none today" when true). Prefer a small **ladder** over a single Goodhart-fragile number.
8. **How we'll know to stop** (§18) — a **kill / falsification criterion** (its own section). This is the item most PRDs skip; it is required here. State what evidence would show the bet is wrong.
9. **What's unresolved** (§19) — **open decisions, each with an owner** and what it blocks. Keep these distinct from requirements.
10. **What it is / depends on** (§16, §6) — dependencies **and a link to the canonical concept note.**

## Standard Sections Beyond the Minimum Set

Template v2 also carries the sections engineering already expects from a PRD in this repo family. They are **standard**, not optional decoration: answer each, or write "n/a — reason".

- **Document control table** — version, status, owner, reviewers, date, **roadmap items**, and the linked tech spec(s).
- **Product Principles (§3)** — the few rules that settle trade-offs the requirements don't.
- **Core Entities (§6)** — the domain objects acted on, each *linked* to its canonical note (never redefined).
- **Platform Integration (§10)** — what the feature needs from and gives to identity/access, tenancy, metering/quotas/billing, audit, and monitoring. One row each, even if "none".
- **Loop Role & Cross-PRD Interfaces (§11)** — which step of the operating loop the PRD owns, which promise it serves, and the interfaces it provides to or consumes from other PRDs. Each shared interface is defined in exactly one place.
- **Failure Handling (§12)** — what fails closed vs open and what is guaranteed never to happen.
- **Data Retention & Compliance (§13)** — what data it holds, for how long, under which obligation.

## Roadmap Traceability

Every PRD names, in its document control table, the roadmap item(s) it is written for, using the milestone names exactly as they appear in the repo's canonical roadmap table. One PRD may cover several roadmap items when they share users, entities and a release boundary; it must still call each one out (in §14, mapping items to phases). A roadmap item that needs a PRD and has none is a planning gap, not an omission to paper over.

The link is two-way. The roadmap table carries a **PRD** column (and a **Tech spec** column) holding the knowledge-console link of each covering note (`<console>/browse/<corpus>/<note-id>`, several separated by `; `). A PRD is not review-ready until every roadmap item it names links back to it (Fitness P-09; enforced by lint where the repo has one).

## PRD → Tech Spec

A PRD says *what* and *why*; the engineering design (*how*) lives in tech specs (`type: spec`, see `tech-spec-standards.md`) that link back to the PRD and trace every functional requirement. The relationship is **many-to-many**: a PRD may be implemented by several specs (or by extending an existing engineering spec), and one spec may implement several related PRDs. One-to-one is not required; traceability in both directions is. A PRD that starts specifying CRDs, schemas or endpoints has crossed into the spec.

## Product Approval Is Separate from Documentation Checks

Passing lint and the fitness checks makes a PRD **review-ready**. It does not make it **approved**. Product approval is a recorded decision by the product owner on the PRD's product decisions, scope and acceptance criteria:

- The PRD lists the **product decisions it proposes** (§20) and its **acceptance criteria** (§15) explicitly, so a reviewer can accept, change or reject each one rather than the document as a whole.
- Approval is recorded in the document control table (*Product approval*: who, date, version) and in a change record. Only then may `status` move from `draft` to `reviewed`. `validated` is reserved for a contract that has been delivered and verified against its acceptance criteria.
- An agent may draft, check and propose. It never records approval on the product owner's behalf.

## As-Built Divergence Needs Product Review

When what is built departs **materially** from an approved PRD, it goes back to product review; recording it in the spec is not enough. *Material* means it changes a functional requirement, an acceptance criterion, a hard-constraint guarantee, a product boundary, or customer-visible behaviour. Until the product owner rules (accept and amend the PRD, or require a fix), the PRD marks the affected requirement **divergent: pending product review** and carries a §19 open decision owned by the product owner. Non-material drift (internal mechanism, naming, sequencing) is recorded in the spec's as-built markers only.

## Confidence Discipline (non-negotiable)

- A PRD for an **unbuilt / proposed** initiative MUST carry `confidence: assumed` and a **status banner** stating it is a *draft PRD for a proposed initiative* — requirements are **intent, not commitments**.
- A PRD **MUST NOT read as a committed build** or assert a capability that is not built. Unbuilt things are `assumed`; use the weakest truthful confidence.
- **No invented numbers.** Success-metric targets are *postures to instrument*, not measured values. Any real number must trace to a benchmark/telemetry source (Fitness S-13).
- **Measured is allowed when earned.** A statement about what exists may carry `measured` (or `validated`) when actual test, benchmark or production-telemetry evidence supports it and is cited. Use the weakest truthful state, not the weakest possible one.
- Unresolved specifics are **Open Decisions**, never invented requirements.

## Shape Discipline

- Lead with a **scope line** that states what the PRD covers and — critically — what it does **not** (the ownership boundary).
- Requirements are **numbered and testable** (`FR-n`, `NFR`); open decisions are numbered (`D-n`) with owners.
- Renumbering requirements is fine, but keep internal cross-references consistent (no stale `FR-x` pointers).
- Keep it to the minimum set plus what the specific product genuinely needs. **Do not over-specify** — a PRD that makes premature architecture decisions has stopped being a PRD. Stop polishing once it can drive the engineering/architecture discovery conversation.

## Fitness

A PRD is subject to the standard [[FITNESS_CHECKLIST]] plus the **PRD-specific checks (P-01 … P-11)** in that file. It must pass them before it is considered review-ready.

## Propagation

Canonical source: **RackAI Wiki** `.kiro/steering/prd-standards.md` + `templates/prd.md` + the P-checks in `08-change-control/FITNESS_CHECKLIST.md` (and the companion tech-spec pack: `tech-spec-standards.md`, `templates/tech-spec.md`, T-checks). To push the current version to the sibling repos, run `scripts/sync-prd-standard.sh` (see that script for the repo list). Re-run after any change to this standard.
