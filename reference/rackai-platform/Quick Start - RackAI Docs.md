---
title: "Quick Start - RackAI Docs"
source: "https://docs.rackai.rax.io/getting-started/quick-start/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## Quick Start

Get a minimal RackAI environment running.

1. Clone the repository.
2. Configure your inventory.
3. Run the provisioning playbook.
```bash
ansible-playbook -i inventory/dev_hosts.yaml deploy_rackai/playbooks/provision.yml
```