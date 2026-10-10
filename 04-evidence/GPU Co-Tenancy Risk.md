---
id: evd-gpu-co-tenancy-risk
type: evidence
status: draft
owner: product
domain: governance
aliases: [gpu co-tenancy risk, gpu co-tenancy, shared gpu risk, time-slicing isolation, mig isolation, gpu side channel, cross-tenant leakage, kv cache leakage, leftoverlocals, container escape]
related: [pol-sovereignty-levels, hub-battlegrounds, hub-evidence, ent-gpu-amd-instinct, ent-gpu-h100, ent-gpu-a30, ent-organization, hub-ai-governance-assurance, prd-sovereign-isolation-assurance]
source_docs: ["web research 2026-10-09 (sources listed per item)"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-evidence
summary: "Sourced evidence on the residual risk of sharing GPUs between tenants, by sharing mode, and what mitigates it."
---

# GPU Co-Tenancy Risk

The evidence behind the residual risk of [[Sovereignty Levels]] Level 0 (shared GPUs) and what Level 1 (dedicated GPUs) removes. Gathered 2026-10-09. **Type:** vendor doc · academic · security researcher · regulator · press. Items marked **[2nd]** were not confirmed against the primary source; check before external use.

> **Confidence `derived`.** The sources are reported as found; their bearing on RackAI is inference. Nothing here describes RackAI's own configuration, which is not yet documented against these risks (see Implications).

## 1. What Each Sharing Mode Isolates

| Mode | Isolation, per the vendor | Source |
|------|---------------------------|--------|
| **NVIDIA time-slicing** | No memory or fault isolation between replicas sharing a GPU; traded away for more users per GPU | NVIDIA GPU Operator, *Time-Slicing GPUs in Kubernetes* ([docs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/26.7/gpu-sharing.html)) · vendor doc |
| **NVIDIA MPS** | Only a limited form of error containment; one client's fatal fault can bring down other users' clients | NVIDIA MPS docs ([docs](https://docs.nvidia.com/deploy/mps/latest/when-to-use-mps.html)) · vendor doc |
| **NVIDIA MIG** | Separate, isolated paths through the memory system (L2 banks, memory controllers, DRAM, SMs) and fault isolation. Up to 7 instances on A100/H100/H200/B200; 4 on A30 | NVIDIA MIG User Guide ([intro](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/introduction.html), [GPUs](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html)) · vendor doc |
| **AMD Instinct partitioning** (SPX/DPX/CPX compute; NPS1/2/4 memory) | Physically separated HBM regions under NPS; AMD frames CPX/NPS4 as enhancing security, but publishes **no side-channel isolation statement** comparable to MIG's | AMD Instinct partitioning docs ([overview](https://instinct.docs.amd.com/projects/amdgpu-docs/en/develop/gpu-partitioning/mi300x/overview.html)) · vendor doc |
| **AMD SR-IOV (MxGPU)** | Per virtual function: independent memory space, interrupts and DMA; no published side-channel or QoS guarantee | AMD virtualization driver docs ([docs](https://instinct.docs.amd.com/projects/virt-drv/en/latest/userguides/Host_configuration.html)) · vendor doc |

## 2. Demonstrated Leakage

**In the silicon** (needs an attacker co-located on the same GPU or node):

| Finding | What leaked | Source |
|---------|-------------|--------|
| **LeftoverLocals** (CVE-2023-4969): GPU local memory not cleared between kernels on AMD, Apple, Qualcomm, Imagination (NVIDIA not affected) | Another user's LLM responses reconstructed (~181 MB per query on a consumer AMD GPU; Instinct not tested). AMD's mitigation is an opt-in mode | Trail of Bits, 2024-01-16 ([blog](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)) · security researcher; AMD-SB-6010 [2nd] |
| **TunneLs**: MIG doesn't partition the last-level TLB | Cross-instance covert channel (~31 kbps) on a commercial cloud | Zhang et al., ACM CCS 2023 ([paper](https://casrl.ece.ucf.edu/wp-content/uploads/2023/05/2023-ccs.pdf)) · academic |
| **Behind Bars**: memory barriers cause cross-instance L2 interference on Hopper MIG | A victim's kernel-launch patterns, which correlate with LLM inference activity | Gu et al., USENIX Security 2026 ([paper](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_gu-cheng.pdf)) · academic |
| **Spy in the GPU-box**: NVLink/L2 contention between GPUs in one DGX | Covert and side channels between *whole* GPUs sharing a multi-GPU box | Dutta et al., ISCA 2023 ([paper](https://par.nsf.gov/servlets/purl/10428033)) · academic |
| **GPU memory remanence** under passthrough | A later VM recovered a previous VM's data (2014; current drivers may differ) | Maurice et al., FC 2014 ([paper](https://www.s3.eurecom.fr/docs/fc14_maurice.pdf)) · academic |
| **GPUHammer**: first Rowhammer on an NVIDIA GPU (A6000, GDDR6) | Bit flips in another user's memory; ECC mitigates; H100 reportedly not vulnerable | The Hacker News, Jul 2025 ([press](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html)) [2nd] |

**In the software and serving stack** (the more common real-world path):

| Finding | What leaked | Source |
|---------|-------------|--------|
| **NVIDIA Container Toolkit escapes** (CVE-2024-0132, bypass CVE-2025-23359; CVE-2025-23266 "NVIDIAScape", CVSS 9.0) | Full host access from a malicious container image; in some cases a whole multi-tenant Kubernetes cluster | Wiz, 2024-09-26 ([blog](https://www.wiz.io/blog/wiz-research-critical-nvidia-ai-vulnerability)) and 2025-07-17 ([blog](https://www.wiz.io/blog/nvidia-ai-vulnerability-cve-2025-23266-nvidiascape)) · security researcher |
| **Shared AI inference platforms** (Hugging Face, Replicate, SAP AI Core) | Other customers' models and data, via malicious models and misconfiguration; containers judged not a sufficient tenant boundary | Wiz, 2024-04-04 ([blog](https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure)); Wiz "SAPwned", Jul 2024 ([blog](https://www.wiz.io/blog/sapwned-sap-ai-vulnerabilities-ai-security)) · security researcher |
| **Shared KV / prefix caches** in vLLM and SGLang across tenants | Other users' prompts reconstructed | Wu et al., NDSS 2025 ([paper](https://www.ndss-symposium.org/wp-content/uploads/2025-1772-paper.pdf)); arXiv 2409.20002 ([paper](https://arxiv.org/abs/2409.20002)) · academic |
| **Prompt caching in commercial APIs** | Cross-user cache sharing detected at 7 API providers | arXiv 2502.07776, Feb 2025 ([paper](https://arxiv.org/abs/2502.07776)) · academic |

## 3. Mitigations and Their Limits

- **MIG** is a real improvement on time-slicing and MPS, but not side-channel-free (TunneLs, Behind Bars). Those channels leak activity patterns, not bulk data.
- **Confidential computing** (NVIDIA H100 and later, with an AMD SEV-SNP or Intel TDX CPU) protects against a hostile host or operator, not against co-tenant side channels; transfer overhead can be large for multi-GPU work ([whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf); arXiv 2409.03992). **No AMD statement was found that MI300 or MI350 support GPU-side confidential computing**; treat it as unavailable.
- **Memory scrubbing** between tenants is opt-in on AMD (the LeftoverLocals mode) and was historically an ECC side effect rather than a control.
- **Isolation layering:** containers alone are not a sufficient tenant boundary where customers can run code; use a VM boundary at minimum (Wiz; UK NCSC Principle 3).

## 4. Regulatory and Industry Guidance

None of this is GPU-specific; it concerns cloud tenancy generally.

| Guidance | What it says about separation | Source |
|----------|-------------------------------|--------|
| **UK NCSC Cloud Security Principle 3** | Prefer hardware-backed separation (usually a hypervisor) where customers run code; dedicated hosting still shares a management plane | NCSC ([page](https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-3-separation-between-customers)) · regulator |
| **US DoD Cloud SRG, Impact Level 5** | Physical separation (e.g. dedicated infrastructure) from non-DoD/non-federal tenants | AWS whitepaper quoting the SRG ([doc](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/case-study.html)) [2nd] |
| **France SecNumCloud 3.2** | EU ownership and control, immunity from non-EU extraterritorial law; strict isolation | Vendor and legal summaries [2nd] |
| **ECB cloud outsourcing guide (Nov 2025, non-binding); DORA; EBA/GL/2019/02** | Risk-based: data location, jurisdiction and audit; **no single-tenancy mandate** | Law-firm summaries [2nd] |

## Implications for RackAI

1. **Level 0 is legitimately sovereign only with serving-layer controls in place.** The common leak paths are software: container escapes, misconfiguration, cross-tenant caches. Dedicated GPUs don't fix those; per-tenant caches, a VM boundary where customers run code, and patching do.
2. **A shared KV cache must never span tenants.** The roadmap includes a *Shared KV cache (improvement)* row behind llm-d inference routing. Its scope should be confirmed as per-tenant at every level. *(Code check 2026-10-10: the shared LMCache example, `rackai@79ca4de:hack/cli/examples/lmcache-shared-kv-modelclass.yaml`, is not separated per tenant; rule B-2 in [[Sovereign Isolation & Assurance PRD]] covers it.)*
3. **Time-slicing and MPS shouldn't carry mutually distrustful tenants** with sensitive data; the vendor states no memory isolation. MIG is stronger but leaks activity patterns.
4. **Level 1 removes the silicon class** (leftover memory, side channels, Rowhammer between tenants). It plausibly matters for proprietary alpha, regulated data, model weights as IP and prompts carrying secrets. Whole GPUs in a shared multi-GPU box can still leak (Spy in the GPU-box), which bears on whether Level 1 needs a dedicated node.
5. **On MI-series hardware, Level 1 is the stronger story:** AMD publishes no isolation claim for its partitions and no GPU confidential computing.
6. **Regulation is mostly risk-based,** not a dedicated-hardware mandate, outside defence (IL5) and some sovereign-cloud regimes. The fit calls in [[Sovereignty Levels]] are therefore judgement, pending security and legal review.

## See Also

- [[Sovereignty Levels]] · [[Three Battlegrounds]] · [[AMD Instinct]]
- [[Evidence Hub]]
- [[Sovereign Isolation & Assurance PRD]] — boundary rules that address these risks (draft)

