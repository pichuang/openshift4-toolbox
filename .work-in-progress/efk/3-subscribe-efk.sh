#!/bin/bash

oc apply -f elasticsearch-operator-subscription.yaml
oc apply -f cluster-logging-subscription.yaml
