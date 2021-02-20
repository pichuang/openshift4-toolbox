# OpenShift 4 Toolbox

## Environments
- Red Hat OpenShift 4.6.16
- Bastion
    - Red Hat Enterprise Linux 7.9
    - Red Hat Ansible 2.9.15
    - Python 3.6.8

## Features
- [x] ETCD Backup - `ansible-playbook backup-etcd.yml`
- [ ] ETCD Restore
- [x] Run commands to multiple nodes within one command - `./shell.sh "timedatectl | grep -i "Local time""`
- [x] Run commands to multiple nodes with prompt mode - `ansible-playbook -i hosts shell_prompt.yml`
- [x] ETCD Health Check Report - `ansible-playbook healthcheck-etcd.yml`
- [x] ETCD Disk Performance Report - `ansible-playbook disk-performance-etcd.yml`
- [x] Add new account and identity provider - `ansible-playbook add-ocp4-account.yml`
- [x] Disable default account `kubeadmin` - `ansible-playbook remove-kubeadmin.yml`

## Prerequisite
1. Edit `hosts` and put your environment in here
2. Use `ansible-playbook -i hosts pingpong.yml` to connect to host and verify a usable python interpreter
3. (Optioanl) `pip3 install -r requirements.txt`
4. Do anything you want to
