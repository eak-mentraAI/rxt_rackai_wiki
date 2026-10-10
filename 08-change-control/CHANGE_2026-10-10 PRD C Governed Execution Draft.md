---
id: chg-2026-10-10-prd-c-governed-execution-authority
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [prd c draft, governed execution prd draft, delegated authority prd draft]
related: [prd-governed-execution-authority, spec-governed-execution-authority, ent-agent-identity, pol-action-controls, ent-governed-harness, prd-workload-declaration-placement, spec-workload-declaration-placement, prd-sovereign-isolation-assurance, src-identity-access-spec, wiki-prd-coverage-plan, hub-roadmap]
source_docs: ["PM direction 2026-10-10: draft every remaining PRD and tech spec to the review stop point", "RSS-Engineering/rackai@79ca4de, rackai-ui@89bddb4, rackai-docs@ccb52a3 (read-only survey)"]
confidence: derived
last_reviewed: 2026-10-10
parent: hub-wiki
summary: "Drafted PRD C (governed execution, delegated authority) and its tech spec v0.1; answers PRD A's open items for C."
---

# CHANGE 2026-10-10 — PRD C Governed Execution & Delegated Authority Draft

## Trigger

The product owner asked for every remaining PRD and its tech spec to be drafted up to the point where product and engineering approval are needed, so the whole batch can be reviewed at once. PRD C is wave 1 in [[PRD Coverage Plan]]. It also has to answer the items PRD A handed to C (A's Q-2, Q-3, Q-14 and Q-16 / DV-3). The skill's Mode 2 precondition (an approved PRD) was waived by the product owner for this batch.

## What Changed

- **New PRD:** [[Governed Execution & Delegated Authority PRD]] (`prd-governed-execution-authority`, v0.1 draft, `confidence: assumed`). Product approval: not yet approved.
  - Roadmap items: *Governed execution harness v1* (Phase 1); *IAC M4 (org-level RBAC + metering/billing/quota perms)* and *Authority under incomplete intent* (open decisions → Phase 2); *Governed harness - full runtime* and *Govern & assure inside the perimeter* (later phases).
  - 26 functional requirements, 13 acceptance criteria, 13 proposed product decisions (PD-1 to PD-13, all *proposed*), 8 open decisions (D-1 to D-8). D-1 is the IAC M4 conflict.
  - It consumes the built IAC services and links [[Governed Harness]], [[Agent Identity]] and [[Action Controls]] without redefining them. Action class, action catalogue, authority grant, authorisation and authority decision are defined in the PRD; whether they get a canonical home is D-8.
- **New spec:** [[Governed Execution & Delegated Authority Tech Spec]] (`spec-governed-execution-authority`, v0.1 draft). Engineering approval and product approval: not yet approved.
  - Design: an action catalogue in code; two CRDs (`ActionAuthorization`, `AuthorityGrant`) created only through authservice mint handlers that follow the API-key mint pattern; `pkg/authority` with `Decide`, `Consume`, `ForPolicyChange`, `ForBoundaryException` and `CheckPlacementApproval`; a customer-only scope class; two built-in roles (`placement-operator`, `security-admin`); audit category `authority`; D-0 evidence kinds `authority-decision` and `authority-grant`.
  - Four milestones, M1–M4 (M1–M2 for MOE-0, M3–M4 for MOE-1). Phase-2 FRs (FR-23 to FR-26) are deferred and traced.
  - Divergences: DV-1 (group-membership lag, non-material) and DV-2 (break-glass recorded, not detected; non-material).
  - Exceptions to A's spec contract are listed in spec §1.6 for A's engineering to accept (Q-3).

## Answers to PRD A's Items (proposed, not approved)

| A item | Answered by |
|---|---|
| Q-2 / D-2: who owns `PlacementPolicy`, org- or tenant-scoped | PRD C PD-4, FR-14; spec §4.2, §1.6 |
| Q-3 / D-3: who holds `placement:approve` / `placement:propose`; disruptive re-placement | PRD C PD-5, FR-16, FR-26; spec §4.2, §4.8 |
| Q-14: approval TTL; approver differs from proposer | PRD C PD-6; spec §4.8, §4.12 (values are D-2) |
| Q-16 / DV-3: delegated-authority model, `authority.ForPolicyChange`, impact-bound authorisation, emergency path | PRD C PD-7, PD-8, FR-6, FR-13, FR-15, FR-17; spec §4.3–§4.7 |

## Code Survey Findings (read-only, `RSS-Engineering/rackai@79ca4de`)

- Org-level role bindings (`scope.level: org`) are built and work under enforcement. What ships off is multiple CustomerOrgs (`rbac.multiOrg.enabled`). `usage:view` and `observability:view` are enforced, and `billing:*` and `quota:*` exist in roles with no routes. This is the substance of the IAC M4 conflict (PRD D-1).
- Authorization has no approval, delegation, separation-of-duties or emergency concept.
- Keycloak groups do not reach the inner apiserver or the webhooks (`X-Remote-Group` is the tenant), so authority has to be evaluated at an authservice mint, not in a webhook.
- Audit actors are `user|service|controller`, with no agent or "on behalf of". Direct cluster changes are recorded as actor `unknown` until the audit webhook ships.
- The committed A spec (`e1ae63f`) references §4.6, §4.6.1 and §4.7, but those sections are missing from the file.

## Propagation

Not applied here. Proposed edits to the roadmap CSV (PRD and Tech spec columns for the five rows), the coverage-plan status line, back-links on [[Agent Identity]], [[Action Controls]] and [[Governed Harness]], and the roadmap row 38 note are returned to the orchestrator, which applies them centrally.

## Not Changed

- No other wiki file was edited. No code repo was written to.
- PRD A and its spec are unchanged. C's requests to A are listed as spec exceptions and open questions.

## Reconciliation

Reconciliation pass 2026-10-10: finalised `ForBoundaryException(exceptionUID, specDigest)` and `ForPolicyChange(policyUID, generation, impactDigest)`, both returning `authorised{ref, authoriser, emergency} | denied | absent`; adapter reads E's `BoundaryException` fields (spec §4.10); D-0 kinds aligned to `policy-decision`, `authority-decision`, `authority-grant` with `audience`, D-0 `recordId` rule and a daily `coverage` record (spec §4.9); consumer actions for G, H, F and J named as later catalogue rows (spec §4.1); new spec Q-13 (H), Q-14 and PRD D-9 (CustomerOrg vs Organization with E); PD-5 and FR-9 notes for G and J.

Reconciliation pass 2026-10-10 (round 2): evidence `basis` changed to `derived` (audit refs only); `policy-decision` emission and claim made explicit and distinct from `authority-decision`; corrections use `supersedes` with `#rN` source IDs; records written through `pkg/evidence.EnqueueTx`; spec Q-5 resolved.

Reconciliation pass 2026-10-10 (round 3, from H): PRD Core Entities reworded: an API key may carry an agent's credential, but the agent's effective authority is the intersection with the delegating user's authority through the grant, never the key's own role.

## PO review disposition 2026-10-10

Recorded as given: **conditional acceptance; not formal artifact approval.** PRD and spec moved to v0.2; status stays `draft`; product approval not yet given.
- **Approved in principle:** PD-2 to PD-5, PD-7, PD-9 to PD-13 (PD-4 text aligned to X-1).
- **PD-6 revised:** separation stays the default; controlled single-authoriser exception with independent oversight, evidence and review (PRD FR-27, AC-14; spec §4.6.2).
- **PD-8 revised:** added RackAI platform-safety containment (contain only; catalogued, customer-notified, evidenced, reviewed) (PRD FR-28, AC-15; spec §4.6.1).
- **PD-1 held** for the IAC owner; built / remaining / dependent capabilities recorded in PRD D-1.
- **X-1:** new PD-14, FR-29, AC-16; spec §4.13 (validated `CustomerOrg.spec.authorityPrincipal`; invariant stated verbatim). PRD D-9 answered.
- **X-3:** new PD-15, FR-31, AC-18; `model.retire` disruptive and never emergency-eligible; `model.security-withdraw` added; F's Q-4 and Q-5 answered (spec Q-15).
- **S-2:** new canonical note [[Authority Context]] (`ent-authority-context`); spec §4.5 interfaces take and return it.
- **J DV-3 interplay:** attribution contract with coverage-gap cases (PRD PD-16, FR-30, AC-17; spec §4.9).
- **Taxonomy and readiness:** PRD §12 and spec §9 restated in [[Failure Mode Taxonomy]] terms; spec §13 carries the four [[Release Readiness States]] and named `blocked-by` blockers; every AC names an expected result, an evidence source and its gate.
- DV-1 and DV-2: no ruling; kept for confirmation.

Envelope addendum 2026-10-10: spec §4.9 adds `scope.authorityPrincipal` (from the Authority Context), coverage `watermark` and `sourceOfRecord`, and omits `verification` (no C kind carries a typed status).

H request 2026-10-10: PRD FR-32 and spec §4.5. Plain user sessions get their Authority Context from the caller-introspection endpoint `GET /namespaces/{ns}/permissions` (new additive `authorityContext` field, derived from the token).

B request 2026-10-10: spec §4.13 adds `authority.PrincipalFor(ctx, organization)`, an in-process lookup that system-produced records (B, D, E, G, J) use to set the authority principal.

F request 2026-10-10: spec §4.2 adds the proposed built-in platform role `model-steward` (`model:approve`), and the §4.1 model gate and promotion entries reference it.

## Open Items

- PRD D-1 to D-8; spec Q-1 to Q-12.
- The roadmap link-back (P-09, T-10) will fail lint until the orchestrator adds the CSV links.
- Product review of PD-1 to PD-13 and AC-1 to AC-13; engineering and product review of the spec, including DV-1 and DV-2.
