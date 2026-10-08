---
id: ent-solution-marketplace
type: entity
status: draft
owner: rackai-product
domain: product
aliases: [solution marketplace, marketplace, rackai marketplace, solution distribution surface, solution catalog, agent marketplace, app marketplace, harness marketplace, fde marketplace]
related: [ent-packaged-solution, ent-governed-harness, ent-openrouter-integration, ent-model-deployment, ent-empirical-map, ent-agent-identity, hub-entities, hub-eac-product-model, hub-ai-operations-product, idx-eight-layer-stack, hub-openrouter, hub-battlegrounds]
source_docs: ["00-hub/Enterprise AI Cloud Product Model.md", "05-wiki/Eight-Layer Stack.md", "00-hub/AI Operations Product.md", "00-hub/Three Battlegrounds.md", "PM/leadership marketplace discussion 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-entities
summary: "Canonical entity (proposed): Consumption-layer surface where FDE-authored Packaged Solutions are published, consumed."
---

# Solution Marketplace

> **Confidence: `assumed` — proposed, not adopted.** This entity models a strategy direction raised in the 2026-10-06 marketplace discussion. Nothing here is shipped; it is framed as a proposal on the [[RackAI Roadmap]] (a cross-cutting Consumption surface, see *Cross-Cutting Surfaces*). It defines the *target shape* and the ownership boundary so the concept has a canonical home; adoption of scope and commercial model is a roadmap decision.

## Definition

The **Solution Marketplace** is a **Consumption-layer distribution surface** on which [[Packaged Solution|Packaged Solutions]] — agents, apps, and harnesses that serve specific outcomes — are **published, discovered, certified, instantiated, and metered** for RackAI customers. It is the mechanism by which Rackspace *drives consumption* of the platform: a solution authored once can be instantiated across many customer estates, so demand scales without engineering effort scaling linearly with it.

It is the **second consumption channel** in the corpus, structurally alongside the [[OpenRouter Initiative|OpenRouter channel]]. Where OpenRouter distributes *model endpoints* to external traffic, the Solution Marketplace distributes *packaged outcomes* to RackAI customers. Both sit at the Consumption layer of the [[Eight-Layer Stack]]; neither is a platform layer.

> **The marketplace (the rails) IS RackAI; the solutions on it are not.** Per the evolved [[Enterprise AI Cloud Product Model]] boundary (2026-10-06), **RackAI is the private AI operating platform = core + rails**, and the marketplace/SDK/certification/metering machinery is part of the **rails** — squarely inside the RackAI boundary. What is *not* RackAI is the **business logic authored on the rails** (the [[Packaged Solution|Packaged Solutions]] themselves — their goals, skills, workflows). The sharper frame: **RackAI owns the factory and the marketplace, not everything produced by the factory.** This keeps "RackAI" from leaking upward into "RackAI owns all the apps" while correctly placing the distribution machinery as RackAI's. The marketplace drives consumption into the **Outcome as a Service** offer.

## The Boundary — who builds what (the load-bearing convention)

This entity exists primarily to draw one line cleanly. It is a **two-sided-platform split**:

> **RackAI (the product org) builds the rails: the marketplace surface, the governance/certification gate, the isolation that lets a third-party-authored solution run safely inside a tenant, and the Solution SDK/standards that make a solution *admissible*. FDEs (and later partners and customers) are the supply side: they author [[Packaged Solution|Packaged Solutions]] *to* that standard and submit them for placement. RackAI never authors the example solutions; the authors never build the platform.**

| Side | Owner | Owns | Does NOT own |
|------|-------|------|--------------|
| **Platform / rails** | **RackAI product org** | The marketplace surface + catalog; the submission → certification → publication gate; the **Solution SDK** and packaging standard; tenant isolation + governance for third-party-authored solutions; metering/attribution of solution consumption | The business logic inside any solution; the customer's ontology/data; which outcomes get built |
| **Supply / authors** | **FDE** (first + canonical), then **partners / customers** | The solutions themselves — the harness pattern, skills, tools, prompts, the target-outcome logic; submitting to the standard; maintaining the solution | The marketplace, the SDK, the certification bar, the isolation model |

This maps exactly onto the [[Three Battlegrounds]] **harness boundary**: Rackspace owns the *execution machinery* (here: the marketplace, SDK, governance — horizontal, same shape across customers); the authors own the *business logic* (here: the solution's goal and workflow — what differs per outcome). The marketplace is defensible for the same reason the harness is: it is not the customer's differentiated logic, it is the operating machinery every distributed solution needs.

It is also the same **producer/consumer discipline** the [[Pillar Working Model]] already applies to the [[Empirical Map]]: producers (FDEs) author to a contract; the owner (RackAI) defines the standard and the surface, and does not author the supply.

## Layer

L1 — Entity Ontology, at the **Consumption** layer of the [[Eight-Layer Stack]] (initiatives/channels, not a platform layer). Position relative to the serving chain:

**Market Demand → Solution Marketplace → [[Packaged Solution]] → [[Governed Harness]] → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

The marketplace sits above the harness: a Packaged Solution bundles a harness (+ skills/tools/target models/corpus binding); the marketplace distributes the solution. Consumers see solutions and the outcomes they produce; they never reference GPUs directly. The marketplace routes *into* the serving chain via Model endpoints — it never bypasses [[Model Deployment]] (graph invariant for every initiative).

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Catalog | The published set of certified [[Packaged Solution|Packaged Solutions]] | set | assumed |
| Submission gate | Intake + review workflow an author's solution passes before listing | struct | assumed |
| Certification bar | The trust/isolation/governance criteria a solution must meet to run inside a (sovereign) tenant | struct | assumed |
| Solution SDK | The packaging standard + tooling that makes a solution admissible and RackAI-aware | ref | assumed |
| Isolation model | How a third-party-authored solution is sandboxed within a tenant boundary | struct | assumed |
| Metering/attribution | Per-solution consumption capture (feeds [[Metering]] + the commercial model) | struct | assumed |
| Author identity | Scoped, attributable identity of the solution author (FDE/partner/customer) | ref | assumed |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Draft standard | SDK + certification bar being defined | Marketplace proposal adopted | Standard published |
| Open to supply | Authors can submit solutions to the standard | SDK + submission gate live | First solution certified |
| Operating | Certified solutions published + consumable in estates | ≥1 certified solution + isolation proven | — |
| Third-party open | Partners/customers (not just FDE) author to the standard | Trust/certification bar proven on FDE solutions | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| PUBLISHES | [[Packaged Solution]] | → | Distributes certified solutions to customers |
| GOVERNS | [[Packaged Solution]] | → | Certification + isolation gate every solution passes |
| ROUTES_TO | [[Model Deployment]] | → | Solution traffic routes into the serving chain via Model endpoints, never GPUs |
| CONSUMES | [[Governed Harness]] | → | Each solution bundles a harness that consumes RackAI inference |
| PRODUCES | [[Empirical Map]] | → | Solution runs are harness×model workloads — a cross-workload telemetry source that feeds the moat |
| USES | [[Agent Identity]] | → | Authors + running solutions act under scoped, attributable identities |
| GOVERNED_BY | [[AI Governance and Assurance]] | ← | Portfolio-wide governance plane sets the trust/isolation requirements |

## Graph Invariants

- A Packaged Solution routes into the serving chain via Model endpoints; it never bypasses [[Model Deployment]] or references GPUs directly (initiative invariant).
- RackAI owns the marketplace, SDK, certification, and isolation; it does **not** author the solutions (boundary convention above).
- The marketplace is a Consumption-layer channel; it does not redefine the [[Governed Harness]] or any platform capability (One-Concept Rule).
- Every solution's consumption is attributable to an author identity and metered (commercial + governance requirement).

## Why This Strengthens the Strategy (not just more surface area)

The corpus is deliberately skeptical of "build it because the platform could contain it." The marketplace earns its place on three grounds, each tied to an existing load-bearing concept:

1. **It feeds the moat.** Every solution is a [[Governed Harness|harness]]×[[Model]] pairing — exactly the unit the [[Empirical Map]] measures. More solutions running across estates → more cross-workload evidence → better placement → the moat compounds. The marketplace is a *telemetry source*, not just a storefront.
2. **It bends the labor curve.** An FDE solution authored once, instantiated many times, is the **workloads-per-operations-FTE** north-star metric ([[AI Operations Product]]) applied to *solutions* — demand that scales faster than FDE headcount. This is why it is a Proof-4 (*Operate at Scale*) surface.
3. **It makes the sovereign story sellable.** A packaged, distributable "RackAI-aware private assistant over your own corpus and your own models" ([[Sovereign Private Assistant]]) turns the alpha-leakage / sovereignty promise ([[Three Battlegrounds]]) into a product you can distribute, not a bespoke engagement each time.

## Open Questions

| Question | Affected Docs | Priority |
|----------|---------------|----------|
| Commercial model: rev-share with FDE/partner/customer authors, or bundled into Outcome as a Service? | [[Enterprise AI Cloud Product Model]], [[Commercial & Capacity Hub]] | High |
| What is the trust/certification bar for a third-party-authored solution to run inside a sovereign tenant? | [[AI Governance and Assurance]], [[Multi-Cluster Governance Brief (Partner)]] | High |
| Does the Solution SDK extend the existing P2 product surface (API/SDK/console), or is it a separate authoring kit? | [[RackAI Organizational Design]] | Medium |
| Sequencing: how early can a submission standard + one FDE reference solution start as a proving ground vs. full marketplace at Proof 4? | [[RackAI Roadmap]] | Medium |

## Evidence

- Source: 2026-10-06 PM/leadership marketplace discussion (drive consumption via FDE-authored agents/apps/harnesses, RackAI owns marketplace + governance + SDK). Precursors in the corpus: the Consumption layer of the [[Eight-Layer Stack]]; **Outcome as a Service** + the FDE cross-cutting engagement in the [[Enterprise AI Cloud Product Model]]; the FDE motion in [[AI Operations Product]]; the repeatable-harness-pattern framing in [[Governed Harness]].
- Confidence rationale: `assumed` — a proposed strategy direction. No capability is shipped; the SDK, certification gate, and marketplace surface do not exist.

## See Also

- [[Solution Marketplace PRD]] — the product requirements document for the rails (draft/proposed)
- [[Packaged Solution]] — the unit the marketplace distributes
- [[Sovereign Private Assistant]] — the canonical worked example of a Packaged Solution
- [[Enterprise AI Cloud Product Model]] — the offer boundary (Outcome as a Service) + RackAI ownership convention
- [[Eight-Layer Stack]] — the Consumption layer this surface lives at
- [[OpenRouter Initiative]] — the first consumption channel; this is the second
- [[AI Operations Product]] — the FDE motion whose output becomes distributable here
- [[Three Battlegrounds]] — the harness boundary this split mirrors
- [[Entity Ontology Hub]]
