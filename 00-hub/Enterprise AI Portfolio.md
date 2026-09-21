---
id: hub-enterprise-ai
type: hub
status: draft
owner: product
domain: strategy
aliases: [enterprise ai, enterprise ai portfolio, enterprise ai offering, portfolio view]
related: [hub-root, hub-rackai-platform, hub-product, hub-openrouter, src-rackai-dev-plan, hub-battlegrounds, hub-load-bearing-bets, evd-sovereign-governed-competitors]
source_docs: ["reference/rackai_dev_plan 2.docx"]
confidence: assumed
last_reviewed: 2026-09-17
parent: hub-root
summary: "Portfolio view: the broadly-scoped Enterprise AI offering under which RackAI is the product surface sold as SKUs."
---

# Enterprise AI Portfolio

**Enterprise AI** is the **portfolio view** — a broadly-scoped collection of products and capabilities that turns the AI stack into something a regulated enterprise can run. **[[RackAI Platform|RackAI]]** is the **product view**: the narrowly-defined, SKU-packaged product that provides the inference-and-below foundation plus the governance and assurance built into it.

> **Portfolio vs product.** Enterprise AI (portfolio) ⊃ RackAI (product) + partner-packaged components (Palantir) + integration with the customer's data foundation. RackAI is one product in the portfolio; it is the foundation the rest builds on. This distinction comes from the [[RackAI Enterprise AI Development Plan]] and is `assumed` confidence pending ratification.

## What Sits in the Portfolio

| Element | Kind | Relationship |
|---------|------|--------------|
| [[RackAI Platform]] | Product (ours) | Foundation — infrastructure up to inference, plus governance/assurance we build in |
| Palantir (Foundry / AIP) | Partner-packaged product | Ontology, authorization, provenance, context assembly, data — sits on top of compute |
| Customer data foundation | Integrated, not built | Customer's own, Palantir, or Uniphore; customer holds their own data and weights |
| Uniphore consumption apps | Consumption surface | End-user assistants, prebuilt apps, no-code builder — a consumption route |

## Two Things This Portfolio Does

Per the dev plan, the work is *enhance RackAI* (harden and extend the inference platform) and *build the Enterprise AI offering* (the governed, operated layer on top). For now the portfolio builds **above the data layer** and integrates with whatever data foundation the customer runs.

## Distribution Channels vs Portfolio

The [[OpenRouter Initiative|OpenRouter inference program]] is **not** a portfolio peer — it is a **distribution channel** for RackAI-served GPU capacity, sitting under inference/serving. Direct tenant consumption is the other channel. Both consume the RackAI product; neither is a separate portfolio product.

## Programs Behind the Portfolio

The dev plan organizes the build into five programs plus productization/ops (P1–P9), on a dev track and a research track. These are captured faithfully in the source companion and mapped to canonical concepts via the [[Eight-Layer Stack]] view:

- **Program 1** — build and operate the governed harness ([[Governed Harness]], [[Empirical Map]], [[Request Routing]])
- **Program 2** — govern and assure inside the perimeter ([[Verification]], [[Perimeter Information-Flow Control]], [[Agent Identity]], [[Governable Self-Modification]])
- **Program 3** — measurement and self-improvement ([[Verification]], [[Loop Planning & Credit Assignment]], [[Self-Improvement Loop]])
- **Program 4** — model and inference maturity bet (AMD/ROCm inference, edge–core, fine-tuning for evolving data)
- **Program 5** — economics of the running system ([[AI FinOps]], the cost loop)

## Partner Bets

The partner elements of this portfolio (Palantir, Uniphore, and the Across.AI candidate) are tracked as **load-bearing bets** in [[Load-Bearing Bets]], mapped to the [[Three Battlegrounds|operator stack]] with the gap each fills and an exit criterion. That note also proposes new bets in the operating layer and its inputs (regulated data/context, governance/assurance, capacity supply, silicon/runtime) and holds the **Palantir architecture + commercial boundary**.

## Related Hubs

- [[Rack AI Knowledge Base]]
- [[RackAI Platform]]
- [[Product Hub]]
- [[Load-Bearing Bets]]
- [[Three Battlegrounds]]
- [[Eight-Layer Stack]]
