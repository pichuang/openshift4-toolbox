#!/bin/bash

set -x

USERROOT="useroot"
DC_NAME="nginx-deployment"

# 1. Create a new SA - userroot
oc create serviceaccount ${USERROOT}

# 2. Add the SA into anyuid SCC list
oc adm policy add-scc-to-user anyuid -z userroot

# 3. Patch specific DeploymentConfig to userroot
oc patch deployment ${DC_NAME} --patch {"spec":{"template":{"spec":{"serviceAccountName":"${USERROOT}"}}}}

