#!/bin/bash


oc get csv -n openshift-operators-redhat
oc get csv -n openshift-logging

echo

oc api-resources --api-group=logging.openshift.io

echo

oc get crd -l operators.coreos.com/elasticsearch-operator.openshift-operators-redhat
oc get crd -l operators.coreos.com/cluster-logging.openshift-logging
