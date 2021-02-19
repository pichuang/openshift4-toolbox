# OpenShift 4 Toolbox

## Environments
- Red Hat OpenShift 4.6.16
- Red Hat Ansible 2.9.15

## Features
- [x] ETCD Backup - `ansible-playbook -i hosts backup-etcd.yml`
- [ ] ETCD Restore
- [ ] ETCD Health Check - `ansible-playbook -i hosts healthcheck-etcd.yml`
- [x] Run commands on multiple nodes within one command - `./shell.sh "timedatectl | grep -i "Local time""`
- [x] Run commands on multiple nodes with prompt mode - `ansible-playbook -i hosts shell_prompt.yml`
