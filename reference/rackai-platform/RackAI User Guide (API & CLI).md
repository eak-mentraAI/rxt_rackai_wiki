---
title: "RackAI User Guide (API & CLI)"
source: "https://docs.rackai.rax.io/user/guides/rackai-user-guide/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## RackAI — User Guide

RackAI is an AI inference and fine-tuning platform that lets you deploy large language models, run inference against them, and fine-tune them with your own data — all through a simple API or CLI.

> [!info] Prefer the web console?
> This guide covers the `rackaictl` CLI and REST API. For a click-through of the RackAI **web console** (UI), see [Welcome to RackAI](https://docs.rackai.rax.io/user/guides/welcome/).

---

## Table of Contents

## Core Concepts

RackAI organizes AI workloads around a small set of building blocks. Understanding how they relate to each other makes everything else click.

| Resource | What it is |
| --- | --- |
| **Organization** | Your tenant. Everything you create lives inside your organization's isolated namespace. |
| **Model** | A model artifact — the weights and metadata for an LLM (e.g. Qwen3-4B, Llama-3-8B). |
| **ModelClass** | A deployment template that pairs a Model with a runtime, resource requirements, and default settings. |
| **ModelDeployment** | A live, running instance of a ModelClass. This is what serves inference traffic. |
| **RegistryCredential** | A stored credential (HuggingFace token, NGC API key, image registry secret) used by other resources. |
| **Dataset** | A training or evaluation dataset uploaded to the platform. |
| **FineTuningJob** | A fine-tuning run that trains a LoRA adapter from a base Model and one or more Datasets. |
| **LoRAAdapter** | A LoRA adapter that can be hot-loaded into a running ModelDeployment — no restart required. |

---

## Getting Started

### The built-in catalog

When your organization is created, RackAI automatically seeds your namespace with a catalog of pre-configured models — including popular open-source LLMs like Qwen, DeepSeek, Llama variants, and RedHatAI mirrors. Each catalog entry includes both a `Model` (the artifact) and a `ModelClass` (a ready-to-use deployment template).

**Public models** (e.g. Qwen, DeepSeek) are ready to deploy immediately — no credential required.

**Gated models** (e.g. Meta Llama family) require a HuggingFace token. See [Credentials and Access](https://docs.rackai.rax.io/user/guides/rackai-user-guide/#credentials-and-access).

To list available models in your namespace:

```bash
rackaictl model list
rackaictl modelclass list
```

### The CLI

All examples in this guide use `rackaictl`. Every resource can also be created from YAML with `-f file.yaml`.

---

## Authentication

RackAI uses Auth0 with an OAuth2 Authorization Code + PKCE flow. The `rackaictl` CLI handles token acquisition, caching, and automatic refresh — you only need to log in once per session.

### First-time setup

```bash
rackaictl auth setup
```

This interactively saves your API endpoint and default organization to `~/.config/rackaictl/config.json`. You can also set these via environment variables instead (see [Environment variables](https://docs.rackai.rax.io/user/guides/rackai-user-guide/#environment-variables) below).

### Logging in

```bash
rackaictl auth login
```

This opens your browser to complete the Auth0 login. Once authenticated, the CLI caches your tokens to `~/.config/rackaictl/credentials.json`. Subsequent commands automatically use the cached token and refresh it when it expires — no re-login required.

To log in for a specific organization:

```bash
rackaictl auth login --organization org-acme
```

### Checking your session

```bash
rackaictl auth status
```

Example output:

```js
✓ Logged in
  User:           you@example.com
  Organization:   org-acme
  ID Token:       valid (expires in 55m0s)
  Refresh Token:  present
  API Endpoint:   https://api.rackai.example.com
```

### Getting a token for direct API calls

To get a valid JWT for use with `curl` or other HTTP clients:

```bash
rackaictl auth token
```

The command prints only the token to stdout (warnings go to stderr), making it safe to use in scripts:

```bash
export API_TOKEN=$(rackaictl auth token)

curl https://<platform>/apis/rackai.rackspace.com/v1alpha1/namespaces/org-acme/inference/my-chatbot/v1/chat/completions \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen3-4b", "messages": [{"role": "user", "content": "Hello!"}]}'
```

The token is automatically refreshed if it has expired before being printed.

### Automation and CI/CD

For scripts and CI pipelines where browser login isn't possible, use a refresh token:

**Step 1.** After logging in interactively, export your refresh token:

```bash
rackaictl auth print-refresh-token
```

> **Security note:** Treat refresh tokens like passwords. Store them in your CI secret manager (e.g. GitHub Actions secrets, Vault), not in source code or plain-text files.

**Step 2.** In your automation, mint a short-lived ID token on demand:

```bash
# Using an environment variable (recommended)
export RACKAI_REFRESH_TOKEN="<your-refresh-token>"
export API_TOKEN=$(rackaictl auth token)

# Or pass it directly on the command line
export API_TOKEN=$(rackaictl auth token --refresh-token "$RACKAI_REFRESH_TOKEN")
```

**Step 3.** Use the token in API calls:

```bash
curl -H "Authorization: Bearer $API_TOKEN" \
  https://<platform>/apis/rackai.rackspace.com/v1alpha1/namespaces/org-acme/inference/my-chatbot/v1/models
```

You can also pass a token directly to any `rackaictl` command without going through the credential store:

```bash
rackaictl modeldeployment list --token "$API_TOKEN"
# or
API_TOKEN="<token>" rackaictl modeldeployment list
```

### Logging out

```bash
# Clear local credentials only (refresh token remains valid server-side)
rackaictl auth logout

# Revoke the refresh token server-side and clear local credentials
rackaictl auth revoke
```

Use `auth revoke` when you suspect a token has been compromised or when retiring a CI token.

### Environment variables

All auth configuration can be provided via environment variables instead of flags or the config file:

| Variable | Purpose | Equivalent flag |
| --- | --- | --- |
| `API_ENDPOINT` | API server URL | `--api-endpoint` |
| `API_TOKEN` | Explicit JWT (bypasses credential store) | `--token` |
| `RACKAI_REFRESH_TOKEN` | Refresh token for automation | `--refresh-token` |
| `RACKAI_ORGANIZATION` | Default organization | `--organization` |
| `AUTH0_DOMAIN` | Override Auth0 domain (advanced) | — |
| `AUTH0_CLIENT_ID` | Override Auth0 client ID (advanced) | — |

Environment variables take precedence over config file values. Explicit flags take precedence over environment variables.

### Token resolution order

When you run any `rackaictl` command, the token is resolved in this priority order:

1. `--token` flag or `API_TOKEN` env var
2. `--refresh-token` flag or `RACKAI_REFRESH_TOKEN` env var (exchanges for a fresh ID token)
3. Cached ID token in `~/.config/rackaictl/credentials.json` (auto-refreshed if expired)

---

## Deploying a Model

A `ModelDeployment` is the resource you create to serve a model. It references a `ModelClass`, which already has the model, runtime, and default resource configuration baked in.

### Quickstart: deploy from the catalog

```bash
rackaictl modeldeployment create my-chatbot \
  --modelclass qwen3-4b
```

Or in YAML:

```yaml
apiVersion: rackai.rackspace.com/v1alpha1
kind: ModelDeployment
metadata:
  name: my-chatbot
  namespace: org-acme
spec:
  modelClass: qwen3-4b
```

### Checking deployment status

```bash
rackaictl modeldeployment describe my-chatbot
```

The deployment goes through a short readiness phase. When it's ready, you'll see:

```js
Status: Ready
Inference Endpoint: https://<platform>/apis/rackai.rackspace.com/v1alpha1/namespaces/org-acme/inference/my-chatbot
```

### Overriding resources and settings

A `ModelDeployment` can override any setting from its `ModelClass`. Common overrides:

**Change replicas:**

```bash
rackaictl modeldeployment create my-chatbot \
  --modelclass qwen3-4b \
  --min-replicas 2 \
  --max-replicas 2
```

**Override runtime args** (e.g. increase max context length):

```yaml
spec:
  modelClass: qwen3-4b
  args:
    - name: max-model-len
      value: "32000"
```

**Remove a class-level arg:**

```yaml
spec:
  args:
    - name: some-flag
      unset: true
```

> **Note on resources:** If you set `resources` on a `ModelDeployment`, it fully replaces the class-level resources — there is no field-level merge. Always include all resource fields (including `nvidia.com/gpu`) when overriding.

### Choosing a runtime

| Runtime | Use when | LoRA support | Requires license |
| --- | --- | --- | --- |
| `vllm` | General-purpose open-weight models | No | No |
| `nim` | NVIDIA NIM containers (image-bundled weights) | No | Yes (NGC API key) |
| `optimized-nim-vllm` | Licensed path with full vLLM features including LoRA | **Yes** | Yes (NGC API key) |

The runtime is set on the `ModelClass`, not the `ModelDeployment`. To use a specific runtime, either pick a catalog ModelClass that already uses it or create your own ModelClass.

---

## Running Inference

Once your `ModelDeployment` is `Ready`, you can call it using the standard OpenAI-compatible API. Your inference endpoint URL is:

```js
https://<platformFQDN>/apis/rackai.rackspace.com/v1alpha1/namespaces/<org-namespace>/inference/<deployment-name>
```

This URL is also available on the deployment's status:

```bash
rackaictl modeldeployment describe my-chatbot
# Inference Endpoint: https://...
```

### Example: chat completions

```bash
curl https://<platform>/apis/rackai.rackspace.com/v1alpha1/namespaces/org-acme/inference/my-chatbot/v1/chat/completions \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-4b",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Example: using the OpenAI Python SDK

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://<platform>/apis/rackai.rackspace.com/v1alpha1/namespaces/org-acme/inference/my-chatbot/v1",
    api_key="<your-token>",
)

response = client.chat.completions.create(
    model="qwen3-4b",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

The platform forwards requests to the underlying engine unmodified. Any parameter that works with vLLM's or NIM's OpenAI-compatible API will work here.

### Streaming

Streaming responses (Server-Sent Events) work without any special configuration. The platform is configured with no proxy-level timeouts on inference routes, so long generations and streaming completions are not interrupted.

---

## Fine-Tuning a Model

A `FineTuningJob` runs a LoRA/QLoRA fine-tuning pipeline on a base model using your datasets. On success it automatically produces a `LoRAAdapter` that you can attach to any deployment of the same base model.

### Prerequisites

1. A `Model` for the base model you want to fine-tune
2. One or more `Dataset` resources with your training data
3. A work PVC (PersistentVolumeClaim) for intermediate training files

### Uploading a dataset

Create a `Dataset` resource, then upload your data:

```bash
rackaictl dataset create my-training-data --format messages
rackaictl dataset upload my-training-data ./data/train.jsonl
```

Supported formats: - `messages` — JSONL with `{"messages": [...]}` structure (chat format) - `text` — plain text JSONL

### Creating a fine-tuning job

```yaml
apiVersion: rackai.rackspace.com/v1alpha1
kind: FineTuningJob
metadata:
  name: my-finetune
  namespace: org-acme
spec:
  training:
    jobType: SFT                      # SFT | RLHF | DPO
    baseModel: qwen3-4b
    numEpochs: 3
    batchSize: 4
    learningRate: "1e-4"
    bf16: true
  peft:
    useQlora: true
    loraR: 16
    loraAlpha: 32
  datasets:
    - name: my-training-data
      type: training
    - name: my-validation-data        # optional
      type: validation
  workPVC:
    claimName: my-work-pvc
    mountPath: /workspace
  displayName: "My first fine-tune"
```

Or via CLI:

```bash
rackaictl finetuningjob create my-finetune \
  --base-model qwen3-4b \
  --job-type SFT \
  --dataset my-training-data:training \
  --dataset my-validation-data:validation \
  --num-epochs 3 \
  --batch-size 4 \
  --learning-rate 1e-4 \
  --use-qlora \
  --work-pvc my-work-pvc
```

### Pipeline stages

The job runs four stages in sequence. Any stage failure halts the pipeline.

| Stage | Description | When it's skipped |
| --- | --- | --- |
| **Preprocessing** | Splits training data into train/validation sets | When a separate validation dataset is provided |
| **Training** | LoRA/QLoRA fine-tuning on the base model | Never — this is required |
| **Evaluation** | Compares the adapter vs. the base model on eval loss | When the base model isn't reachable |
| **Upload** | Creates a `LoRAAdapter` CRD from the trained weights | When storage is not configured |

### Monitoring progress

```bash
# Quick overview
rackaictl finetuningjob list

# Detailed status
rackaictl finetuningjob describe my-finetune
```

Top-level job phases:

| Phase | Meaning |
| --- | --- |
| `Pending` | Waiting for datasets, PVCs, or the base model to be ready |
| `Running` | At least one stage is executing |
| `Succeeded` | All stages completed; all epochs ran |
| `SucceededEarlyStop` | Training stopped early because the metric stopped improving — the best checkpoint was saved. This is a success outcome. |
| `Failed` | A stage failed; pipeline halted |

### Evaluation results

After a successful run, you can read the evaluation metrics:

```bash
rackaictl finetuningjob describe my-finetune
# Evaluation:
#   Result:           Improved
#   Baseline Eval Loss: 1.797
#   Adapter Eval Loss:  1.030
#   Delta:            -0.767 (-53.58% PPL)
```

### Using the output adapter

After `status.phase` becomes `Succeeded` or `SucceededEarlyStop`, the produced `LoRAAdapter` is ready. You can find its name under `status.loraAdapterUpload.loraAdapterName`. See [LoRA Adapters](https://docs.rackai.rax.io/user/guides/rackai-user-guide/#lora-adapters) for how to attach it to a deployment.

---

## LoRA Adapters

LoRA adapters let you customize model behavior without redeploying. Adapters are hot-loaded into running deployments — no restart, no downtime.

> **Runtime requirement:** LoRA is only supported on the `optimized-nim-vllm` runtime.

### Prerequisites on the ModelDeployment

To use LoRA adapters, your `ModelDeployment` must have:

1. The `--enable-lora` flag set (as a value-less arg)
2. The env var `VLLM_ALLOW_RUNTIME_LORA_UPDATING=true`
```yaml
spec:
  modelClass: qwen3-4b-optimized     # must use optimized-nim-vllm runtime
  args:
    - name: enable-lora               # no value — this is a boolean flag
  env:
    - name: VLLM_ALLOW_RUNTIME_LORA_UPDATING
      value: "true"
```

### Attaching a FineTuningJob-produced adapter

After your fine-tuning job succeeds, simply add the adapter name to your deployment:

```yaml
spec:
  modelClass: qwen3-4b-optimized
  loraAdapters:
    - qwen3-4b-finance-q1-2026        # the LoRAAdapter produced by your FTJ
  args:
    - name: enable-lora
  env:
    - name: VLLM_ALLOW_RUNTIME_LORA_UPDATING
      value: "true"
```

The platform loads the adapter into all running replicas within ~10 seconds. No pod restart occurs.

### Uploading an adapter manually

If you have a pre-trained adapter (e.g. from HuggingFace), you can upload it directly:

```bash
# 1. Create the LoRAAdapter resource
rackaictl loraadapter create my-adapter --model qwen3-4b

# 2. Upload the adapter files
rackaictl loraadapter upload my-adapter ./adapter_files/

# The platform verifies file integrity and transitions to Ready automatically.
```

### Checking adapter status

```bash
rackaictl loraadapter describe my-adapter
# Phase: Ready
# Files: adapter_config.json (612B), adapter_model.safetensors (16MiB)
# Used by: my-chatbot
```

### Calling a specific adapter at inference time

When your deployment has multiple adapters loaded, specify which one to use in the API call using the `model` field:

```json
{
  "model": "qwen3-4b-finance-q1-2026",
  "messages": [{"role": "user", "content": "Summarize this earnings report..."}]
}
```

To call the base model without any adapter, use the base model's name.

### Removing an adapter

Remove it from the `loraAdapters` list in your deployment spec. The platform unloads it from all replicas automatically.

```bash
rackaictl modeldeployment update my-chatbot --remove-lora-adapter qwen3-4b-finance-q1-2026
```

---

## Autoscaling

RackAI uses Prometheus metrics and KEDA to autoscale `ModelDeployment` replicas. Autoscaling is available on `vllm` and `optimized-nim-vllm` runtimes.

### Enabling autoscaling

```yaml
spec:
  modelClass: qwen3-4b
  scaling:
    minReplicas: 1
    maxReplicas: 8
    metric: WaitingAndRunningRequests
    target: "5"                       # scale when avg queue depth per replica exceeds 5
    autoscalingEnabled: true          # required — autoscaling does not engage without this
```

> **Important:** `autoscalingEnabled: true` is required. Setting `metric` and `target` without this flag has no effect.
> 
> **Important:** `maxReplicas` defaults to `1`. Always set it explicitly when configuring autoscaling, otherwise scale-out will never occur.

### Available metrics

| Metric | Best for |
| --- | --- |
| `WaitingAndRunningRequests` | **Recommended.** Scales on queue depth + in-flight requests. Protects against scaling down mid-request. |
| `WaitingRequests` | First-token latency sensitive workloads |
| `RunningRequests` | Concurrency-bounded workloads |
| `ActiveRequests` | Engine-agnostic; scales on edge (Envoy) request count |
| `VLLMKVCacheUtilization` | Memory-bound workloads |
| `GPUMemoryUtilization` | GPU memory pressure (requires DCGM exporter) |

For `WaitingRequests`, `RunningRequests`, `WaitingAndRunningRequests`, and `VLLMKVCacheUtilization`, `target` is an integer count or ratio per replica. For `VLLMKVCacheUtilization` and `GPUMemoryUtilization`, `target` is a fraction (e.g. `"0.8"` for 80%).

### Scale to zero

Setting `minReplicas: 0` enables scale-to-zero. When your deployment has no traffic, it scales down completely. The first incoming request wakes it back up automatically.

```yaml
spec:
  scaling:
    minReplicas: 0
    maxReplicas: 4
    metric: WaitingAndRunningRequests
    target: "5"
    wakeHoldSeconds: 300      # keep warm for 5 minutes after last request
    autoscalingEnabled: true
```

> **Note:** Scale-to-zero adds cold-start latency. The first request after scale-down waits for the model to load. Use `wakeHoldSeconds` to tune how long the deployment stays warm after the last request.

### Inheriting autoscaling from a ModelClass

You can configure autoscaling defaults on a `ModelClass` and override per-deployment:

```yaml
# ModelClass — sets defaults
spec:
  scaling:
    metric: WaitingAndRunningRequests
    target: "5"
    autoscalingEnabled: true

---
# Deployment — just override the replica bounds
spec:
  modelClass: qwen3-4b
  scaling:
    minReplicas: 2
    maxReplicas: 16
    # inherits metric, target, autoscalingEnabled from the class
```

To opt out of autoscaling on a specific deployment when the class enables it:

```yaml
spec:
  scaling:
    minReplicas: 2
    maxReplicas: 2
    autoscalingEnabled: false
```

### Checking autoscaling status

```bash
rackaictl modeldeployment describe my-chatbot
# Autoscaling:
#   Status:  Active
#   Metric:  WaitingAndRunningRequests
#   Target:  5
#   Desired: 3
#   Ready:   2
```

---

## Credentials and Access

`RegistryCredential` is how you provide the platform with tokens and secrets it needs to pull private models, container images, or run licensed runtimes.

### Credential types

| Type | Used for | Example |
| --- | --- | --- |
| `modelPull` | Downloading private models from a registry (e.g. HuggingFace) | `HF_TOKEN` |
| `imagePull` | Pulling private container images (e.g. from `nvcr.io`) | Docker config JSON |
| `license` | Runtime license keys for NIM and Optimized-NIM-VLLM | `NGC_API_KEY` |

### Creating a credential

```bash
# HuggingFace token (for gated models like Llama)
rackaictl registrycredential create hf-token \
  --type modelPull \
  --secret-name hf-token-secret

# The underlying Kubernetes Secret must exist in your namespace:
kubectl create secret generic hf-token-secret \
  --from-literal=HF_TOKEN=<your-hf-token>
```
```bash
# NGC API key (for NIM runtimes)
rackaictl registrycredential create ngc-license \
  --type license \
  --secret-name ngc-secret

kubectl create secret generic ngc-secret \
  --from-literal=NGC_API_KEY=<your-ngc-api-key>
```

### Using credentials

Reference credentials by name in your resources:

```yaml
# On a Model (for pulling private weights)
spec:
  source:
    type: URI
    uri: hf://meta-llama/Llama-3-8B
    modelPullCredential: hf-token     # RegistryCredential name

---
# On a ModelDeployment (for licensed runtimes)
spec:
  modelClass: llama-nim
  licenseCredential: ngc-license       # single license credential
  imagePullCredentials:
    - ngc-image-pull                   # can specify multiple
```

### Credential rotation

When you update the underlying Kubernetes Secret, RackAI automatically detects the change and rolls the affected deployment pods to pick up the new credentials. No manual action required.

---

## Organizations and Multi-Tenancy

Your organization is an isolated tenant environment. All resources you create — models, datasets, deployments — live within your organization's namespace and are not visible to other organizations.

### Isolation

- All resources in your namespace can only reference other resources in the same namespace. There is no way to reference a model, credential, or adapter from another organization's namespace.
- Your organization has full access to manage its own resources (models, datasets, fine-tuning jobs, deployments).

---

## Reference: CLI Quick Reference

```bash
# Models
rackaictl model list
rackaictl model describe <name>

# Model Classes
rackaictl modelclass list
rackaictl modelclass describe <name>
rackaictl modelclass create <name> --model <model> --runtime vllm

# Deployments
rackaictl modeldeployment list
rackaictl modeldeployment describe <name>
rackaictl modeldeployment create <name> --modelclass <class>
rackaictl modeldeployment update <name> --max-replicas 4
rackaictl modeldeployment delete <name>

# Datasets
rackaictl dataset list
rackaictl dataset create <name> --format messages
rackaictl dataset upload <name> ./data.jsonl

# Fine-Tuning Jobs
rackaictl finetuningjob list
rackaictl finetuningjob describe <name>
rackaictl finetuningjob create <name> --base-model <model> ...

# LoRA Adapters
rackaictl loraadapter list
rackaictl loraadapter describe <name>
rackaictl loraadapter create <name> --model <base-model>
rackaictl loraadapter upload <name> ./adapter-files/

# Credentials
rackaictl registrycredential list
rackaictl registrycredential create <name> --type modelPull --secret-name <k8s-secret>
```

All commands support `-f <file.yaml>` for creating resources from YAML manifests. Pass `-o yaml` or `-o json` to `describe` commands for structured output.

---

## Known Issues

### Inferencing

- Selection of GPU accelerator type is not available during model deployment

### UI

- AI Studio chat interface intermittently fails when interacting with base model or LoRA adapter. CLI and direct API calls work.
- Cannot create new organizations from the UI.