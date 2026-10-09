---
id: chg-2026-10-08-intent-constraints-contract
type: change
status: draft
owner: product
domain: strategy
aliases: [intent and constraints change, operating envelope change, intent constraints contract]
related: [hub-battlegrounds, hub-roadmap, hub-minimum-operable-estate, ent-model-deployment-spec, idx-open-questions, chg-2026-10-07-onsite-strategy-framing, hub-ai-governance-assurance, ent-agent-identity]
source_docs: ["roadmap review feedback 2026-10-08 (intent + constraints)", "product owner response 2026-10-08"]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-wiki
summary: "Intent and constraints as the operating philosophy joining the two identity centres; loops wired into the roadmap."
---

# 2026-10-08 — Intent and Constraints Contract

## Trigger

Roadmap review feedback: the foundational abstraction is *intent + explicit and inherited constraints + context + authority → operational objective + admissible operating envelope + uncertainty*; "the user declares intent and constraints, and the rest follows." The product owner's direction: make this a clear, explicit part of the central identity, **not** a third co-equal pillar, and do not add it silently.

## Decision

Intent and constraints is the **operating philosophy that connects the two identity centres** (product owner framing, 2026-10-08): the sovereign boundary establishes what the enterprise controls; the operator takes responsibility for what happens within it. It is the contract between the two identity centres (Operator, Sovereign provider). It is not a new centre, pillar, engine or workstream. The Operator owes the declaration its *realization*; the Sovereign provider owes it the *envelope*; both must prove their part. It is also what crosses the harness boundary: the customer owns the declaration, RackAI owns realization and evidence.

## Objects Changed

- **[[Three Battlegrounds]]**: new subsection *The contract between the centres: intent and constraints*, with the centre-to-contract table, the four constraint sources (declared, inherited, discovered, derived) mapped to existing homes, hard / soft / adaptive constraints, the underspecification rule (infer, ask, escalate or stop, report infeasibility; never relax a hard constraint silently), and how the contract scores the strategic-choice test. One line added under the harness boundary; Operator Stack diagram edge labelled "declares intent + constraints". Aliases and related edges added; no IDs changed.
- **[[RackAI Roadmap]]** operating loop: the "governance envelope" node is widened to the **operating envelope** (declared + inherited + discovered constraints), with a customer-intent input; a note maps the loop to *intent → specification → plan → action → observation → correction*. No proofs, milestones, workstreams or P-items added.
- **[[Open Questions]]**: new entry — who has authority to turn an interpretation of incomplete intent into an executable (especially irreversible) commitment.

## Second pass (same day): wiring the loop into the roadmap

- **[[Three Battlegrounds]]**: the centres' promises are widened rather than a box added. Operator = delivering the intended outcome (decisions, adaptations, controls, evidence). Sovereign = the enterprise keeps control of its intent, authority, data, execution boundaries and evidence as implementations change. Section renamed to *The operating philosophy between the centres*. A five-behaviors table (intent to objective, objective to realization, continuous adaptation, governed autonomy, evidence and assurance) maps each behavior to existing components.
- **[[RackAI Roadmap]]**: a *Loop coverage today* table under the operating loop (each turn → delivery → status → P-item). **P-004** now owns the customer **declaration surface** (no customer-facing declaration object exists; quota is GPU-centric). **P-006** now carries the **incomplete-intent rule**, built from Metering M4 admission control, Action Controls and Agent Identity.
- **[[Minimum Operable Estate]]**: acceptance artifacts 1 and 4 now express the contract (scope written as declared intent and constraints; evidence report shows the envelope held). No sixth artifact.
- **[[Model Deployment Specification]]**: positioned as RackAI's realization record, to be derived from the customer declaration; a customer GPU pin becomes a hard placement constraint.
- Correction recorded: the "RackAI chooses by default; customers constrain when necessary" principle was already adopted 2026-10-06; the gap is the declaration surface and quota model, not the principle.

## Third pass: the AI Operating System loop

