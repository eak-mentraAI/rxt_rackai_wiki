---
title: "Cluster Deployment - RackAI Docs"
source: "https://docs.rackai.rax.io/guides/cluster-deployment/"
author:
published:
created: 2026-09-04
description: "Documentation for RackAI"
tags:
  - "clippings"
---
## Deploy Infra / K8s Cluster on Production

This guide walks through deploying a production-ready HA Kubernetes cluster on Rackspace Undercloud using the `rackai.deploy_rackai` Ansible collection. The automation provisions bare metal servers, configures networking, and delegates Kubernetes bootstrap to [Kubespray](https://github.com/kubernetes-sigs/kubespray), then deploys cluster add-ons (Calico, MetalLB, Longhorn, Helm, cert-manager).

**Repository:** https://github.com/RSS-Engineering/ansible-collection-deploy-rackai

---

## PHASE 1: Setup Your Local Machine

### Step 1.1: Clone the Repository

```bash
cd ~/projects  # or wherever you want to work
git clone git@github.com:RSS-Engineering/ansible-collection-deploy-rackai.git
cd ansible-collection-deploy-rackai
```

### Step 1.2: Create Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` at the start of your terminal prompt.

### Step 1.3: Install Python Dependencies

```bash
pip install -r deploy_rackai/requirements.txt
```

This installs packages like `openstacksdk`, `netaddr`, etc.

### Step 1.4: Install Ansible Collections

```bash
ansible-galaxy collection install -r deploy_rackai/requirements.yml
```

This downloads external Ansible collections (Kubespray, OpenStack, Kubernetes modules) and the Longhorn role.

### Step 1.5: Link the Ansible Collection

```bash
mkdir -p ~/.ansible/collections/ansible_collections/rackai
ln -sfn "$(pwd)/deploy_rackai" \
  ~/.ansible/collections/ansible_collections/rackai/deploy_rackai
```

This tells Ansible where to find the `rackai.deploy_rackai` collection.

---

## PHASE 2: Setup Undercloud Access

### Step 2.1: Add Undercloud Configuration

> [!note] Prerequisites
> - You must be a member of the **`undercloud-sddc`** LDAP group. Request access through your manager or IT access portal.
> - Your SSH key must be **authorized for the RSS-Engineering GitHub org** via SSO (GitHub → Settings → SSH keys → Configure SSO → Authorize RSS-Engineering).

Create or edit `~/.config/openstack/clouds.yaml`:

```bash
mkdir -p ~/.config/openstack
```

Add your Undercloud cloud configuration. The exact values depend on your environment — check with your team or the Undercloud documentation for the correct `auth_url`, `project_name`, `project_domain_id`, and `region_name`.

```yaml
clouds:
  <cloud-name>:
    auth_type: v3websso
    identity_provider: sso
    protocol: openid
    auth:
      auth_url: https://<keystone-endpoint>/v3
      project_name: <your-project>
      project_domain_id: <your-domain-id>
    region_name: <your-region>
```

### Step 2.2: Verify AppGate Connection

Make sure you're connected to AppGate (VPN). Ask your IT team if unsure.

### Step 2.3: Authenticate to Undercloud

For WSL users, set the browser so the SSO login opens in Windows:

```bash
export OS_CLOUD=<cloud-name>
export BROWSER="/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
```

Authentication happens automatically via browser when you run any `openstack` command. The v3websso plugin opens a browser for SSO login.

### Step 2.4: Test Authentication

```bash
openstack server list
```

If you see output (even if empty), you're authenticated ✅

### Step 2.5: Register Your SSH Keypair

First, verify your SSH key exists:

```bash
ls ~/.ssh/id_rsa.pub
```

If it doesn't exist, create one:

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
```

Then register it:

```bash
openstack keypair create --public-key ~/.ssh/id_rsa.pub rackai-prod-key
```

Verify it was created:

```bash
openstack keypair list
```

You should see `rackai-prod-key` ✅

---

## PHASE 3: Create Production Inventory Files

### Step 3.1: Create Production Hosts File

```bash
cp inventory/kubernetes_hosts.yaml.example inventory/production_hosts.yaml
```

Edit `inventory/production_hosts.yaml` to define your cluster. Each host **must** have `admin_password` set to the vault variable reference. Example:

```yaml
---
kube_control_plane:
  hosts:
    rackai-cp-0:
      admin_password: "{{ vault_k8s_admin_password }}"
    rackai-cp-1:
      admin_password: "{{ vault_k8s_admin_password }}"
    rackai-cp-2:
      admin_password: "{{ vault_k8s_admin_password }}"

kube_node:
  hosts:
    rackai-wk-0:
      admin_password: "{{ vault_k8s_admin_password }}"
    rackai-wk-1:
      admin_password: "{{ vault_k8s_admin_password }}"
      # Example: override image/flavor for a single host (GPU worker)
      image: "Ubuntu 24.04 Nvidia CUDA with CI"
      flavor: pai2.xlarge

# Environment wrapper (rename 'example' to 'production')
production:
  children:
    kube_control_plane:
    kube_node:

# Kubespray group aliases (required — don't edit)
etcd:
  children:
    kube_control_plane:

calico_rr:
  hosts: {}

k8s_cluster:
  children:
    kube_control_plane:
    kube_node:
    calico_rr:
```

**Key points:** - Each host **must** have `admin_password: "{{ vault_k8s_admin_password }}"` — this is where Ansible gets the password from the vault - The **first host in `kube_control_plane`** (here: `rackai-cp-0`) will initialize the cluster via `kubeadm init` - Rename the environment wrapper group from `example` to `production` (or your env name) - Keep the Kubespray group aliases (`etcd`, `k8s_cluster`, `calico_rr`) exactly as shown — they're required by Kubespray - Per-host overrides like `image` and `flavor` are optional (useful for GPU nodes)

### Step 3.2: Create Production Group Variables

```bash
mkdir -p inventory/group_vars/production
```

Create `inventory/group_vars/production/10_local.yml`:

```yaml
---
customer_prefix: rackai
datacenter: dfw3
ssh_key_name: rackai-prod-key
local_python_interpreter: /path/to/your/venv/bin/python3
```

Replace `/path/to/your/venv/bin/python3` with your actual venv path (e.g., `/home/yourusername/ansible-collection-deploy-rackai/.venv/bin/python3`).

### Step 3.3: Create Ansible Vault for Secrets

```bash
ansible-vault create inventory/group_vars/production/vault.yml
```

This opens an editor. Enter:

```yaml
---
vault_k8s_admin_password: YourStrongPasswordHere
```

Save and exit. Remember the vault encryption password — you'll need it when running the playbook.

> [!warning] Important
> The vault variable must be named `vault_k8s_admin_password` (with the `k8s_` prefix), not `vault_admin_password`. This matches the template and collection expectations.

### Step 3.4: Verify Inventory Files

```bash
test -f inventory/production_hosts.yaml && echo "✓ production_hosts.yaml exists"
test -f inventory/group_vars/production/10_local.yml && echo "✓ 10_local.yml exists"
test -f inventory/group_vars/production/vault.yml && echo "✓ vault.yml exists"
```

All should exist ✅

---

## PHASE 4: Deploy the Kubernetes Cluster

### Step 4.1: Run the Deployment

```bash
export BROWSER="/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"  # WSL users only
export OS_CLOUD=<cloud-name>
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i inventory/production_hosts.yaml \
  deploy_rackai/playbooks/provision-kubespray.yml \
  --ask-vault-pass
```

**This will take 20-45 minutes** depending on Undercloud performance.

The playbook will:

1. Create networks, subnets, and routers in Undercloud
2. Reserve mgmt IPs for the kube-vip VIP and MetalLB private-pool
3. Provision bare metal servers (3 control planes + 2 workers)
4. Wait for cloud-init to finish and authorize team SSH keys
5. Run Kubespray to bootstrap the Kubernetes cluster with:
	- containerd container runtime
		- kubeadm-managed HA control plane
		- kube-vip for API VIP management
		- Calico CNI
		- Helm, metrics-server, cert-manager
		- MetalLB controller
6. Deploy per-pool MetalLB L2Advertisements with interface scoping
7. Deploy Longhorn distributed storage

Watch the output for progress. You'll see plays like:

```js
PLAY [Provision host networks in Undercloud] ***
PLAY [Discover Undercloud subnet details] ***
PLAY [Reserve VIP master ports before provisioning servers] ***
...
```

### Step 4.2: Wait for Completion

The playbook will complete when you see:

```js
PLAY RECAP ****
rackai-cp-0  : ok=XX changed=XX unreachable=0 failed=0
rackai-cp-1  : ok=XX changed=XX unreachable=0 failed=0
rackai-cp-2  : ok=XX changed=XX unreachable=0 failed=0
rackai-wk-0  : ok=XX changed=XX unreachable=0 failed=0
rackai-wk-1  : ok=XX changed=XX unreachable=0 failed=0
```

If you see `failed=0` for all hosts, deployment succeeded ✅

---

## PHASE 5: Verify Kubernetes Cluster

### Step 5.1: Get Kubeconfig

Kubespray writes the admin kubeconfig to your control machine at:

```js
inventory/artifacts/admin-production.conf
```

Use it:

```bash
export KUBECONFIG=inventory/artifacts/admin-production.conf
kubectl get nodes
```

> [!note] Note
> If `inventory/artifacts/` doesn't exist, kubespray creates it during the cluster play.

### Step 5.2: Verify Cluster is Running

```bash
kubectl get nodes
```

You should see all nodes as `Ready`:

```js
NAME         STATUS   ROLES           AGE   VERSION
rackai-cp-0  Ready    control-plane
rackai-cp-1  Ready    control-plane
rackai-cp-2  Ready    control-plane
rackai-wk-0  Ready    <none>
rackai-wk-1  Ready    <none>
```

### Step 5.3: Verify Cluster Components

```bash
# Check all pods are running
kubectl get pods -A

# Check storage (Longhorn)
kubectl get storageclass
kubectl get pods -n longhorn-system

# Check load balancing (MetalLB)
kubectl get pods -n metallb-system

# Check Calico networking
kubectl get pods -n kube-system | grep calico
```

---

## Scaling the Cluster

### Adding Nodes

Edit `inventory/production_hosts.yaml`, add the new host under `kube_node`:

```yaml
kube_node:
  hosts:
    rackai-wk-2:
      admin_password: "{{ vault_k8s_admin_password }}"
      flavor: pai2.xlarge
      image: "Ubuntu 24.04 4k sector"
```

Re-run the playbook:

```bash
ansible-playbook -i inventory/production_hosts.yaml \
  deploy_rackai/playbooks/provision-kubespray.yml \
  --ask-vault-pass
```

Existing nodes are skipped (idempotent). Only the new node is provisioned and joined to the cluster.

Verify:

```bash
kubectl get nodes
```

### Removing Nodes

1. Drain and reset the node using Kubespray:
```bash
ansible-playbook -i inventory/production_hosts.yaml \
  kubernetes_sigs.kubespray.remove_node \
  -e node=rackai-wk-2 \
  --ask-vault-pass
```
1. Delete the OpenStack server:
```bash
openstack server delete rackai-wk-2
```
1. Remove the host entry from `inventory/production_hosts.yaml`.

> [!note] Note
> Kubespray cannot remove the first control plane node (`rackai-cp-0`). If you need to retire it, build a new control plane cluster elsewhere first.

---

## Running Specific Deployment Phases

The playbook is modular. Use tags to run only certain parts:

```bash
# Only provision Undercloud resources (networks, servers)
ansible-playbook -i inventory/production_hosts.yaml \
  deploy_rackai/playbooks/provision-kubespray.yml \
  --tags network,servers,reserve_ips --ask-vault-pass

# Only build/upgrade the Kubernetes cluster (skip Undercloud and add-ons)
ansible-playbook -i inventory/production_hosts.yaml \
  deploy_rackai/playbooks/provision-kubespray.yml \
  --tags cluster --ask-vault-pass

# Only install/refresh add-ons (MetalLB, Longhorn)
ansible-playbook -i inventory/production_hosts.yaml \
  deploy_rackai/playbooks/provision-kubespray.yml \
  --tags metallb,longhorn --ask-vault-pass
```

**Available tags:** - `network` — Create Undercloud networks, subnets, routers - `reserve_ips` — Reserve master ports for VIPs - `servers` — Boot VMs, attach trunk ports, wait for cloud-init, install SSH keys - `cluster` or `kubespray` — Run Kubespray to build the cluster - `metallb` — Install MetalLB L2Advertisements and rp\_filter config - `longhorn` — Install Longhorn distributed storage

---

## Troubleshooting

### Playbook fails during inventory validation

- Check that each host in `kube_control_plane` and `kube_node` has `admin_password: "{{ vault_k8s_admin_password }}"`
- Verify the vault file exists at `inventory/group_vars/production/vault.yml`
- Ensure the vault password is correct when prompted

### Nodes stuck in NotReady or cloud-init hangs

- SSH into a node and check cloud-init status: `cloud-init status`
- Check if cloud-init logs for errors: `cat /var/log/cloud-init-output.log`
- Verify network connectivity to Undercloud DNS and NTP

### Kubespray cluster.yml fails

- Check kubelet is running on all nodes
- Verify kube-vip pod is in `Running` state: `kubectl get pod -n kube-system | grep kube-vip`
- Check for port conflicts (6443 for API, 10250 for kubelet)

### MetalLB speakers fail to start

- Verify the controller is running: `kubectl get pods -n metallb-system`
- Check that the `memberlist` secret exists: `kubectl get secret -n metallb-system memberlist`
- Review speaker pod logs: `kubectl logs -n metallb-system -l app=speaker`

### Longhorn not available

- Check prerequisites are installed: `systemctl status iscsid` on each node
- Verify Longhorn pods are running: `kubectl get pods -n longhorn-system`
- Check disk space on nodes: `df -h` (Longhorn needs at least 10GB free per node)

---

## Updating the Collection

When pulling updates from the repo:

```bash
git pull origin main
ansible-galaxy collection install -r deploy_rackai/requirements.yml --force
```

The symlink (`ln -sfn` from Step 1.5) automatically reflects code changes on `git pull` — no need to reinstall the local collection.

---

## Support & Contacts

For any issues, reach out to:

| Contact | Email | Role |
| --- | --- | --- |
| Deshna Shah | deshna.shah@rackspace.com | Deployment lead |
| Dan Hand | dan.hand@rackspace.com | Collection author / K8s infra |
| Jovan Rajapakse | jovan.rajapakse@rackspace.co.uk | Undercloud / platform |
| Undercloud Support | [Undercloud Support Channel](https://teams.microsoft.com/) | Infrastructure issues (quotas, bare metal, networking) |

---

## Reference

- Repository: https://github.com/RSS-Engineering/ansible-collection-deploy-rackai
- Collection README: `deploy_rackai/README.md`
- Top-level README: `README.md`
- Kubespray: https://github.com/kubernetes-sigs/kubespray