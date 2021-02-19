#!/usr/bin/env python3

"""
Usage: ./who-is-ocp4-etcd-leader.py -h
Return ETCD Leader ID: ./who-is-ocp4-etcd-leader.py id
Return ETCD LEADER NAME: ./who-is-ocp4-etcd-leader.py name 
Return ETCD Leader ENDPOINT: ./who-is-ocp4-etcd-leader.py endpoint
"""

import openshift as oc
import json
import argparse

#
# Check OpenShift OC Command can work well
#

# print('OpenShift client version: {}'.format(oc.get_client_version()))
# print('OpenShift server version: {}'.format(oc.get_server_version()))

#
# Obtain etcd information from OpenShfit OC commmand
# 

with oc.project('openshift-etcd'), oc.timeout(10*60):

    etcd_selector = oc.selector('pods', labels={ 'app': 'etcd' }).qnames()
    # print(etcd_selector)
    # Output: ['pod/etcd-master0', 'pod/etcd-master1', 'pod/etcd-master2']

    etcdctl_endpoint_status = "etcdctl endpoint status --cluster -w json"
    etcdctl_endpoint_status_result = oc.selector(etcd_selector[0]).object().execute(['/bin/bash'], 
        container_name='etcdctl', stdin=etcdctl_endpoint_status).out()

    etcdctl_member_list = "etcdctl member list -w json"
    etcdctl_member_list_result = oc.selector(etcd_selector[0]).object().execute(['/bin/bash'], 
        container_name='etcdctl', stdin=etcdctl_member_list).out()

#
# Find out etcd leader
# NAME / ID / ENDPOINT
# 

LEADER_ID = ""
LEADER_ENDPOINT = ""
LEADER_NAME = ""

etcdctl_endpoint_status_json = json.loads(etcdctl_endpoint_status_result)
for etcdctl_endpoint in etcdctl_endpoint_status_json:
    if etcdctl_endpoint['Status']['header']['member_id'] == etcdctl_endpoint['Status']['leader']:
        LEADER_ID = etcdctl_endpoint['Status']['leader']
        LEADER_ENDPOINT = etcdctl_endpoint['Endpoint']
        # print(LEADER_ID) # Return etcd endpoint
        # print(ENDPOINT) # Return etcd endpoint

etcdctl_member_list_result_json = json.loads(etcdctl_member_list_result)
for etcdctl_member in etcdctl_member_list_result_json['members']:
    # print(etcdctl_member['clientURLs'])
    if etcdctl_member['clientURLs'][0] == LEADER_ENDPOINT:
        LEADER_NAME = etcdctl_member['name']
        # print(etcdctl_member['name']) # Return etcd leader name

def id(args):
    print(LEADER_ID)

def name(args):
    print(LEADER_NAME)

def endpoint(args):
    print(LEADER_ENDPOINT)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

id_parser = subparsers.add_parser('id')
id_parser.set_defaults(func=id)
name_parser = subparsers.add_parser('name')
name_parser.set_defaults(func=name)
leader_parser = subparsers.add_parser('endpoint')
leader_parser.set_defaults(func=endpoint)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function