---
title: "RackAI Deployment - RackAI Docs"
source: "https://docs.rackai.rax.io/guides/rackai-deployment/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## RackAI Platform Deployment (Single Cluster)

This guide provides instructions for deploying the RackAI Platform on **Rackspace Managed Platform for Kubernetes (RMPK)**. RackAI enables organizations to deploy and serve Large Language Models (LLMs) at scale with enterprise-grade security and multi-tenancy.

At a high level the deployment is: set up infrastructure → install the **data plane** → configure **Auth0** → install the **control plane** → verify.

If you still need to stand up the underlying cluster, see the [Cluster Deployment Guide](https://docs.rackai.rax.io/guides/cluster-deployment/).

---

## 1\. Terminology

| Term | Meaning |
| --- | --- |
| Management workstation | The machine from which your RackAI cluster is accessible |
| RackAI cluster | The Kubernetes cluster where both RackAI and the workload LLMs run |

---

## 2\. Architecture overview

RackAI follows a **single-cluster** architecture: the same cluster hosts the RackAI components (in the `rackai-system` namespace) and the actual workloads (LLMs, etc.). The control plane reaches the data plane via the "GPU cluster kubeconfig", which — in a single-cluster deployment — is the kubeconfig of the same cluster.

---

## 3\. Prerequisites

### 3.1 Platform requirements

| Requirement | Description |
| --- | --- |
| RMPK environment | Active Rackspace Managed Platform for Kubernetes |
| Storage provisioner | A dynamic storage provisioner (required by the object store and fine-tuning jobs). PVs used by Redis and SeaweedFS must use `ReclaimPolicy=Retain`. Volume expansion is required for production, as the Redis DB runs master/replica (not sharded). See [volume expansion](https://kubernetes-csi.github.io/docs/volume-expansion.html). |
| Helm | v3.x or later on the management workstation |
| kubectl | Kubernetes CLI on the management workstation |
| Auth0 account | Configured Auth0 tenant for authentication |
| DNS provider | Access to configure DNS records for the RackAI domain |
| TLS certificates | Valid certificates for the RackAI frontproxy domain (HTTPS) |

### 3.2 Network requirements

RackAI requires **2 load balancers** for production deployments:

| Load balancer | Purpose | Visibility |
| --- | --- | --- |
| Gateway LB | Exposes the KServe inference gateway for model serving | Internal (reachable by frontproxy) |
| Frontproxy LB | Public entry point for the RackAI UI and API | Public (user-facing) |

### 3.3 Domain requirements

You need **1 DNS domain** configured:

| Domain | Protocol | Purpose |
| --- | --- | --- |
| `rackai.example.com` | HTTPS | Frontproxy — user-facing API and UI access |

> [!note] Wildcard/dash domains
> If you rely on a single-label wildcard certificate such as `*.racks.io`, use a dash-style hostname like `<customer>-rackai.racks.io` (a nested `rackai.<customer>.racks.io` would not be covered by that wildcard).

### 3.4 Kubernetes clusters

RackAI requires **1 Kubernetes cluster**:

| Cluster | Purpose |
| --- | --- |
| RackAI cluster | Holds RackAI's components in the `rackai-system` namespace and the actual workloads (LLMs, etc.) |

---

## 4\. Minimum hardware requirements

| Cluster | CPU | Memory | GPU |
| --- | --- | --- | --- |
| RackAI cluster | 32000m (32 cores) | 64Gi | Yes (required to run LLMs) |

See [Appendix A](https://docs.rackai.rax.io/guides/rackai-deployment/#appendix-a-hardware-requirements) for GPU and per-model VRAM guidance.

---

## 5\. Infrastructure setup

### 5.1 Prepare nodes for RMPK

- Provision nodes meeting the hardware requirements.
- Install the OS — **Ubuntu 24.04 LTS** is recommended and currently supported.
- Configure networking so all nodes can communicate.

### 5.2 Create the Kubernetes cluster in RMPK

Create one cluster in your RMPK environment:

| Setting | Value |
| --- | --- |
| Name | `rackai-plane` (or any name you prefer) |
| Node type | CPU + GPU (needs both CPU and GPU nodes) \*\* |
| Container runtime | containerd |
| CNI | Calico |
| K8s version | v1.33 or above |

> [!note] Note
> \*\* The CPU/GPU distinction keeps CPU workloads off the GPU nodes so those resources stay available for GPU-only workloads.

### 5.3 Configure storage provisioners

The cluster requires a **dynamic storage provisioner** for Persistent Volumes, for example:

- Cinder (OpenStack)
- OpenEBS
- Longhorn
- Local Path Provisioner (testing only)

> [!tip] Sizing Longhorn volumes
> Check the **schedulable** capacity in the Longhorn UI before sizing (not the raw total). A practical starting point is **300 GB volume servers**, growing toward ~500 GB, for models, LoRA adapters, and datasets. Grow either by increasing volume size or by adding more volume servers.

### 5.4 Configure load balancer provisioners

The cluster requires a **load-balancer provisioner**, for example:

- CCM (OpenStack)
- MetalLB
- Cilium
- OpenELB

---

## 6\. Data plane setup

The data plane hosts KServe and runs the actual model inference workloads.

### 6.1 Prerequisites

- `kubectl` configured to access the data plane cluster ([install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)).
- `helm` v3+ ([install helm](https://helm.sh/docs/intro/install/)).
```bash
# Verify cluster access
kubectl cluster-info
kubectl get nodes
```

### 6.2 Run the data plane setup script

The automated setup script installs:

- **NVIDIA GPU Operator** — GPU drivers and device plugins
- **cert-manager** — certificate management
- **Envoy Gateway** — Gateway API implementation
- **K8s Gateway API CRDs**
- **KServe** — model serving framework
- **ClusterServingRuntime** — vLLM runtime configuration
- **SeaweedFS** — object storage for artifacts (datasets and models)
- **SeaweedFS CSI** — file access to SeaweedFS objects for workloads (inference/fine-tuning)
```bash
# Make sure the script is downloaded and available in your current environment.
mkdir -p ./scripts
curl <url-to-download-setup-script> -o ./scripts/setup-rackai-dataplane.sh

# Make the script executable
chmod +x ./scripts/setup-rackai-dataplane.sh

# Configure environment variables

# Optional (can also be passed via the --ingress-domain flag)
export INGRESS_DOMAIN="example.com"                # Your inference domain

# Required
export STORAGE_CLASS="storage-class-name-here"     # must have reclaimPolicy=Retain
export REDIS_HA_PASSWORD="your-redis-password"
export SEAWEEDFS_ADMIN_PASSWORD="seaweedfs-admin-pass"

# Run the setup script
./scripts/setup-rackai-dataplane.sh \
  --ingress-domain <YOUR_DOMAIN> \
  --kubeconfig <PATH_TO_RACKAI_CLUSTER_KUBECONFIG> \
  --install
```

Other flags to install, reinstall, uninstall, or check status:

```bash
./setup-rackai-dataplane.sh --kubeconfig <path> --ingress-domain <domain> --install
./setup-rackai-dataplane.sh --kubeconfig <path> --uninstall
./setup-rackai-dataplane.sh --kubeconfig <path> --ingress-domain <domain> --reinstall
./setup-rackai-dataplane.sh --kubeconfig <path> --status
```

### 6.3 Configure the inference gateway

The inference gateway needs an external IP. With an automatic load-balancer provisioner (e.g. OpenStack CCM) an IP should already be assigned. Check and note it:

```bash
kubectl get gateway -n kserve kserve-ingress-gateway \
  -o jsonpath='{.status.addresses[0].value}'
```

> [!note] Note
> If no IP is assigned, wait for one. If it stays `<pending>` for a long time, there may be an issue with the load-balancer provisioner.

### 6.4 Verify data plane installation

```bash
# Check all pods are running
kubectl get pods -n kserve
kubectl get pods -n envoy-gateway-system
kubectl get pods -n gpu-operator
kubectl get pods -n cert-manager

# Verify GPU availability
kubectl get nodes -o json | jq '.items[].status.allocatable["nvidia.com/gpu"]'

# Verify ClusterStorageContainer
kubectl get clusterstoragecontainer

# Verify ClusterServingRuntime
kubectl get clusterservingruntime

# Verify SeaweedFS pods
kubectl get pods -n seaweed

# Verify SeaweedFS CSI DaemonSets
kubectl get ds -n seaweed-csi

# Verify SeaweedFS StorageClass
kubectl get storageclass seaweedfs-storage
```

### 6.5 Installation summary

Components installed by the script, with versions and sources:

| Component | Version | Source | Namespace |
| --- | --- | --- | --- |
| NVIDIA GPU Operator | v25.10.0 | `nvidia/gpu-operator` (Helm) | `gpu-operator` |
| cert-manager | v1.19.3 | `jetstack/cert-manager` (Helm) | `cert-manager` |
| Envoy Gateway | v1.5.2 | `oci://docker.io/envoyproxy/gateway-helm` | `envoy-gateway-system` |
| GatewayClass "envoy" | — | raw `kubectl apply` | cluster-scoped |
| Envoy traffic policy | — | raw `kubectl apply` + patch | `envoy-gateway-system` |
| KServe | v0.15.0 | `oci://ghcr.io/kserve/charts/kserve` | `kserve` |
| ClusterServingRuntime (vLLM v0.15.1) | — | raw `kubectl apply` | cluster-scoped |
| Redis HA | 25.4.1 | `bitnami/redis` (Helm) | `seaweed` |
| SeaweedFS | 0.0.1 | `oci://registry-1.docker.io/rackspacengpc/rackai-seaweedfs` | `seaweed` |
| SeaweedFS CSI | 0.2.16 | `seaweedfs-csi/seaweedfs-csi-driver` (Helm) | `seaweedfs-csi` |

### 6.6 Export the RackAI cluster kubeconfig

The control plane needs access to the data plane cluster. Export the kubeconfig:

```bash
# Get the kubeconfig (method depends on your setup) — this step is optional
kubectl config view --raw --minify > rackai-kubeconfig.yaml

# Base64-encode for use in the control-plane secret (needed in the next step)
cat rackai-kubeconfig.yaml | base64 -w 0 > rackai-kubeconfig.b64
```

---

## 7\. Auth0 setup

### 7.1 Create an Auth0 tenant

Log in to [manage.auth0.com](https://manage.auth0.com/) (create an account if it's your first time) and create a new tenant for the project.

### 7.2 Configure applications

Configure three Auth0 applications to use Auth0 as the product's authentication system.

#### 7.2.1 RackaiUI

Used by the RackAI web UI to handle logins.

1. Go to the **Applications** tab.
2. Click **\+ Create Application**.
3. Name it **`RackaiUI`** and choose **Single Page Web Applications** (the name is case-sensitive).
4. In **Settings**, set:
5. **Allowed Callback URLs:** `http://localhost:3000`, `http://localhost:3000/onboarding`
6. **Allowed Logout URLs:** `http://localhost:3000/signin`
7. **Allowed Web Origins:** `http://localhost:3000`
8. In **Organizations**, select **Both**.

#### 7.2.2 Rackai Control Plane Services

Used by the RackAI control-plane services to access Auth0 APIs.

1. Go to **Applications → + Create Application**.
2. Name it **`Rackai Control Plane Services`** and choose **Machine to Machine Applications**.
3. On the "Authorize Machine to Machine Application" screen, select **Auth0 Management API**.
4. Enable these permissions and click **Authorize**:
5. `create:organizations`
6. `read:organizations`
7. `create:organization_members`
8. `create:organization_connections`
9. `create:organization_member_roles`
10. `create:organization_invitations`
11. `read:connections`
12. `read:clients`
13. In **Credentials**, pick **Client Secret (Post)** as the authentication method.

#### 7.2.3 Rackai CLI

Used by the RackAI CLI to access Auth0 APIs.

1. Go to **Applications → + Create Application**.
2. Name it **`RackaiCLI`** and choose **Native** under Application Properties.
3. Set **Allowed Callback URLs** to `http://localhost:18787/callback`.
4. Set **Maximum ID Token Lifetime** to `10800`.
5. Enable **Set Idle Refresh Token Lifetime** and set it to `1296000`.
6. Enable **Set Maximum Refresh Token Lifetime** and set it to `2592000`.
7. Click **Save**.

### 7.3 Configure the admin organization

The **`rackai`** organization is the admin organization in the RackAI control plane — anyone logged into it has full admin rights.

1. Go to **Organizations → + Create Organization**.
2. Set **Name:** `rackai`, **Display name:** `RackAI`.
3. Click **Add Organization**.
4. In **Members**, add the users who should administer the RackAI deployment (the deployment admins — **not** necessarily the customer cloud admin).
5. Use **Invitations** to invite users not yet in the Auth0 database.
6. In **Connections**, click **Enable Connections** and select **Username-Password-Authentication**. Do **not** enable auto-membership.

---

## 8\. Control plane setup

The control plane hosts the RackAI API server, manager, organizer, and frontproxy.

### 8.1 Prerequisites

- `kubectl` configured to access the control plane cluster.
- `helm` v3+.
- Base64-encoded kubeconfig for the data plane cluster.
- Base64-encoded TLS certificates for the frontproxy domain.
- Auth0 account configured.
```bash
kubectl get storageclass
```

> [!warning] Critical
> The RackAI API server requires persistent storage. Ensure a StorageClass exists and update the chart values with the correct name.

### 8.2 Download the RackAI chart

```bash
helm repo add rackai oci://registry-1.docker.io/rackspacengpc/rackai --version 0.0.1
```

### 8.3 Prepare base64 values

The chart accepts TLS certificates and the GPU cluster kubeconfig directly in the values file as base64-encoded strings.

```bash
# Encode the frontproxy TLS certificate and key (for HTTPS)
cat /path/to/tls.crt | base64 -w 0 > tls-crt.b64
cat /path/to/tls.key | base64 -w 0 > tls-key.b64

# Encode the data plane cluster kubeconfig (from section 6.6)
cat rackai-kubeconfig.yaml | base64 -w 0 > rackai-kubeconfig.b64

# Encode the model registry token (to pull models from a registry like Hugging Face)
cat token.txt | base64 -w 0 > token.b64
```

> [!note] macOS
> On macOS, use `base64` without the `-w 0` flag: `base64 < file`.

### 8.4 Prepare the values file

Create a `values-production.yaml` with your configuration:

```yaml
rackai-frontproxy:
  tlsSecret:
    crtB64: "<PASTE_TLS_CRT_B64_HERE>"  # From tls-crt.b64
    keyB64: "<PASTE_TLS_KEY_B64_HERE>"  # From tls-key.b64
  auth:
    domain: "<YOUR_AUTH0_DOMAIN>.auth0.com"
    issuer: "https://<YOUR_AUTH0_DOMAIN>.auth0.com/"
    jwkUrl: "https://<YOUR_AUTH0_DOMAIN>.auth0.com/.well-known/jwks.json"
    audiences:
      - "<YOUR_AUTH0_CLIENT_ID>"
  aiCluster:
    inferenceDomain: "<INFERENCE_DOMAIN>"      # Example "example.com"
    endpoint:
      hostname: "<GATEWAY_LOADBALANCER_IP>"    # IP of the Gateway LB

rackai-apiserver:
  model-regsitry-token: "<PASTE_MODEL_REGISTRY_TOKEN_B64_HERE>"  # From token.b64
  storage:
    pvc:
      storageClassName: "<STORAGECLASS_AVAILABLE_IN_CLUSTER>"    # StorageClass to use

rackai-manager:
  auth0:
    domain: "<YOUR_AUTH0_DOMAIN>.auth0.com"
    mgmtdomain: "<YOUR_AUTH0_DOMAIN>.auth0.com"
    clientID: "<YOUR_AUTH0_CLIENT_ID>"
    clientSecret: "<YOUR_AUTH0_CLIENT_SECRET>"
  rackaiFQDN: "UPDATE_THIS_TO_RackAI_FQDN"     # Example "https://rackai.example.com"
  gpuClusterConfig:
    kubeconfigB64: "<PASTE_RackAI_KUBECONFIG_B64_HERE>"  # From rackai-kubeconfig.b64
```

> [!warning] Important
> Replace all placeholder values (`<...>`) with your actual configuration.

### 8.5 Install the RackAI chart

```bash
helm upgrade --install rackai oci://registry-1.docker.io/rackspacengpc/rackai \
  --version 0.0.1 \
  --namespace rackai-system \
  --wait \
  --timeout 10m \
  --create-namespace \
  -f values-production.yaml
```

#### 8.5.1 What the RackAI chart contains

- **RackAI API Server** (K3S API server) — runs the K3S API server image; a bootstrap script installs the RackAI CRDs (models, model classes, …).
- **RackAI Manager** — manages inference services when a user deploys a model from the UI; runs controllers that watch the `model` CR and act on it.
- **RackAI Front Proxy** — an Envoy proxy that enforces auth on the inference endpoints users consume and handles user authn and session.
- **RackAI UI** — the main user interface for the platform.
- **RackAI Organizer** — helps the UI perform login/sign-up by talking to Auth0 (e.g. fetching which orgs a user belongs to).

Deployments:

```js
k get deploy -n rackai-system
NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
rackai-apiserver            1/1     1            1           20d
rackai-controller-manager   1/1     1            1           20d
rackai-frontproxy           1/1     1            1           20d
rackai-organizer            1/1     1            1           20d
rackai-ui                   1/1     1            1           20d
```

Secrets the chart deploys:

```js
k get secret -n rackai-system
NAME                           TYPE                DATA   AGE
rackai-apiserver-proxy-certs   kubernetes.io/tls   2      22d
rackai-apiserver-tls-certs     kubernetes.io/tls   2      20d
rackai-kubeconfig-admin        Opaque              1      22d
auth0-credentials              Opaque              4      20d
gpu-cluster-config             Opaque              1      20d
```
- `rackai-kubeconfig-admin` — used by the RackAI manager to talk to the API server internally.
- `auth0-credentials` — used by the Organizer and manager for Auth0.
- `gpu-cluster-config` — the kubeconfig for the AI cluster hosting models.
- `rackai-apiserver-proxy-certs` — mTLS between the front proxy and the API server.
- `rackai-apiserver-tls-certs` — TLS certificates for the front proxy (Envoy) to serve HTTPS.

### 8.6 Wait for deployment

```bash
# Watch pods come up
kubectl get pods -n rackai-system -w

# Check all deployments
kubectl get deployments -n rackai-system

# View logs if needed
kubectl logs -n rackai-system deployment/rackai-controller-manager -f
kubectl logs -n rackai-system deployment/rackai-apiserver -f
```

### 8.7 Expose the frontproxy

The frontproxy service needs an external IP. With an automatic load-balancer provisioner (e.g. OpenStack CCM) an IP should already be assigned. Note it:

```bash
kubectl get svc rackai-frontproxy -n rackai-system \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

> [!note] Note
> If no IP is assigned, wait; if it stays `<pending>`, check the load-balancer provisioner.

### 8.8 Configure DNS records

Create DNS records pointing at the frontproxy load balancer:

| Record type | Name | Value | Purpose |
| --- | --- | --- | --- |
| A | `rackai.example.com` | `<FRONTPROXY_LB_IP>` | Reaching the RackAI UI and API |

> [!warning] IPs can change on reinstall
> A reinstall may not produce the same load-balancer IP. Re-check and update DNS after any reinstall.

---

## 9\. Verification

The deployment is complete — try it out by visiting the domain configured above.

```bash
kubectl get pods -n rackai-system
kubectl get svc,ingress -n rackai-system
```

All pods should be `Running` / `Ready`, and the frontproxy domain should resolve and serve the RackAI UI.

---

## Troubleshooting

Most issues seen during deployment are **infrastructure-related**, not RackAI bugs.

A PVC won't delete

PVCs have finalizers, so a normal delete may hang. You can force deletion or remove the finalizer, but prefer fixing the root cause. Note the reclaim policy for Redis/SeaweedFS PVs is `Retain`.

Pods fail on a specific node (FS notifier)

A node-level **FS notifier (inotify)** configuration may need updating. If it isn't fixed, **any** new pod scheduled onto that node hits the same problem — update the node configuration rather than only rescheduling.

The GPU operator is taking a long time

Expected — the GPU operator is the slowest data-plane component to come up. Give it time before assuming a failure.

A load balancer IP stays `<pending>`

Check the load-balancer provisioner (e.g. OpenStack CCM, MetalLB). No IP means the gateway/frontproxy cannot be reached.

---

## Appendix A: Hardware requirements

### B.1 GPU hardware requirements

LLMs require significant GPU VRAM. Select GPU hardware based on the models you plan to deploy.

| GPU model | VRAM | Recommended use case |
| --- | --- | --- |
| NVIDIA A10 | 24 GB | Small models (≤8B parameters) |
| NVIDIA A100 40GB | 40 GB | Medium models (8B–30B) |
| NVIDIA A100 80GB | 80 GB | Large models (30B–70B) |
| NVIDIA H100 80GB | 80 GB | Large models with faster inference |
| NVIDIA H200 | 141 GB | Very large models (70B+) |

### B.2 LLM VRAM requirements

| Model | Parameters | Precision | Min VRAM | Recommended VRAM | GPU configuration |
| --- | --- | --- | --- | --- | --- |
| Llama 3.1 8B | 8B | FP16 | 16 GB | 24 GB | 1× A10/A100 |
| Llama 3.1 8B | 8B | INT8 | 10 GB | 16 GB | 1× A10 |
| Mistral 7B | 7B | FP16 | 14 GB | 24 GB | 1× A10/A100 |
| Llama 3.1 70B | 70B | FP16 | 140 GB | 160 GB | 2× A100 80GB |
| Llama 3.1 70B | 70B | INT8 | 70 GB | 80 GB | 1× A100 80GB |
| Llama 3.3 70B | 70B | FP16 | 140 GB | 160 GB | 2× A100 80GB |
| DeepSeek-V2 | 236B (MoE) | FP16 | 160 GB | 320 GB | 4× A100 80GB |
| DeepSeek-V3 | 671B (MoE) | FP8 | 320 GB | 640 GB | 8× H100 80GB |
| DeepSeek-R1 | 671B (MoE) | FP8 | 320 GB | 640 GB | 8× H100 80GB |
| Qwen2.5 72B | 72B | FP16 | 144 GB | 160 GB | 2× A100 80GB |
| Mixtral 8x7B | 47B (MoE) | FP16 | 94 GB | 160 GB | 2× A100 80GB |

> [!note] Note
> VRAM requirements are approximate and vary with context length, batch size, and inference-framework optimizations. vLLM typically needs 10–20% extra VRAM overhead for the KV cache.