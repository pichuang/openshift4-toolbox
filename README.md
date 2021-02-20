# OpenShift 4 Toolbox

```
                              \\\\\\\
                            \\\\\\\\\\\\
                          \\\\\\\\\\\\\\\
  -----------,-|           |C>   // )\\\\|
           ,','|          /    || ,'/////|
---------,','  |         (,    ||   /////
         ||    |          \\  ||||//''''|
Red Hat  ||    |           |||||||     _|
OpenShift||    |______      `````\____/ \
   4     ||    |     ,|         _/_____/ \
         ||  ,'    ,' |        /          |
         ||,'    ,'   |       |  YOU    \  |
_________|/    ,'     |      /           | |
_____________,'      ,',_____|      |    | |
             |     ,','      |      |    | |
             |   ,','    ____|_____/    /  |
             | ,','  __/ |             /   |
_____________|','   ///_/-------------/   |
              |===========,'
```

## Environments
- Red Hat OpenShift 4.6.17
- Bastion
    - Red Hat Enterprise Linux 7.9
    - Red Hat Ansible 2.9.15
    - Python 3.6.8

## Features
- [x] ETCD Backup - `ansible-playbook backup-etcd.yml`
- [ ] ETCD Restore
- [x] Run commands to multiple nodes within one command - `./shell.sh "timedatectl | grep -i "Local time""`
- [x] Run commands to multiple nodes with prompt mode - `ansible-playbook shell_prompt.yml`
- [x] ETCD Health Check Report - `ansible-playbook healthcheck-etcd.yml`
- [x] ETCD Disk Performance Report - `ansible-playbook disk-performance-etcd.yml`
- [x] Add new account and identity provider - `ansible-playbook add-ocp4-account.yml`
- [x] Disable default account `kubeadmin` - `ansible-playbook remove-kubeadmin.yml`
- [x] Add Machineset on vSphere - `ansible-playbook add-vsphere-machineset.yml`
    - Prerequisite: [RedHatOfficial/ocp4-vsphere-upi-automation][1]
- [x] Save container images to tar archive - `ansible-playbook save-containe-images.yml`
- [x] Reboot OpenShift cluster gracefully - `ansible-playbook graceful-ocp4-reboot.yml`
    - Youtube: https://youtu.be/G7XTY7TXltE
- [x] Shutting down the cluster gracefully - `ansible-playbook graceful-ocp4-shutdown.yml`
    - Youtube: https://youtu.be/Q6rv2bLXoNA
- [x] deadman is an observation software for host status using ping. - `ansible-playbook monitoring-host-reboot.yml`

## Prerequisite
1. Edit `hosts` and put your environment first
2. Use `ansible-playbook pingpong.yml` to connect to host and verify a usable python interpreter
3. (Optioanl) `pip3 install -r requirements.txt`
4. Do anything you want to

## Tested Recording

|   Date   | Status | OpenShift Version | Ansible Version | Bastion OS Version |
|:--------:|:------:|:-----------------:|:---------------:|:------------------:|
| 20210220 |   OK   |       4.6.17      |      2.9.15     |      RHEL 7.9      |
| 20210220 |   OK   |       4.6.16      |     2.4.2.0     |      RHEL 7.9      |
| 20210220 |   OK   |       4.5.31      |     2.4.2.0     |      RHEL 7.9      |

[1]: https://github.com/RedHatOfficial/ocp4-vsphere-upi-automation