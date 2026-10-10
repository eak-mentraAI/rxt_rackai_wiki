---
id: ev-sovereign-private-assistant
type: evidence
status: draft
owner: rackai-product
domain: product
aliases: [sovereign private assistant, private chatgpt, sovereign chatgpt, rackai-aware assistant, private knowledge assistant, sovereign assistant reference solution]
related: [ent-packaged-solution, ent-solution-marketplace, ent-governed-harness, ent-model, ent-dataset, hub-battlegrounds, hub-ai-operations-product, hub-eac-product-model]
source_docs: ["01-entities/Packaged Solution.md", "01-entities/Solution Marketplace.md", "00-hub/Three Battlegrounds.md", "PM/leadership marketplace discussion 2026-10-06"]
confidence: assumed
last_reviewed: 2026-10-08
parent: hub-evidence
summary: "Worked Packaged Solution example: a ChatGPT-like assistant over a private corpus and the customer's sovereign models."
---

# Sovereign Private Assistant

> **Confidence: `assumed` — an illustrative reference example, not a shipped product.** This note is the **canonical worked example** of a [[Packaged Solution]] and of what the [[Solution Marketplace]] distributes. It exists to make the marketplace concept concrete; it does not assert a built capability or any performance number.

## What It Is

A **ChatGPT-like conversational interface** that is **RackAI-aware** and runs entirely within a customer's control boundary:

- the interface answers over a **private knowledge corpus** stored in **privately hosted Rackspace storage** (object or file);
- it reasons using the **customer's own sovereign models** (not a public frontier endpoint);
- it is **packaged as a single [[Packaged Solution]]** — harness + skills/tools + target models + corpus/storage binding — authored by an FDE and published to the [[Solution Marketplace]] for other RackAI customers to instantiate.

## The Concern It Solves — Alpha Leakage

The buyer problem: teams want a capable assistant over their proprietary knowledge, but sending that knowledge (and their questions about it) to a public frontier model risks **alpha leakage** — proprietary signal escaping the control boundary through prompts, context, or provider-side retention. For many regulated or competitively sensitive workloads, that risk makes public inference a non-starter ([[Three Battlegrounds]], "what *private* means — control over where data, models, inference, and operational context execute").

This solution removes the risk at the architecture level: **the corpus never leaves private Rackspace storage, and inference runs on the customer's sovereign models inside the estate.** The sovereignty promise becomes a concrete, distributable artifact rather than a bespoke engagement.

## How It Maps to the Canonical Model

| Packaged-Solution part | In this example | Canonical home |
|------------------------|-----------------|----------------|
| **Target outcome** | "Answer questions over our private corpus, safely" | [[Packaged Solution]] (business logic — author-owned) |
| **Harness** | Retrieval + context assembly + guardrails over the corpus | [[Governed Harness]] (RackAI machinery) |
| **Skills & tools** | Corpus search/retrieval, citation, redaction guardrail | [[Packaged Solution]] attributes |
| **Target models** | The customer's **sovereign** models | [[Model]] (served via [[Model Deployment]]) |
| **Corpus / storage binding** | Private Rackspace **object/file storage** holding the knowledge corpus | [[Dataset]] + CODB Object Store ([[RackAI Roadmap]]) |
| **Interface** | ChatGPT-like chat UI, RackAI-aware | the consumption surface of the solution |

## Why It Is a Good First Marketplace Example

- **It ties the whole stack together in one artifact** — storage + sovereign models + harness + a consumer interface — so it exercises the [[Packaged Solution]] definition end to end.
- **It is author-built, RackAI-governed** — an FDE authors it to the Solution SDK standard; RackAI certifies isolation (the corpus stays in-tenant) and publishes it. The [[Solution Marketplace]] boundary is demonstrated, not just asserted.
- **It is re-instantiable** — "private assistant over your corpus and your models" is a shape many customers want, so one FDE-authored solution serves many estates. That is the workloads-per-FTE leverage ([[AI Operations Product]]) the marketplace exists to create.
- **It feeds the moat** — each instantiation is a harness×model workload the [[Empirical Map]] records.

## Boundary Check (so "RackAI" does not leak upward)

- **RackAI (product org) provides:** the marketplace, the Solution SDK/standard, the certification + isolation gate, inference + model serving the harness consumes.
- **The FDE author provides:** the solution's goal, the retrieval/guardrail skills, the corpus binding, the chat experience — the **business logic**.
- **The customer provides / retains:** their corpus, their sovereign models, their control boundary.

This is the [[Three Battlegrounds]] harness boundary applied to a concrete solution: horizontal machinery is RackAI's; the differentiated outcome logic is the author's; the data and models stay the customer's.

## Open Questions

| Question | Affected Docs |
|----------|---------------|
| What is the minimum isolation certification that lets this run inside a *regulated/sovereign* tenant? | [[Solution Marketplace]], [[AI Governance and Assurance]] |
| Is the corpus binding a thin pointer to [[Dataset]] + Object Store, or does it need its own packaging primitive? | [[Packaged Solution]], [[RackAI Roadmap]] (CODB Object Store) |
| Commercial: is this bundled into Outcome as a Service, or listed with an author rev-share? | [[Enterprise AI Cloud Product Model]] |

## Evidence

- Source: 2026-10-06 marketplace discussion (the sovereign-ChatGPT-over-private-corpus example given as a representative Packaged Solution).
- Confidence rationale: `assumed` — an illustrative design, not a benchmarked or shipped solution. No performance or cost number is asserted; cost-per-outcome would be `measured` only from a real instantiation.

## Relationships

Typed edges (canonical types only). `→` = this note is the subject; `←` = the target is the subject (e.g. `CONSUMES ←` means the target consumes this note). Body tables above are kept as written.

| Relationship | Target | Direction | Notes |
|--------------|--------|-----------|-------|
| IMPLEMENTS | [[Packaged Solution]] | → | The unit this example instantiates |
| USES | [[Governed Harness]] | → | The machinery it wraps |
| USES | [[Model]] | → | Customer's sovereign models, served via [[Model Deployment]] |
| USES | [[Dataset]] | → | Private corpus binding |
| DEPENDS_ON | [[Solution Marketplace]] | → | Where it would be published |

## See Also

- [[Packaged Solution]] — the unit this example instantiates
- [[Solution Marketplace]] — where it would be published
- [[Governed Harness]] — the machinery it wraps
- [[Three Battlegrounds]] — the sovereignty + harness-boundary basis
- [[Evidence Hub]]
