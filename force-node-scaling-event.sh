#!/bin/bash

PROJECT_NAME="test-clusterautoscale"

oc new-project ${PROJECT_NAME}
oc project ${PROJECT_NAME}
oc create -n ${PROJECT_NAME} -f assets/fake-heavy-job.yml

sleep 10

oc get pods -n ${PROJECT_NAME} -w

echo
echo "watch -n10 'oc get machines -n openshift-machine-api'"
echo