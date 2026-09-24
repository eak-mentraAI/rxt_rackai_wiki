---
id: idx-gpu-capacity-demand-rationale
type: index
status: draft
owner: product
domain: capacity
aliases: [gpu capacity demand rationale, capacity demand rationale, prod capacity sizing rationale, moe capacity rationale]
related: [hub-commercial, wf-demand-forecasting, idx-fleet-inventory, asm-fleet-competitiveness, ent-glm-5-3-flash, ent-nemotron-3-ultra, idx-openrouter-integration-plan, idx-first-bet-glm, fml-gpus-per-replica, fml-tokens-per-gpu-second, fml-gpu-hours-per-1m-tokens, idx-unit-economics, bench-openrouter-leaderboard-2026-09]
source_docs: ["reference/RackAI - GPU Capacity.xlsx", "reference/RACKAI-347-AIM-Engine-techspec.docx"]
confidence: assumed
last_reviewed: 2026-09-24
parent: wf-demand-forecasting
summary: "Demand rationale for prod GPU count proposal — derives concurrency targets from leaderboard, topology, and capacity."
---

# GPU Capacity Demand Rationale

## Purpose

This note provides the demand-side derivation behind the GPU counts in the capacity proposal (`reference/RackAI - GPU Capacity.xlsx`). That proposal correctly acknowledges the absence of a measured demand signal and relies on assumed concurrency figures. This note makes those assumptions explicit, derives them from available evidence, surfaces their confidence state, and identifies the decision that needs to be made on GLM Flash hardware selection before the proposal goes upstream.

> **Confidence: `assumed` throughout.** No production traffic exists yet. Every number here is derived from leaderboard observation, topology math, and analogical reasoning from external benchmarks. Numbers should be revisited the moment Phase 1 telemetry or Phase 3 live traffic is available.

---

## The Two Demand Sources We Are Sizing For

The prod capacity proposal serves two distinct workloads. They have different demand profiles and should be reasoned about separately.

| Workload | Driver | Demand signal quality |
|----------|--------|:---------------------:|
| **OpenRouter public provider** (GLM 5.3 Flash, Nemotron 3.5 Lightning) | OpenRouter routing — market-driven, grows with rank | `measured` from leaderboard; RackAI share `assumed` |
| **Model Inferencing / MOE-0 / MOE-1** (Gemma 4 31B, enterprise tenants) | Committed/agreed enterprise demand | `assumed` — no signed estate yet |

---

## 1. OpenRouter Demand Derivation

### 1.1 Observable demand for our target models

The [[OpenRouter Leaderboard Snapshot]] (2026-09-03) gives the total tokens processed across *all* providers for each model in a given period. These are the two models in the capacity proposal:

| Model | This-month total (all providers) | This-week total | Trend |
|-------|--------------------------------:|----------------:|-------|
| GLM 5.3 Flash | 11.8T tokens | 11.4T tokens | ↑>999% (breakout mover) |
| Nemotron 3 Ultra / 3.5 Lightning | ~15.8T this month (Ultra free) | ~4.4T this week | ↑52% |

These figures represent the **full OpenRouter market** for each model. RackAI will enter as one provider competing for a share of that pool.

### 1.2 Estimating RackAI's realistic share

OpenRouter routes proportionally to performance (latency, throughput, uptime, price). As a new entrant, RackAI should plan for a **conservative initial share** while API conformance and rank are being established, with upside as performance improves. Three share scenarios:

| Scenario | RackAI share of GLM pool | Rationale |
|----------|:------------------------:|-----------|
| Conservative (launch) | 5–10% | New entrant, rank establishing, API conformance ramp |
| Base (3–6 months) | 15–25% | Competitive TTFT/throughput, full conformance, good uptime |
| Optimistic (post-AMD scale) | 30–40% | Strong performance, AMD capacity live, pricing competitive |

**Conservative scenario math for GLM 5.3 Flash (launch sizing):**

GLM 5.3 Flash is processing ~11.4T tokens/week across all providers. At 10% share that is ~1.14T tokens/week for RackAI, or roughly **163B tokens/day**, or approximately **1.9M tokens/second** averaged over a 24-hour day.

However, token traffic is not flat — inference workloads have strong hourly and daily peaks. A **3× peak multiplier** applied to the daily average (conservative for an agentic/coding workload) gives a **peak throughput target of ~5.7M tokens/second**.

That is the market-level demand signal. The capacity question is: how many GPUs does it take to serve that?

### 1.3 Translating tokens/second to GPUs

Using the [[Tokens per GPU-Second Formula]] at illustrative values:

```
tokens_per_gpu_second = 750  (assumed / illustrative; no measured RackAI benchmark yet)
```

