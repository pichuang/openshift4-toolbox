#!/bin/bash

#
# shell.sh "timedatectl"
# shell.sh "timedatectl | grep -i "Local time""
#

display_usage() {
  echo -e "\nUsage: $0 [command] \n"
  echo -e "Example: shell.sh \"timedatectl\""
  echo -e "Example: shell.sh \"timedatectl | grep -i \"Local time\"\" \n"
}


if [ $# -lt 1 ]
then
  display_usage
  exit 1
fi

ansible -i hosts openshift4 -m shell -a "$1"
