---
id: evd-compute-supply-sovereign-demand-2026
type: evidence
status: draft
owner: product
domain: strategy
aliases: [why now evidence, ai compute supply demand, compute demand outpaces supply, sovereign ai demand, datacenter power scarcity, dc vacancy, gpu price decline, ai overbuild]
related: [hub-why-now, hub-battlegrounds, hub-evidence, ent-gpu-amd-instinct, asm-dc-capacity-available, asm-mi350p-serving-competitive, evd-gpu-neocloud-competitors, evd-sovereign-governed-competitors, wiki-roadmap-narratives]
source_docs: ["web research 2026-10-09 (sources listed per item)"]
confidence: derived
last_reviewed: 2026-10-09
parent: hub-evidence
summary: "Sourced 2025–26 evidence that AI compute demand outruns supply, power gates capacity and sovereign demand is rising."
---

# AI Compute Supply and Sovereign Demand 2026

External market evidence behind the [[Why Now]] argument, gathered 2026-10-09. Each item names its source, date and type. **Type:** P = primary (company filing, official body) · V = vendor claim · 3P = independent third party (vendor-sponsored where noted) · C = counter-evidence. Items marked **[2nd]** were confirmed only through secondary coverage: check the primary source before using them outside this wiki.

> **Confidence `derived`.** The individual figures are reported by their sources; their bearing on RackAI is inference. None of this is RackAI demand. RackAI has no measured demand signal yet ([[GPU Capacity Demand Rationale]]).

## 1. AI compute demand still outruns supply

