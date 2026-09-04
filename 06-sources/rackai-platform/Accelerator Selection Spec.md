---
id: src-accelerator-selection-spec
type: source
status: reviewed
owner: infrastructure
domain: infrastructure
aliases: [accelerator selection tech spec, acceleratorclass spec, gpu selection]
related: [hub-rackai-platform, src-rackai-release-1-0-0]
source_docs: []
confidence: derived
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI Accelerator Selection technical spec (AcceleratorClass, GPU scheduling, node affinity)."
---

# Accelerator Selection Spec

## Provenance

- Origin: `reference/rackai-platform/Accelerator_Selection_TechSpec.docx`
- Classification: architecture

## Summary

Defines **AcceleratorClass** — the abstraction by which a Model Deployment selects hardware (GPU type/vendor, node affinity, resource sizing). Supports NVIDIA and AMD; exposes allocatable vs used device capacity via automated inventory discovery. Accelerator selection + scheduling and inventory shipped in 1.0.0 (see [[RackAI 1.0.0 Release Notes]]). This is the platform mechanism that binds the serving chain (Model Deployment → Serving Runtime → **Accelerator Class** → GPU fleet).

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Accelerator class / GPU selection | [[Accelerator Class]] | L1 |
| GPU scheduling | [[Standard Model Deployment]] | L2 |
| Fleet capacity visibility | [[Fleet Inventory]] | L4 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
