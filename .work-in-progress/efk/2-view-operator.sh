#!/bin/bash
oc get packagemanifests {cluster-logging,elasticsearch-operator} -n openshift-marketplace
