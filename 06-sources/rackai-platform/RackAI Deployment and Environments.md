---
id: src-rackai-deployment-envs
type: source
status: validated
owner: infrastructure
domain: infrastructure
aliases: [rackai deployment docs, mainline environments, cluster deployment, opencenter setup]
related: [hub-rackai-platform, src-rackai-release-1-0-0]
source_docs: []
confidence: measured
last_reviewed: 2026-09-04
parent: hub-rackai-platform
summary: "Source: RackAI deployment, cluster setup, and mainline dev/staging/production environment docs."
---

# RackAI Deployment and Environments

## Provenance

- Origin: `reference/rackai-platform/Main-line - RackAI Docs.md`, `RackAI Deployment - RackAI Docs.md`, `Cluster Deployment - RackAI Docs.md`, `openCenter Cluster Setup.md`, `Installation - RackAI Docs.md`, `Project-Specific - RackAI Docs.md`
- Classification: reference / operational

## Summary

How RackAI is deployed and where it runs. Mainline environments follow a **dev → staging → production** progression under `*.rackai.rax.io` on Rackspace undercloud bare-metal Kubernetes:

- **dev** (`dev.rackai.rax.io`) — building.
- **staging** (`rackai-one.staging.rax.io`) — active; nodes include 4×H100, 2×L4, 4×L40 (only H100s currently usable).
- **production** (`rackai.rax.io`) — **planned** (K8s provider/platform TBD).

Cluster deployment uses the `rackai.deploy_rackai` Ansible collection (Kubespray-based) plus add-ons (Calico, MetalLB, Longhorn, cert-manager); GitOps via openCenter. This grounds the **Environment** entity and confirms **single-cluster, single-region** today (no multi-region — relevant to the [[OpenRouter Initiative]] P1 gap).

## Concepts Extracted

| Concept | Canonical Note | Layer |
|---------|----------------|-------|
| Environments (dev/staging/prod) | [[Environment]] | L1 |
| Cluster / single-region footprint | [[GPU Cluster]], [[Region]] | L1 |
| Deployment tooling | [[RackAI Control Plane]] | L1 |

## See Also

- [[Source Inventory]]
- [[Source-to-Concept Crosswalk]]