| # | Evidence | Source, date | Type |
|---|----------|--------------|:----:|
| 1.1 | NVIDIA Q2 FY27 revenue $96.2B (+106% YoY); Data Center $89.0B (+117% YoY) | NVIDIA 8-K press release, 2026-08-26 ([SEC](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)) | P |
| 1.2 | Microsoft: Azure +43%, demand still above available capacity; FY27 capex ~$175B, aiming to roughly double total capacity in two years | Microsoft FY26 Q4 call, 2026-07-29 ([summary](https://www.marketbeat.com/instant-alerts/microsoft-q4-earnings-call-highlights-2026-07-29/)) | P [2nd] |
| 1.3 | Microsoft, Alphabet, Amazon and Meta guide to ~$725B combined 2026 capex, ~+77% on 2025; >$1T expected in 2027 (Evercore, BofA) | Q1 2026 earnings season ([aggregation](https://aiweekly.co/alerts/amazon-microsoft-alphabet-meta-plan-725b-ai-capex-in-2026)) | 3P [2nd] |
| 1.4 | Oracle remaining performance obligations $664B, +$209B YoY; >$30B new AI cloud contracts in the quarter (BofA: ~half of RPO is one customer) | Oracle Q1 FY27 release, 2026-09-10 ([Oracle](https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/)) | P |
| 1.5 | CoreWeave Q2 2026 revenue ~$2.6B (+112% YoY), backlog ~$104B; 2026 capex guide raised to $35–39B (GAAP net loss ~$626M) | CoreWeave Q2 2026 results, Aug 2026 ([CoreWeave IR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/)) | P |
| 1.6 | Google processes >3.2 quadrillion tokens a month, ~7x YoY (self-reported, all surfaces) | Google I/O 2026 keynote, May 2026 ([Google](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)) | V |
| 1.7 | Data-centre electricity demand +17% in 2025 vs ~3% for all demand; still expected to roughly double by 2030 | IEA, *Key Questions on Energy and AI*, Apr 2026 ([coverage](https://letsdatascience.com/news/ai-drives-surge-in-data-centre-electricity-demand-16cbe703)) | P [2nd] |

## 2. Power and space, not chips, are the gating resource

| # | Evidence | Source, date | Type |
|---|----------|--------------|:----:|
| 2.1 | North American primary-market vacancy at a record-low 1.4% despite ~34% inventory growth; 7,481 MW under construction, 80.4% preleased | CBRE *North American Data Center Trends H1 2026*, 2026-09-02 ([CBRE](https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction); [coverage](https://www.constructiondive.com/news/data-center-all-time-low-vacancy-record-construction/829339/)) | 3P |
| 2.2 | Power availability, not land or capital, is the dominant limiting factor | JLL *2026 Global Data Center Outlook*, early 2026 ([coverage](https://datacenterfrontier.com/cloud/article/55341273/jlls-2026-global-data-center-outlook-navigating-the-ai-supercycle-power-scarcity-and-structural-market-transformation)) | 3P [2nd] |
| 2.3 | Concern about power availability rising; modal rack density 11 kW (from 9 kW) | Uptime Institute *Global Data Center Survey 2026*, 2026-07-29 ([Uptime](https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2026)) | 3P |
| 2.4 | Power limits hold capacity below demand through 2027 | Moody's, 2026 ([DCD](https://www.datacenterdynamics.com/en/news/us-hyperscaler-capex-to-top-700bn-in-2026-investors-fear-overbuild-and-weak-returns-moodys/)) | 3P [2nd] |

**Why this matters for RackAI:** if powered space is the constraint, capacity that fits *existing* air-cooled racks is worth more than its chip count suggests. The MI350P is a passively air-cooled, 600 W PCIe card ([[AMD Instinct]]), so it fits standard racks without liquid cooling. That's a vendor specification, not a measured efficiency.

## 3. Sovereign and private AI demand is rising

| # | Evidence | Source, date | Type |
|---|----------|--------------|:----:|
| 3.1 | Sovereign-cloud IaaS spend $80B in 2026, +35.6%; Europe +83%; governments then regulated industries lead; ~20% of current workloads move from global to local providers | Gartner, 2026-02-09 ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-02-09-gartner-says-worldwide-sovereign-cloud-iaas-spending-will-total-us-dollars-80-billion-in-2026)) | 3P |
| 3.2 | By 2030, >75% of European and Middle Eastern enterprises move workloads to sovereign solutions, from <5% in 2025 | Gartner *Top Strategic Technology Trends 2026*, Oct 2025 ([coverage](https://www.crnasia.com/india/news-network/news/gartner-unveils-top-strategic-technology-trends-for-2026)) | 3P [2nd] |
| 3.3 | NVIDIA sovereign AI revenue >$30B in FY26, over 3x YoY | NVIDIA Q4 FY26 call, Feb 2026 ([summary](https://futurumgroup.com/?p=87030)) | P [2nd] |
| 3.4 | 68% of executives find residency and sovereignty requirements across geographies challenging; 91% don't fully understand their AI vendor dependencies (n=1,000) | IBM IBV / Oxford Economics, 2026-06-17 ([IBM](https://newsroom.ibm.com/2026-06-17-ibm-study-limited-control-and-rising-dependencies-leave-enterprises-exposed-in-the-age-of-ai)) | 3P (vendor-sponsored) |
| 3.5 | 66% moved AI workloads from public cloud to on-prem or private cloud in the past year (n=1,500); but inference still runs hybrid 31% / public 30% / private 22% / on-prem 8% | Cloudera, Aug 2026 ([coverage](https://virtualizationreview.com/articles/2026/08/12/cloudera-survey-66-percent-repatriated-ai-workloads-from-public-cloud.aspx)) | 3P (vendor-sponsored) |
| 3.6 | EU AI Gigafactories call: up to 7 sites of >100k processors each, ~€10B public + ~€20B private; closes 2026-11-12 | European Commission, opened ~2026-07-30 ([coverage](https://pasqualepillitteri.it/en/news/9162/eu-call-seven-ai-gigafactories-30-billion)) | P [2nd] |

**Not a reason:** the EU AI Act Digital Omnibus (Reg. (EU) 2026/1744, in force 2026-07-27) postponed high-risk obligations to 2027–2028 ([analysis](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)). The sovereign case rests on residency, control and dependency risk, not an imminent AI Act deadline.

## 4. Counter-evidence (keep it in view)

| # | Evidence | Source | Type |
|---|----------|--------|:----:|
| C1 | H100 on-demand prices ~$1.80–3.50/hr by Q2 2026, down ~64–75% from the 2024 peak; reserved pricing reportedly firmer [2nd] | GPU price indices ([Introl](https://introl.com/blog/gpu-cloud-price-collapse-h100-64-percent-drop-2025), [Silicon Data](https://www.silicondata.com/blog/h100-rental-price-over-time)); figures inconsistent | C |
| C2 | Hyperscaler capex >$700B in 2026 raises fears of overbuild and weak returns | Moody's, 2026 ([DCD](https://www.datacenterdynamics.com/en/news/us-hyperscaler-capex-to-top-700bn-in-2026-investors-fear-overbuild-and-weak-returns-moodys/)) [2nd] | C |
| C3 | AI infrastructure called a bubble, though unlikely to burst before 2027 | Macquarie ([SCMP](https://www.scmp.com/business/banking-finance/article/3354118/ai-infrastructure-investment-bubble-unlikely-burst-2027-macquarie)) | C |
| C4 | Hyperscalers don't disclose AI-only utilization or per-site returns, so neither shortage nor overbuild can be tested directly | — | C |

**Reading the counter-evidence:** commodity GPU-hours are getting cheaper while powered space and committed capacity stay tight. That favours selling operation, placement and control rather than raw GPUs, which is the identity's position anyway ([[Three Battlegrounds]]: we refuse to compete as a frontier GPU cloud).

## Overall Read

- **Strong:** capacity tightness and capex momentum (primary filings); record-low vacancy with power as the gate (CBRE, Uptime, Moody's).
- **Moderate:** the sovereign trend. Gartner is solid; most enterprise surveys are vendor-sponsored and measure intent, not spend.
- **Weak / absent:** anything specific to RackAI. No independent MI350P benchmark exists; vendor tokens-per-dollar claims depend on pricing.

## See Also

- [[Why Now]]: the argument this evidence supports
- [[GPU Neocloud Competitors]] · [[Sovereign & Governed AI Competitors]]
- [[Evidence Hub]]
