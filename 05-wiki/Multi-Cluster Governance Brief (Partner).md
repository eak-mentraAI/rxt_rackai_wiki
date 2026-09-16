---
id: idx-vmware-avi-governance-brief
type: index
status: draft
owner: product
domain: strategy
aliases: [multi-cluster governance brief, vmware avi partner brief, avi ai gateway brief, partner governance brief]
related: [hub-wiki, ent-serving-runtime, ent-capacity-pool, ent-organization, ent-rackai-control-plane, wf-request-routing, wf-identity-access, idx-open-questions]
source_docs: [rackai_deployment_docs, rackai_user_guide_api_cli, project_specific_rackai_docs]
confidence: assumed
last_reviewed: 2026-09-16
parent: hub-wiki
summary: "Architectural briefing shared with the VMware Avi (Broadcom) team: RackAI's current serving, tenancy, routing, and policy model, the responsibilities RackAI expects to retain, and areas where Avi may provide complementary capabilities."
---

# RackAI × VMware Avi — AI Gateway Partner Brief

RackAI is evaluating how a global traffic and governance layer could complement its Kubernetes-native model-serving platform as deployments expand across clusters and regions. This brief summarizes RackAI's current serving, tenancy, routing, and policy model; identifies the responsibilities RackAI expects to retain; and highlights areas where VMware Avi may provide complementary capabilities. The objective is to establish a shared architectural baseline and identify concrete integration options for further evaluation.

**Audience:** The VMware Avi (Broadcom) team.
**Scope:** Written to stand alone — no prior RackAI knowledge assumed. Platform facts reflect RackAI as built today; capabilities attributed to a gateway layer are candidate roles for discussion, not confirmed Avi features.

---

## 1. What RackAI Is

RackAI is Rackspace's Kubernetes-native platform for serving and fine-tuning AI models. Customers deploy a model from a catalog and receive a standard, OpenAI-compatible API endpoint (`/v1/chat/completions`, `/v1/models`, streaming supported). The platform runs on GPU fleets (NVIDIA and AMD) across a mix of substrates — bare metal, Rackspace VMs, and managed Kubernetes. Everything a customer owns — models, deployments, datasets, fine-tuning jobs, adapters, credentials — is scoped to their tenant. RackAI is the control plane and serving layer; consumers address model endpoints, never GPU hardware or clusters directly.

---

## 2. How Models Are Realized and Served

**A model deployment is a Kubernetes custom resource.** When a tenant deploys a model, RackAI's control plane (a set of Kubernetes operators) reconciles a `ModelDeployment` resource into a running inference service. That service:

- Runs on a **serving runtime** (inference engine) chosen per model — today vLLM, NVIDIA NIM, an optimized NIM/vLLM path, and AMD's AIM runtime. Engine choice is bounded by GPU type (e.g., AMD GPUs run vLLM-class engines; some NVIDIA-only engines don't run on AMD).
- **Autoscales** based on load, including scale-to-zero when idle.
- Exposes **one OpenAI-compatible endpoint** per deployment. That endpoint is the only surface consumers address.
- Can serve a base model with a **fine-tuned adapter** applied on top, without standing up a separate full model.

**Capacity is pooled, not pinned to raw hardware.** Deployments draw from logical *capacity pools* mapped onto GPU nodes and clusters — for example a dedicated pool per priority model, plus purpose pools for launch/canary, reserve, warm standby, and spot. A deployment always draws from exactly one pool and never from individual GPUs directly. This lets capacity be reshaped in software without touching the deployment contract.

**The integration surface** is therefore a *model endpoint backed by a deployment on a capacity pool*, reconciled by the control plane. Any gateway layer should integrate at that endpoint and treat everything below it as opaque.

---

## 3. How Traffic Reaches Models Today

Each RackAI cluster is a self-contained serving stack. Within a cluster:

- Inference services are fronted by an **Envoy-based gateway implementing the Kubernetes Gateway API** — the cluster's HTTP front door.
- The gateway sits behind a **cluster-local load-balancer IP** (bare-metal load balancing on production clusters, node-level load balancing on smaller ones).
- Requests flow: client → DNS → cluster load-balancer IP → Envoy gateway → model inference service → model pod.

**The multi-cluster gap:** because each cluster runs its own Envoy gateway and load-balancer IP, there is **no single global front door across clusters today**. A fleet of N clusters presents N independent entry points and N hostnames. This is a deliberate characteristic of the current single-cluster-per-environment design, not a defect in Envoy — but it is the gap a global traffic layer would close: one entry point, health-aware and geo-aware steering to the right cluster, and cross-cluster policy enforcement, routing *to* the per-cluster Envoy gateways rather than replacing them.

It helps to distinguish three capabilities that are often bundled together, since Avi may treat them as separate products:

