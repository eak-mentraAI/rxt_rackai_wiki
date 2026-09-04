---
id: chg-2026-09-04-rackai-platform-rescope
type: change
status: draft
owner: knowledge-graph-steward
domain: governance
aliases: [rackai platform rescope, platform rescope change, openrouter-as-initiative rescope]
related: [hub-rackai-platform, hub-openrouter, hub-root, idx-source-inventory, idx-crosswalk, idx-open-questions]
source_docs: [rackai_platform_prd, rackai_release_1_0_0, rackai_api_reference, rackai_console_docs, rackai_deployment_envs, rackai_ui_architecture, identity_access_spec, metering_spec, monitoring_audit_spec, accelerator_selection_spec]
confidence: derived
last_reviewed: 2026-09-04
parent: hub-wiki
summary: "Rescoped the corpus from the OpenRouter inference program to the RackAI platform, with OpenRouter as one initiative."
---

# 2026-09-04 — RackAI Platform Rescope

## Trigger

Business decision: this knowledge base becomes the **RackAI platform** knowledge base, with the OpenRouter inference program modeled as **one initiative** on top of the platform (not the top-line scope). Authoritative RackAI reference material (PRDs, technical specs, product/console/CLI docs, API reference, deployment/environment docs, and the web-UI codebase) was brought in as source, and the platform concepts were modeled into the graph.

Decisions locked: **RackAI** is the canonical product name (`RMPAI` and `RackAI Aurora` are aliases); model domain concepts, not UI components; executed in committable stages.

## Objects Changed

### Governance & standards
- `init/init.md`, `.kiro/steering/rackai-operating-standards.md`, `.kiro/steering/agent-behavior.md` — rescoped to RackAI platform; truth hierarchy gained a "RackAI platform product specs" tier + a **shipped-beats-planned** rule; graph invariants gained tenancy, fine-tuning, and initiative-attachment invariants; canonical-name rule added.

### Hubs (00-hub)
- Added [[RackAI Platform]] (hub-rackai-platform) and [[OpenRouter Initiative]] (hub-openrouter).
- Reframed [[Rack AI Knowledge Base]] (root) to platform scope with platform+initiatives and serving-chain diagrams.
- Reframed [[Product Hub]] as the OpenRouter initiative's strategy; broadened [[Commercial & Capacity Hub]] intro; regrouped [[Entity Ontology Hub]] and extended [[Operations Hub]].

### Reference relocation
- `reference/rackai-platform/` (22 authoritative RackAI docs) and `reference/openrouter/` (OpenRouter docx + git-ignored annotations); `reference/README.md` added; `.gitignore` updated.

### Sources (06-sources)
- Added 9 RackAI platform source notes under `06-sources/rackai-platform/`; split [[Source Inventory]] into OpenRouter-initiative and RackAI-platform sections; added 11 rows to [[Source-to-Concept Crosswalk]].

### Entities added (01-entities / 03-commercial)
- [[Organization]], [[Model Class]], [[Dataset]], [[Fine-Tuning Job]], [[LoRA Adapter]], [[Registry Credential]], [[Accelerator Class]], [[RackAI Control Plane]], [[Environment]], [[API Key]], [[OpenRouter Private Model Integration]], [[Model Catalog Endpoint]], [[Billing & Payment]].

### Workflows added (02-operations/workflows)
- [[Fine-Tuning]], [[Identity & Access Control]], [[Metering]], [[Monitoring & Observability]], [[Audit]].

### Entities extended in place (reconciled with K8s CRD reality)
- [[Model]], [[Model Deployment]], [[Serving Runtime]] — added tenancy/accelerator/fine-tuning/model-class relationships and shipped-runtime facts without discarding the OpenRouter framing.

### Indexes / glossary
- [[Entity Index]] regrouped and extended; [[Glossary]] gained RackAI, Organization, Model Class, Accelerator Class, LoRA/QLoRA, Metering-vs-Billing, and OpenRouter Private Model entries + the canonical-name note.

## Confidence Changes

| Note | Confidence | Reason |
|------|:----------:|--------|
| Shipped-platform entities (Organization, Model Class, Dataset, Fine-Tuning Job, LoRA Adapter, Registry Credential, Accelerator Class, Control Plane, Environment) | measured | Grounded in RackAI 1.0.0 docs / API reference |
| [[API Key]], [[Metering]], [[Audit]], [[Model Catalog Endpoint]], [[Billing & Payment]] | assumed | Planned/gap — not shipped |
| [[OpenRouter Private Model Integration]] | derived | Building blocks exist; end-to-end unvalidated |
| [[Fine-Tuning Job]] | measured (SFT) / assumed (RL, DPO) | RL & DPO "Coming Soon" |

## Conflicts Surfaced (not hidden)

1. **Fine-tuning methods** — data model advertises supervised/reinforcement/dpo; only Supervised is shipped. → Open Question.
2. **Dual deployment paths** — legacy Platform9 vs current Docker+Helm+nginx. → Open Question.
3. **Billing gap** — billing is an explicit non-goal yet a P0 for the OpenRouter public-provider path. → Open Question.
4. **API Key ship status** — primary dependency for OpenRouter Path A; shipped-vs-planned unconfirmed. → Open Question.

All four recorded in [[Open Questions]].

## Fitness / Consistency Result

- **Structural:** Pass — all touched files pass `scripts/lint-frontmatter.sh`; full-corpus wikilink scan shows no real unresolved links; no duplicate IDs; new hub/entity IDs unique.
- **Story consistency:** Pass — one coherent story (RackAI platform; OpenRouter as an initiative); shipped vs planned honestly separated; conflicts surfaced not smoothed; canonical name enforced with aliases.
- **Layer integrity:** Pass — initiatives attach above Demand and route through Model endpoints; no layer-skipping; tenancy invariant added.

See [[CONSISTENCY_REPORT]] for the detailed pass.

## See Also

- [[RackAI Platform]]
- [[OpenRouter Initiative]]
- [[Wiki Hub]]
