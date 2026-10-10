---
id: pol-verification-status
type: policy
status: draft
owner: rackai-product
domain: governance
aliases: [verification status, verified vs qualified, typed verification statuses, what verified means]
related: [prd-customer-observability-evidence, prd-empirical-map-routing, prd-model-lifecycle, prd-sovereign-isolation-assurance, prd-workload-declaration-placement, ent-evidence-report, pol-failure-taxonomy, pol-release-readiness]
source_docs: ["Product-owner review disposition, PRD batch B–J, 2026-10-10 (finding S-1)"]
confidence: assumed
last_reviewed: 2026-10-10
parent: hub-governance
summary: "Separate, typed statuses for configuration, performance, boundary and evidence claims; never one 'verified' Boolean."
---

# Verification Status Vocabulary

## Purpose

"Verified" was being used for four different claims across the PRDs. A qualified configuration is not proof that a workload meets its service level. A met service level does not prove a sovereignty boundary held. Complete evidence collection does not prove the outcome succeeded. This note fixes one typed status per claim, so no PRD collapses them into a single Boolean. Each PRD keeps its own rules for reaching a status. This note only fixes the names and what each one may be used to claim.

## Rule

Each claim type has its own status field and its own owner. A status of one type is never used as evidence for another.

| Claim type | Status field | Values | Owner (rules) | May be used to claim |
|---|---|---|---|---|
| **Configuration qualification**: this serving configuration (by `scid`) passed the lifecycle gates | `qualification` | `qualified`, `not-qualified`, `failed`, `revoked` | F produces; G owns the `scid` identity | The configuration may be *offered* |
| **Performance verification**: evidence shows this option meets a declared service-level target for this workload | `performance` | `verified`, `unverified` (with a reason), `known-fails` | G (rules), A (applies at placement) | The option *meets* the target. Only `verified` may be presented as meeting it |
| **Containment qualification**: this runtime path stops deterministically | `containment` | `qualified`, `not-qualified` | A (A spec §4.9.1) | The runtime may host declaration-managed workloads |
| **Boundary control status**: a boundary control is configured and operating | `boundary` (per rule) | `held`, `not-held`, `unverified` | E | The control was operating. It is **not** proof that no forbidden flow occurred, unless the rule states an observed-flow basis |
| **Evidence completeness**: the records for a period were collected and reconciled against the source of truth | `coverage` | `complete`, `incomplete`, `unknown` | D | Collection was complete. It is **not** proof that the outcome succeeded |

**Feasibility is a separate axis.** It is never a verification status. A placement option is always shown with both of these:
- **Feasibility:** `feasible`, `infeasible` (with its category), or `not-offered` (no qualified configuration).
- **Performance:** `verified` or `unverified`.

Customers must be able to tell *feasible and verified*, *feasible but unverified*, *infeasible* and *not offered* apart. *Unverified* never means unavailable, and *feasible* never implies a performance guarantee ([[Workload Declaration & Placement PRD]] PD-2).

**Ranking evidence is not verification evidence.** Evidence good enough to rank options (e.g. a B3 benchmark card) may inform a recommendation. Only the performance rules of [[Empirical Map & Evidence-Informed Routing PRD]] produce `verified`.

## Scope

Every PRD, tech spec, API field, console label and evidence record (D-0 `verification`) that states one of the claims above.

## Governs

| Target | Relationship |
|--------|--------------|
| [[Evidence Report]] | GOVERNS → which status may appear as which claim |
| [[Workload Declaration & Placement Tech Spec]] | CONSTRAINS → placement option display |
| [[Model Lifecycle PRD]] | CONSTRAINS → qualification and offering |
| [[Sovereign Isolation & Assurance PRD]] | CONSTRAINS → boundary claims |

## Enforcement

The D-0 kinds registry ([[Customer Observability & Evidence Report Tech Spec]]) binds each `kind` to the one status type it may carry. Records claiming a status outside their type fail validation. In reviews, Fitness P-07 and T-07 (confidence honesty) apply to these labels.

## See Also

- [[Failure Mode Taxonomy]]
- [[Release Readiness States]]
- [[Governance Hub]]
