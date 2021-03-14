#!/bin/bash

# https://www.openshift.com/blog/openshift-4-pro-tip-custom-branding

# Artwork
# https://github.com/cncf/artwork/blob/master/examples/graduated.md#kubernetes-logos

# Add a Custom Logo and Product Name
oc create configmap console-custom-logo \
    --from-file=kubernetes-horizontal-white.png \
    -n openshift-config

# Edit the web console's operator configuration

oc apply -f custom-branding.yml

