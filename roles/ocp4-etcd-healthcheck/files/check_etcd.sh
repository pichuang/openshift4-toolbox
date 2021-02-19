#!/bin/bash
id=$(sudo crictl ps --name etcdctl | awk 'FNR==2{ print $1}')
sudo crictl exec -it $id /bin/bash -c "etcdctl member list -w table"
echo 
sudo crictl exec -it $id /bin/bash -c "etcdctl endpoint health --cluster"
echo
sudo crictl exec -it $id /bin/bash -c "etcdctl endpoint health -w table"
echo
sudo crictl exec -it $id /bin/bash -c "etcdctl endpoint status -w table --cluster"