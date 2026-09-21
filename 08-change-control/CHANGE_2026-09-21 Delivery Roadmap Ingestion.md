---
id: chg-2026-09-21-delivery-roadmap-ingestion
type: change
status: reviewed
owner: product
domain: strategy
aliases: [delivery roadmap ingestion change, xlsx ingestion, roadmap ground-truth change]
related: [hub-roadmap, src-rackai-delivery-roadmap, idx-capability-gap-register, ent-api-key, wf-metering, pol-change-packet]
source_docs: ["reference/RackAI - Roadmap.xlsx"]
confidence: measured
last_reviewed: 2026-09-21
parent: hub-wiki
summary: "Change packet: ingested the delivery-roadmap xlsx, re-anchored the canonical roadmap, and corrected confidence states."
---

# Change Packet — Delivery Roadmap Ingestion (2026-09-21)

## 1. Source of Change

- **Trigger:** new source document — the real delivery roadmap `reference/RackAI - Roadmap.xlsx` (staffed, Jira-tracked, dated) was identified as the roadmap the canonical note should be formed around. The canonical roadmap had been built on the strategy-side spines only; this reconciles it to ground truth.
- **Date:** 2026-09-21
- **Requester/Owner:** user direction → product

## 2. Affected Concept(s)

- **New source:** [[RackAI Roadmap (Delivery Plan)]] (`src-rackai-delivery-roadmap`, `measured`) + CSV export.
- **Reworked:** [[RackAI Roadmap]] (`hub-roadmap`) — milestone spine re-anchored on real delivery milestones; P-003–P-007 added.
- **Confidence-corrected:** [[Capability Gap Register]], [[API Key]], [[Metering]], [[Request Routing]].
- **Layer:** L5 (roadmap/planning) + L4 (evidence) + L1/L2 (entity/workflow confidence).
- **Change type:** new source + major rework + confidence updates + edge additions.

## 3. Truth-Hierarchy Note (shipped beats planned)

The xlsx is `measured` delivery data and outranks the `assumed`/`planned` strategy sources for "what exists today." Applied: capabilities the corpus listed as planned/missing but the xlsx shows shipped/in-progress were corrected (weakest *truthful* state — in-progress → `partial`/`derived`, complete → `measured`). Source narratives (Engineering Roadmap, dev plan) were **not** edited — they remain read-only; the reconciliation lives in the canonical roadmap and the evidence layer.

## 4. Objects Changed / Added

- **Added:** `src-rackai-delivery-roadmap` (`06-sources/RackAI Roadmap (Delivery Plan).md`); 7 CSVs in `reference/rackai-roadmap-csv/`.
- **Reworked:** `hub-roadmap` — Milestones section now lists real milestones (IAC/Platform/Metering/Auditing/Observability M1–M4 with Jira/owners/status, M2 features, Uniphore Phase 1) under the four proofs; ⚠ gaps routed to proposals; Material Progress table shows shipped-vs-gap; five new proposals **P-003–P-007** (all Proposed, not adopted).
- **Confidence corrections:**
  - `ent-api-key`: `assumed` → **`measured`** (shipped, IAC M1 / RACKAI-204).
  - `wf-metering`: `assumed` → **`derived`** (Metering M1 in progress / RACKAI-352).
  - `idx-capability-gap-register`: metering planned→partial; API Key planned→shipped; RBAC planned→partial (org-level dropped); audit→partial; DPO→in-progress; smart-routing→partial; summary/through-line/caveats rewritten.
  - `wf-request-routing`: added delivery-status note (llm-d routing in progress / RACKAI-311).

## 5. Edges Added

- `hub-roadmap` ↔ `src-rackai-delivery-roadmap`; `idx-capability-gap-register` → `src-rackai-delivery-roadmap`, `hub-roadmap`; `ent-api-key` / `wf-metering` → delivery-roadmap source.
- Crosswalk: 4 rows added (delivery roadmap → Delivery Plan note, → canonical roadmap, → confidence-corrected notes). Source Inventory: 1 row added.

## 6. Key Facts Captured (from the xlsx)

- **Shipped (Complete):** IAC M1 (JWT/API-key auth, APIKey CRD, Gateway auth — RACKAI-204), IAC M2 (platform RBAC — RACKAI-333), IAC M3 (audit-log query API — RACKAI-351); M2: API Layer Validation, KServe upgrade, FT context-parallel, Accelerator selection ph3.
- **In progress:** Platform M1–M4 (telemetry), Metering M1, inference routing (llm-d), AMD AIM, speculative decoding, DPO, dataset mgmt, synthetic data.
- **Dropped:** **IAC M4 "Won't Do"** (org-level RBAC + metering/billing/quota permissions).
- **Backlogged (Pri-6):** multi-region support, GPU node access support.
- **Open (RXT):** billing, delivery platform (SNOW?), authentication replacement (Auth0 → Zitadel/Keycloak, post-May).

## 7. Open Questions Created

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Adopt P-005 (Empirical Map v1 + evidence routing) — the moat is absent from delivery; who owns it? | [[RackAI Roadmap]], [[Empirical Map]] | High |
| Reinstate IAC M4 (org-level RBAC)? Why was it "Won't Do"? (P-006) | [[RackAI Roadmap]], [[Capability Gap Register]] | High |
| Cost-model owner + fleet cost inputs (P-003) | [[RackAI Roadmap]], [[Cost per GPU-Hour]] | High |
| Compliance-attestation milestone — none on the delivery plan (P-006) | [[RackAI Roadmap]], [[Governance Hub]] | High |
| Billing (open RXT question) — still blocks Path B public provider | [[Capability Gap Register]], [[Billing & Payment]] | High |
| Supply-abstraction interface before control plane hardens (P-004) | [[RackAI Roadmap]] | Medium |

## 8. Contradictions Surfaced / Resolved

- **Resolved:** corpus said auth/API-key/RBAC/audit were planned/`assumed`; the xlsx shows them shipped — corrected across Register, API Key, Metering.
- **Surfaced (not hidden):** the delivery plan is strong on the Proof-1 measurement substrate but **absent exactly where the operator identity lives** — the moat (Empirical Map, Proof 2) and the identity proof (harness + attestation + MOE, Proof 3); org-level RBAC was dropped and Proof-4 prerequisites are Pri-6 backlog. These are the P-003–P-007 agenda, left explicit rather than smoothed over.

## See Also

- [[CHANGE_PACKET]]
- [[RackAI Roadmap]] · [[RackAI Roadmap (Delivery Plan)]]
- [[Capability Gap Register]]
