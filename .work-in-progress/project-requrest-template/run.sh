#!/bin/bash

# https://docs.openshift.com/container-platform/4.6/applications/quotas/quotas-setting-per-project.html#quotas-scopes_quotas-setting-per-project
oc apply -f project-requrest-template.yml -n openshift-config
