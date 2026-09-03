---
id: bench-{name}
type: evidence
status: draft
owner: team-or-role
domain: performance
aliases: []
related: []
source_docs: []
confidence: measured
last_reviewed: YYYY-MM-DD
parent: hub-evidence
summary: "One-line description of this benchmark run or supporting data."
---

# {Benchmark Run / Evidence Name}

## What Was Measured

Model, runtime, quantization, hardware, and configuration under test.

## Setup

| Parameter | Value |
|-----------|-------|
| Model | [[...]] |
| Serving Runtime | |
| Quantization | |
| GPU type / count | |
| Topology | |
| Parallelism | |
| Batch config | |
| Workload profile | |

## Results

| Metric | Value | Unit |
|--------|-------|------|
| TTFT P50 / P95 | | ms |
| Output tokens/sec | | |
| Tokens/sec/GPU | | |
| Concurrency | | |
| Cost / 1M tokens | | |

## Validates

| Claim / Coefficient | ID | Confidence After |
|---------------------|----|------------------|
| [[coeff-...]] / [[met-...]] | | measured |

## See Also

- [[Evidence Hub]]
- [[Benchmark Library]]
