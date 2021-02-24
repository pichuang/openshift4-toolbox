# OpenShift 4 Toolbox

> Speed delivery with Red Hat Ansible and OpenShift 4

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

## Current Environments
- Red Hat OpenShift 4.6.17 using [vSphere UPI][1]
- VMware vSphere 7.0.1 build: 17005016
- Bastion
    - Red Hat Enterprise Linux 7.9
    - Red Hat Ansible 2.9.15
    - Python 3.6.8

## Toolbox
### OpenShift 4 ETCD
- [x] ETCD Backup - `ansible-playbook backup-etcd.yml`
    - YouTube: https://youtu.be/hVijextRADs
- [x] ETCD Health Check Report - `ansible-playbook healthcheck-etcd.yml`
    - YouTube: https://youtu.be/FGwCmCuQNrg
- [x] ETCD Disk Performance Report - `ansible-playbook disk-performance-etcd.yml`
    - YouTube: https://youtu.be/6qjsh9J3ndM
- [x] Use `ionice` to set high i/o priority for etcd process - `ansible-playbook ionice-etcd.yml`

### Execute commands on specifc nodes
- [x] Run commands to multiple nodes within one command - `./shell.sh "timedatectl | grep -i "Local time""`
- [x] Run commands to multiple nodes with prompt mode - `ansible-playbook shell_prompt.yml`

### OpenShift 4 Machine Management
- [x] Add Machineset on vSphere - `ansible-playbook add-vsphere-machineset.yml`
- [x] Add MachineHealthCheck - `ansible-playbook add-machinehealthcheck.yml`
    - YouTube: https://youtu.be/ZT1IWEiw-EY
- [x] Add MachineAutoScaler - `ansible-playbook add-machineautoscaler.yml`
    - YouTube: https://youtu.be/vWrJ-NCO2oc
- [x] Add ClusterAutoScaler - `ansible-playbook add-clusterautoscaler.yml`
- [x] Causing a Scaling Event for testing purpose - `./force-node-scaling-event.sh`

### OpenShift 4 Power Control
- [x] Reboot OpenShift cluster gracefully - `ansible-playbook graceful-ocp4-reboot.yml`
    - YouTube: https://youtu.be/G7XTY7TXltE
- [x] Shutting down the cluster gracefully - `ansible-playbook graceful-ocp4-shutdown.yml`
    - YouTube: https://youtu.be/Q6rv2bLXoNA

### OpenShift 4 Authentication
- [x] Add new account and identity provider - `ansible-playbook add-ocp4-account.yml`
- [x] Disable default account `kubeadmin` - `ansible-playbook remove-kubeadmin.yml`

### OpenShift 4 Security
- [ ] Pull Audit Log

### OpenShift 4 Time
- [x] Check System Time - `ansible-playbook check-system-time.yml`
- [ ] Change Timezone

### OpenShift 4 Certificates
- [ ] Add API server certificates

### NFS
- [ ] Install [NFS Suvbdir External Provisioner][6]

### Service Mesh
- [x] Install [Red Hat Service Mesh][4]

### ACM
- [x] Install [Red Hat Advanced Cluster Management for Kubernetes][5]

### Misc
- [x] Save container images to tar archive - `ansible-playbook save-containe-images.yml`
- [x] deadman is an observation software for host status using ping. - `ansible-playbook monitoring-host-reboot.yml`
- [ ] Kubeeye

## Prerequisite
1. Edit `hosts`, `ansible.cfg` and put your own environment setting first
2. Use `ansible-playbook pingpong.yml` to connect to host and verify a usable python interpreter
3. (Optioanl) `pip3 install -r requirements.txt`
4. Do anything you want to do

## Tested Recording

|   Date   | Status | OpenShift Version | Ansible Version | Bastion OS Version |
|:--------:|:------:|:-----------------:|:---------------:|:------------------:|
| 20210222 |   OK   |       4.6.1       |      2.9.15     |      RHEL 7.9      |
| 20210220 |   OK   |       4.6.17      |      2.9.15     |      RHEL 7.9      |
| 20210220 |   OK   |       4.6.16      |     2.4.2.0     |      RHEL 7.9      |
| 20210220 |   OK   |       4.5.31      |     2.4.2.0     |      RHEL 7.9      |

## Welcome to contribute!

- [OpenSource Contribution Guidelines][3]

## References
- [RedHatOfficial/ocp4-vsphere-upi-automation][1]
- [openshift/training][2]

[1]: https://github.com/RedHatOfficial/ocp4-vsphere-upi-automation
[2]: https://github.com/openshift/training
[3]: https://redhat-cop.github.io/contrib/
[4]: https://github.com/pichuang/redhat-service-mesh-demo
[5]: https://github.com/pichuang/redhat-acm-demo
[6]: https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner