---
id: val-erebine-inference-claims
type: validation
status: draft
owner: performance-eng
domain: performance
aliases: [validate erebine inference claims, erebine benchmark, erebine ttft test, erebine prefix cache test, erebine 2.7ms test]
related: [hub-evidence, idx-validation-register, evd-erebine-competitive-analysis, met-ttft, met-tokens-per-gpu-second, met-output-throughput, coeff-kv-cache-hit-rate]
source_docs: ["https://erebine.ai", "erebine OpenAI-compatible API probe (2026-09-15): /v1/models, /v1/endpoints, /<slug>/v1/chat/completions", "scripts/erebine-benchmark.py run 2026-09-15T22:37Z (n=20)"]
confidence: measured
last_reviewed: 2026-09-15
parent: hub-evidence
summary: "Validation of Erebine's inference claims vs. measurable API behavior (run 2026-09-15); prefix cache confirmed."
---

# Validate Erebine Inference Claims

Answers open question 1 of the [[Erebine Competitive Analysis]]: *can Erebine's inference be provisioned and benchmarked to test its published claims?* The feasibility half is now **confirmed** — inference is reachable on the bundled key. This note is the runnable test design for the measurement half.

## Feasibility (measured 2026-09-15)

The earlier `endpoint_not_found` was a **routing-path error**, not a provisioning gap. Corrected findings:

- `GET /proj_.../v1/endpoints` lists **6 active endpoints**. Chat model `Qwen3.8-27B` is live as endpoint slug **`ed`** on tier `gpu_nvidia_shared_nvl`, worker `SJC3`.
- Correct call shape is **slug-routed** with `model` in the body: `POST /proj_.../ed/v1/chat/completions` `{"model":"Qwen3.8-27B", ...}`. A non-streaming completion returned HTTP 200 in ~1.97 s.
- Streaming works: first SSE chunk at **~624 ms** (client-side TTFT proxy over public internet), ~52 chunks/s decode.
- `usage.prompt_tokens_details.cached_tokens` is exposed and **varies per request** (observed 32 then 0) — the prefix-cache claim is directly observable.

So the test below is runnable today; only a signed-in plan with published figures is needed to compare against the vendor's own numbers.

## Claims Under Test

| # | Erebine claim | Source | Directly measurable? |
|---|---------------|--------|:--------------------:|
| E-1 | Router decision p99 **2.7 ms** | site "measured claims" | **No — not from client** (see Caveats) |
| E-2 | Prefix cache reuse ("912 tok reused") | site worked example | **Yes** — `cached_tokens` in `usage` |
| E-3 | Serving TTFT competitive | implied | Partial — client-side proxy only |
| E-4 | Decode throughput (tokens/s) | implied | Yes — token count / stream wall time |
| E-5 | `erepress` trims billed tokens | pricing copy | Yes — `X-Erepress` header + `usage` deltas with erepress on vs off |

## Results (run 2026-09-15T22:37Z · `measured`)

Harness `scripts/erebine-benchmark.py`, n=20 latency iterations, endpoint slug `ed` → `Qwen3.8-27B`, worker `SJC3:agent-2f2fd17a-d04`, tier `gpu_nvidia_shared_nvl`, from a single client over public internet.

| # | Claim | Result | Verdict |
|---|-------|--------|:-------:|
| E-2 | Prefix cache reuse | Cold request `cached_tokens=32/660`; after one warm-up, `cached=640/660` (~**97%**) and held steady across reps 2–5 | **Confirmed** |
| E-3 | Serving TTFT | Client-proxy TTFT p50 **509 ms**, p95 1675 ms, p99 3439 ms | **Measured (proxy)** |
| E-4 | Decode throughput | Median **83.6 chunks/s**; median stream wall 1.30 s | **Measured** |
| E-5 | `erepress` trims billed tokens | Workspace toggle reads `enabled=true` via MCP, but no per-response `X-Erepress` header on short prompts and no billing delta isolated this run | **Partial** |
| E-1 | Router decision p99 2.7 ms | Not observable from client (no server-side decision metric in headers/usage) | **Unverifiable** |

**Reading the numbers.** E-2 is the clean win: the prefix cache is real and aggressive (~97% of a 660-token prompt reused once warm), directly corroborating the site's "prefix hit — tokens reused" story. TTFT and decode are honest **client-side** figures — they bundle Erebine's routing + prefill + network RTT to `SJC3`, so they are *not* comparable to a server-internal 2.7 ms and carry shared-tier noise (p99 3.4 s tail on a `_shared_` tier). E-5 could be tightened by flipping the owner erepress toggle off and re-billing an identical long prompt; that was deliberately **not** done here to avoid mutating the workspace's live config. E-1 remains a vendor claim.

