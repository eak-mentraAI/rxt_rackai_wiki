---
id: ent-packaged-solution
type: entity
status: draft
owner: rackai-product
domain: product
aliases: [packaged solution, solution package, marketplace solution, packaged outcome, solution artifact, agent package, harness package, published solution]
related: [ent-solution-marketplace, ent-governed-harness, ent-model, ent-model-deployment, ent-dataset, ent-agent-identity, ent-empirical-map, hub-entities, hub-eac-product-model, hub-ai-operations-product, hub-battlegrounds]
source_docs: ["00-hub/Enterprise AI Cloud Product Model.md", "01-entities/Governed Harness.md", "00-hub/AI Operations Product.md", "PM/leadership marketplace discussion 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-06
parent: hub-entities
summary: "Canonical entity (proposed): Solution Marketplace unit — harness, skills/tools, target models, corpus binding."
---

# Packaged Solution

> **Confidence: `assumed` — proposed, not adopted.** The distributable unit of the [[Solution Marketplace]], defined here so the marketplace has something concrete to publish. Nothing is shipped; adoption follows the marketplace proposal on the [[RackAI Roadmap]].

## Definition

A **Packaged Solution** is a distributable artifact that bundles everything needed to deliver a **specific outcome** on top of RackAI: a [[Governed Harness|harness]] pattern, its **skills and tools**, the **target models** it runs against, and a **corpus / storage binding** (where its knowledge and data live). It is authored by an **FDE** (first and canonically), submitted to the [[Solution Marketplace]], certified, and then **instantiated** inside a customer's estate — once authored, many times instantiated.

It is deliberately **more than a [[Governed Harness]]**. The harness is the *execution scaffolding* around a model (context, tools, memory, control flow, guardrails). A Packaged Solution *contains* a harness but adds the parts that make it a shippable product: the target-outcome definition, the skill/tool set bound to that outcome, the model selection, the data/corpus binding, and the packaging metadata the marketplace needs (author identity, certification record, instantiation parameters). The harness is horizontal machinery; the Packaged Solution is the **business logic** wrapped around it.

> **Boundary note (built *on* RackAI, not *is* RackAI).** Per the [[Three Battlegrounds]] harness boundary and the [[Enterprise AI Cloud Product Model]] boundary (RackAI = operating platform: **core + rails**): the solution is **authored on the RackAI rails** (SDK, marketplace, packaging/certification) and wraps a harness whose **runtime interface is part of RackAI**, but the **solution's goal, skills, and workflow are business logic** owned by the author (FDE/partner/customer). A Packaged Solution is therefore an **Outcome as a Service** artifact that is *built on* RackAI — not a RackAI platform capability. This is the same line the harness boundary draws; the Packaged Solution just makes the business-logic side a distributable thing.

## Layer

L1 — Entity Ontology, at the **Consumption** layer, bundling down into the harness/serving chain:

**Market Demand → [[Solution Marketplace]] → Packaged Solution → [[Governed Harness]] → [[Model]] → [[Model Deployment]] → [[Serving Runtime]] → [[Capacity Pool]] → [[GPU Fleet]] → [[Topology]]**

A Packaged Solution is published and governed by the [[Solution Marketplace]]; it wraps a [[Governed Harness]] and binds target models + a corpus. It routes into the serving chain via Model endpoints — never GPUs directly.

## Attributes

| Attribute | Description | Type | Confidence |
|-----------|-------------|------|:----------:|
| Target outcome | The specific business outcome the solution serves | struct | assumed |
| Harness | The [[Governed Harness]] pattern it instantiates | ref | assumed |
| Skills & tools | The skill/tool set bound to the outcome | set | assumed |
| Target models | The model(s) it runs against — including a customer's **sovereign** models | set | assumed |
| Corpus / storage binding | Where the solution's knowledge/data live (e.g. private Rackspace object/file storage) | ref | assumed |
| Author identity | Scoped, attributable identity of the author (FDE/partner/customer) | ref | assumed |
| Certification record | Evidence the solution passed the marketplace trust/isolation bar | struct | assumed |
| Instantiation parameters | What a customer sets when instantiating it in their estate | struct | assumed |
| Cost per outcome | Measured from first instantiation (→ [[Cost per Outcome]]) | metric | assumed |

## Lifecycle States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| Authored | FDE builds the solution to the Solution SDK standard | SDK available | Submitted |
| Submitted | Entered into the marketplace submission gate | Author submits | Certified or rejected |
| Certified | Passed the trust/isolation/governance bar | Certification bar met | Published |
| Published | Listed + consumable in the [[Solution Marketplace]] | Certification + listing | Instantiated / delisted |
| Instantiated | Running inside a customer estate | Customer deploys it | Retired |
| Retired | Superseded or decommissioned | — | — |

## Relationships

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| BELONGS_TO | [[Solution Marketplace]] | → | Published + governed by the marketplace |
| USES | [[Governed Harness]] | → | Wraps a harness pattern as its execution machinery |
| CONSUMES | [[Model Deployment]] | → | Runs against model endpoints, never GPUs |
| USES | [[Model]] | → | Targets specific (incl. sovereign/customer-owned) models |
| USES | [[Dataset]] | → | Binds a corpus / storage source for its knowledge |
| MEASURED_BY | [[Empirical Map]] | → | Each instantiation is a harness×model workload recorded as cross-workload evidence |
| USES | [[Agent Identity]] | → | Runs under a scoped, attributable identity |

## Graph Invariants

- A Packaged Solution routes into the serving chain via Model endpoints; it never bypasses [[Model Deployment]] or references GPUs directly.
- A Packaged Solution contains exactly one [[Governed Harness]] pattern; it does not redefine the harness (One-Concept Rule — the harness stays canonical in [[Governed Harness]]).
- The harness is RackAI-enabled machinery; the solution's goal/skills/workflow are author-owned business logic (harness boundary).
- Every instantiation is attributable to an author identity and metered.

## Evidence

- Source: 2026-10-06 marketplace discussion (agents with skills, tools, packaged in harnesses that serve specific outcomes; corpus-storage + sovereign-model example). Builds on the [[Governed Harness]] "many harnesses, one per workload — a repeatable *pattern*" framing and the **Outcome as a Service** offer in the [[Enterprise AI Cloud Product Model]].
- Confidence rationale: `assumed` — the packaging standard and the artifact do not exist yet. [[Sovereign Private Assistant]] is the first worked example.

## See Also

- [[Solution Marketplace]] — where Packaged Solutions are published + governed
- [[Sovereign Private Assistant]] — the canonical worked example
- [[Governed Harness]] — the execution machinery a solution wraps
- [[Enterprise AI Cloud Product Model]] — the Outcome-as-a-Service offer this resolves into
- [[Three Battlegrounds]] — the harness/business-logic boundary
- [[Entity Ontology Hub]]
