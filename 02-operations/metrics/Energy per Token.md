---
id: met-energy-per-token
type: metric
status: draft
owner: performance-eng
domain: capacity
aliases: [energy per token, joules per token, tokens per kwh, tokens/kwh, watts per token, watts/token, energy efficiency]
related: [met-tokens-per-gpu-second, met-gpu-utilization, coeff-cost-per-gpu-hour, fml-cost-per-1m-tokens, pol-benchmark-evidence-chain, ent-gpu-amd-instinct, hub-inference-optimization]
source_docs: ["operator brief: MI350P benchmarking program (2026-10-07)", "https://inferencex.semianalysis.com/agentx"]
confidence: assumed
last_reviewed: 2026-10-07
parent: hub-operations
summary: "Energy consumed per output token (J/token), and its inverse tokens/kWh, co-measured during serving runs."
---

# Energy per Token

## Definition

**Energy per token** is the accelerator (or node) energy consumed per output token at a stated operating point. Its inverse, **tokens per kWh**, is the efficiency form used in economics.

> **Unit note.** "Watts per token" (a common shorthand) is dimensionally a power-per-throughput ratio: W ÷ (tokens/s) = joules/token. This note uses **J/token** and treats "watts/token" as an alias of the same quantity.

B3 is the **measurement source**; B5 only interprets it economically (energy cost per token via power price). It must be **co-measured** — power sampled from Infra's GPU telemetry during the same serving run that produced the token count. Energy from a separate B1 soak is not valid ([[Benchmark Evidence Chain]] side channel).

## KPI Job

Internal economics (power is an input to [[Cost per GPU-Hour]]) and strategic positioning (energy efficiency is a sovereign/enterprise buyer criterion; [[AgentX Benchmark Standard|AgentX]] reports throughput per provisioned power).

## Unit

joules per output token (J/token); tokens per kWh = 3.6×10⁶ / (J/token).

## Source or Formula

- `energy per token = mean GPU (or node) power over the run window × window duration / output tokens in the window`
- Inputs: Infra power telemetry (for AMD: `amd-smi` / ROCm SMI exporter; for NVIDIA: DCGM), serving token counts. Scope (GPU-only vs. node vs. facility PUE-adjusted) must be stated on the card.

## Targets & SLOs

| Direction | Target | Guardrail |
|-----------|--------|-----------|
| ↓ (J/token) | No target; reported per profile at the SLO-qualified point | Scope (GPU / node / facility) always stated |

## Measures

| Measures | Direction |
|----------|-----------|
| [[Model Deployment]] | MEASURES → |
| [[GPU Node]] | MEASURES → |

## Evidence

- Confidence rationale: `assumed` — no power telemetry is confirmed at deployment grain ([[KPI Telemetry Target List]] §3 lists GPU telemetry as "to validate").

## See Also

- [[Operations Hub]] · [[Tokens per GPU-Second]] · [[Cost per GPU-Hour]] · [[Benchmark Evidence Chain]]
