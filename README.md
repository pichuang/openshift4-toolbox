# OpenShift 4 Toolbox

## Environments
- Red Hat OpenShift 4.6.16
- Red Hat Ansible 2.9.15

## Features
- [x] ETCD Backup - `ansible-playbook backup-etcd.yml`
- [ ] ETCD Restore
- [x] ETCD Health Check - `ansible-playbook healthcheck-etcd.yml`
- [x] Run commands to multiple nodes within one command - `./shell.sh "timedatectl | grep -i "Local time""`
- [x] Run commands to multiple nodes with prompt mode - `ansible-playbook -i hosts shell_prompt.yml`
