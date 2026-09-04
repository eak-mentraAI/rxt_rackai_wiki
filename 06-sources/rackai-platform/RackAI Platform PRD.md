---
id: src-rackai-platform-prd
type: source
status: reviewed
owner: platform-eng
domain: platform
aliases: [rmpai prd, rackai prd, platform prd, uniphore la prd]
related: [hub-rackai-platform, src-rackai-release-1-0-0, src-rackai-api-reference]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: the north-star PRD defining the RackAI (RMPAI) enterprise AI platform vision, users, and requirements."
---

# RackAI Platform PRD (RMPAI)

## Provenance

- Origin: `reference/rackai-platform/PRD - RackAI (Uniphore) - LA.docx`
- Author / owner: RMPAI product team (Amine Badaoui)
- Version: Draft — 2026-03-10
- Classification: strategy / planning

> **Naming:** this PRD calls the product **RMPAI**. That is an alias of **RackAI** (canonical). Do not model RMPAI as a separate product.

## Summary

North-star PRD for a **private, cloud-agnostic enterprise AI platform** for inference, fine-tuning, governance, and developer experience. Positions RackAI to match managed-service developer experience while preserving infrastructure control, cost transparency, portability, and governance. Key strategic differentiators: cloud-agnostic Kubernetes footprint, unified multi-engine inference (vLLM, TensorRT-LLM, SGLang, NVIDIA NIM), integrated fine-tuning (SFT, RL alignment, LoRA/QLoRA), and performance optimizations (dynamic batching, prompt caching, speculative decoding) as product capabilities.

## Shipped vs. Planned

Much of this PRD is **aspirational** (Draft). Where it describes capabilities not in the [[RackAI 1.0.0 Release Notes]] (e.g. TensorRT-LLM/SGLang runtimes, RL fine-tuning, quotas, billing, smart routing), those concepts are modeled at `assumed` confidence until shipped. Notably, **"LLM-as-a-Service" (multi-model serving, usage metering, routing, tenant controls)** appears here as a use case — relevant to the [[OpenRouter Initiative]] but not shipped.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| The platform itself | [[RackAI Platform]] | hub |
| Multi-engine inference | [[Serving Runtime]] | L1 |
| Fine-tuning workflows | [[Fine-Tuning]] | L2 |
| Governance / quotas / billing (planned) | [[Billing & Payment]] | L3 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