- **Global traffic management** — one front door, health- and geography-aware steering across clusters and regions.
- **Local load balancing** — distributing traffic within a cluster (a role the per-cluster Envoy gateway plays today).
- **AI-aware gateway functions** — request/response inspection, token-level metering, model- and tool-aware routing, and prompt/response guardrails.

RackAI's clearest present gap is **global traffic management**; the AI-aware functions are a candidate area explored in sections 6 and 8.

---

## 4. Multi-Cluster Governance — The Five Layers

"Governance across clusters" decomposes into five distinct control problems. Separating them clarifies which responsibilities RackAI expects to retain and which a gateway layer could carry.

| Layer | Question it answers | Ownership RackAI expects |
|-------|--------------------|--------------------------|
| **1. Identity & access** | Who is this caller, and what may they do — on any cluster? | RackAI provides identity; gateway integrates with it |
| **2. Tenancy & deployment registry** | Which tenant owns which deployment, on which cluster? | RackAI is source of truth; gateway consumes it |
| **3. Policy** | Quotas, model-access, region/residency — authored once, enforced everywhere | Shared: routing-time enforcement at the edge; placement-time enforcement in the platform |
| **4. Metering & audit** | Consolidated accounting and audit trail across clusters | Shared: traffic/usage metering at the edge; cost/margin accounting in the platform |
| **5. Traffic routing** | Which cluster and deployment should serve this request? | Candidate for the gateway (global edge) + platform's model-aware routing |

**Identity underpins tenant-scoped layers.** Tenant-aware routing, authorization, per-tenant quotas, and usage attribution all take *identity* as their input: policy means "tenant X may only use region Y," metering attributes usage to a tenant, residency binds a tenant to a region. A gateway can carry these at the edge only if it consumes a trusted identity RackAI provides — it must rely on RackAI as the authoritative source of tenant identity and relationships. Basic health- or geography-based steering does **not** depend on tenant identity and can operate independently; identity becomes essential the moment routing or enforcement is tenant-specific.

**Where RackAI retains ownership regardless of a gateway layer:**

- **Cost accounting** — GPU-hours consumed, revenue per GPU-hour, margin per model. Only the platform sees GPU utilization; edge metering captures request/token usage but not cost.
- **Placement residency** — where a deployment, its cache, and any training data physically live. An edge layer can enforce *routing* residency ("don't send this request to the wrong region"); regulated workloads need both halves.
- **Identity issuance** — the foundation every tenant-scoped layer depends on.

---

## 5. Access & Tenancy

**Tenancy is enforced at the Kubernetes layer, not just the UI.** In RackAI:

- The tenant unit is an **Organization**. Every resource — models, deployments, datasets, jobs, adapters, credentials — is owned by exactly one Organization.
- Each Organization maps to a **dedicated Kubernetes namespace**. The namespace is the primary isolation boundary; the broader isolation model also relies on RBAC, network policy, secrets handling, and admission controls layered on top.
- Organizations are **provisioned by Rackspace** (no self-service signup). A user is associated with one or more Organizations through the identity plane.
- Consumers address **model endpoints scoped to their Organization**; they never receive access to clusters or GPU hardware. The cluster on which a deployment runs is abstracted away.

The model is **isolated tenant scopes with explicit cross-tenant membership**: a tenant's resources live in an isolated namespace, and a user reaches multiple tenants only through explicit membership, not implicit reach.

**Extending to multi-cluster (the design target):**

- A tenant's identity and policy are **global** — recognized on every cluster.
- A tenant's *deployments* remain **placed** on specific clusters/regions for capacity, residency, and locality reasons.
- A global registry maps tenant → cluster(s) → deployments, so an edge tier can route a caller's request to the right cluster's endpoint and reject the wrong one.

The default posture is **least privilege**: a caller reaches exactly the endpoints its Organization owns, wherever those deployments are placed. Broader access is granted by explicit policy. A gateway layer would be expected to enforce this posture at the edge, not relax it.

---

## 6. MCP & Agents

To set expectations precisely: **RackAI serves models via a standard OpenAI-compatible API. It does not today ship a Model Context Protocol (MCP) server, a tool-calling broker, or an agent runtime as a platform feature.** "Agentic" describes the *workloads* RackAI targets — several priority models are chosen because they excel at coding and agentic use, and serving engines with strong shared-prefix reuse are favored for chat/RAG/agent traffic.

- **Today:** agents and MCP-based tools integrate by calling RackAI model endpoints like any OpenAI-compatible backend. Tool orchestration, MCP servers, and agent state live in the customer's or partner's application layer, not in RackAI.
- **Candidate area:** an AI-aware gateway could host MCP- and agent-facing controls — tool-call routing, per-tool policy, MCP endpoint exposure, agent-session guardrails — in front of the model endpoints. This is a forward-looking, additive design area, not a shipped RackAI function, and its feasibility depends on Avi's current capabilities (see the questions in section 7).

