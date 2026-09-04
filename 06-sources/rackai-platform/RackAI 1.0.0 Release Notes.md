---
id: src-rackai-release-1-0-0
type: source
status: validated
owner: platform-eng
domain: platform
aliases: [rackai 1.0.0, release bulletin 1.0.0, rackai release notes]
related: [hub-rackai-platform, src-rackai-platform-prd, src-rackai-console-docs]
source_docs: []
confidence: measured
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI 1.0.0 release bulletin — the authoritative record of what actually shipped."
---

# RackAI 1.0.0 Release Notes

## Provenance

- Origin: `reference/rackai-platform/RackAI 1.0.0 - RackAI Docs.md` (docs.rackai.rax.io/release-notes/1.0.0/)
- Published: 2026-07-30
- Classification: reference (release record)

## Summary

The authoritative record of **shipped** RackAI capability at 1.0.0. This is the highest-authority source for "what exists today" and wins over PRD/spec claims when they conflict (per the shipped-beats-planned rule).

Shipped in 1.0.0:

- **Accelerator selection & scheduling** — `AcceleratorClass` with node affinity, `--accelerator-class` CLI flag, read-access RBAC.
- **AMD GPU support end to end** — AMD AIM inference runtime, fine-tuning on AMD GPUs, GPU-memory autoscaling on AMD nodes.
- **Accelerator inventory & visibility** — automated discovery, live capacity, GPU SKUs reported in `ModelDeployment` status.
- **Web console** — GPU Overview card, accelerator-aware UI, LoRA for AIM deployments, **Keycloak sign-in via an `@auth0/auth0-react` shim**, reconciliation polling.
- **Delivery** — container images (`rackspacengpc/…:1.0.0`), Helm umbrella chart (apiserver, frontproxy, manager, organizer, ui) + dataplane charts (SeaweedFS, CSI, monitoring, KEDA).

Control-plane components: `rackai-manager`, `rackai-organizer`, `rackai-stub`, `rackai-copier`, `rackai-model-downloader`, `rackai-trainer`, `rackai-evaluator`, `rackai-preprocessor`, `rackai-dataset-validator`, `rackai-ui`.

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Accelerator selection | [[Accelerator Class]] | L1 |
| Serving runtimes (vLLM/NIM/AIM) | [[Serving Runtime]] | L1 |
| Deployment status/SKU reporting | [[Model Deployment]] | L1 |
| Control plane components | [[RackAI Control Plane]] | L1 |
| Autoscaling (KEDA) | [[Autoscaling]] | L2 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
