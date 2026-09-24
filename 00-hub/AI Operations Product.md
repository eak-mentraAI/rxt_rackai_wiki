---
id: hub-ai-operations-product
type: hub
status: draft
owner: product
domain: strategy
aliases: [ai operations product, aiops product, operating model, managed ai operations, fde motion, operator delivery motion, run-the-service]
related: [hub-roadmap, hub-battlegrounds, hub-minimum-operable-estate, hub-load-bearing-bets, hub-governance, hub-operations, src-rackai-dev-plan, wiki-pillar-working-model, hub-org-design]
source_docs: ["reference/jd/EXTERNAL_PDM_Product_Operations_JD.md", "06-sources/RackAI Enterprise AI Development Plan.md", "00-hub/Three Battlegrounds.md", "00-hub/RackAI Roadmap.md", "CEO strategy review 2026-09-21"]
confidence: assumed
last_reviewed: 2026-09-21
parent: hub-roadmap
summary: "The operating model as product: boundaries, SLOs, incident model, FDE motion; runs through all four proofs."
---

# AI Operations Product

The **operating model as product.** If RackAI's identity is *Operator* ([[Three Battlegrounds]]), then how we operate — the service boundaries, SLOs, incident model, handoffs, and forward-deployed engineering — cannot be an implementation detail figured out after Engineering ships a platform. It **is** part of the product. This note is the canonical home for that workstream, elevated to first-class in the [[RackAI Roadmap]] and running vertically through all four proofs.

> **Confidence.** `assumed` — this workstream is newly elevated and not yet staffed or ratified. Its precursors in the corpus are dev-plan **P5/P6** (run-the-service ops, support — both "handoff candidates") and the Product Operations JD. Nothing here is shipped; the operating model is a target, not a current capability.

## Why This Is a Product, Not a Cost Center

A managed-services labor business scales headcount with customers. An *operator product* scales customers faster than headcount — the operating model, runbooks, and automation are the product surface, and the [[Empirical Map]] flywheel is what bends the labor curve. The metric that decides which one RackAI becomes is **workloads operated per operations FTE** ([[RackAI Roadmap]] north-star family). This workstream owns that metric.

Especially true for Rackspace: taking operational responsibility for infrastructure someone else created is the historical identity ([[Three Battlegrounds]]). AI Operations Product is the AI-era expression of it.

## What This Workstream Owns

| Area | Scope |
|------|-------|
| **Operating model** | How an estate is run day to day; the division of responsibility between RackAI, customer, and partners |
| **Service boundaries** | What RackAI is on the hook for vs. the customer vs. the application/ontology partner (ties to the [[Three Battlegrounds\|harness boundary]]) |
| **SLOs** | Availability, latency, incident-response, and recovery commitments per estate tier |
| **Incident model** | Detection, escalation, response, blameless postmortem, customer comms |
| **Customer handoffs** | What is handed to the customer vs. retained; runbooks for shared operations |
| **FDE escalation** | Forward-deployed-engineer motion for onboarding and deep customer-specific work |
| **Lifecycle responsibility** | Model/version lifecycle, deprecation, change management inside the customer boundary |
| **Estate onboarding** | The path from signed customer to operated estate |
| **Operational acceptance criteria** | The gate a workload must pass before RackAI will operate it |

## Relationship to the Four Proofs

This workstream is vertical — it shows up in every proof, deepening as the operator matures.

| Proof | AI Operations Product contribution |
|-------|-----------------------------------|
| **Proof 1 — Observe** | Define the operational-acceptance criteria and the incident/observability baseline; decide what "operable" even means |
| **Proof 2 — Decide** | Encode operating decisions (placement/routing) as runbooks the [[Empirical Map]] can later assist |
| **Proof 3 — Control** | Own the operating model for the first [[Minimum Operable Estate]] — SLOs, handoffs, audit, the first FDE onboarding |
| **Proof 4 — Operate the Estate** | Full managed-ops + FDE motion; drive workloads-per-FTE leverage as estates multiply |

## The Human→Automated Ladder Applies Here Too

Per the roadmap's governing principle, the operating model starts human-run and is automated only where operating has taught us what to automate:

- **Human-operated:** engineers run the estate to a runbook.
- **Instrumented:** every operational action and outcome is captured.
- **Assisted:** the Empirical Map and runbook tooling recommend actions.
- **Automated:** proven actions become closed-loop ([[RackAI Roadmap]] Proof 4).

## Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Staffing/ownership: is this a distinct pod, or split across dev-plan P5/P6 + Product Operations? | [[RackAI Organizational Design]] | High |
| What are the operational acceptance criteria for a workload RackAI will operate? | [[Minimum Operable Estate]] | High |
| SLO tiers and the commercial model for managed operations (and the FDE motion's cost structure) | [[Load-Bearing Bets]], [[Commercial & Capacity Hub]] | Medium |
| Where does the RackAI/customer/partner responsibility line sit for incidents that cross the harness boundary? | [[Three Battlegrounds]] | High |

## See Also

- [[RackAI Roadmap]] — the workstream is elevated here
- [[Minimum Operable Estate]] — the first estate this workstream operates
- [[Three Battlegrounds]] — why the operating model is product, not overhead
- [[Empirical Map]] — the flywheel that bends the labor curve