- **[[Three Battlegrounds]]**: the experience line is now canonical (*you tell us what you want, what matters, and what you won't compromise; we deliver the how, stay inside your boundaries, and prove what we accomplished*). A four-step **AI Operating System loop** table (tell us → we deliver the how → inside your boundaries → prove it) names it as how both promises become an experience, mapped to the centres, the roadmap operating loop and MOE-1. Aliases added: ai operating system, ai operating system loop, aios loop.
- **[[RackAI Roadmap]]**: the operating-loop note names this as the AI Operating System loop.

## Fourth pass: Concierge Engineer and delivery-sheet proposals

- **[[RackAI Roadmap]]**: new **P-008 Concierge Engineer** (conversational declaration surface; first consumer of the P-006 control envelope; delegated not inherited authority; public APIs only; only "RackAI can't yet" becomes a product signal, content-free; v0 Answer → v1 Act with confirmation → v2 Governed autonomy). Added to the proposals table (D3) and the loop-coverage table.
- **Delivery plan (adopted, same day)**: the product owner adopted the loop changes directly into the delivery CSVs, keeping their shape and inventing no owners, Jira IDs, priorities, effort or dates (a short-lived proposals file and check script were removed).
  - `rackai-2026-roadmap.csv`: Metering M3 (quotas in constraint terms), Metering M4 (explicit infeasibility), Auditing M3 (envelope-held evidence) task text widened; IAC M4 dependency notes P-006 authority (still Won't Do); AI Performance Benchmarks depends on ratified SLOs; accelerator row renamed; GPU node access Won't Do; Workload Profiles UX → M2 Feature *Workload declaration (intent + constraints) & profiles UX*; Concierge Engineer v0/v1/v2 added (Not Started, TBD).
  - `rackai-m2.csv`: accelerator rename (row + priority list), GPU node access Won't Do, Concierge Engineer v0/v1/v2 added with no man-weeks or priority.
  - `action-tracker.csv`: four decisions (SLO thresholds, authority under incomplete intent, declare vs. choose, Concierge model placement and liability), no owner.
  - The CSVs now lead the xlsx; [[RackAI Roadmap (Delivery Plan)]] says so.

## Fifth pass: review findings adopted

A review of the 15-change package was accepted with two adjustments (no duplicate maturity ladder; decision logic assigned to the existing orchestrator, not a new box).

- **Delivery CSVs**: the Workload declaration dependency no longer uses the old "Accelerator selection" name (now RACKAI-336 telemetry, with automated selection marked future, P-005). Concierge v1 no longer applies quota changes; it drafts them for an authorized approver after a policy check (2026 Roadmap and RackAI M2 sheets).
- **[[RackAI Roadmap]]**: P-005 framed as the first increment of the operator's decision capability, with step 2 split into *determining* (P-005) and *improving* (P-007) the how, owned by the orchestrator; v1 acceptance test (evidence-backed, explained recommendation with stated assumptions and uncertainty). P-008 gains the quota gate and entry/exit criteria per phase; dates follow agreement on criteria. The governing-principle ladder now states how step 2 walks it.
- **[[Minimum Operable Estate]]**: minimum evidence contract for artifact 4 (performance, policy decisions, actions, outcomes).
- **[[Three Battlegrounds]]**: the outcome boundary (RackAI owns the realization outcome, not the business result of the customer's application) and step-2 maturity line.

## Sixth pass: reconciled into the complete roadmap

The loop changes had been applied to the wrong file: `reference/rackai-roadmap-csv/` (raw 2026-09-21 xlsx export) instead of the PM-annotated roadmap `05-wiki/RackaI Roadmap 10062026.csv` (14 columns: Track, Proof, Capability Stage, Disposition, PM discussion; the source of [[Milestone Release Map]]), which was the most complete version and already carried the two 2026-10-06 decisions. Reconciled:

- **the PM-annotated roadmap CSV** (58 → 64 rows; untouched rows byte-identical). New rows: *Workload declaration (intent + constraints)* (T1.S2, Decision Required; absorbs the declare-vs-choose decision); *Per-profile SLO thresholds* (T3.S1, Decision Required); *Authority under incomplete intent* (T2.S3, Decision Required); *Concierge Engineer* CE.S0 / CE.S1 / CE.S2 (Cross-track, Gap; agent model placement and liability folded into CE.S1). Annotated with *Loop (2026-10-08)*: AI Performance Benchmarks, Customer observability, Supply-abstraction interface, Empirical Map v1 (acceptance test), IAC M3 + Auditing, Metering M4 (constraint quotas + explicit infeasibility), IAC M4, MOE-1 (evidence contract, outcome boundary, human-operated step 2). No owners, Jira or dates invented.
- **`reference/rackai-roadmap-csv/`** restored to the faithful xlsx export; [[RackAI Roadmap (Delivery Plan)]] says roadmap changes belong in the PM-annotated CSV.
- **[[Milestone Release Map]]**: Concierge Engineer stages CE.S0–S2 (a RackAI product surface spanning tracks); workload declaration added to T1.S2.
- **[[RackAI Roadmap]]**: loop-coverage note and P-008 point to the PM-annotated CSV.
- The cause of the drift (two roadmap CSVs with no stated precedence) is tabled.

## Seventh pass: review clarifications, reference guard, rename

- **Canonical roadmap table renamed** `05-wiki/RackaI Roadmap 10062026.csv` → **`05-wiki/RackAI Roadmap.csv`** (a dated name read as a snapshot, one cause of the drift). Current notes updated; earlier change records keep the old name as history.
- **Review clarifications** (roadmap now 66 rows): *Metering M3* row added (QuotaPolicy, prerequisite to M4 enforcement; facts from the 2026-09-21 delivery export, no owner/dates carried); Empirical Map v1 requires a **learning event** (constraints, alternatives, chosen realization, predicted vs actual outcome, delta; v1 passes only when a later decision uses the records and beats the static baseline), mirrored in P-005; *MOE-1 evidence report* row added as a deliverable with an accountable owner still to be named (also in [[Minimum Operable Estate]]); Concierge CE.S2 explicitly **not** a prerequisite for MOE-1 (MOE-1 is human-operated, v0–v1 at most), mirrored in P-008.
- **Reference guard**: Reference-Is-Intake Rule in `agent-behavior.md`; "corpus beats intake" in the truth hierarchy; `reference/README.md` and the delivery-plan source note no longer call the export authoritative; a "which file is current" callout in [[RackAI Roadmap]]; the pre-commit hook blocks modifying or deleting existing `reference/` files (override `ALLOW_REFERENCE_EDIT=1`).

## Eighth pass: Solution Marketplace in the roadmap table

The marketplace was in the roadmap narrative and the [[Milestone Release Map]] (MK.S0–S5) but had no rows in the roadmap table. Added eight Cross-track / Proof 4 rows after the Concierge stages (74 rows total): MK.S0 (Experiment), MK.S1–S4 (Gap), MK.S5 (Backlog), and two Decision Required rows from the [[Solution Marketplace]] open questions (sovereign-tenant certification bar, gating MK.S2; commercial model, gating MK.S4). No owners, Jira or dates. Kept as a Proof-4 watch item rather than a P-item.

## Vocabulary (for engineering, kept out of the identity note)

| Review / AIOS v0.3–v0.4 term | RackAI corpus home |
|---|---|
| Objective constraints | Declared constraints (customer business logic) |
| Governance Policy / Governance Engine | Inherited constraints; [[AI Governance and Assurance]], minimum control envelope (D3 / P-006) |
| Runtime constraints | Discovered constraints; [[Empirical Map]], operating loop |
| Orchestrator (planning, optimization, replanning) | Decide / place stages inside the [[Governed Harness]] |
| Harness (binds a Capability to an implementation) | [[Governed Harness]] |
| Assurance Policy / Assurance Engine | Assurance half of [[AI Governance and Assurance]]; compliance envelope |
| Authority, delegation | [[Agent Identity]] |

"Control envelope" (D3) and "compliance envelope" keep their meanings: they are the inherited part of the operating envelope and its evidence, respectively.

## Not Changed (deliberately)

No new hub, entity, pillar or engine. The two-centre identity, the strategic-choice test, the four proofs and the harness boundary all stand; the contract explains how they connect.

## Confidence

`assumed`: a product framing from the roadmap review, not yet ratified by leadership or tested with customers. The AIOS v0.3 architecture it draws on is not in this corpus.
