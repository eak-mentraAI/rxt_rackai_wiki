---
id: val-mi350p-qualification
type: validation
status: draft
owner: performance-eng
domain: performance
aliases: [validate mi350p, mi350p qualification validation, mi350p validation control record]
related: [bench-amd-mi350p-qualification, pol-benchmark-evidence-chain, ent-gpu-amd-instinct, asm-mi350p-serving-competitive, idx-validation-register]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "critical review of benchmarking notes (2026-10-07)"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-evidence
summary: "Validation control record for MI350P: per-tier decisions, evidence IDs, acceptors, restrictions, revalidation."
---

# Validate MI350P Qualification

> **Control record, not a plan.** The [[AMD MI350P Qualification Plan]] defines what should happen. This note records what *did* happen: per tier and configuration, which evidence was accepted, by whom, on what date, and with what restrictions. Rows link to immutable evidence (VCP versions, Benchmark Run IDs, bundle links), never to prose.

## What Is Being Validated

That [[AMD Instinct]] MI350P capacity can be accepted (B1/B2), has a selected serving configuration (B3), is qualified for named traffic classes as a service (B4), and has stated economics (B5). Each tier is judged against the acceptance criteria in the [[Benchmark Evidence Chain]].

## Method

Tier artifacts per the [[Benchmark Evidence Chain]]: Node Acceptance Records → Validated Cluster Profile → Benchmark Cards + evidence bundles → Service Qualification Record → Economics Sheet.

## Outcome Vocabulary

| Outcome | Meaning |
|---------|---------|
| not started | No run executed |
| blocked | Cannot start; blocker named |
| in progress | Runs executing |
| qualified | Acceptance criteria met; acceptor signed |
| qualified with restrictions | Met for a stated subset (e.g. Interactive on GLM only; not multi-tenant yet) |
| failed | Criteria not met; disposition recorded |
| requires revalidation | Previously accepted evidence invalidated by a change (see triggers) |

## Control Record — by Tier

| Tier | Scope | Status | Evidence (IDs / links) | Acceptance criterion | Acceptor | Decision / date | Blocker |
|------|-------|--------|------------------------|----------------------|----------|-----------------|---------|
| Pass 0 | Topology, compatibility, FP8 readiness, model fit | blocked | — | Answers recorded for 0.1–0.5 | Inference Optimization | — | D4 topology confirmation |
| B1 | All MI350P nodes | not started | — | Every node within vendor-spec tolerance | Infra | — | D4 |
| B2 | `VCP-MI350P-001` | not started | — | Infrastructure requirements met (accepted); reference performance validated or not, recorded separately | Inference and Serving Services | — | D1 reference model + tolerance; D3 owner |
| B3 | Reference model, Throughput | not started | — | Card + bundle registered, ≥ 3 repeats | Inference Optimization | — | B2 |
| B3 | GLM 5.3 Flash, Interactive + Throughput | not started | — | Default config selected (T4.S5) | Inference Optimization (+ Serving for regression baseline) | — | Pass 0 compatibility/fit |
| B4 | GLM 5.3 Flash, selected config | not started | — | All three B4 categories pass at ratified SLO | Inference and Serving Services + AI Governance and Assurance | — | D2 ratified SLOs |
| B5 | GLM 5.3 Flash, SQR point | not started | — | Economics sheet with confidence labels | Inference Optimization (FinOps) | — | Validated cost inputs ([[Cost per GPU-Hour]]) |

Qualification is **per configuration and traffic class**. Add a row for each new configuration rather than overwriting.

## Failure Disposition

| Failure | Disposition |
|---------|-------------|
| B1 node fails | Exclude the node; the VCP is issued on passing nodes only; Infra opens a vendor case |
| B2 infrastructure requirements not met | VCP not accepted; no B3 may cite it. Diagnose; re-run after the fix as a new VCP version |
| B2 reference outside tolerance | Record "reference performance not validated" with the diagnosis (stack vs. hardware vs. non-comparable conditions). Blocks acceptance only if D1 decides reference validation gates it; always blocks the public reference claim |
| B3 no feasible config meets provisional thresholds | Record as a result; options: different TP/replica layout, challenger backend, BF16, or restrict to Throughput-class traffic |
| B4 category fails | *Qualified with restrictions* if other classes pass; otherwise failed. Isolation or sovereignty failure blocks multi-tenant offer |
| B5 economics unattractive | Feeds commercial decision: price, product placement (e.g. batch tier), or capacity reallocation — not a re-run |

## Revalidation Triggers

Per the change-impact rules in the [[Benchmark Evidence Chain]]:

- Firmware, driver, kernel, or base ROCm changes → B2, then affected B3.
- Engine, runtime image, or serving flags → affected B3 via the [[Performance Regression Gate]]; B4 only if the operating point moves.
- SLO threshold changes → re-score B4.
- Cost inputs → recompute B5.

## Documents This Can Change

| Document | Field / Value | Potential Change |
|----------|---------------|------------------|
| [[AMD Instinct]] | Topology, HBM, serving stack, horizontal scaling | assumed → measured |
| [[MI350P Serving Competitive]] | Clauses C1–C3 (only with matched H100 evidence) | assumed → measured / refuted |
| [[Available Hardware Sufficient for Priority Models]] | AMD half | partially measured |
| [[Tokens per GPU-Second]], [[TPOT]], [[TTFT]], [[Energy per Token]] | MI350P values | assumed → measured |
| [[Benchmark Library]] | MI350P rows | planned → recorded |

## Status

| Status | Result | Date |
|--------|--------|------|
| open | Plan and control record created; no tier executed; Pass 0 blocked on D4 | 2026-10-07 |

## See Also

- [[Evidence Hub]]
- [[Validation Register]]
- [[AMD MI350P Qualification Plan]]
