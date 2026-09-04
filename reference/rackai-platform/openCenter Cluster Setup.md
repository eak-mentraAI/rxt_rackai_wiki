---
title: "openCenter Cluster Setup"
source: "https://docs.rackai.rax.io/guides/opencenter-cluster-setup/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## openCenter Cluster: Init, Generate, and Set

This guide covers configuring a bare-metal cluster with the `opencenter` CLI (`cluster init`, `cluster set`, `cluster generate`) and pushing the generated GitOps repository to a remote. It picks up after the Undercloud/physical provisioning is finished.

CLI source: [openCenter-cli](https://github.com/opencenter-cloud/openCenter-cli).

## Assumed starting state

The following are already in place before running any of the commands below:

- Bare-metal nodes are racked, powered, and reachable over the target node subnet.
- The node subnet, gateway, DNS resolvers, and NTP servers are configured on the physical network.
- Each node runs a supported base OS (Ubuntu 24.04) with a working cloud-init or equivalent first-boot configuration.
- Each node is SSH-reachable from your workstation using the SSH key that will be referenced by `opencenter.infrastructure.ssh.key_path`.
- The physical interfaces you plan to use for `vip_interface` and `cni_iface` (for example `mgmt.102`, `bond0.30`) already exist on every node.
- You have the node inventory: hostnames and their assigned IPs on `subnet_nodes`.

For the physical provisioning itself, see the [Cluster Deployment Guide](https://docs.rackai.rax.io/guides/cluster-deployment/).

---

## 1\. Prerequisites

| Requirement | Details |
| --- | --- |
| `opencenter` CLI | Latest release from [openCenter-cli releases](https://github.com/opencenter-cloud/opencenter-cli/releases). Verify with `opencenter version`. |
| `git` | For repo creation and push |
| `sops`, `age` | The CLI shells out to `sops` for encryption |
| `gh` (optional) | Simplifies remote repo creation on GitHub |
| GitHub access | Push permission on the target org, with a PAT or SSH key |

```bash
opencenter version
sops --version
age --version
```

---

## 2\. Phase 1: initialise the cluster config

### 2.1 Run cluster init

```bash
opencenter cluster init rackai-dev --org rss-engineering --type baremetal
```

Defaults `init` writes:

- Directory `~/.config/opencenter/clusters/<org>/<cluster>/`
- `<cluster>-config.yaml` with bare-metal defaults, schema version `"2.0"`
- SOPS Age keypair at `~/.config/opencenter/clusters/secrets/<org>/<cluster>/age/keys/<cluster>-key.txt`
- SSH keypair at `~/.config/opencenter/clusters/secrets/<org>/<cluster>/ssh/<cluster>{,.pub}`

Flags:

| Flag | Purpose |
| --- | --- |
| `--org <name>` | Organisation directory (default `opencenter`) |
| `--type baremetal` | Provider type |
| `--config-file <path>` | Seed from an existing config file |
| `--force` | Overwrite an existing config for the same cluster |
| `--no-keygen` | Skip Age and SSH key generation |
| `--no-sops-keygen` | Skip Age key generation only |
| `--regenerate-keys` | Recreate keys even if they exist |
| `--full-schema` | Emit every available field |
| `--strict` | Fail if required values are missing after defaults |
| `--server-pool <spec>` | Add extra server pool definitions (repeatable) |
| `--<dot.notation>=<value>` | Override any field, for example `--opencenter.meta.env=dev` |

You can also pass `rss-engineering/rackai-dev` as the name and skip `--org`. The CLI splits on the first `/`.

### 2.2 Verify what got created

```bash
opencenter cluster active
opencenter cluster describe rackai-dev
ls ~/.config/opencenter/clusters/<org>/<cluster>/
ls ~/.config/opencenter/clusters/secrets/<org>/<cluster>/age/keys/
ls ~/.config/opencenter/clusters/secrets/<org>/<cluster>/ssh/
```

> [!warning] Back up the Age key file
> The private Age key at `~/.config/opencenter/clusters/secrets/<org>/<cluster>/age/keys/<cluster>-key.txt` is the only thing that can decrypt secrets in the GitOps repo. Store it in the team secret manager the same day it is generated. Never commit it.

---

## 3\. Phase 2: config anatomy (bare metal)

The config uses schema v2 (`schema_version: "2.0"`) and lives in `<cluster>-config.yaml`.

### 3.1 Top-level layout

```yaml
---
schema_version: "2.0"
metadata:                   # timestamps and creator, managed by the CLI
opencenter:                 # cluster spec
deployment:                 # deployment method and module refs (kubespray)
opentofu:                   # OpenTofu backend for infra provisioning
secrets:                    # SOPS config and service-specific secret material
```

### 3.2 opencenter.meta

```yaml
opencenter:
  meta:
    name: rackai-dev
    organization: rss-engineering
    env: dev
    region: iad3-staging
    stage: bootstrap        # managed by the CLI
    status: success         # managed by the CLI
```

Do not hand-edit `stage` or `status`. The CLI updates them during `generate` and `deploy`.

### 3.3 opencenter.cluster

```yaml
opencenter:
  cluster:
    cluster_name: rackai-dev
    base_domain: k8s.opencenter.cloud
    cluster_fqdn: rackai-dev.iad3-staging.k8s.opencenter.cloud
    admin_email: admin@example.com
    kubernetes:
      version: 1.35.4
      api_port: 6443
      kube_vip_enabled: true
      subnet_pods: 10.42.0.0/16
      subnet_services: 10.43.0.0/16
      network_plugin:
        calico:
          enabled: true
          version: 3.31.6
          vxlan_mode: Always
          network_policy: true
          cni_iface: mgmt.102
          autodetect_cidr: 10.97.6.32/27
          install_method: helm
      security:
        pod_security_standards: baseline
        audit_logging: true
        encryption_at_rest: true
      oidc:
        enabled: false
```

### 3.4 opencenter.infrastructure

```yaml
opencenter:
  infrastructure:
    provider: baremetal
    ssh:
      authorized_keys:
        - ssh-rsa AAAA...       # team SSH keys installed on all nodes
      username: ubuntu
      key_path: /Users/you/.ssh/id_rsa
    os_version: "24"
    node_naming:
      prefix: rackai-dev
      suffix: iad3-staging
    networking:
      subnet_nodes: 10.97.6.32/27
      allocation_pool_start: 10.97.6.34
      allocation_pool_end: 10.97.6.60
      gateway: 10.97.6.33
      vrrp_ip: 10.97.6.62
      vrrp_enabled: true
      loadbalancer_provider: metallb
      dns_nameservers: [8.8.8.8, 8.8.4.4]
      vip_interface: mgmt.102
    compute:
      master_count: 3
      worker_count: 2
      master_nodes:
        - { name: rackai-dev-cp-0,  access_ip_v4: 10.97.6.54 }
        - { name: rackai-dev-cp-1,  access_ip_v4: 10.97.6.36 }
        - { name: rackai-dev-cp-2,  access_ip_v4: 10.97.6.51 }
      worker_nodes:
        - { name: rackai-dev-wrk-0, access_ip_v4: 10.97.6.47 }
        - { name: rackai-dev-wrk-1, access_ip_v4: 10.97.6.58 }
```

### 3.5 opencenter.services and opencenter.managed\_services

Bare-metal clusters keep the OpenStack CCM/CSI and vSphere CSI services disabled:

```yaml
opencenter:
  services:
    calico:                { enabled: true,  namespace: calico-system }
    cert-manager:          { enabled: true,  namespace: cert-manager }
    fluxcd:                { enabled: true,  namespace: flux-system }
    kube-prometheus-stack: { enabled: true,  namespace: observability }
    keycloak:
      enabled: true
      namespace: keycloak
      hostname: auth.rackai-dev.iad3-staging.k8s.opencenter.cloud
      instances: 3
    longhorn:              { enabled: true,  namespace: longhorn-system }
    metallb:               { enabled: true,  namespace: metallb-system }
    openstack-ccm:         { enabled: false }
    openstack-csi:         { enabled: false }
    vsphere-csi:           { enabled: false }
  managed_services:
    alert-proxy:
      enabled: false
      http_route_fqdn: alerts.rackai-dev.iad3-staging.k8s.opencenter.cloud
```

### 3.6 opencenter.gitops

```yaml
opencenter:
  gitops:
    repository:
      url: https://github.com/rss-engineering/rackai-gitops.git
      branch: main
      path: clusters/rackai-dev
      local_dir: /Users/you/.config/opencenter/clusters/gitops/rss-engineering
    base_repo:
      url: https://github.com/opencenter-cloud/openCenter-gitops-base.git
      release: "2026.01"
      branch: main
    auth:
      token:
        provider: github
        token: ${env:GITHUB_TOKEN}    # never commit a plaintext PAT
    flux:
      interval: 5m
      prune: true
```

### 3.7 deployment, opentofu, and top-level secrets

```yaml
deployment:
  auto_deploy: true
  method: kubespray
  kubespray:
    version: 2.31.0
    modules:
      kubespray:
        source: github.com/opencenter-cloud/openCenter-gitops-base.git//iac/provider/kubespray?ref=main
        enabled: true

opentofu:
  enabled: true
  backend:
    type: local
    local:
      path: .opentofu-local-rackai-dev/terraform.tfstate

secrets:
  sops_age_key_file: /Users/you/.config/opencenter/clusters/secrets/rss-engineering/rackai-dev/age/keys/rackai-dev-key.txt
  ssh_key:
    private: /Users/you/.config/opencenter/clusters/secrets/rss-engineering/rackai-dev/ssh/rackai-dev
    public:  /Users/you/.config/opencenter/clusters/secrets/rss-engineering/rackai-dev/ssh/rackai-dev.pub
    cypher: ed25519
  keycloak:
    client_secret: ${env:KEYCLOAK_CLIENT_SECRET}
    admin_password: ${env:KEYCLOAK_ADMIN_PASSWORD}
  grafana:
    admin_user: admin
    admin_password: ${env:GRAFANA_ADMIN_PASSWORD}
  sops:
    enabled: true
    age_key_file: /Users/you/.config/opencenter/clusters/secrets/rss-engineering/rackai-dev/age/keys/rackai-dev-key.txt
    encrypted_regex: ^(data|stringData|secret)$
```

### 3.8 Compute IPs, CIDRs, VIPs, and interfaces

Cluster networking spans three disjoint networks plus a set of interfaces that must already exist on the nodes.

```js
+-------------------------------------------------------------+
|  Node network (physical or VLAN)                            |
|    subnet_nodes           = 10.97.6.32/27                   |
|    gateway                = 10.97.6.33                      |
|    allocation_pool        = 10.97.6.34 ... 10.97.6.60       |
|    vrrp_ip (kube-vip)     = 10.97.6.62                      |
|    k8s_api_ip (override)  = optional, falls back to vrrp_ip |
|    vip_interface          = mgmt.102     (kube-vip binds)   |
|    cni_iface (Calico)     = mgmt.102     (pod traffic)      |
+-------------------------------------------------------------+
        |                                            |
        | (Calico VXLAN or IPIP overlay on top)      |
        v                                            v
+-----------------------------+  +-----------------------------+
|  Pod CIDR                   |  |  Service CIDR               |
|    subnet_pods              |  |    subnet_services          |
|      10.42.0.0/16           |  |      10.43.0.0/16           |
+-----------------------------+  +-----------------------------+
```

> [!warning] CIDRs must not overlap
> `subnet_nodes`, `subnet_pods`, and `subnet_services` must be disjoint from each other and from any reachable external network (storage, DNS, corporate ranges). `cluster validate` does not catch overlap.

#### 3.8.1 Node network

Path prefix: `opencenter.infrastructure.networking.*`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `subnet_nodes` | CIDR v4 | Yes | Physical or VLAN network the nodes sit on. Also fed to Calico as the `autodetect_cidr` fallback and to Kubespray hardening rules. |
| `allocation_pool_start` | IPv4 | Yes | First IP handed out to nodes. Keep the gateway, VIP, and MetalLB range outside this pool. |
| `allocation_pool_end` | IPv4 | Yes | Last IP handed out to nodes. |
| `gateway` | IPv4 | Yes | Default gateway advertised on the node subnet. |
| `vrrp_ip` | IPv4 | Required when `vrrp_enabled: true` | kube-vip virtual IP for the Kubernetes API. Must be inside `subnet_nodes` and outside the allocation pool. Also used as `k8s_internal_ip` when no separate external API IP is set. |
| `vrrp_enabled` | bool | No (defaults to `true` at template level) | Enables kube-vip. |
| `vip_interface` | string | Recommended | Interface name kube-vip binds the VIP to (`mgmt.102`, `bond0.30`, `eth0`). Empty triggers auto-detection. On multi-NIC hosts, set it explicitly. |
| `loadbalancer_provider` | enum | Yes | `metallb` for bare metal. |
| `dns_zone_name` | FQDN | Yes | Zone used for the cluster FQDN. |
| `dns_nameservers` | list of IPv4 | Yes (min 1) | Applied at cloud-init time. |
| `ntp_servers` | list | Yes (min 1) | Time drift breaks TLS between components. |
| `security.allowed_cidrs` | list of CIDR | No | Firewall rules for the Kubernetes API port. |
| `security.deny_all` | bool | No | Locks the node subnet down to `allowed_cidrs` only. |

The API listens on `opencenter.cluster.kubernetes.api_port` (default `6443`). The endpoint is `https://<vrrp_ip>:<api_port>`.

**API-address override:**

```yaml
opencenter:
  infrastructure:
    k8s_api_ip: 10.97.6.100         # optional, falls back to vrrp_ip when empty
```

Set `k8s_api_ip` when the external API endpoint differs from `vrrp_ip`, for example a hardware load-balancer sitting in front of kube-vip. The generator adds it to Kubespray's `supplementary_addresses_in_ssl_keys` so the API certificate is valid for both addresses.

#### 3.8.2 Kubernetes overlay CIDRs

Path prefix: `opencenter.cluster.kubernetes.*`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `subnet_pods` | CIDR v4 | Yes | Pod IP range, fed to Calico's default IPPool. Not routed on the physical network. |
| `subnet_services` | CIDR v4 | Yes | ClusterIP range. Intra-cluster only. |
| `api_port` | int | Yes | API server port (default `6443`). |
| `kube_vip_enabled` | bool | No | Enables kube-vip inside the cluster. |

#### 3.8.3 CNI (Calico) interface selection

Path prefix: `opencenter.cluster.kubernetes.network_plugin.calico.*`

| Field | Type | Notes |
| --- | --- | --- |
| `enabled` | bool | Must be `true` when Calico is the CNI. |
| `install_method` | enum | `helm` (default) or `kustomize-helm`, installed by Flux after bootstrap. Use `kubespray` only for legacy migrations. |
| `cni_iface` | string | Explicit interface name Calico binds to. Overrides autodetect when set. |
| `calico_interface_autodetect` | enum | `first-found`, `interface`, or `cidr`. With `cidr`, Calico picks the NIC whose IP is inside `autodetect_cidr`. |
| `autodetect_cidr` | CIDR v4 | Required when `calico_interface_autodetect: cidr`. Usually equals `subnet_nodes`. |
| `vxlan_mode` / `ipip_mode` | enum | `Always`, `CrossSubnet`, or `Never`. Set one, not both. |
| `network_policy` | bool | Enables Calico NetworkPolicy enforcement. |
| `nat_outgoing` | bool | `false` when pods should egress with their real IP. |

`vip_interface` (kube-vip) and `cni_iface` (Calico) can point at different interfaces when the VIP lives on a management NIC and pod traffic uses a data NIC. In most Undercloud layouts they are the same interface.

#### 3.8.4 Compute nodes

Node identities and IPs are explicit. The CLI does not provision hardware. List every host that will join the cluster.

Path prefix: `opencenter.infrastructure.compute.*`

```yaml
opencenter:
  infrastructure:
    compute:
      master_count: 3               # must equal len(master_nodes)
      worker_count: 2               # must equal len(worker_nodes)
      worker_count_windows: 0
      master_nodes:
        - name: rackai-dev-cp-0     # DNS-1123 hostname
          access_ip_v4: 10.97.6.54  # inside subnet_nodes, outside allocation_pool
        - name: rackai-dev-cp-1
          access_ip_v4: 10.97.6.36
        - name: rackai-dev-cp-2
          access_ip_v4: 10.97.6.51
      worker_nodes:
        - name: rackai-dev-wrk-0
          access_ip_v4: 10.97.6.47
        - name: rackai-dev-wrk-1
          access_ip_v4: 10.97.6.58
      # windows_nodes: [ ... ]        # only when worker_count_windows > 0
```

Per-node fields (`StaticNode`):

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `name` | string | Yes | DNS-1123 hostname. Written into the Kubespray inventory as `ansible_host`. |
| `access_ip_v4` | IPv4 | Yes | Node's primary IP on `subnet_nodes`. |
| `id` | string | No | Provider-side ID. Populated by import/sync. Leave empty on initial write. |

#### 3.8.5 Bastion (optional)

```yaml
opencenter:
  infrastructure:
    bastion:
      enabled: true
      address: 10.97.6.5           # reachable jump host
```

When `enabled: true`, the Kubespray inventory routes SSH through `address` using `ProxyCommand`. When empty or `false`, Ansible connects to nodes directly.

#### 3.8.6 Worked example (/27)

For `subnet_nodes: 10.97.6.32/27` the usable range is `.33` to `.62` (broadcast `.63`). A safe layout:

| Purpose | Address(es) |
| --- | --- |
| Gateway | `10.97.6.33` |
| Node allocation pool | `10.97.6.34` to `10.97.6.60` |
| kube-vip (`vrrp_ip`) | `10.97.6.62` |
| MetalLB pool (external services) | outside the node subnet or a reserved sub-range |
| Pod CIDR | `10.42.0.0/16` |
| Service CIDR | `10.43.0.0/16` |

Yields:

```yaml
opencenter:
  cluster:
    kubernetes:
      api_port: 6443
      subnet_pods:     10.42.0.0/16
      subnet_services: 10.43.0.0/16
      network_plugin:
        calico:
          enabled: true
          install_method: helm
          cni_iface: mgmt.102
          calico_interface_autodetect: cidr
          autodetect_cidr: 10.97.6.32/27
          vxlan_mode: Always
          network_policy: true
          nat_outgoing: false
  infrastructure:
    networking:
      subnet_nodes:          10.97.6.32/27
      gateway:               10.97.6.33
      allocation_pool_start: 10.97.6.34
      allocation_pool_end:   10.97.6.60
      vrrp_ip:               10.97.6.62
      vrrp_enabled:          true
      vip_interface:         mgmt.102
      loadbalancer_provider: metallb
      dns_zone_name:         rackai-dev.iad3-staging.k8s.opencenter.cloud
      dns_nameservers: [8.8.8.8, 8.8.4.4]
      ntp_servers:
        - time.iad3-staging.example.com
        - time2.iad3-staging.example.com
    compute:
      master_count: 3
      worker_count: 2
      master_nodes:
        - { name: rackai-dev-cp-0,  access_ip_v4: 10.97.6.54 }
        - { name: rackai-dev-cp-1,  access_ip_v4: 10.97.6.36 }
        - { name: rackai-dev-cp-2,  access_ip_v4: 10.97.6.51 }
      worker_nodes:
        - { name: rackai-dev-wrk-0, access_ip_v4: 10.97.6.47 }
        - { name: rackai-dev-wrk-1, access_ip_v4: 10.97.6.58 }
```

#### 3.8.7 Setting network fields with cluster set

Every scalar above is reachable via `cluster set`:

```bash
opencenter cluster set rackai-dev \
  opencenter.cluster.kubernetes.subnet_pods=10.42.0.0/16 \
  opencenter.cluster.kubernetes.subnet_services=10.43.0.0/16 \
  opencenter.infrastructure.networking.subnet_nodes=10.97.6.32/27 \
  opencenter.infrastructure.networking.gateway=10.97.6.33 \
  opencenter.infrastructure.networking.allocation_pool_start=10.97.6.34 \
  opencenter.infrastructure.networking.allocation_pool_end=10.97.6.60 \
  opencenter.infrastructure.networking.vrrp_ip=10.97.6.62 \
  opencenter.infrastructure.networking.vrrp_enabled=true \
  opencenter.infrastructure.networking.vip_interface=mgmt.102 \
  opencenter.infrastructure.networking.loadbalancer_provider=metallb

opencenter cluster set rackai-dev \
  opencenter.cluster.kubernetes.network_plugin.calico.cni_iface=mgmt.102 \
  opencenter.cluster.kubernetes.network_plugin.calico.calico_interface_autodetect=cidr \
  opencenter.cluster.kubernetes.network_plugin.calico.autodetect_cidr=10.97.6.32/27
```

Repeated lists (`dns_nameservers`, `ntp_servers`, `master_nodes`, `worker_nodes`) need YAML edits. Use `opencenter cluster edit <name>` or re-run `cluster init --config-file <edited.yaml>`.

### 3.9 Reference syntax

Any string value can use:

| Syntax | Resolved from |
| --- | --- |
| `${ref:opencenter.meta.name}` | Another field in the same config |
| `${env:VAR_NAME}` | Environment variable at load time |
| `${file:/absolute/path}` | Contents of the referenced file |

Use these for secrets instead of pasting values into the YAML.

---

## 4\. Phase 3: adjust values with cluster set

`cluster set` edits fields in place with dot notation and preserves the rest of the YAML formatting.

```bash
opencenter cluster set rackai-dev opencenter.meta.env=prod

opencenter cluster set rackai-dev \
  opencenter.cluster.admin_email=platform@example.com \
  opencenter.gitops.repository.url=https://github.com/rss-engineering/rackai-gitops.git \
  opencenter.gitops.repository.branch=main

opencenter cluster set rackai-dev --strict \
  opencenter.cluster.kubernetes.version=1.35.4

opencenter --dry-run cluster set rackai-dev opencenter.meta.env=stage
```

Use `opencenter cluster edit <cluster>` to open the whole config in `$EDITOR` for larger changes. Run `opencenter cluster validate <cluster>` before generating.

Related commands:

```bash
opencenter cluster validate <cluster>     # schema and business rules
opencenter cluster normalize <cluster>    # backfill defaults on old configs
opencenter cluster export <cluster>       # print the effective (hydrated) config
opencenter cluster doctor <cluster>       # environment and readiness checks
```

---

## 5\. Phase 4: generate the GitOps repository

`cluster generate` renders the GitOps tree at `opencenter.gitops.repository.local_dir`:

```bash
opencenter cluster generate rackai-dev

opencenter --dry-run cluster generate rackai-dev

opencenter cluster generate rackai-dev --force

opencenter cluster generate rackai-dev --skip-validation

opencenter cluster generate rackai-dev --render-only

opencenter cluster generate rackai-dev --gitops-auth=ssh   # or =token
```

Layout under `local_dir`:

```js
<local_dir>/
├── .git/
├── .gitignore                             # excludes .terraform, kubespray, keys
├── .sops.yaml                             # creation rules for encryption
├── .opencenter/
│   ├── hooks/pre-commit                   # blocks unencrypted secret commits
│   └── scripts/scan-secrets               # security-only manifest scan
├── README.md
├── applications/
│   └── overlays/<cluster>/                # per-cluster Kustomize overlays
│       ├── kustomization.yaml
│       ├── services/                      # cert-manager, longhorn, metallb, ...
│       └── managed-services/              # alert-proxy, ...
├── infrastructure/
│   └── clusters/<cluster>/                # OpenTofu main.tf and kubespray inputs
└── clusters/
    └── <cluster>/                         # Flux bridge (GitRepository, Kustomization)
```

Only files created or modified in this run are counted in `Manifests created`. `.git`, `.terraform`, `venv`, `kubespray`, `.opentofu-local*`, and `.bin` are excluded from both the pre-generation snapshot and the count.

### 5.1 Install the pre-commit hook

```bash
cd <local_dir>
git config core.hooksPath .opencenter/hooks
chmod +x .opencenter/hooks/pre-commit
```

Every `git commit` now runs `opencenter cluster validate-manifests --staged --security-only`.

To bypass in an emergency:

```bash
OPENCENTER_SKIP_HOOKS=1 git commit -m "..."
```

### 5.2 Sync secrets before deploy

```bash
opencenter secrets sync rackai-dev
opencenter secrets status
opencenter cluster validate rackai-dev
```

---

## 6\. Phase 5: create the remote repository and push

`cluster generate` initialises a local git repo. The remote at `opencenter.gitops.repository.url` must exist before `cluster deploy`.

### 6.1 Create the remote

With `gh`:

```bash
gh repo create rss-engineering/rackai-gitops \
  --private \
  --description "openCenter GitOps repository (rackai-dev)"
```

Or in the GitHub UI, create an empty repo at `https://github.com/rss-engineering/rackai-gitops`. Do not initialise it with a README, licence, or `.gitignore`; the generated tree already contains these.

### 6.2 Wire up the local repo

```bash
cd <local_dir>

git status

# URL must match opencenter.gitops.repository.url exactly.
git remote add origin https://github.com/rss-engineering/rackai-gitops.git
# For SSH auth:
git remote set-url origin git@github.com:rss-engineering/rackai-gitops.git

git branch -M main
```

### 6.3 First commit and push

```bash
git add -A
git commit -m "chore: initial generate for rackai-dev"
git push -u origin main
```

If the pre-commit hook rejects the commit, fix the flagged files and retry.

### 6.4 After later runs

`cluster deploy` prints the follow-up steps. The pattern:

```bash
opencenter secrets sync <cluster>
git add -A
git commit -m "deploy <cluster>: <what changed>"
git push
```

Commit or stash before `deploy`; see [Caveat 7](https://docs.rackai.rax.io/guides/opencenter-cluster-setup/#caveat-7-dirty-working-tree-breaks-deploy).

### 6.5 Add or debug services after deployment

Three patterns cover the common cases after the cluster is up.

#### Enable a built-in service

Every entry under `opencenter.services` and `opencenter.managed_services` is a service the CLI knows how to render. Toggle one on, regenerate, commit:

```bash
opencenter cluster service enable <name>
opencenter cluster generate rackai-dev
opencenter secrets sync rackai-dev
git add -A && git commit -m "enable <name>" && git push
```

`opencenter cluster service options <name>` lists the fields you can override in the config for that service. `opencenter cluster service status` shows all service states.

#### Add a service outside the built-in registry

For a Helm chart or manifest the CLI does not ship a template for, drop it into the cluster overlay and let Flux reconcile it. From the generated repo root:

```js
applications/overlays/<cluster>/services/my-tool/
├── kustomization.yaml
├── helmrepository.yaml   # or gitrepository.yaml / ocirepository.yaml
└── helmrelease.yaml      # or plain manifests
```

Add the folder to the overlay `kustomization.yaml`:

```yaml
resources:
  - services/my-tool
```

Any secrets under `data`, `stringData`, or `secret` keys are encrypted automatically by the `.sops.yaml` creation rules. Commit and push; Flux picks the additions up at the next reconcile.

Do not re-run `opencenter cluster generate` to pick up custom folders; `generate` only touches paths the CLI owns. `generate --force` overwrites the overlay and produces `.bak-<timestamp>` copies of anything it displaces (see [Caveat 10](https://docs.rackai.rax.io/guides/opencenter-cluster-setup/#caveat-10-force-on-generate-writes-bak-timestamp-files)), so keep custom manifests under their own subfolder (for example `services/custom/<name>/`) if you regularly use `--force`.

#### Quick out-of-band debug (bypass GitOps)

For a temporary tool that does not need to survive reconciliation, install directly against the cluster kubeconfig:

```bash
eval "$(opencenter cluster env <cluster>)"      # exports KUBECONFIG
helm install debug-tool <chart> --namespace debug --create-namespace
```

Flux does not manage the release. If Flux prunes the namespace or the chart lands in a directory Flux reconciles, the release will disappear. Remove it with `helm uninstall` when you are done, or promote it into the overlay above.

---

## 7\. Phase 6: DNS records

Every user-facing hostname on the cluster resolves to the Envoy Gateway data-plane LoadBalancer IP allocated by MetalLB. Nothing in the GitOps repo or the CLI creates DNS records. Those live at whichever provider owns the zone, usually outside this repo. Skip this step and the pods come up but nothing reaches them from a browser.

### 7.1 Find the Gateway IP

Once `cluster deploy` finishes and Flux has reconciled the platform overlays, read the Gateway's assigned address:

```bash
export KUBECONFIG=$(opencenter cluster env <cluster> --print-kubeconfig)

kubectl get gateway -A -o wide
```

Look for the platform gateway (`rackspace-system/rmpk-gateway` on `rss-engineering` clusters). The `ADDRESS` column holds the LoadBalancer IP MetalLB assigned to it from `private-pool` or `public-pool`. Confirm the Gateway is fully programmed:

```bash
kubectl -n <gateway-namespace> get gateway <gateway-name> \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} {.message}{"\n"}{end}'
```

Both `Accepted=True` and `Programmed=True` are required before the IP will answer traffic.

### 7.2 Records to create

Every hostname listed on a `Gateway.spec.listeners[].hostname` needs an `A` record pointing at the same LoadBalancer IP.

Read the current listener list off the running cluster:

```bash
kubectl get gateway -A \
  -o custom-columns=NS:.metadata.namespace,NAME:.metadata.name,HOSTS:'.spec.listeners[*].hostname'
```

For a typical `rackai-dev` build that is:

| Hostname | Purpose |
| --- | --- |
| `auth.<cluster>.<base_domain>` | Keycloak |
| `harbor.<cluster>.<base_domain>` | Harbor UI and registry |
| `grafana.<cluster>.<base_domain>` | Grafana |
| `prometheus.<cluster>.<base_domain>` | Prometheus web UI |
| `alertmanager.<cluster>.<base_domain>` | Alertmanager |
| `dashboard.<cluster>.<base_domain>` | Headlamp |
| `longhorn.<cluster>.<base_domain>` | Longhorn UI |
| `gitops.<cluster>.<base_domain>` | GitOps UI (if enabled) |

If the RackAI dataplane is installed on the cluster, add a wildcard for the inference gateway too:

| Hostname | Purpose |
| --- | --- |
| `*.default.ai.<cluster>.<base_domain>` (or model-specific) | KServe InferenceService routes |

The inference gateway (`kserve/kserve-ingress-gateway`) lives on its own LoadBalancer IP. Read it the same way (`kubectl get gateway -n kserve ...`) and point the wildcard at that address.

### 7.3 Verify

For each hostname:

```bash
dig +short auth.rackai-dev.iad3-staging.k8s.opencenter.cloud
curl -kv -H 'Host: auth.rackai-dev.iad3-staging.k8s.opencenter.cloud' \
     https://<gateway-ip>/
```

`dig` should return the Gateway IP. `curl` with an explicit `Host` header bypasses DNS and tests the Gateway plumbing directly. Once DNS is in place, `https://<hostname>/` from a browser reaches the same endpoint.

### 7.4 Reinstall changes the IP

MetalLB does not guarantee the same LoadBalancer IP across a full uninstall and reinstall of the Envoy Gateway release. After a reinstall, `kubectl get gateway` may report a different IP and every DNS record needs updating. Pin the address with a `metallb.io/loadBalancerIPs` annotation on the Gateway's `Service` if you need it to survive teardown.

---

## 8\. Known caveats

### Caveat 1: schema is v2 only

`schema_version: "2.0"` is the only value the loader accepts. Older v1 configs must be migrated with `opencenter cluster migrate-layout ...` before they can be loaded. `cluster init` always writes v2.

### Caveat 2: --type sticks; pick it at init

`init` writes provider-specific defaults on first creation. Switching provider later means editing or regenerating the config; `cluster set` has no `--type` flag. To start over:

```bash
opencenter cluster init <name> --type baremetal --force
```

### Caveat 3: absolute paths are machine-local

`opencenter.gitops.repository.local_dir`, `secrets.sops_age_key_file`, and `secrets.ssh_key.private/public` are absolute paths. Anyone cloning the config on a different machine must update these (via `cluster init` or `cluster set`). Prefer `${env:...}` references for portability:

```yaml
secrets:
  sops_age_key_file: ${env:SOPS_AGE_KEY_FILE}
```

### Caveat 4: SOPS Age key is the master key

The Age recipient in `.sops.yaml` decrypts every secret in the GitOps repo. The private key lives at `~/.config/opencenter/clusters/secrets/<org>/<cluster>/age/keys/<cluster>-key.txt`. Store it in the team secret manager the same day it is generated. The CLI does not back this up.

### Caveat 5: GitHub tokens must never be committed plaintext

`opencenter.gitops.auth.token.token` accepts a raw PAT. Replace it with a reference before committing:

```yaml
opencenter:
  gitops:
    auth:
      token:
        provider: github
        token: ${env:GITHUB_TOKEN}
```
```bash
export GITHUB_TOKEN=ghp_...
```

Or switch to SSH:

```bash
opencenter cluster generate rackai-dev --gitops-auth=ssh
opencenter cluster set rackai-dev \
  opencenter.gitops.repository.url=git@github.com:rss-engineering/rackai-gitops.git
```

### Caveat 6: pre-commit hook must be enabled per clone

`.opencenter/hooks/pre-commit` only fires after `git config core.hooksPath .opencenter/hooks`. Add this to the onboarding steps for the GitOps repo.

### Caveat 7: dirty working tree breaks deploy

`cluster deploy` runs `git pull --rebase` on the GitOps repo before provisioning. Uncommitted changes fail the rebase and stop the deploy before any infrastructure changes. Commit or stash first.

### Caveat 8: origin must match repository.url

`cluster deploy` verifies that `git remote get-url origin` matches `opencenter.gitops.repository.url`. Mismatch aborts:

```js
git remote origin in <local_dir> points to "<actual>", but git_url is "<expected>"
Update the remote with: git -C <local_dir> remote set-url origin <expected>
```

### Caveat 9: Kubespray runs from OpenTofu; do not run it twice

The bare-metal OpenTofu module includes a `null_resource` that runs the Kubespray Ansible playbook during `opentofu apply`. The standalone `kubespray-*` steps in the deploy pipeline are intentionally disabled. Running `ansible-playbook cluster.yml` by hand after a successful deploy will run Kubespray a second time against the live cluster.

### Caveat 10: --force on generate writes.bak-\<timestamp> files

Re-running `generate` on an existing tree without `--force` fails. With `--force`, every existing file is copied to `<file>.bak-YYYYMMDD-HHMMSS` before being overwritten. Sweep the backups periodically:

```bash
find <local_dir> -name "*.bak-*" -mtime +14 -delete
```

### Caveat 11: keep OpenStack and vSphere services disabled

For `provider: baremetal`, keep `openstack-ccm`, `openstack-csi`, and `vsphere-csi` disabled in `opencenter.services`. These services target other providers and will fail to reconcile on a bare-metal cluster.

### Caveat 12: --full-schema is verbose

`opencenter cluster init <name> --full-schema` writes every field the schema knows about, most of which are already provider defaults. Prefer the default minimal output and add fields with `cluster set` as needed.

### Caveat 13: CIDRs must not overlap

`subnet_nodes`, `subnet_pods`, `subnet_services`, and any reachable external range (storage, corporate networks, upstream DNS) must be mutually disjoint. `cluster validate` does not check this. Overlap surfaces later as partial connectivity or MetalLB advertising addresses that the upstream router owns.

### Caveat 14: vrrp\_ip must sit in subnet\_nodes and outside the allocation pool

`vrrp_ip` is a real IP on the node subnet. Nodes ARP for it and one of them answers via kube-vip. If it falls inside `[allocation_pool_start, allocation_pool_end]`, OpenTofu will assign that address to a node port and the VIP will flap. Reserve one IP outside the pool (typical convention: the last usable address in the subnet).

### Caveat 15: vip\_interface and cni\_iface must exist on every node

kube-vip binds the VIP to `vip_interface`; Calico binds pod traffic to `cni_iface`. Interface names come from the OS (`bond0.30`, `mgmt.102`, `enp3s0f0`). Cloud-init and Kubespray do not create these interfaces. Verify with `ip -br link` on every host before running `deploy`. When interface naming varies across hosts, use `calico_interface_autodetect: cidr` with `autodetect_cidr: <subnet_nodes>`.

### Caveat 16: --render-only skips validation and encryption

`opencenter cluster generate --render-only` regenerates templated files in place. It does not run the full setup pipeline (encryption sweep, manifest validation, provisioning template refresh). Use it for template tweaks; use plain `generate` before deploying.

---

## 9\. End-to-end example

```bash
# 1. Init the cluster
opencenter cluster init rackai-dev \
  --org rss-engineering \
  --type baremetal

# 2. Point at the real GitOps remote and set the env label
opencenter cluster set rackai-dev \
  opencenter.gitops.repository.url=https://github.com/rss-engineering/rackai-gitops.git \
  opencenter.meta.env=dev

# 3. Validate
opencenter cluster validate rackai-dev

# 4. Generate the GitOps repository
opencenter cluster generate rackai-dev

# 5. Encrypt secrets
opencenter secrets sync rackai-dev

# 6. Wire up hooks and remote, then push
CONFIG=~/.config/opencenter/clusters/rss-engineering/rackai-dev/rackai-dev-config.yaml
cd "$(yq '.opencenter.gitops.repository.local_dir' "$CONFIG")"
git config core.hooksPath .opencenter/hooks
gh repo create rss-engineering/rackai-gitops --private
git remote add origin https://github.com/rss-engineering/rackai-gitops.git
git branch -M main
git add -A
git commit -m "chore: initial generate for rackai-dev"
git push -u origin main

# 7. Deploy (optional)
opencenter cluster deploy rackai-dev
```