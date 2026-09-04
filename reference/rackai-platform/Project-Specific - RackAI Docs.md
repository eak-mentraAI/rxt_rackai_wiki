---
title: "Project-Specific - RackAI Docs"
source: "https://docs.rackai.rax.io/getting-started/environments-customer/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## Customer / Project-Specific RackAI Environments

This page is the source of truth for RackAI environments dedicated to a specific customer or internal effort. Each environment is a Kubernetes cluster; the summary table gives a quick inventory, and the sections below capture the full detail for each one.

For the canonical dev/staging/production progression, see [Main-line Environments](https://docs.rackai.rax.io/getting-started/environments-mainline/).

To update it, edit `docs/getting-started/environments-customer.md` and keep the summary table and detail sections in sync.

## Summary

| Environment | Tier | Domain | K8s provider | Platform | Status |
| --- | --- | --- | --- | --- | --- |
| [pmk](https://docs.rackai.rax.io/getting-started/environments-customer/#pmk) | Dev | [aurora-ai.platform9.horse](https://aurora-ai.platform9.horse/) | Platform9 Kubernetes | Spot/Flex | Active |
| [spot](https://docs.rackai.rax.io/getting-started/environments-customer/#spot) | Dev | [aurora-aicluster.platform9.horse](https://aurora-aicluster.platform9.horse/) | Rackspace Spot | Spot/Flex | Active |
| [opencenter](https://docs.rackai.rax.io/getting-started/environments-customer/#opencenter) | Dev | [opencenter.rackai.rax.io](https://opencenter.rackai.rax.io/) | TBD | OSPC | Active |
| [rackai-k3s-amd-staging](https://docs.rackai.rax.io/getting-started/environments-customer/#rackai-k3s-amd-staging) | Staging | [amd.rackai.rax.io](https://amd.rackai.rax.io/) | Self-managed k3s | Rackspace VMs - SR-IOV | Active |
| [uniphore](https://docs.rackai.rax.io/getting-started/environments-customer/#uniphore) | Production | [uniphore.rackai.rax.io](https://uniphore.rackai.rax.io/) | Rackspace undercloud | Undercloud - BareMetal | Active |

## pmk

Tier

Development

Public domain

[https://aurora-ai.platform9.horse](https://aurora-ai.platform9.horse/)

K8s cluster access

Log in to PMK at [pf9-ngpc-clusters-iv.platform9.net](https://pf9-ngpc-clusters-iv.platform9.net/ui/infrastructure/clusters/managed/qbert/cf4cd7ca-0f71-4d31-ae5b-bbaf80586f52/nodes) and download your kubeconfig.

K8s provider

Platform9 Kubernetes

Platform

Spot/Flex

Nodes

3 × A30 (1 GPU per node)

Load balancer

`rackai-frontproxy` — 66.70.103.69 (30947)  
`envoy-gateway` — 66.70.103.9 (30490)

Notes

Used for UI and accelerator-class testing.

## spot

Tier

Development

Public domain

[https://aurora-aicluster.platform9.horse](https://aurora-aicluster.platform9.horse/)

K8s cluster access

Log in to [spot.rackspace.com](https://spot.rackspace.com/), use org `aurora-platform`, and get your own kubeconfig for the `aurora-data-plane` cluster.

K8s provider

Rackspace Spot

Platform

Spot/Flex

Nodes

2 × A30 (1 GPU per node)

Load balancer

TBD

Notes

Currently used by folks at Rackspace for monitoring work.

## opencenter

Tier

Development

Public domain

[https://opencenter.rackai.rax.io](https://opencenter.rackai.rax.io/)

K8s cluster access

Kubeconfig available at [Password Safe project 43080](https://passwordsafe.corp.rackspace.com/projects/43080), under the Kubeconfigs category. The credential field must be base64-decoded before use: `cat <credential> | base64 -d`

K8s provider

TBD

Platform

OSPC

Nodes

TBD

Load balancer

TBD

Notes

Used for OpenCenter integrated development work.

## rackai-k3s-amd-staging

Tier

Staging — AMD GPU

Public domain

[https://amd.rackai.rax.io](https://amd.rackai.rax.io/)

K8s cluster access

SSH bastion only. The kubeconfig lives at `/etc/rancher/k3s/k3s.yaml` on node-1. Port `6443` is not reachable directly (`INPUT DROP` plus a source allowlist), so tunnel through the bastion or work on-node.

K8s provider

Self-managed k3s v1.32.9+k3s1 (embedded etcd, 3 servers)

Platform

Rackspace VMs with SR-IOV AMD GPU passthrough (MI350X VF)

Nodes

4 × identical nodes — 1 × MI350X VF 288GB, EPYC 9575F 24 vCPU, 251 GiB RAM, 720G root + 5T Longhorn  
`rackspace-1` / `rackspace-2` / `rackspace-3` — server + etcd  
`rackspace-4` — agent

Load balancer

k3s ServiceLB (klipper) — every Service is advertised on all 4 node IPs. No MetalLB: the servers span three /24s, so L2 mode would not work.  
KServe gateway on `:80`, `rackai-frontproxy` on `:443`.

Storage

Longhorn 1.12.1 — 2 replicas, `reclaimPolicy=Delete`, reserve and min-available both 10% → ~9.8 TB usable for PVCs.  
SeaweedFS — 10 volume servers × 100Gi, `defaultReplication=000` (Longhorn owns redundancy) → ~1 TB model storage.

Notes

Running RackAI 1.1.0-rc.1 with 2 models serving. Inference domain is `rax.io`; the `*.rackai.rax.io` TLS certificate expires 30 Dec 2026.  
AMD GPU Operator v1.5.1 with `driver.enable=false` (host ROCm 7.14.0); the DeviceConfig selector is overridden to `amd-vgpu` to pick up the SR-IOV VFs.  
The AI-cluster client uses an in-cluster kubeconfig via the `rackai-aicluster` service account; that token expires 2027-08-25.

Known issues

`amd-aim-pull-secret` is missing, so the recipe-sync Job stays Pending and holds 1 of the 4 GPUs; the manager crashloops roughly every 5.5 minutes.  
There is no explicit `:443` firewall rule — external access currently relies on the existing source allowlist.

## uniphore

Tier

Production

Public domain

[https://uniphore.rackai.rax.io](https://uniphore.rackai.rax.io/)

K8s cluster access

Kubeconfig available at [Password Safe project 43080](https://passwordsafe.corp.rackspace.com/projects/43080), under the Kubeconfigs category. The credential field must be base64-decoded before use: `cat <credential> | base64 -d`

K8s provider

Rackspace undercloud

Platform

Undercloud - BareMetal

Nodes

8 × H100 (across 2 nodes)

Load balancer

TBD

Notes

Production environment used by Uniphore.