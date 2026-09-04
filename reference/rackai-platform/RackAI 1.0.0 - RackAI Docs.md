---
title: "RackAI 1.0.0 - RackAI Docs"
source: "https://docs.rackai.rax.io/release-notes/1.0.0/"
author:
published: 2026-07-30
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## RackAI Release Bulletin — 1.0.0

## What's New

**Control plane (`rackai`)**

- **Accelerator selection & scheduling.** Choose hardware for a deployment via AcceleratorClass with node affinity, a `--accelerator-class` flag in `rackaictl`, and read-access RBAC.
- **AMD GPU support end to end.** New AMD AIM inference runtime, fine-tuning on AMD GPUs, and GPU-memory autoscaling on AMD nodes.
- **Accelerator inventory & visibility.** Automated discovery with live capacity, plus accelerator info and GPU SKUs reported in `ModelDeployment` status.
- **Install flexibility.** New `SKIP_CERT_MANAGER` / `SKIP_GATEWAY_API` flags let you skip provisioning components your cluster already has.

**Web console (`rackai-ui`)**

- **GPU visibility in the UI.** New GPU Overview card on the home page (capacity + by-model layout) and GPU availability shown directly in accelerator dropdowns.
- **AMD & accelerator-aware UI.** AMD AIM inference runtime with AcceleratorClass selection, accelerator SKUs rendered per vendor, and status-reported accelerator on deployment details.
- **LoRA for AIM deployments.** Enable LoRA adapters on AIM-runtime deployments.
- **Enterprise sign-in.** Keycloak auth via a drop-in `@auth0/auth0-react` shim.
- **Live status.** Model and dataset reconciliation polling, a model-deployment details panel, and a failure banner for failed fine-tuning jobs.
- **Data management polish.** Dataset edit dialog with optional fields, formatted size on the model-stores table, URL-driven modals, and stronger organization-name validation.

## Fixes & Improvements

- **Control plane:** corrected GPU-memory autoscaling on AMD nodes; refreshed AIM / `gemma-4` model classes (pinning the optimized NIM runtime image by digest); dataplane fixes (enabled SeaweedFS workers, 3 GB volume-size limit, longer model-downloader verify timeout); added kube-state-metrics, AMD GPU, and kubelet/cAdvisor scrape targets.
- **Web console:** more accurate deploy and fine-tuning forms (autoscaling/custom-args summaries, AMD-aware fields, model-name display, validation-dataset selection); GPU Overview card hides gracefully when no GPU status is reported; improved homepage responsiveness; tables gained filtering, per-user sorting, and cache status; resolved open Dependabot alerts.

## Deploy / Install

**Container images** (`rackspacengpc/…:1.0.0`)

Control plane & finetuning: `rackai-manager`, `rackai-organizer`, `rackai-stub`, `rackai-copier`, `rackai-model-downloader`, `rackai-trainer`, `rackai-evaluator`, `rackai-preprocessor`, `rackai-dataset-validator`; plus the web console `rackai-ui`.

**Helm charts** — published to `oci://registry-1.docker.io/rackspacengpc` at version `1.0.0`.

Control plane umbrella chart (bundles apiserver, frontproxy, manager, organizer, ui):

```bash
helm install rackai oci://registry-1.docker.io/rackspacengpc/rackai --version 1.0.0
```

Dataplane charts (`scripts/deployment/setup-rackai-dataplane.sh` installs these with the required values):

```bash
helm install rackai-seaweedfs oci://registry-1.docker.io/rackspacengpc/rackai-seaweedfs --version 1.0.0
helm install rackai-seaweedfs-csi oci://registry-1.docker.io/rackspacengpc/rackai-seaweedfs-csi --version 1.0.0
helm install rackai-monitoring oci://registry-1.docker.io/rackspacengpc/rackai-monitoring --version 1.0.0
helm install rackai-keda oci://registry-1.docker.io/rackspacengpc/rackai-keda --version 1.0.0
```
Technical Appendix (internal engineering detail)

### RSS-Engineering/rackai — 1.0.0

