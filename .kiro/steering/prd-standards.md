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

## Location, Naming, Type

- **Location:** `05-wiki/`. (Not `06-sources/` — that is for ingested *external* docs. A PRD authored here is not a source.)
- **Filename:** `<Thing> PRD.md`.
- **ID:** `prd-<slug>`.
- **Note type:** `prd` — a **first-class canonical note type** across this repo family and in knowledge-platform ingestion (ID prefix `prd-`). A repo adopting this standard MUST list `prd` in its operating-standards type list and in its frontmatter lint (if it has one). Do not use `index` as a stand-in.
- **Template:** author from `templates/prd.md`.

## Required Frontmatter

Standard note frontmatter applies, plus:
- `type: prd`
- `parent:` the canonical concept note's hub (usually `hub-product`)
- `related:` MUST include the canonical concept note's ID
- `summary:` ≤ 120 characters (hard limit — over-length summaries break ingestion; see Fitness S-16)
- `confidence:` honest per the discipline below

## The Minimum Viable Set (a PRD is incomplete without all ten)

Every PRD MUST answer these. Section numbers follow `templates/prd.md`.

1. **Why it exists** — problem/opportunity. If evidence is thin, state it as an explicit **hypothesis**, not a fact.
2. **Who it's for** — users/personas. If two-sided, name both sides and what each needs.
3. **What's in and explicitly out** — **goals and non-goals.** The boundary (what belongs to another team/product/offer) is as important as the scope.
4. **What it must do** — functional requirements, **testable**, prioritized **MUST / SHOULD / MAY**.
5. **What must be true non-functionally** — security, isolation, compliance, performance, scale.
6. **How it becomes real** — scope & phasing. Prefer **prototype-first** sequencing where the shape is uncertain (build one real instance → extract the general contract → productize), consistent with the "operate before automate" principle.
7. **How we'll know it worked** — success metrics with **honest baselines** (state "none today" when true). Prefer a small **ladder** over a single Goodhart-fragile number.
8. **How we'll know to stop** — a **kill / falsification criterion** (its own section, §12 in the template). This is the item most PRDs skip; it is required here. State what evidence would show the bet is wrong.
9. **What's unresolved** — **open decisions, each with an owner** and what it blocks. Keep these distinct from requirements.
10. **What it is / depends on** — dependencies **and a link to the canonical concept note.**

## Confidence Discipline (non-negotiable)

- A PRD for an **unbuilt / proposed** initiative MUST carry `confidence: assumed` and a **status banner** stating it is a *draft PRD for a proposed initiative* — requirements are **intent, not commitments**.
- A PRD **MUST NOT read as a committed build** or assert a capability that is not built. Unbuilt things are `assumed`; use the weakest truthful confidence.
- **No invented numbers.** Success-metric targets are *postures to instrument*, not measured values. Any real number must trace to a benchmark/telemetry source (Fitness S-13).
- Unresolved specifics are **Open Decisions**, never invented requirements.

## Shape Discipline

- Lead with a **scope line** that states what the PRD covers and — critically — what it does **not** (the ownership boundary).
- Requirements are **numbered and testable** (`FR-n`, `NFR`); open decisions are numbered (`D-n`) with owners.
- Renumbering requirements is fine, but keep internal cross-references consistent (no stale `FR-x` pointers).
- Keep it to the minimum set plus what the specific product genuinely needs. **Do not over-specify** — a PRD that makes premature architecture decisions has stopped being a PRD. Stop polishing once it can drive the engineering/architecture discovery conversation.

## Fitness

A PRD is subject to the standard [[FITNESS_CHECKLIST]] plus the **PRD-specific checks (P-01 … P-08)** in that file. It must pass them before it is considered review-ready.

## Propagation

Canonical source: **RackAI Wiki** `.kiro/steering/prd-standards.md` + `templates/prd.md` + the P-checks in `08-change-control/FITNESS_CHECKLIST.md`. To push the current version to the sibling repos, run `scripts/sync-prd-standard.sh` (see that script for the repo list). Re-run after any change to this standard.
