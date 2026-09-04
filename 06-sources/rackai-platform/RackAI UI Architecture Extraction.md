---
id: src-rackai-ui-architecture
type: source
status: reviewed
owner: platform-eng
domain: platform
aliases: [rackai-ui, ui architecture, ui codebase extraction, rackai web console architecture]
related: [hub-rackai-platform, src-rackai-api-reference, src-rackai-console-docs]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: architectural extraction of the RackAI web UI codebase (entities, API surface, implied backend systems)."
---

# RackAI UI Architecture Extraction

## Provenance

- Origin: analysis of the `rackai-ui-main` codebase (RSS-Engineering/rackai-ui). The code itself is **not** copied into this repo (per the operating standard: extract, don't embed); this note records the extraction.
- Method: structured read of `src/api-client/`, `src/app/data/*/model.ts`, auth/OIDC config, build/deploy config.
- Classification: reference (derived from source code)

## Summary

React 18 + TypeScript SPA (Webpack 5, MUI, Redux Toolkit, Axios), Auth0 with a runtime-switchable Keycloak/OIDC shim, served as static files behind nginx. It is a front end over a **Kubernetes aggregated API** — every domain entity is a Custom Resource with `metadata`/`spec`/`status`/`conditions`.

**Entities (with status enums)** confirmed from `data/*/model.ts`: Model (SourceType URI/Upload; Phase Pending/Processing/Ready/Failed), ModelClass (Runtime vllm/nim/optimized-nim-vllm/aim), ModelDeployment (scaling, resources, LoRA, InferenceService ref, resolved accelerator SKUs), AcceleratorClass (nvidia/amd; allocatable/used capacity), FineTuningJob (methods supervised/reinforcement/dpo; SFT+QLoRA hyperparameters), LoRAAdapter, Dataset (Format messages/files), RegistryCredential (modelPull/license/imagePull), Organization (Auth0 → namespace).

**Implied backend systems:** K8s aggregated API, deployment/InferenceService operator, multi-engine serving runtime, model registry, dataset store, fine-tuning orchestrator, LoRA service, GPU fleet inventory, secret service, dual IdP integration, API gateway, analytics/billing hooks (Stripe/Amplitude).

## Conflicts Surfaced (do not hide)

1. **Fine-tuning methods:** the data model supports supervised / reinforcement / dpo, but the UI only wires **Supervised**; docs mark RL & DPO "Coming Soon." → open question.
2. **Deployment paths:** legacy Platform9 (RPM/scp) vs current Docker+Helm+nginx coexist in the codebase. → open question.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Domain CRDs → entities | [[Entity Ontology Hub]] (all L1 platform entities) | L1 |
| K8s aggregated control plane | [[RackAI Control Plane]] | L1 |
| Identity (Auth0/Keycloak, org→namespace) | [[Identity & Access Control]] | L2 |
| Fine-tuning orchestration | [[Fine-Tuning]] | L2 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
- [[Open Questions]]
