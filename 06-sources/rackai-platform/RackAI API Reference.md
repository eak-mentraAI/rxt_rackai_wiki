---
id: src-rackai-api-reference
type: source
status: validated
owner: platform-eng
domain: platform
aliases: [rackai api reference, api reference, rackai rest api]
related: [hub-rackai-platform, src-rackai-console-docs, src-rackai-ui-architecture]
source_docs: []
confidence: measured
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI REST API reference — the resource + identity API surface and inference endpoints."
---

# RackAI API Reference

## Provenance

- Origin: `reference/rackai-platform/RackAI API Reference.md`
- Classification: reference (API spec)

## Summary

Authoritative API surface for RackAI. Two planes:

- **Resource plane** — Kubernetes aggregated API at `/apis/rackai.rackspace.com/v1alpha1`, namespaced CRUD over the domain CRDs (Model, ModelClass, ModelDeployment, Dataset, FineTuningJob, LoRAAdapter, RegistryCredential, AcceleratorClass), reconciliation via `status`/`conditions`/`observedGeneration`.
- **Identity plane** — `/apis/auth.rackai.io/v1` for organization/auth resources.

**Inference** is OpenAI-compatible, served per deployment at `{inferenceEndpointURI}/v1/chat/completions` (and `/v1/completions`), plus `/v1/models`, with streaming supported.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Resource API / control plane | [[RackAI Control Plane]] | L1 |
| OpenAI-compatible serving | [[Serving Runtime]], [[Model Deployment]] | L1 |
| Identity / org API | [[Organization]], [[Identity & Access Control]] | L1/L2 |
| API keys (planned) | [[API Key]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
