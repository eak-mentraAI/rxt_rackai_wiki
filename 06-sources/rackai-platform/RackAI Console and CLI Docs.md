---
id: src-rackai-console-docs
type: source
status: validated
owner: platform-eng
domain: product
aliases: [rackai console docs, welcome to rackai, rackai user guide, rackaictl]
related: [hub-rackai-platform, src-rackai-api-reference, src-rackai-release-1-0-0]
source_docs: []
confidence: measured
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI product documentation (web console + CLI/API user guide) — the shipped product experience and vocabulary."
---

# RackAI Console and CLI Docs

## Provenance

- Origin: `reference/rackai-platform/Welcome to RackAI (Console).md`, `RackAI User Guide (API & CLI).md`, `Quick Start - RackAI Docs.md`
- Classification: reference (product docs)

## Summary

The shipped product experience and the canonical user-facing vocabulary. Everything is scoped to an **Organization** (no self-service signup; Rackspace provisions via Auth0). Three product areas:

- **Inference** — Model Deployments (per-deployment OpenAI-compatible endpoint) and AI Studio (interactive chat testing).
- **Fine Tuning** — Datasets → Jobs (Supervised available; RL & DPO "Coming Soon") → LoRA Adapters.
- **Resources** — Models (catalog/registry) and Registry Credentials (Model Pull / License / Image Pull).

End-to-end flow: add credentials → confirm/add model → deploy → test in AI Studio → upload dataset → run fine-tuning job → apply resulting LoRA adapter.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Organization (tenant) | [[Organization]] | L1 |
| Model catalog | [[Model]] | L1 |
| Model deployment | [[Model Deployment]] | L1 |
| Datasets | [[Dataset]] | L1 |
| Fine-tuning jobs | [[Fine-Tuning Job]] | L1 |
| LoRA adapters | [[LoRA Adapter]] | L1 |
| Registry credentials | [[Registry Credential]] | L1 |
| Fine-tuning pipeline | [[Fine-Tuning]] | L2 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
