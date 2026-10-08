---
id: chg-2026-10-07-benchmark-evidence-chain
type: change
status: draft
owner: performance-eng
domain: performance
aliases: [benchmark evidence chain change, mi350p benchmarking program change 2026-10-07]
related: [pol-benchmark-evidence-chain, bench-amd-mi350p-qualification, met-tpot, met-goodput, met-slo-attainment, met-energy-per-token, asm-mi350p-serving-competitive, val-mi350p-qualification, ent-gpu-amd-instinct, idx-benchmark-library]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "critical review of benchmarking notes (2026-10-07)"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-wiki
summary: "Added the Benchmark Evidence Chain (B1–B5 tiers, handoffs, claim rights), four metrics, and the MI350P plan."
---

# 2026-10-07 — Benchmark Evidence Chain

## Trigger

Rackspace deployed a new AMD MI350P fleet and needs a benchmarking program that gets it taken seriously. The operator brief sketched a five-layer stack (silicon → AI infrastructure → serving → enterprise service → economics) and two governance rules. The task: reconcile it with canonical structure, declare the dividing lines and handoffs between owners, and unify them into one chain of evidence.

## Reconciliation Decisions

- **Named B1–B5, not L1–L5** — L1–L5 are already the knowledge-graph layers; the tiers are mapped onto the [[Eight-Layer Stack]] and the serving chain instead of adding a competing numbering.
- **The hard seam is the Kubernetes line, between B2 and B3** (per [[Pillar Working Model]] / [[RackAI Organizational Design]]). The brief's joint "RackAI + Infra" serving layer became single-owned by [[Inference Optimization]], citing Infra's Validated Cluster Profile.
- **"RackAI" split into its pillars** — B3/B5 Inference Optimization, B4 Inference and Serving Services with AI Governance & Assurance co-signing isolation, Product Operations checking claims, AI Harness consuming cards via the [[Empirical Map]].
- **Customer-specific performance moved to an outer edge** (Customer Workload Qualification), outside the RackAI claim boundary per the [[Enterprise AI Cloud Product Model]].
- **Workload profiles are [[Traffic Class]] instances** (existing alias "workload profile"); Agentic added as a fourth profile via the existing [[AgentX Benchmark Standard]].
- **Benchmark Card is a format, not an entity** — it renders [[Benchmark Run]]s; defined inside the policy.
- **Economics computed at the B4 SLO-qualified point**, and capped at the confidence of [[Cost per GPU-Hour]] (`assumed`).

## Objects Changed

- **Added:**
  - [[Benchmark Evidence Chain]] (`pol-benchmark-evidence-chain`, policy) — tiers, handoff register (H1 Node Acceptance Record, H2 Validated Cluster Profile, H3 Benchmark Card, H4 Service Qualification Record, H5 Economics Sheet), claim-rights matrix, card format, standard profiles, external anchors.
  - [[TPOT]] (`met-tpot`, ITL alias), [[Goodput]] (`met-goodput`), [[SLO Attainment]] (`met-slo-attainment`), [[Energy per Token]] (`met-energy-per-token`, tokens/kWh and watts/token aliases).
  - [[AMD MI350P Qualification Plan]] (`bench-amd-mi350p-qualification`, evidence) — B1→B5 run plan, card skeletons, open decisions D1–D4.
  - [[MI350P Serving Competitive]] (`asm-mi350p-serving-competitive`); [[Validate MI350P Qualification]] (`val-mi350p-qualification`).
- **Changed (extended, no redefinition):** [[AMD Instinct]] (status deployed — operator-reported; Benchmarking and Claims section; summary), [[Fleet Inventory]] (incoming-capacity line), [[Benchmark Run]] (tier, cluster-profile, concurrency, TPOT, energy attributes), [[Traffic Class]] (standard profiles), [[Benchmark Library]] (governing standard, MI350P row), [[Assumption Register]], [[Validation Register]], [[Open Questions]], [[Inference Optimization]], [[Evidence Hub]], [[Operations Hub]], [[Metric Index]], [[KPI Hierarchy]], [[Capability Gap Register]], [[Milestone Release Map]] (T4.S5), [[Pillar Working Model]] (seam 8), [[Source-to-Concept Crosswalk]].
- **Deprecated:** none.

## Edges

- **Added:** Benchmark Evidence Chain GOVERNS Benchmark Run / Benchmark Library / MI350P plan; USES Traffic Class; SUPPORTS Performance Regression Gate and Empirical Map; CONSTRAINS Cost per 1M Tokens. AMD Instinct MEASURED_BY MI350P plan. New metrics MEASURE Model Deployment / Capacity Pool / GPU Node.
- **Removed:** none.

## Confidence Changes

| Note | Old | New | Reason |
|------|-----|-----|--------|
| All added notes | — | assumed | Program standard and plan only; no run executed |
| [[AMD Instinct]] status | ETA ~Oct 2026 (assumed) | Deployed, operator-reported (assumed) | Not yet in Fleet Inventory ground truth |

No performance numbers were introduced. Every card cell is `pending`.

## Downstream Propagation Check

