---
id: chg-2026-09-28-roadmap-reviewer-feedback
type: change
status: draft
owner: product
domain: governance
aliases: [roadmap reviewer feedback 2026-09-28, pm roadmap review incorporation]
related: [hub-roadmap, hub-battlegrounds, ent-empirical-map, idx-openrouter-integration-plan, hub-openrouter, hub-ai-governance-assurance, wf-monitoring, idx-unit-economics]
source_docs: ["PM/leadership roadmap review 2026-09-28", "00-hub/RackAI Roadmap.md"]
confidence: validated
last_reviewed: 2026-09-28
parent: hub-wiki
summary: "Incorporated PM/leadership roadmap-review feedback into the canonical RackAI Roadmap: operating loop, cost intelligence, placement policy, Proof 2/3/4 reframes, OpenRouter distribution, observability split."
---

# 2026-09-28 — Roadmap Reviewer Feedback Incorporation

## Trigger

PM/leadership review of the [[RackAI Roadmap]] (2026-09-28). The review largely re-derived the existing four-proof structure (a positive signal the doc is sound), but surfaced several genuinely missing items and pushed for emphasis changes. Feedback was folded directly into the canonical roadmap (adopted framing edits, not a new "Proposed" block), since it concerns how the roadmap tells its story rather than defining new entities.

A verification pass before editing (`grep`) confirmed which items were genuinely absent from the corpus vs. already present.

## Objects Changed

- **Added (sections in [[RackAI Roadmap]]):**
  - *The Operating Loop* — explicit `meter → characterize → accumulate evidence → decide → route/place → observe → feed back` Mermaid diagram + a loop-stage → proof → canonical-home mapping table. This is the reviewer's single biggest ask ("show the loop, not scattered pieces").
  - *The Enterprise Control Plane* (Proof 3) — a control-by-control table (policy/guardrails, workload identity, model provenance, isolation, action authorization, auditability, compliance evidence, human approval, governed execution) linking existing canonical homes; plus a certification-vs-product-controls callout.
  - Proof 4 groupings — *Fleet Operations*, *Model Lifecycle*, *Multi-estate Operations* with PM notes.
  - *Cross-Cutting Surfaces* — OpenRouter as External Distribution & Validation (incl. BYOM, Inference-aaS, direct-IaaS open question); the customer-observability vs operator-intelligence split; the fine-tuning "host the artifact, not the toolchain" stance; and CODB (Object Store, CI).
- **Changed:**
  - Cost model elevated from a gap aside to a first-class *Unit Economics / Cost Intelligence* workstream item (Proof 1 milestone + items tables), enumerating GPU-hour cost, power/colo/network allocation, depreciation, storage, cost/token, utilization-adjusted cost, margin. Notes the metered-usage-≠-monetary-cost gap and the undercloud/finance data dependency.
  - "Supply abstraction" reframed as *Workload Placement Policy* in Proof 1 (with the unresolved product decision: how much GPU-level choice the customer keeps vs. RackAI selecting from workload + constraints; GPU-centric quota tension). The underlying interface name is preserved in P-004/D2/workstream; a naming bridge added to P-004.
  - Proof 2 milestone table restructured into *strategic flywheel* vs *techniques*, governed by one test ("does this improve a workload-placement decision?"). Techniques (speculative decoding, Refrag, AMD AIM, DPO, SFT/LoRA, semantic router) carry PM dispositions (reprioritize / weigh cost / follow P-001).
  - P-001 extended with the checkpointing/resume "moving external" signal reinforcing the partner-delivery direction.
  - *Open Roadmap Gaps* list extended with 4 new items (semantic router; OpenRouter BYOM/IaaS + direct-IaaS; customer-observability surface; CODB object store + CI).
  - Frontmatter `last_reviewed` → 2026-09-28; added the review to `source_docs`.

- **Deprecated:** none.

## Edges

- **Added (links from [[RackAI Roadmap]]):** [[Unit Economics Model]], [[Traffic Class]] (workload characterization), [[Monitoring & Observability]], [[Capacity Pool]], [[Model Radar]], [[Action Controls]], [[Perimeter Information-Flow Control]], [[Agent Identity]], [[Audit]], [[Canary & Rollback]], [[GPU Reallocation]], [[Capacity Pool Model]] — all pre-existing canonical homes (no new concepts defined; One-Concept Rule preserved).
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| hub-roadmap (overall) | derived | derived | Framing/emphasis edits only; no capability upgraded to shipped. New items labelled `gap`/`open question`/`not captured in delivery`. |

No performance numbers were introduced. All new items are gaps, open questions, or reframes; none asserts a benchmarked/telemetry value.

## Open Questions Created