> **Note:** 750 tok/GPU-sec is the formula's illustrative worked example. It must be replaced with a measured value from the M2 AI Performance Benchmark milestone before this rationale is promoted above `assumed`. The CoreWeave reference in the capacity sheet uses SXM H100 metrics — our NVL PCIe H100s will post lower throughput per GPU, making this estimate potentially optimistic.

At 750 tok/GPU-sec, the conservative peak demand of ~5.7M tok/sec would require:

```
5,700,000 / 750 ≈ 7,600 GPUs
```

That is clearly not a useful number — it's the *entire market*. The point is to back into a **share-weighted** GPU requirement.

**At 10% market share and 3× peak:**

```
10% of 1.9M tok/sec × 3 peak = 570,000 tok/sec peak
570,000 / 750 tok/GPU-sec ≈ 760 GPUs
```

That is still far beyond the proposed fleet, which means one of two things: either our initial market share will be **much smaller than 10%** (more likely), or throughput per GPU is higher than the illustrative 750 figure (possible at FP8 with prefix caching on GLM's coding workload — prefix cache hit rates can cut effective compute significantly).

**Recalibrating to match the proposed GPU count:**

The proposal allocates roughly 26× H100 + 12× MI350P per prod site for all model inferencing combined. Assuming GLM Flash gets roughly 8–12 H100 equivalents at any given time:

```
At 750 tok/GPU-sec × 10 GPUs = 7,500 tok/sec capacity
At 1× context-cached efficiency boost → perhaps 12,000–15,000 tok/sec effective
```

That 7,500–15,000 tok/sec capacity corresponds to a **market share of roughly 0.13–0.26%** of GLM's current weekly volume at peak. That is the honest realistic starting position — a fraction of a percent, not 5–10%.

**What this means for the proposal:**

The GPU count is not wrong. It is sized for a **real but modest initial share**, then scales as rank and traffic grow. The proposal's framing of "5–8 concurrent users" maps to this — it is not a demand forecast, it is a **minimum viable capacity** to hold rank and serve a real workload. The right framing for Amine and Guy is: *we are not expecting to absorb a large share of GLM's global traffic at launch; we are sizing for a functional starting floor that lets us rank, measure, and scale.*

### 1.4 The concurrency assumption unpacked

The proposal says "8 concurrent users" for the OpenRouter models and "5 concurrent users" for Model Inferencing. Here is where those numbers come from structurally:

For GLM 5.3 Flash at FP8 on H100 (2–4 GPUs per replica per [[GPUs per Replica]]):

- 1 replica = 2–4 H100, serves a continuous-batch stream of requests
- At ~262k context length with prefix caching, GLM's coding/agentic requests are largely prefix-reusable, so effective concurrency per replica is higher than a pure generation workload
- "8 concurrent users" is a conservative estimate of the request pipeline a single-replica deployment can handle without queue depth growing

This is not a market sizing assumption — it is a serving capacity assumption. The **market share ceiling** at that concurrency is small (as shown above). That is appropriate for launch; the question is whether it represents enough minimum viable capacity to achieve a score on the OpenRouter leaderboard.

> **Key number OpenRouter uses for uptime scoring:** providers only enter uptime evaluation after **100+ requests**. At 8 concurrent users the ramp to 100 requests is fast (~minutes of traffic), so the concurrency floor is fine for evaluation purposes.

---

## 2. Model Inferencing (MOE-0 / MOE-1) Demand Derivation

This is the harder demand signal to derive because it depends on negotiated estates, not market routing.

### 2.1 What we know

- The proposal assumes **10 user accounts, 50/50 NVIDIA/AMD split** for Model Inferencing.
- The model is **Gemma 4 31B BF16** at 5 concurrent users.
- No signed MOE-0 estate exists yet; demand here is pre-commercial.

### 2.2 Sizing logic for MOE-0

MOE-0 is an internal operating rehearsal, not a commercial deployment. The right sizing question is: *how much load do we need to rehearse at to produce meaningful operating intelligence?*

A single Gemma 4 31B BF16 deployment at ~31B parameters on H100:

```
Weight footprint at BF16: ~62 GB
H100 usable memory at 88%: ~70 GB
GPUs per replica: ceil(62 / 70) = 1 (fits on a single H100, with KV cache pressure at 262k context)
At 262k context × BF16 KV per token: significant KV overhead → likely 2 H100 per replica with long context
```

At 5 concurrent users and 10 accounts:
- 5 concurrent requests × ~2 H100/replica = 10 H100 minimum for a single-site, no-redundancy serving floor
- Add a second replica for redundancy: 20 H100 minimum

The proposal's 26× H100 (min 20) per site is consistent with this reasoning plus headroom for burst.

### 2.3 The AMD split rationale

The 50/50 NVIDIA/AMD split is **strategically correct** for MOE-0 regardless of demand level. Running the same model on both fleets simultaneously during MOE-0 is the cheapest way to:

1. Generate the comparative telemetry that feeds the [[Empirical Map]] (the roadmap's explicit flywheel input)
2. Validate the AIM Engine integration (RACKAI-347) in a real serving context
3. Give the operating team real heterogeneous-fleet experience before MOE-1 brings an external customer

The split is not a demand assumption — it is an **operating rehearsal design choice**. It should be stated explicitly as such to Amine and Guy.

---

## 3. The GLM Flash Hardware Decision (Unresolved)

The capacity sheet presents three hardware options for GLM 5.3 Flash and does not make a recommendation:

| Option | Hardware | Count (req/min) |
|--------|----------|:---------------:|
| 1 | MI350P AMD | 4 / 2 |
| 2 | H100 NVLink (TP=4) | 6 / 4 |
| 3 | L40S (TP=4, PP=2) | 10 / 8 |

**Recommendation: Option 1 (MI350P) as the default, Option 2 (H100) as the fallback.**

Rationale:
- AMD is the primary incoming fleet and the AIM Engine integration (RACKAI-347) is scoped specifically to land GLM-class models on MI350P via the AIM profile catalog. Using MI350P for GLM is exactly the scenario AIM Engine was designed for.
- GLM at ~27B class fits in 1–2 MI350P at FP8 per [[GPUs per Replica]]; 4× MI350P gives two replicas with headroom — the right minimum for a functioning prod deployment.
- Option 2 (H100) is the fallback if MI350P is not commissioned or AIM Engine integration is not ready by the time OpenRouter Phase 3 launches. Do not use H100 for GLM if MI350P is available — keep H100 capacity for Nemotron and Gemma, where NVIDIA-specific optimizations (and in Nemotron's case NVIDIA-alignment) are the stronger fit.
- Option 3 (L40S) introduces hardware not present in prod, adds pipeline complexity, and has no strategic case. Drop it.

**Gate for the MI350P option:** AIM Engine integration reaches production readiness on the AMD dataplane before Phase 3 launch. If it does not, fall back to Option 2.

---

## 4. Demand Assumptions Summary (to attach to the proposal)

| Assumption | Value | Confidence | Exit criterion |
|------------|-------|:----------:|----------------|
| RackAI initial OpenRouter market share (GLM) | <1% of weekly volume at launch | assumed | Phase 3 live traffic telemetry |
| Peak-to-average traffic multiplier | 3× | assumed | Phase 1 telemetry showing hourly distribution |
| Tokens per GPU-second (H100, GLM FP8) | ~750 illustrative; likely higher with prefix caching | assumed | M2 AI Performance Benchmark |
| Tokens per GPU-second (MI350P, GLM FP8) | Unknown — no benchmark yet | assumed | MI350P benchmark post-commissioning |
| Concurrent users per OpenRouter model | 8 (OpenRouter); 5 (Model Inferencing) | assumed | Live queue depth telemetry |
| Gemma 4 31B GPUs per replica (H100, BF16, 262k ctx) | 2 H100 per replica | assumed | Hardware-fit benchmark |
| 50/50 NVIDIA/AMD split for Model Inferencing | Operating design choice, not demand-driven | derived | MOE-0 design sign-off |
| External demand for MOE-1 | Unquantified — no signed estate | assumed | First signed MOE-1 customer |

---

## 5. What Changes This Rationale

In order of impact:

1. **M2 AI Performance Benchmark** landing — replaces the 750 tok/GPU-sec illustrative figure with a measured one for each hardware/model combination. This is the single number that changes every downstream calculation.
2. **Phase 1 private-model telemetry** — first real request distribution (hourly pattern, concurrency distribution, context length distribution). Replaces the 3× peak multiplier assumption.
3. **Phase 3 public GLM traffic** — first measured market-share data point. Immediately upgrades OpenRouter share from `assumed` to `measured`.
4. **MI350P commissioning + AIM Engine validation** — enables the AMD benchmark and resolves the GLM hardware option decision.
5. **MOE-0 operating commitment** — the moment an internal estate is committed to MOE-0, replace the "10 accounts, 5 concurrent users" placeholder with actual committed workload specs.

---

## See Also

- [[Demand Forecasting]]
- [[Fleet Inventory]]
- [[Fleet Competitiveness]]
- [[First Bet — GLM 5.3 Flash]]
- [[OpenRouter Integration Plan]]
- [[GPUs per Replica]]
- [[Tokens per GPU-Second Formula]]
- [[Unit Economics Model]]
- [[OpenRouter Leaderboard Snapshot]]