- Dependents found with `kg.py in` on ent-gpu-amd-instinct, ent-benchmark-run, idx-benchmark-library, ent-traffic-class; hubs/indexes updated as listed.
- IDs and aliases preserved; "workload profile" stays an alias of Traffic Class.
- Formula chain unchanged; the policy references it and constrains where it is evaluated (SQR operating point).
- No scorecard changed (no measured values).
- Frontmatter lint passes.
- Pre-commit hook: `scripts/install-git-hooks.sh` fails inside a git worktree (`.git` is a file); hooks are shared from the main checkout, where the pre-commit hook is already installed.

## Open Questions Created

Added to [[Open Questions]]: per-profile SLO thresholds unratified (blocks B4); profile shape definitions; ownership of the B2 vendor-reference reproduction; MI350P reference-model choice; power telemetry at deployment grain. Existing MI350P quantity/topology question extended.

## Revision — Critical Review (2026-10-07, same day)

A critical review judged the architecture sound but not execution-ready. Adopted, with four deliberate deviations agreed with the product owner.

**Adopted:**

- **Policy**
  - Evidence bundle (the card summarizes reproducible evidence: digests, configs, workload/arrival definition, raw data, scripts, ≥ 3 repeats with variance).
  - Open-loop arrival-rate sweeps alongside closed-loop concurrency.
  - Qualification scope matrix (required / conditional / not applicable); standard checkpoints with justified extension and early stop.
  - Test classes (standard-compliant / standard-inspired / RackAI-internal).
  - Rule 1 softened to "currently valid upstream evidence", not mandatory re-runs.
  - "Requests are not users" rule.
  - B4 acceptance categories: performance isolation, operational resilience, private/sovereign operation (co-signed by AI Governance and Assurance).
  - Steward / executor / approver ownership lines.
- **Qualification plan:** rebuilt as Pass 0 (topology D4 first, compatibility, FP8 readiness, model fit via [[GPUs per Replica]] and [[Model Weight Footprint]], topology choice), then three passes (baseline → competitive serving → enterprise readiness). Backend hierarchy: vLLM primary, SGLang optimization challenger, AIM integration challenger. Initial scope cut to 1 reference card plus GLM × 2 profiles.
- **Validation note:** converted into a control record (per-tier status, evidence IDs, acceptor, outcome vocabulary incl. *qualified with restrictions*, failure disposition, revalidation triggers).
- **Smaller fixes:**
  - SLO attainment removed from B3 cards; B3 goodput is provisional with named thresholds.
  - Energy per token measured at B3, interpreted at B5.
  - B5 reframed on cost per 1M *successful* tokens, usable capacity, utilization, and demand assumptions.
  - `asm-h200-sufficient` given a scope line separating fit from competitiveness.

**Deviations from the review:**

1. **Versioning:** split into the VCP (infrastructure only) and the serving configuration recorded on each card, with a change-impact table. A serving change no longer invalidates hardware acceptance.
2. **Competitiveness assumption:** kept as **one** note with three independently validated clauses (C1 performance B3→B4, C2 operability B4, C3 economics B5), each requiring matched H100 evidence, rather than three notes. Restated as workload-specific, with per-GPU / per-replica / per-dollar-at-SLO comparison views. Fixes the prior inconsistency, where the plan marked it measured after B3.
3. **90% threshold:** not written as a criterion. Recorded only as an unratified proposal inside an open question.
4. **Decision gates:** no new gates defined. A "Decisions the Evidence Feeds" section maps tiers to existing gates: VCP acceptance at the Kubernetes line, Milestone Release Map T4.S5, the Model Launch Gate (Pillar Working Model seam 1), and the Proof-1 commercial gate.

**Propagated:**

- [[Benchmark Run]]: serving configuration, load mode, evidence bundle, test class; concurrency = requests.
- Metric notes: [[Goodput]] (provisional vs qualified), [[Energy per Token]], [[SLO Attainment]].
- Registers and indexes: Assumption Register, Validation Register, [[Benchmark Library]], [[Traffic Class]], [[Pillar Working Model]] seam 8, [[Available Hardware Sufficient for Priority Models]].
- [[Open Questions]]: reproduction contract widened; competitive band and user model added; profile shapes widened.

No confidence changed; no numbers introduced.

## Revision 2 — Onsite Brief Review (2026-10-07, same day)

A leadership onsite brief was produced from these notes (hosted as a private artifact, not stored in the corpus). Its review prompted three corpus changes:

- **Reference reproduction decoupled.** B2 now records two separate outcomes: *infrastructure accepted* and *reference performance validated*. Whether the second gates infrastructure acceptance or only serving qualification is an open question. Updated in the policy (B2 question, H2 acceptance rule, B2 claim rights), the qualification plan (hardware-acceptance criterion, Pass 1 exit, D1), and the validation record (B2 criterion, failure disposition).
- **Rule 12, "Reuse before re-running".** Existing results are inventoried first, and registered at their tier if they meet the bundle bar.
- **New open questions:** what to prove first (D0, leadership); the role of reference reproduction; reusable existing evidence. The competitive-band question now lists the candidate win definitions.

No confidence changed; no numbers introduced.