| Question | Affected Docs |
|----------|---------------|
| Workload Placement Policy: does RackAI select everything beyond workload+constraints, or does the customer keep GPU-level control? (GPU-centric quota tension) | [[RackAI Roadmap]], [[Capacity Pool]], P-004 |
| Should Inference-as-a-Service be a direct `rackai.rax.io` feature, or stay an OpenRouter-only proving surface? | [[RackAI Roadmap]], [[OpenRouter Initiative]] |
| Is checkpointing/resume formally out of scope (moving external)? | [[RackAI Roadmap]] P-001 |
| CODB: Object Store — block storage allocated to the product vs. Rackspace Managed Object Store? | [[RackAI Roadmap]] |
| CI pipeline missing for model and FT images — who owns it? | [[RackAI Roadmap]] |
| Semantic router — is it needed? (gated on Empirical Map evidence) | [[RackAI Roadmap]], [[Empirical Map]] |

## Downstream Propagation Check

- **Dependent notes updated?** No dependent note required changes: all edits either reframe roadmap prose or link to existing canonical homes. No canonical definition was altered, so [[Empirical Map]], [[Unit Economics Model]], [[Monitoring & Observability]], [[AI Governance and Assurance]], etc. did not need edits.
- **Canonical IDs/aliases preserved?** Yes — `hub-roadmap` and all linked IDs unchanged.
- **Formulas/metrics/coefficients/scorecards affected?** None — no numeric or formula content changed.
- **Source-to-Concept Crosswalk?** No new source concept extracted; the review is logged as a `source_docs` entry and in this packet. No crosswalk row required.

## Fitness / Consistency Result

- Structural checks: **Pass** — all 18 wikilink targets introduced verified to resolve to existing files (`find` sweep, 0 missing).
- Consistency pass: **Pass** — "Workload Placement Policy" vs "supply-abstraction interface" reconciled with an explicit naming bridge (policy = product lens, interface = mechanism); no duplicated concepts; layer purity held (hub links down, does not redefine).
- Confidence propagation: **Pass** — nothing upgraded to shipped; new items are `gap`/`open`.
- Regressions: none identified.

## See Also

- [[RackAI Roadmap]]
- [[Wiki Hub]]
- [[CHANGE_PACKET]]

---

# 2026-09-28 (addendum) — Sequencing Logic + Fine-tuning Reframe

## Trigger

Follow-up in the same review: (1) fine-tuning should be framed as a **partner-evaluation / integration** problem, with RackAI owning the **model-serving function** rather than the training toolchain; (2) a deeper concern — **in the absence of demand signals, the roadmap's ordering looks arbitrary** — needs a stated hypothesis for *why this order, and why we're doing things in this order*.

## Objects Changed

- **Added — new top-level section in [[RackAI Roadmap]]:** *Sequencing Logic — why this order, when we have no demand signal.* States the ordering hypothesis (*sequence to buy the most information and preserve the most optionality at the lowest irreversible cost, not to satisfy an absent forecast*), the three ordering principles (irreversibility/cost-of-delay, optionality, evidence-generation), how each proof's position is justified by them, and the connection to kill criteria K1–K3 as the ordering rationale. Includes a one-line version for the "why this order?" exec question. Placed after *The Operating Loop*, before *How to Read This Roadmap*.
- **Changed — P-001 (fine-tuning) reframed:** disposition is now *evaluate partner(s) to deliver fine-tuning (Uniphore leading candidate), RackAI owns the integration / model-serving function (host, serve, operate the artifact), not the training toolchain.* Updated the three-way split table (delivery row → "evaluate partner(s)"; operations row → "integration & serving — the core RackAI job"), the strategic-decision line, the D4 executive-decision cell, the exec-summary D4 bullet, and the P-001 proposal-table one-liner. Framed as a Principle-2 (optionality) move in the new sequencing logic.

## Edges

- **Added:** [[RackAI Roadmap]] → [[GPU Capacity Demand Rationale]] (the note that already acknowledges no measured demand exists — grounds the sequencing section); [[RackAI Roadmap]] → [[Model Deployment]] (the serving surface RackAI retains in the fine-tuning split); two internal anchor links (Sequencing Logic ↔ Kill Criteria, P-001 ↔ Sequencing Logic).
- **Removed:** none.

## Confidence Changes

None. The sequencing logic is a reasoning/framing layer (`derived`, consistent with the hub); no capability upgraded; no numbers introduced.

## Open Questions Created

| Question | Affected Docs |
|----------|---------------|
| Fine-tuning delivery partner evaluation: which partner(s) beyond Uniphore are in scope, and what are the evaluation criteria? | [[RackAI Roadmap]] P-001, [[Load-Bearing Bets]] |
| Does the integration/serving boundary for a partner-delivered fine-tuning artifact need its own interface spec (handoff contract)? | [[RackAI Roadmap]] P-001, [[Model Deployment]] |

## Fitness / Consistency Result

- Structural checks: **Pass** — [[Model Deployment]] and [[GPU Capacity Demand Rationale]] verified to exist; both internal heading anchors verified to match exactly.
- Consistency pass: **Pass** — fine-tuning terminology ("evaluate partner(s) / Uniphore leading / integration & serving") reconciled across all six touchpoints; no competing definition introduced; sequencing logic does not contradict the existing "cheap now / expensive later" and "do not automate before we operate" statements — it names the principle they were already applying.
- Regressions: none.
