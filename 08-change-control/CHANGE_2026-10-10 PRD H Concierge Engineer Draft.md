---
id: chg-2026-10-10-prd-h-concierge-engineer
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd h draft, concierge engineer prd draft, concierge engineer tech spec draft]
related: [prd-concierge-engineer, spec-concierge-engineer, ent-agent-identity, pol-action-controls, ent-governed-harness, ent-workload-declaration, idx-capability-gap-register, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["PM direction 2026-10-10: draft every remaining PRD and tech spec to the point of product and engineering review", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD H (Concierge Engineer) and its tech spec, both v0.1, from a read-only code survey; nothing approved."
---

# CHANGE 2026-10-10 — PRD H Concierge Engineer Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted up to the point where product and engineering approval are needed, and reviewed as one batch. PRD H is wave 3. Mode 1, then Mode 2, of the PRD → spec workflow. The Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Concierge Engineer PRD]] (`prd-concierge-engineer`, v0.1 draft, `confidence: assumed`). It covers *Concierge Engineer v0 (Answer)* (Phase 1), *Concierge Engineer v1 (Act with confirmation)* (Phase 2) and *Concierge Engineer v2 (Governed autonomy)* (later, named only).
  - H is a **consumer only**: public APIs, through the front door, as the user; v1 acts only through A's declaration API under C's delegated identity and confirmation gate.
  - The Concierge Engineer is defined inside the PRD (§6). No canonical note: only H uses the concept.
  - 22 FRs (v0: FR-1 to FR-11; v1: FR-12 to FR-21; v2: FR-22), 16 ACs, 12 proposed decisions (PD-1 to PD-12), 9 open decisions (D-1 to D-9).
- **New spec:** [[Concierge Engineer Tech Spec]] (`spec-concierge-engineer`, v0.1 draft). A new `rackai-concierge` service with a tool registry over public endpoints, a read-only client in v0, citations and a grounding check, a four-way "can't" classifier, a content-free gap-signal table, an `agent` audit category and `agent-action` evidence records in the D-0 envelope. v1 consumes C's delegation and confirmation interfaces and A's declaration API. Three milestones (M1 to M3). The spec names the v0 and v1 roadmap rows only; v2 is not designed.
- **Divergences:** DV-1 (v0 agent attribution in the Concierge's own audit only, non-material), DV-2 (incident answers for non-admins from status only, non-material while D-4 is open), DV-3 (quota drafts have no object to target until Metering M3, **candidate material**).

## Grounding Findings (read-only)

- The only chat in the product is a model playground (`rackaictl chat`, AI Studio); no assistant or tool-using code exists.
- Usage, observability and audit read APIs exist behind ext_authz. Telemetry endpoints return empty series until Monitoring emits them; the quota read is a TODO.
- Audit reads need `rolebindings:manage`, which only the admin role holds.
- These read APIs and `permissioncheck` are not in `openapi-external.yaml`.
- No delegated or on-behalf-of identity exists; API keys carry their own role. RBAC enforcement is off by default.

## Not Changed

- No other file was edited. Roadmap links, the coverage-plan status and canonical back-links are proposed to the orchestrator.
- No code repo was written to.

## Open Items

- PRD D-1 to D-9; spec Q-1 to Q-11. D-1 (agent model location for Level 1), D-2 (liability) and C's interfaces (Q-2, Q-3) gate v1.
- Product approval not given. Engineering approval not given.

## Reconciliation

- Reconciliation pass 2026-10-10: aligned with C and D. Spec Q-2/Q-3 resolved by C's answer: delegated identity is an `AuthorityGrant` (delegate kind `Agent`) carried as an `act` claim, and confirmation is an `ActionAuthorization` `agent.step.confirm` minted by the user. Both are C Phase 2 (C spec Q-13). Spec §1.3, §1.6, §4.6, §6.2, §7 and M3 updated, and PRD FR-14, FR-15, §14 and §16 now name the C Phase-2 dependency and sequencing. The spec §4.8 evidence record is aligned to the final D-0: recordId formula, `sourceId`, `claimVersion`, `audience`, `actor.onBehalfOf`, `derived` basis, and a daily `coverage` record. Q-8 resolved: the service links `pkg/evidence.EnqueueTx` in the same transaction as its audit row. New Q-12 (evidence-outbox database role, with D). DV-3 unchanged.

## PO review disposition 2026-10-10

The product owner's ruling was *conditional acceptance, not formal artifact approval*. Product approval is still not given, the status stays `draft`, and both the PRD and the spec are now v0.2. Rulings applied:
- **PD-1 to PD-12:** each is *proposed, approved in principle*, with the sovereignty gate and the C Phase 2 dependency enforced as release gates.
- **PD-2:** FR-7 now says read-only is enforced outside the model and never by prompting. AC-5 now includes prompt-induced write attempts.
- **PD-5:** v1 acts only through A's public declaration API. Recorded as approved in principle.
- **PD-8:** the agent's inference, conversation history, tool results and temporary context stay inside the customer's boundary. A platform-hosted Level 0 model is not acceptable for Level 1 tenants, and the Concierge is *not offered* to such a tenant until suitable in-boundary execution exists. Added §9 release gate, §14 blocker and AC-18. Spec: §4.4, and `ConciergeSettings.llmDeployment` with `NotOffered` status.
- **DV-3 (revise):** the quota output is now a non-executable quota-request draft with no submit or apply path, and it never implies a change. Changed PRD FR-17 and AC-13, and spec §1.4 and §4.6.
- **Cost correction:** usage, estimated charges (only from D's customer charge view) and actual charges (only from billing) are now separate. A charge is never derived from usage, and internal cost is never shown (D PD-4). Added PRD FR-1a and AC-17; updated §1, §4, §5 and §7. Spec §4.2 adds charge tools and grounding of currency figures.
- **C Phase 2 as a release blocker:** the PRD §14 v1 row and spec M3 now carry an explicit `blocked-by` entry.
- **Authority Context:** consumed as given for agent actions. Changed PRD §6 and FR-15/16, and spec §4.6.
- **Shared contracts:**
  - PRD §12 and spec §9 are restated in the [[Failure Mode Taxonomy]].
  - Milestones carry [[Release Readiness States]] and named blockers.
  - Each AC now names its evidence source and gate.
  - Mechanisms in other teams' areas are labelled as consumer requirements (spec I-1 to I-3, Q-12, new Q-13).
- **D envelope addendum:** `scope.authorityPrincipal` comes from the Authority Context. Coverage records carry `sourceOfRecord` and `watermark`, and D reconciles them against `audit.agent_audit_log`.
- Reconciliation 2026-10-10 (C answer to Q-13): Q-13 is closed on C FR-32 and C spec §4.5. The v0 `authorityPrincipal` now comes from the `authorityContext` field of `/permissions`. M1 gains `blocked-by: C M2 (FR-32)`.