Raw records: `scripts/erebine-benchmark.py --json` output (kept out of the repo; regenerate with the harness).

## Method

**Harness.** Any OpenAI-compatible client against `POST /proj_.../ed/v1/chat/completions`, `stream:true`, capturing per-request: `usage` (prompt/completion/cached tokens), response headers (`X-Erebine-Routed-Model`, `X-Erebine-Routed-Endpoint`, `X-Erebine-Worker-ID`, `X-Erepress`), and client timestamps for TTFT (first chunk) and total decode time.

1. **TTFT + decode (E-3, E-4)** — fixed short prompt, `max_tokens` ∈ {32, 256}, N≥50 iterations, sequential + a small concurrent burst (e.g. 8). Report p50/p95/p99 client TTFT and tokens/s. Pin worker via the `X-Erebine-Worker-ID` header so latency is attributed to one node.
2. **Prefix cache (E-2)** — build a long shared prefix (≥1k tokens), vary only the suffix. Fire the same prefix M times; record `cached_tokens` vs `prompt_tokens`. Claim holds if cached rises materially after a warm-up request. Confirm a cold prefix reports `cached=0`.
3. **erepress (E-5)** — toggle via `erebine.erepress.set` (owner) on/off; send identical prompts; compare billed `prompt_tokens` and the `X-Erepress` header between modes.
4. **Router decision latency (E-1)** — **cannot be isolated from a client**; end-to-end wall time includes queue + prefill + network. Only obtainable if Erebine exposes a server-side decision metric (none seen in headers/usage). Treat E-1 as **not client-verifiable** and record it as a standing open question rather than a passable test.

**Comparison to RackAI.** Feed E-2/E-3/E-4 outputs through the same competitive-comparison lens used for [[TTFT]] and [[Tokens per GPU-Second]]. Note the axes are not identical: RackAI's KPIs are *per-GPU serving* numbers from its own fleet; Erebine's client-observed numbers bundle its routing + network. A fair comparison requires same model, similar hardware tier, and same prompt shape — otherwise the result is directional only.

## Isolation / Fairness Controls

- Same base model both sides (`Qwen3.8-27B` is available on Erebine; requires an equivalent RackAI deployment to compare).
- Record hardware tier (`service_tier` = `gpu_nvidia_shared_nvl`) — "shared" tiers carry noisy-neighbour variance; flag it.
- Run from a fixed network vantage; report client geography since TTFT includes RTT to `SJC3`/`DFW3`.
- Separate cold-start (first hit, possibly `provisioning_state: pending`) from warm steady-state.

## Documents This Can Change

| Document | Field / Value | Potential Change |
|----------|---------------|------------------|
| [[Erebine Competitive Analysis]] | E-1…E-5 rows | asserted → measured / refuted |
| [[Erebine Competitive Analysis]] | open question 1 | resolved (feasibility) + narrowed (E-1 not client-verifiable) |
| [[TTFT]] | competitive reference point | add external Erebine datapoint |
| [[Tokens per GPU-Second]] | competitive reference point | add external Erebine datapoint |
| [[KV Cache Hit Rate]] | external comparison | populate from E-2 |

## Status

| Status | Result | Date |
|--------|--------|------|
| feasibility-confirmed | inference reachable; TTFT proxy ~624 ms, decode ~52 chunks/s, cached_tokens observable | 2026-09-15 |
| **run complete** | E-2 confirmed (~97% warm reuse); E-3 TTFT p50 509 ms / p99 3439 ms (client proxy); E-4 83.6 chunks/s; E-5 partial; E-1 unverifiable | 2026-09-15 |
| open | E-5 billing delta (needs owner erepress off/on); RackAI same-model side-by-side comparison | — |

## Caveats

- Client-side TTFT is **not** Erebine's "2.7 ms router decision" — the 2.7 ms is a server-internal metric we cannot see. E-1 stays a vendor `asserted` claim.
- The bundled key is metered per token; a real run spends credit and is bounded by the `1536`/min rate limit seen in headers.
- Erebine numbers are one hosted endpoint on a shared tier, not a controlled fleet — good for directional comparison, not for a clean per-GPU claim against RackAI.

## See Also

- [[Erebine Competitive Analysis]]
- [[Evidence Hub]]
- [[Validation Register]]
- [[TTFT]]
- [[Tokens per GPU-Second]]