---

## 7. Summary and Questions for Avi

**Architectural baseline:**

- **Serving** — Kubernetes-reconciled deployments, one OpenAI-compatible endpoint each, drawing from logical capacity pools. Integrate at the endpoint, never at the hardware.
- **Traffic** — a per-cluster Envoy/Gateway-API front door today; no global front door yet. Closing that gap is RackAI's clearest present need.
- **Ownership RackAI retains** — identity issuance, tenancy source-of-truth, placement residency, and cost/margin accounting.
- **Candidate gateway roles** — global traffic management, edge policy and residency-routing, tenant-aware routing, usage metering, and (forward-looking) AI-aware MCP/agent and guardrail functions.
- **Access** — isolated tenant scopes with explicit cross-tenant membership; consumers address endpoints, not clusters.

**Questions for Avi:**

1. How would Avi consume and propagate a RackAI-issued tenant identity across global, regional, and per-cluster components?
2. Which global, regional, and per-cluster components does an Avi deployment require, and how do they relate to the three capabilities (global traffic management, local load balancing, AI-aware gateway)?
3. What AI-specific routing, token metering, and streaming guardrails exist in the product today, versus roadmap?
4. How are residency and tenant policies synchronized across sites and audited?
5. How does an Avi deployment coexist with and preserve the existing per-cluster Envoy / Gateway API layer?

---

## Appendix A — Priority Policy Requirements

The policy categories that map cleanly onto how RackAI is built and priced, and that a governance layer would need to express:

- **Tenant isolation & least privilege** — a caller reaches only its Organization's endpoints, wherever its deployments live. Mirrors the namespace-per-tenant model; the baseline.
- **Region / data-residency routing** — pin a tenant's traffic (and, at the platform, its placement) to approved regions. Enables consistent residency enforcement as RackAI expands regulated and residency-sensitive workloads across clusters and regions.
- **Quotas & rate limits per tenant / per model** — protect shared capacity and make usage accountable; a prerequisite for fair multi-tenant serving and metering.
- **Model-access control** — which Organizations may call which models (e.g., private/customer models vs. shared catalog models).
- **Admission control under load** — when a pool is saturated, throttle, queue, or shed lower-priority traffic. RackAI's serving model already assumes capacity is finite and pooled, so admission policy fits naturally.
- **Capacity-pool / priority policy** — route by workload class to the right pool (latency-sensitive vs. large-context vs. high-throughput agent traffic) and honor reserve/warm/spot tiers.

The through-line: RackAI is a **multi-tenant, capacity-constrained, economically-metered** platform. Policies expressing tenant boundaries, region constraints, fair capacity sharing, and workload-appropriate routing fit; policies that assume unlimited capacity or ignore tenancy do not.

---

## Appendix B — Guardrails: Input vs. Response

A governance layer for AI traffic needs two distinct guardrail stages; conflating them is a common mistake.

**Input-side (before the model runs):**
- **Request validation** — well-formed OpenAI-schema requests, allowed model/parameter ranges, context-length and max-output limits.
- **Authentication & authorization** — valid tenant identity, and the tenant is permitted to call this model in this region.
- **Rate / quota enforcement** — the request is within quota and the pool can admit it.
- **Content / prompt guardrails** — optional screening of prompts (blocked categories, injection patterns, PII rules) before spending GPU time.
- *Economic point:* rejecting a bad or unauthorized request before it reaches a GPU saves the most expensive resource in the system.

**Response-side (during/after generation):**
- **Output validation** — schema/format conformance, structured-output constraints, max-length enforcement.
- **Content safety** — screening generated text for policy violations before it returns.
- **Streaming** — because responses stream token-by-token, response guardrails must operate on a stream (buffer-and-check or incremental inspection), not just a complete payload.
- **Usage capture** — token counts and metering finalize when a request completes or is terminated (including interrupted streams), feeding the accounting layer.

**Candidate division of labor:** an edge gateway is well positioned for request validation, auth hand-off, rate/quota enforcement, and prompt/response content guardrails; RackAI owns model execution, pool-level admission, and cost-side accounting. A clean design keeps cheap rejection at the edge, model-aware admission in the platform, and content guardrails wherever the policy lives — with the input and response stages always explicit. Which of these an AI gateway performs today is a question for Avi (section 7).

---

## Related

- [[Wiki Hub]] · [[RackAI Platform]] · [[Serving Runtime]] · [[Capacity Pool]] · [[Organization]] · [[Request Routing]] · [[Open Questions]]
