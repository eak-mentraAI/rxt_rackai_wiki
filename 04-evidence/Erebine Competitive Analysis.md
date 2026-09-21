---
id: evd-erebine-competitive-analysis
type: evidence
status: draft
owner: product
domain: strategy
aliases: [erebine, erebine.ai, erebine analysis, competitor erebine, "the layer underneath"]
related: [hub-evidence, idx-capability-gap-register, hub-rackai-platform, hub-openrouter-initiative, hub-commercial-capacity]
source_docs: ["Rack AI v2/README.txt", "Rack AI v2/claude-desktop-config.json", "https://erebine.ai", "erebine MCP server (api.erebine.ai) tools/prompts/resources listing", "erebine OpenAI-compatible /v1/models probe"]
confidence: measured
last_reviewed: 2026-09-15
parent: hub-evidence
summary: "Competitive analysis of Erebine (erebine.ai): a zero-lock-in, OpenAI-compatible inference router plus MCP workspace-intelligence layer, validated against a live API key from the Rack AI v2 bundle."
---

# Erebine Competitive Analysis

## Purpose

Analyze **Erebine** ([erebine.ai](https://erebine.ai)) as a competitor to the [[RackAI Platform]]. Evidence comes from two independent sources, cross-checked against each other:

1. **Live API validation** — the `Rack AI v2` sister bundle ships a Claude Desktop MCP config with a working workspace API key. Every capability marked `measured` below was confirmed by a real call on 2026-09-15.
2. **Website claims** — marketing copy and the "measured claims" section of erebine.ai. These are labelled `asserted` (vendor claim, unverified) since they cannot be confirmed from the key we hold.

> Confidence discipline (per [[Evidence Hub]]): API-observed behavior is `measured`; vendor marketing numbers are `asserted`; anything inferred across the two is `derived`. Downstream confidence never exceeds the weakest input.

## What Erebine Is (Positioning)

Erebine markets itself as **"the layer underneath — zero lock-in inference."** The stated thesis: *"Everything we removed is the feature. No contracts, no proprietary formats, no reserved-capacity hostage math."* It presents as an **OpenAI-compatible router over a mesh** ("answers to no pantheon" — the Erebus/primordial-dark branding). Content was rephrased for compliance with licensing restrictions.

Two products are offered:
- **Hosted** — the public router at `api.erebine.ai`, metered in credits per token.
- **Sovereign / self-hosted** — "the whole stack, in your datacenter": the same router, mesh, and workspace platform licensed to run on the customer's own accelerators, priced per node/month (frontend node, router node, agent), six-month minimum, node rates on request.

## Access Model (from the `Rack AI v2` bundle)

- The bundle is **not** a full inference SDK. Its `README.txt` states plainly: **"Inference models: not wired here."** It configures **workspace tools over MCP** only.
- The key is a workspace-scoped bearer token (`ere_...`) bound to workspace `ws_7mbuLOlg5aMhDwB13MhNsSpc`, project `proj_5C32A487-26E5-42`.
- Transport: **streamable HTTP MCP** at `https://api.erebine.ai/proj_.../v1/mcp`, protocol version `2025-06-18`, server `erebine-router`. Session handshake (`initialize` → `notifications/initialized` → session id) works.
- The client (Claude Desktop) talks Anthropic Messages format; Erebine's inference surface is **OpenAI-compatible**, so the two are deliberately decoupled — MCP tools ride alongside whatever model the client is signed into. Editor bundles (opencode, VS Code, Codex, Cursor, Hermes, pi, Cline) are offered separately to drive Erebine's models.

## Validated Capabilities (MCP surface — `measured`)

The server advertises **~19 tools, 6 prompts, 4 resources**. Confirmed by live call:

| Capability group | Tools (validated) | Result |
|---|---|---|
| **Workspace intelligence** | `intelligence.brief`, `intelligence.decisions`, `intelligence.timeline`, `intelligence.graph`, `intelligence.analyze`, `intelligence.track_decision`, `intelligence.track_milestone`, `intelligence.relate` | `brief` returned a structured (empty, fresh) project state; a decision/milestone knowledge graph with typed edges (supports, supersedes, blocks, implements, contradicts, refines) |
| **Memory** | `memory.save`, `memory.recall`, `memory.search` | `save` returned `mem_...` id; semantic search across memories/docs/artifacts/decisions/milestones when an embedder is configured |
| **Artifacts** | `artifact.create`, `artifact.read`, `artifact.update`, `artifact.list` | Full round-trip: created `cart_...` v1 (30 B), read back content, updated to v2. Workspace-scoped, versioned, 1 MiB cap |
| **Utility** | `calc.evaluate` | Deterministic math: `sqrt(144)+sin(pi/2)` → `13` (correct) |
| **Workspace / session** | `workspace.get`, `workspace.list`, `session.init` | Returned workspace metadata (kind: chat, visibility: team, created 2026-09-15) |
| **Owner controls** | `erepress.set`, `evolution.set` | `erepress` (in-path token compression) = **enabled**; `evolution` (MCP guidance-evolution loop) = **enabled**, breaker `closed` |

Prompts: `brief`, `erepress`, `mcp-loop`, `onboard`, `save-this`, `session.init`.
Resources: `erebine://workspace/current/brief`, `erebine://workspace/current/recent-decisions` (+ templated memory/artifact reads).

**Interpretation:** the validated product is a **cross-editor "workspace intelligence" layer** — persistent memory, a decision/milestone knowledge graph, versioned artifacts, and semantic recall, delivered over MCP so it follows the developer across Cursor/VS Code/Claude/etc. This is adjacent to, not the same as, RackAI's serving/fine-tuning platform.

## Validated Inference Surface (`measured`, partial)

- `GET /proj_.../v1/models` → **HTTP 200**, OpenAI-compatible catalog of **6 models** owned by this account: `LFM2.5-8B-A1B`, `harrier-oss-v1-0.6b`, `granite-embedding-reranker-english-r2`, `cohere-transcribe-03-2026`, `Qwen3-TTS-12Hz-1.7B-CustomVoice`, `Qwen3.8-27B`. Spans text, embedding/rerank, transcription (ASR), and TTS modalities.
- `GET /proj_.../v1/endpoints` → **HTTP 200**, **6 active endpoints**. Each model has a live endpoint with a **slug**, worker id, region, and tier — e.g. `Qwen3.8-27B` is served as slug **`ed`** (worker `SJC3`, tier `gpu_nvidia_shared_nvl`).
- **Inference works.** The correct call is **slug-routed** with `model` in the body: `POST /proj_.../ed/v1/chat/completions` `{"model":"Qwen3.8-27B", ...}`. A completion returned **HTTP 200 in ~1.97 s**; streaming gives a first chunk at **~624 ms** (client-side TTFT proxy) and ~52 chunks/s; `usage.prompt_tokens_details.cached_tokens` is exposed and varies per request.
- **Correction (2026-09-15):** an earlier probe reported `endpoint_not_found` and concluded serving was not provisioned. That was a **routing-path error** — it used the model *name* as the path segment instead of the endpoint *slug*. Endpoints are in fact live; latency/throughput/quality **are** measurable from this key. See [[Validate Erebine Inference Claims]].

## Website Claims (vendor `asserted`, except where a benchmark run upgraded them to `measured`)

Content rephrased for compliance with licensing restrictions.

| Claim | Erebine's stated figure | Verifiable from our key? |
|---|---|---|
| Router decision latency | **p99 2.7 ms** (rolling 5,000-decision window, worst active router) | No — asserted (server-internal; not client-isolable — see [[Validate Erebine Inference Claims]] E-1). Client-observed *end-to-end* TTFT p50 509 ms / p99 3.4 s bundles routing+prefill+network, so it neither confirms nor refutes 2.7 ms |
| Wire security | **0 pickle**: CURVE auth + MessagePack framing every hop; two CVE classes "deleted, not patched" (cve-2024-9053, cve-2025-32444) | No — asserted (headers show a Caddy edge, HSTS, CORS) |
| Routing intelligence | **16 signals** scored per worker per request (model-cache affinity, prefix-cache match, EWMA latency, KV pressure, +12) — "arithmetic, not round robin" | Partially corroborated — the "prefix-cache match" signal is real (see E-2 below); the 16-signal count and per-request scoring stay asserted |
| Footprint | 4 regions, 10 agents online, live limb | No — asserted |
| OpenAI compatibility | One env-var (`OPENAI_BASE_URL`) change; keep existing SDKs | **Measured** — `/v1/models`, `/v1/chat/completions` (non-stream + SSE stream), and `usage` are OpenAI-shaped; live completion returned in ~1.97 s |
| Any silicon | NVIDIA CUDA, AMD ROCm, Apple Metal; hardware set per endpoint; macOS/iOS/Linux native | No — asserted |
| Bring your own model | Upload safetensors, hardware-isolated sandbox, versioned rollback | No — asserted (model catalog is real, upload path untested) |
| Isolation | Runtime/data/network isolation; CURVE auth per mesh hop | No — asserted |
| Prefix cache | "prefix hit — 912 tok reused" in worked example | **Measured — confirmed** (E-2): a repeated 660-token prompt went from `cached_tokens=32` cold to **640 (~97%)** warm and held. See [[Validate Erebine Inference Claims]] |

Commercial model (asserted): **credits metered per token**; plans (Free → Starter → Hot-shot → Extra → Double Extra Deluxe) differ by grant size and per-token multiplier; compute tiers (Free CPU → NVIDIA Shared NVL → NVIDIA Shared → Self-Hosted) differ by silicon/isolation. `erepress` trims tokens before billing; priority routing bills over the standard rate. Figures are gated behind sign-in.

## Erebine vs. RackAI Platform

| Dimension | Erebine (validated + claimed) | [[RackAI Platform]] |
|---|---|---|
| Core stance | Zero lock-in, OpenAI-compatible **router over a mesh**; "the layer underneath" | Kubernetes-native inference **+ fine-tuning** platform with explicit tenancy and control plane |
| Inference API | OpenAI-compatible (`/v1`), path- and DNS-routed per endpoint (`measured` catalog) | OpenAI-compatible endpoints via [[Model Deployment]] / KServe |
| Fine-tuning | Not evident in bundle/site (BYO-model upload only, `asserted`) | [[Fine-Tuning Job]] → [[LoRA Adapter]]; SFT shipped, RL/DPO planned |
| Multi-tenancy | Workspace/project scoping (`measured`); team visibility | [[Organization]] tenancy, RBAC (thin today per [[Capability Gap Register]]) |
| Developer surface | **MCP workspace-intelligence layer** — memory, decision graph, artifacts, cross-editor (`measured`) — a differentiator RackAI does not have | None comparable; RackAI exposes serving, not an agent-memory layer |
| Routing | 16-signal composite scorer, p99 2.7 ms (`asserted`) | Smart-routing gateway is **planned**, not shipped (Gap Register §4) |
| Hardware | Any silicon incl. Apple Metal (`asserted`) | [[Accelerator Class]] over NVIDIA H100/L40S/A30, AMD Instinct; no Metal |
| Self-hosted | Full-capability sovereign license, per-node pricing (`asserted`) | RackAI is itself the on-prem/K8s platform |
| Token compression | `erepress` in-path compression, **enabled** (`measured` toggle) | No equivalent canonical capability |
| Evidence posture | Publishes specific perf numbers (unverifiable from our key) | No telemetry/benchmarks yet — all KPIs `assumed` (Gap Register §2) |

## Threat Assessment

- **Where Erebine is ahead (or claims to be):** a live, developer-facing **workspace-intelligence/MCP layer** that travels across editors (validated and genuinely working); a published, arithmetic routing story with a concrete latency number; explicit zero-lock-in / OpenAI-compat positioning; a full-capability self-hosted license. RackAI has none of the memory/decision-graph developer surface, and its smart routing is still planned.
- **Where the comparison is unproven:** Erebine's headline performance and security claims (2.7 ms p99, CURVE/MessagePack, 16 signals, any-silicon) are **vendor assertions we could not verify** — the same evidence bar RackAI itself has not met. Neither side has independent benchmarks in this corpus.
- **Where RackAI is differentiated:** first-class **fine-tuning** ([[Fine-Tuning Job]]/[[LoRA Adapter]]), explicit Kubernetes-native **tenancy + control plane**, and an accelerator-class abstraction tied to a real GPU fleet. Erebine's fine-tuning story is limited to BYO-model upload (unverified).

## Open Questions (candidates for the register)

1. ~~Can Erebine's inference be benchmarked to test the 2.7 ms and prefix-cache claims?~~ **Feasibility answered (2026-09-15):** inference is reachable and TTFT/decode/`cached_tokens`/`erepress` are measurable — see [[Validate Erebine Inference Claims]]. Narrowed residual: the **2.7 ms router-decision** figure is a server-internal metric **not isolable from a client**, so E-1 stays a standing unknown even after a full run.
2. Does RackAI need a competing developer **memory/knowledge-graph** surface, or is that out of scope for an inference+fine-tuning platform?
3. Is `erepress`-style in-path token compression a capability RackAI should evaluate for token-cost reduction?
4. How does Erebine's per-node sovereign licensing compare commercially to RackAI's own on-prem deployment model?

## Method / Reproducibility

- MCP handshake and every tool call above were issued against `api.erebine.ai` with the bundled key on 2026-09-15; results are quoted from live responses.
- Inference probe: catalog and `/v1/endpoints` read succeeded; slug-routed chat (`/ed`) returned live completions. An initial name-routed attempt returned `endpoint_not_found` and was corrected once `/v1/endpoints` revealed the slug scheme.
- Two probe writes (`kiro-probe-1` artifact, one memory) were created on Erebine's side during validation and neutralized afterward; they do not affect the analysis.

## See Also

- [[Evidence Hub]]
- [[Capability Gap Register]]
- [[RackAI Platform]]
- [[OpenRouter Initiative]]
- [[Commercial & Capacity Hub]]