- **Compare:** https://github.com/RSS-Engineering/rackai/compare/0.0.2...1.0.0
- **Release:** https://github.com/RSS-Engineering/rackai/releases/tag/1.0.0
- **Scope:** changes since 0.0.2 (tag baseline); 32 commits
- **JIRA tickets:** RACKAI-147, RACKAI-185, RACKAI-186, RACKAI-203, RACKAI-217, RACKAI-219, RACKAI-229, RACKAI-232, RACKAI-239, RACKAI-242, RACKAI-249, RACKAI-250, RACKAI-251, RACKAI-307, RACKAI-312, RACKAI-318, RACKAI-321, RACKAI-324

#### Features

- phase 1 accelerator selection (AcceleratorClass + nodeAffinity) ([#147](https://github.com/RSS-Engineering/rackai/pull/147)) — [`f60433a`](https://github.com/RSS-Engineering/rackai/commit/f60433aaec1d6db11e3e8b396d13ba9f55acd825)
- remove Tolerations from AcceleratorClass ([#159](https://github.com/RSS-Engineering/rackai/pull/159)) — [`afefd8f`](https://github.com/RSS-Engineering/rackai/commit/afefd8f9b4cd6c785ed9780405b890fca001efa6)
- disambiguate acceleratorClass="" from "auto" ([#160](https://github.com/RSS-Engineering/rackai/pull/160)) — [`c6137d6`](https://github.com/RSS-Engineering/rackai/commit/c6137d6283e52d07325c8ea5a72f674ce8e19564)
- read access for AcceleratorClass — RBAC + CLI ([#163](https://github.com/RSS-Engineering/rackai/pull/163)) — [`e760806`](https://github.com/RSS-Engineering/rackai/commit/e760806208a21cf34fddf28594e45582b9262a44)
- add --accelerator-class flag to rackaictl create commands ([#166](https://github.com/RSS-Engineering/rackai/pull/166)) — [`657b036`](https://github.com/RSS-Engineering/rackai/commit/657b036a91ebe171a49707d5cbcab031adb60cea)
- add AMD AIM inference runtime ([#161](https://github.com/RSS-Engineering/rackai/pull/161)) — [`dcec242`](https://github.com/RSS-Engineering/rackai/commit/dcec242af3aa4e56e200f4be2a62799f730f6ce3)
- add SKIP\_CERT\_MANAGER, SKIP\_GATEWAY\_API and SKIP\_GATEWAY\_API flags ([#174](https://github.com/RSS-Engineering/rackai/pull/174)) — [`88755fc`](https://github.com/RSS-Engineering/rackai/commit/88755fca16dd6a8323e335eaec122a8ad9412da1)
- fine tuning on AMD GPUs ([#158](https://github.com/RSS-Engineering/rackai/pull/158)) — [`9679711`](https://github.com/RSS-Engineering/rackai/commit/96797111036fc45fc638ce6ef324b5401efd2e4b)
- add accelerator info to ModelDeployment status ([#183](https://github.com/RSS-Engineering/rackai/pull/183)) — [`9189854`](https://github.com/RSS-Engineering/rackai/commit/9189854690f2b3d1686ab93a43ad2dc37f124d92)
- report GPU SKUs in ModelDeployment status ([#197](https://github.com/RSS-Engineering/rackai/pull/197)) — [`9b18855`](https://github.com/RSS-Engineering/rackai/commit/9b18855875fecc1f0b758ee7b1f9c11247abf98f)
- accelerator inventory automation — discovery, live capacity, AMD support, tolerations ([#178](https://github.com/RSS-Engineering/rackai/pull/178)) — [`6975402`](https://github.com/RSS-Engineering/rackai/commit/697540217618752a70f2b0f21bc9eef49bf6c6a0)

#### Bug Fixes

- update the go mod to use RSS-Engineering as module repos ([#157](https://github.com/RSS-Engineering/rackai/pull/157)) — [`b388a74`](https://github.com/RSS-Engineering/rackai/commit/b388a7437f8a7999d925013c607edfde91ed1dcb)
- enable seaweedfs workers in dataplane setup ([#170](https://github.com/RSS-Engineering/rackai/pull/170)) — [`a5a941d`](https://github.com/RSS-Engineering/rackai/commit/a5a941dfef78cff71fc1afd7ba63337782fe44fb)
- update aim modelclasses ([#172](https://github.com/RSS-Engineering/rackai/pull/172)) — [`2a83aad`](https://github.com/RSS-Engineering/rackai/commit/2a83aadc08df33a6209e6296e84b46c600df011e)
- rename modelclass, model and file names to maintain consistency — [`1a88c09`](https://github.com/RSS-Engineering/rackai/commit/1a88c0926548751e887b959ded0161a290028ab3)
- the GPU-memory autoscaling on AMD nodes ([#177](https://github.com/RSS-Engineering/rackai/pull/177)) — [`4a2f0ed`](https://github.com/RSS-Engineering/rackai/commit/4a2f0edd84627770c1dc2b1d3622949b01e96f4b)
- update gemma-4-31b-it-optimized-nim-vllm modelclass ([#210](https://github.com/RSS-Engineering/rackai/pull/210)) — [`a4608db`](https://github.com/RSS-Engineering/rackai/commit/a4608db9e7531c0aa019b59c060728830de0f248)
- stop release-please from rewriting pinned amdEvaluator tag — [`b5d82a6`](https://github.com/RSS-Engineering/rackai/commit/b5d82a62cbc8dcb545a77615aeaa8718308527be)

#### CI

- use annotation-based updaters to preserve comments ([#189](https://github.com/RSS-Engineering/rackai/pull/189)) — [`9cd4545`](https://github.com/RSS-Engineering/rackai/commit/9cd45453189128f32d172cfb2ee5ce3611bb71ae)
- run release-please on maintenance branches — [`3466d03`](https://github.com/RSS-Engineering/rackai/commit/3466d03c73f2ad86eca0c0a17bf18f8d9df6bdb2)

#### Miscellaneous

- release 1.0.0 — [`d3c4043`](https://github.com/RSS-Engineering/rackai/commit/d3c4043918229c2b011bea726be4fffd750c727d)
- release 1.0.0 ([#216](https://github.com/RSS-Engineering/rackai/pull/216)) — [`02965af`](https://github.com/RSS-Engineering/rackai/commit/02965afbc1613ec99d63b98893dc2c2f4730a6bd)

#### Other

- add kube-state-metrics, AMD GPU, and kubelet/cAdvisor scrape targets ([#173](https://github.com/RSS-Engineering/rackai/pull/173)) — [`2867da8`](https://github.com/RSS-Engineering/rackai/commit/2867da8cbe3fd5c3d35edbd70d493d2b419e9aa5)
- bumped auth0 version from 1.21 to 1.44 to get pass the deprecation notice ([#179](https://github.com/RSS-Engineering/rackai/pull/179)) — [`090292b`](https://github.com/RSS-Engineering/rackai/commit/090292b354b03b1fa367e846771fd87d959f1603)
- add 3GB volume size limit for seaweedfs. Increase verify timeout in model downloader script to 15m ([#193](https://github.com/RSS-Engineering/rackai/pull/193)) — [`f119e18`](https://github.com/RSS-Engineering/rackai/commit/f119e187f41abce6fcf725f790ae9f8c67a97062)
- update modelclass for optimized nim runtime, to use image sha256 by replacing latest tag ([#196](https://github.com/RSS-Engineering/rackai/pull/196)) — [`b47ee0c`](https://github.com/RSS-Engineering/rackai/commit/b47ee0c86cd6147795cd782c8488dea565da1598)
- Change release version from 0.0.2 to 0.0.3 ([#198](https://github.com/RSS-Engineering/rackai/pull/198)) — [`1f4784f`](https://github.com/RSS-Engineering/rackai/commit/1f4784fae8f03d6f8a61c43c59995f612d2ba11a)
- setting ftj default resources in manager values ([#199](https://github.com/RSS-Engineering/rackai/pull/199)) — [`754d25d`](https://github.com/RSS-Engineering/rackai/commit/754d25dae79e08a538f433698e8c73cc5d4f508d)
- regenerate generated files — [`a3f80df`](https://github.com/RSS-Engineering/rackai/commit/a3f80df058116c82fc43ad5b41d5547bdfbd7279)
- fixed the finetuning deps versions ([#202](https://github.com/RSS-Engineering/rackai/pull/202)) — [`8092612`](https://github.com/RSS-Engineering/rackai/commit/809261249019d3784de163335b21ac3e699d550c)
- add support for gemma-4 with nim optimized runtime ([#205](https://github.com/RSS-Engineering/rackai/pull/205)) — [`2f09c97`](https://github.com/RSS-Engineering/rackai/commit/2f09c974865ca48d800ff71cead9729e86c86053)
- Change release version from 0.0.3 to 0.0.4 — [`4341691`](https://github.com/RSS-Engineering/rackai/commit/43416918f7dbe18f2c18e935feb0305dd6d58338)

### RSS-Engineering/rackai-ui — 1.0.0

- **Release:** https://github.com/RSS-Engineering/rackai-ui/releases/tag/1.0.0
- **Scope:** commits since 2026-06-06 (date-based one-off — prior UI releases are untagged); 53 commits
- **JIRA tickets:** RACKAI-204, RACKAI-329

#### Features

- redesign GPU Overview card (capacity + by-model layout) ([#162](https://github.com/RSS-Engineering/rackai-ui/pull/162)) — [`bc9a058`](https://github.com/RSS-Engineering/rackai-ui/commit/bc9a05896d74c3d0c0d130e0ab54d2ff004d97d8)
- add GPU Overview card to the Home page — [`4b6c814`](https://github.com/RSS-Engineering/rackai-ui/commit/4b6c8148754126f7ed66ea9272b270a203efb14b)
- surface GPU availability in accelerator dropdowns ([#159](https://github.com/RSS-Engineering/rackai-ui/pull/159)) — [`76c3e4c`](https://github.com/RSS-Engineering/rackai-ui/commit/76c3e4c0de6e77c231d3b2b38db90e3848559124)
- improve homepage responsiveness and add ClippedBadges component ([#155](https://github.com/RSS-Engineering/rackai-ui/pull/155)) — [`ee50e91`](https://github.com/RSS-Engineering/rackai-ui/commit/ee50e916e2f906cc881d9ee71ef628033d02e9cd)
- implement runtime badge colors and refactor related components ([#153](https://github.com/RSS-Engineering/rackai-ui/pull/153)) — [`83786ad`](https://github.com/RSS-Engineering/rackai-ui/commit/83786ad852127ed0266f9a61977f81abf0608be8)
- render ModelDeployment accelerator SKUs as a list with vendor ([#147](https://github.com/RSS-Engineering/rackai-ui/pull/147)) — [`ef61a5d`](https://github.com/RSS-Engineering/rackai-ui/commit/ef61a5d24a9b51b8785d9455d691d43d482612ad)
- add failure message banner for failed fine-tuning jobs ([#148](https://github.com/RSS-Engineering/rackai-ui/pull/148)) — [`ee201ec`](https://github.com/RSS-Engineering/rackai-ui/commit/ee201ecd1ab23fc0098e412161ad0b6a092380e2)
- Keycloak UI auth via a drop-in @auth0/auth0-react shim ([#145](https://github.com/RSS-Engineering/rackai-ui/pull/145)) — [`c7c9fa9`](https://github.com/RSS-Engineering/rackai-ui/commit/c7c9fa90f8519696c6cb85f8c08bf83e7b74eef0)
- surface status-reported accelerator on deployed model details, with tests ([#139](https://github.com/RSS-Engineering/rackai-ui/pull/139)) — [`eb7756d`](https://github.com/RSS-Engineering/rackai-ui/commit/eb7756d1093ca2674852a656c63dd04878d85ff9)
- enable LoRA adapters for AIM-runtime deployments (RACKAI-268) ([#132](https://github.com/RSS-Engineering/rackai-ui/pull/132)) — [`c849af1`](https://github.com/RSS-Engineering/rackai-ui/commit/c849af1fb9cb7c4e044773dfe1ee0f7e08ecb5cc)
- AMD AIM inference runtime + AcceleratorClass in the UI ([#121](https://github.com/RSS-Engineering/rackai-ui/pull/121)) — [`c92f1ce`](https://github.com/RSS-Engineering/rackai-ui/commit/c92f1ce536af756070b57435edd0112de1e797af)
- add Model deployment details panel ([#120](https://github.com/RSS-Engineering/rackai-ui/pull/120)) — [`dd68c63`](https://github.com/RSS-Engineering/rackai-ui/commit/dd68c63db91ee947c086254163834484e4cc0db3)
- add getDataset method and implement polling for dataset reconciliation ([#119](https://github.com/RSS-Engineering/rackai-ui/pull/119)) — [`56c24cb`](https://github.com/RSS-Engineering/rackai-ui/commit/56c24cbfc13f1f91317c0c12da951ce3f4b56091)
- add getModel method and implement model reconciliation polling ([#118](https://github.com/RSS-Engineering/rackai-ui/pull/118)) — [`51596b3`](https://github.com/RSS-Engineering/rackai-ui/commit/51596b3f25bb9d03a238a4ffa2b447c56c9454c6)
- add formatted size display to model stores table ([#113](https://github.com/RSS-Engineering/rackai-ui/pull/113)) — [`ea60028`](https://github.com/RSS-Engineering/rackai-ui/commit/ea600285d53d5339bfb2a3b8eedcfd5406253a4c)
- enhance organization name validation and error messaging in forms ([#111](https://github.com/RSS-Engineering/rackai-ui/pull/111)) — [`8e56892`](https://github.com/RSS-Engineering/rackai-ui/commit/8e568927f3a34a52658509befb9a871cdd7312ee)
- implement URL-driven modals for improved dialog management across pages ([#110](https://github.com/RSS-Engineering/rackai-ui/pull/110)) — [`c9de437`](https://github.com/RSS-Engineering/rackai-ui/commit/c9de4376a055717b1962819353b7668f668d9fe1)
- enhance dataset management with edit dialog and optional fields ([#108](https://github.com/RSS-Engineering/rackai-ui/pull/108)) — [`de610eb`](https://github.com/RSS-Engineering/rackai-ui/commit/de610eb47578a6f9489e7521ad55cba62b7fdf6b)

#### Bug Fixes

- skip Auth0 org-list call in keycloak mode ([#165](https://github.com/RSS-Engineering/rackai-ui/pull/165)) — [`ddbcff7`](https://github.com/RSS-Engineering/rackai-ui/commit/ddbcff7c6ed3f166797ea4bbc2ae7773d35f23cd)
- hide GPU Overview card when no GPU status reported ([#164](https://github.com/RSS-Engineering/rackai-ui/pull/164)) — [`6b1a14a`](https://github.com/RSS-Engineering/rackai-ui/commit/6b1a14a2f960656ed37ec6dbddd40941c284c96b)
- update GPU Overview card messages for clarity ([#163](https://github.com/RSS-Engineering/rackai-ui/pull/163)) — [`ab547a2`](https://github.com/RSS-Engineering/rackai-ui/commit/ab547a2f005e0d7e71577d6031d422128a21eaf9)
- gate GPU Overview card on load; test donut segment guards — [`246ff7b`](https://github.com/RSS-Engineering/rackai-ui/commit/246ff7b9d5a4eef97f0990932fb70af30223bbf2)
- improve homepage responsiveness by adjusting grid gaps and layout for resource cards ([#157](https://github.com/RSS-Engineering/rackai-ui/pull/157)) — [`c17977f`](https://github.com/RSS-Engineering/rackai-ui/commit/c17977fa9f70c637d00e0e99d42b0e9d10aa01ee)
- show LoRA (not QLoRA) for AMD fine-tuning jobs in details view ([#154](https://github.com/RSS-Engineering/rackai-ui/pull/154)) — [`ba8b1ef`](https://github.com/RSS-Engineering/rackai-ui/commit/ba8b1ef1616321cc29fbf522fb27310e4b8e0cf0)
- set version number to 0.0.3 in package.json ([#150](https://github.com/RSS-Engineering/rackai-ui/pull/150)) — [`53e28bf`](https://github.com/RSS-Engineering/rackai-ui/commit/53e28bf85d00d37635c1950881b209222aae1623)
- use the actual response, not stale state, in useUpdateAction ([#143](https://github.com/RSS-Engineering/rackai-ui/pull/143)) — [`d33f0fa`](https://github.com/RSS-Engineering/rackai-ui/commit/d33f0fa8a4a2f29ffe2fcbcaa5fa7e927220353c)
- clean up.gitignore by removing unnecessary entries and organizing sections ([#142](https://github.com/RSS-Engineering/rackai-ui/pull/142)) — [`3c9b5a5`](https://github.com/RSS-Engineering/rackai-ui/commit/3c9b5a5ee5da1d0a472c0dafc6b6555e33ee65fd)
- conditionally display Save Interval for AMD Trainer support ([#141](https://github.com/RSS-Engineering/rackai-ui/pull/141)) — [`320d992`](https://github.com/RSS-Engineering/rackai-ui/commit/320d992c9153e6745e083010e8c02664cb645b1f)
- correct invalid tsconfig ignoreDeprecations value and test fixture type ([#138](https://github.com/RSS-Engineering/rackai-ui/pull/138)) — [`7ae533b`](https://github.com/RSS-Engineering/rackai-ui/commit/7ae533b72e9fe1baa17b0c04d80bf32c30c0986b)
- resolve open Dependabot security alerts across dependency tree ([#137](https://github.com/RSS-Engineering/rackai-ui/pull/137)) — [`980eed5`](https://github.com/RSS-Engineering/rackai-ui/commit/980eed526c361fc8fa3cdb82f2a5af4519c9b843)
- remove accelerator counts from vendor toggle ([#131](https://github.com/RSS-Engineering/rackai-ui/pull/131)) — [`618e6c9`](https://github.com/RSS-Engineering/rackai-ui/commit/618e6c9f97984162b39595e1f35edcf706436db4)
- keep in-flight LoRA uploads out of terminal Failed (RACKAI-267) ([#130](https://github.com/RSS-Engineering/rackai-ui/pull/130)) — [`eadaa4f`](https://github.com/RSS-Engineering/rackai-ui/commit/eadaa4f1bdda5015ee766b78c84b5304dfa4b522)
- fine-tuning end time, AMD-aware fields, and validation dataset selection ([#129](https://github.com/RSS-Engineering/rackai-ui/pull/129)) — [`1c96e75`](https://github.com/RSS-Engineering/rackai-ui/commit/1c96e75bb83584c47aa979e1954162b2f0fd5e41)
- show only display name in model dropdown after selection ([#128](https://github.com/RSS-Engineering/rackai-ui/pull/128)) — [`794761a`](https://github.com/RSS-Engineering/rackai-ui/commit/794761a40083cb99474bc082ddd2e3c3f001c7f8)
- don't auto-select model; always show Model in deploy summary ([#127](https://github.com/RSS-Engineering/rackai-ui/pull/127)) — [`c3d110b`](https://github.com/RSS-Engineering/rackai-ui/commit/c3d110bb195d67026a50c97bbea8db3e1f2eafdf)
- reflect autoscaling and custom args in deploy summary ([#126](https://github.com/RSS-Engineering/rackai-ui/pull/126)) — [`df2aab6`](https://github.com/RSS-Engineering/rackai-ui/commit/df2aab68e2a5fdaa7da7a1ed78ce39caf5c320a7)
- include model data in editModel function call ([#116](https://github.com/RSS-Engineering/rackai-ui/pull/116)) — [`160dd32`](https://github.com/RSS-Engineering/rackai-ui/commit/160dd322fd88fa99b5056c0dcb0219891e9485ed)
- correct model detail navigation and adjust grid layout for models catalog ([#112](https://github.com/RSS-Engineering/rackai-ui/pull/112)) — [`7d9a5a6`](https://github.com/RSS-Engineering/rackai-ui/commit/7d9a5a6b072bee8bb78f3f3a6e4809354f7f12eb)

#### Refactoring

- remove unused test files and utility functions ([#135](https://github.com/RSS-Engineering/rackai-ui/pull/135)) — [`3cdbaae`](https://github.com/RSS-Engineering/rackai-ui/commit/3cdbaae6a1c3f21c6edd7dcc724f4f6808afd64d)

#### Tests

- add unit test coverage for hooks, utils, data, and components ([#152](https://github.com/RSS-Engineering/rackai-ui/pull/152)) — [`1c34f92`](https://github.com/RSS-Engineering/rackai-ui/commit/1c34f923c4c9024cc107e80acf402bbf6f9cc64b)
- add unit tests for src/pages with Jest + RTL ([#136](https://github.com/RSS-Engineering/rackai-ui/pull/136)) — [`41c008a`](https://github.com/RSS-Engineering/rackai-ui/commit/41c008aefc7d3ff19710a9517077fb1a42733ba)

#### Miscellaneous

- set up Jest + React Testing Library ([#122](https://github.com/RSS-Engineering/rackai-ui/pull/122)) — [`3cf157c`](https://github.com/RSS-Engineering/rackai-ui/commit/3cf157c9b57a3742a91cdcb574811c562353d1ba)

#### Other

- v1.0.0 — [`d60a843`](https://github.com/RSS-Engineering/rackai-ui/commit/d60a843622aacdf875c3c5c62faca0e14b9176b8)
- Update runtime badge colors ([#156](https://github.com/RSS-Engineering/rackai-ui/pull/156)) — [`fffbe6f`](https://github.com/RSS-Engineering/rackai-ui/commit/fffbe6f0b08a71e1f80997be124d6805fb362197)
- Remove leftover Apache LICENSE file copied from template, not applicable to this project ([#149](https://github.com/RSS-Engineering/rackai-ui/pull/149)) — [`2cb15d5`](https://github.com/RSS-Engineering/rackai-ui/commit/2cb15d55b6d54dcfacbe5e3200f45c3955909dcf)
- RACKAI-266: consistent display-name/resource-name identity + standardized dropdown sorting ([#125](https://github.com/RSS-Engineering/rackai-ui/pull/125)) — [`1fc030d`](https://github.com/RSS-Engineering/rackai-ui/commit/1fc030d96c63f3024c3e7f43c8a3bb22e47d29c8)
- Added filtering options for model data table and implemented per-user table sorting prefs ([#117](https://github.com/RSS-Engineering/rackai-ui/pull/117)) — [`0659836`](https://github.com/RSS-Engineering/rackai-ui/commit/06598369bb544d55fdff002782c519f3939ab372)
- Update model caching logic and add cache status to models table ([#115](https://github.com/RSS-Engineering/rackai-ui/pull/115)) — [`4bfb7d3`](https://github.com/RSS-Engineering/rackai-ui/commit/4bfb7d3be34d30b305d09939bca86bce29ff1780)
- Improve data table design ([#114](https://github.com/RSS-Engineering/rackai-ui/pull/114)) — [`d7ddff3`](https://github.com/RSS-Engineering/rackai-ui/commit/d7ddff331ee405465d889865c8ac49ab73717a8c)
- RACKAI -189 / feat: enhance model deployment form with caching requirements and UI … ([#109](https://github.com/RSS-Engineering/rackai-ui/pull/109)) — [`d812de2`](https://github.com/RSS-Engineering/rackai-ui/commit/d812de20daace647f196cdf808104d8ec5fbae43)
- Enhance model details panel with additional metadata. Add description column to table ([#106](https://github.com/RSS-Engineering/rackai-ui/pull/106)) — [`1512fe6`](https://github.com/RSS-Engineering/rackai-ui/commit/1512fe6eda3c9db27e78374e7a7770f95790ed17)
- Add an edit form for LoRA adapters. Add a description column to the adapters table ([#105](https://github.com/RSS-Engineering/rackai-ui/pull/105)) — [`7e11e24`](https://github.com/RSS-Engineering/rackai-ui/commit/7e11e24bb965c964b47dbafbcddfe71e0af4065e)
- Show min/max scaling replicas in deployment card ([#104](https://github.com/RSS-Engineering/rackai-ui/pull/104)) — [`746a3d5`](https://github.com/RSS-Engineering/rackai-ui/commit/746a3d5f418f4a2fa538209037cc052ed59fc802)