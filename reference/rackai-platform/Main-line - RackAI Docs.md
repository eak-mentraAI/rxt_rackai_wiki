---
title: "Main-line - RackAI Docs"
source: "https://docs.rackai.rax.io/getting-started/environments-mainline/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## Main-line RackAI Environments

This page is the source of truth for the main-line RackAI environments — the canonical dev → staging → production progression for the flagship RackAI deployment, reachable under the `*.rackai.rax.io` domain. The summary table gives a quick inventory, and the sections below capture the full detail for each one.

For environments dedicated to a specific customer or project, see [Customer / Project-Specific Environments](https://docs.rackai.rax.io/getting-started/environments-customer/).

To update it, edit `docs/getting-started/environments-mainline.md` and keep the summary table and detail sections in sync.

## Summary

| Environment | Tier | Domain | K8s provider | Platform | Undercloud | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [dev](https://docs.rackai.rax.io/getting-started/environments-mainline/#dev) | Dev | [dev.rackai.rax.io](https://dev.rackai.rax.io/) | Rackspace undercloud | Undercloud - BareMetal | `uc_iad3_staging` | Building |
| [staging](https://docs.rackai.rax.io/getting-started/environments-mainline/#staging) | Staging | [rackai-one.staging.rax.io](https://rackai-one.staging.rax.io/) | Rackspace undercloud | Undercloud - BareMetal | `rax-prod-dfw3` | Active |
| [production](https://docs.rackai.rax.io/getting-started/environments-mainline/#production) | Production | [rackai.rax.io](https://rackai.rax.io/) | TBD | TBD | `rax-prod-dfw3` | Planned |

## dev

Tier

Development

Public domain

[https://dev.rackai.rax.io](https://dev.rackai.rax.io/)

K8s cluster access

Kubeconfig available at [Password Safe project 43080](https://passwordsafe.corp.rackspace.com/projects/43080), under the Kubeconfigs category. The credential field must be base64-decoded before use: `cat <credential> | base64 -d`

K8s provider

Rackspace undercloud

Platform

Undercloud - BareMetal

Undercloud

`uc_iad3_staging` (IAD3)

Nodes

TBD

Servers

Primary management interface (`mgmt.102`) hostnames and IP addresses:

| Hostname | Role | mgmt.102 IP |
| --- | --- | --- |
| rackai-dev-cp-0 | Control plane | 10.97.6.54 |
| rackai-dev-cp-1 | Control plane | 10.97.6.36 |
| rackai-dev-cp-2 | Control plane | 10.97.6.51 |
| rackai-dev-wrk-0 | Worker | 10.97.6.47 |
| rackai-dev-wrk-1 | Worker | 10.97.6.58 |

Kubernetes API VIP (kube-vip on `mgmt.102`): `10.97.6.62`.

SSH access

Log in as the `ubuntu` user over the management VLAN IP shown above. Your public key must be registered with the environment's OpenStack keypair (`rackai-dev-key`).

```bash
ssh ubuntu@<mgmt.102-ip>
```

Example — first control-plane node:

```bash
ssh ubuntu@10.97.6.54
```

Notes

Environment under construction.

## staging

Tier

Staging

Public domain

[https://rackai-one.staging.rax.io](https://rackai-one.staging.rax.io/)

K8s cluster access

Kubeconfig available at [Password Safe project 43080](https://passwordsafe.corp.rackspace.com/projects/43080), under the Kubeconfigs category. The credential field must be base64-decoded before use: `cat <credential> | base64 -d`

K8s provider

Rackspace undercloud

Platform

Undercloud - BareMetal

Undercloud

`rax-prod-dfw3` (DFW3)

Nodes

4 × H100 (single node)  
2 × L4 (single node)  
4 × L40 (single node)

Servers

Primary management interface (`mgmt.102`) hostnames and IP addresses:

| Hostname | Role | mgmt.102 IP |
| --- | --- | --- |
| rackai-stg-cp-0 | Control plane | 10.26.16.49 |
| rackai-stg-cp-1 | Control plane | 10.26.16.58 |
| rackai-stg-cp-2 | Control plane | 10.26.16.43 |
| rackai-stg-wk-0 | Worker | 10.26.16.40 |
| rackai-stg-wk-1 | Worker | 10.26.16.38 |
| rackai-stg-wk-2 | Worker | 10.26.16.53 |

Kubernetes API VIP (kube-vip on `mgmt.102`): `10.26.16.35`.

SSH access

Log in as the `ubuntu` user over the management VLAN IP shown above. Your public key must be registered with the environment's OpenStack keypair (`rackai-staging-key`).

```bash
ssh ubuntu@<mgmt.102-ip>
```

Example — first control-plane node:

```bash
ssh ubuntu@10.26.16.49
```

Notes

Only the H100s are currently usable.

## production

Tier

Production

Public domain

[https://rackai.rax.io](https://rackai.rax.io/)

K8s cluster access

TBD

K8s provider

TBD

Platform

TBD

Undercloud

`rax-prod-dfw3` (DFW3)

Nodes

TBD

Servers

Primary management interface (`mgmt.102`) hostnames and IP addresses:

| Hostname | Role | mgmt.102 IP |
| --- | --- | --- |
| rackai-prd-cp-0 | Control plane | 10.26.16.133 |
| rackai-prd-cp-1 | Control plane | 10.26.16.156 |
| rackai-prd-cp-2 | Control plane | 10.26.16.145 |
| rackai-prd-worker-0 | Worker | 10.26.16.148 |
| rackai-prd-worker-1 | Worker | 10.26.16.143 |

Kubernetes API VIP (kube-vip on `mgmt.102`): `10.26.16.158`.

SSH access

Log in as the `ubuntu` user over the management VLAN IP shown above. Your public key must be registered with the environment's OpenStack keypair (`rackai-prod-key`).

```bash
ssh ubuntu@<mgmt.102-ip>
```

Example — first control-plane node:

```bash
ssh ubuntu@10.26.16.133
```

Notes

—