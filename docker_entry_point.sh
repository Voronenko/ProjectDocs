#!/bin/bash

if [ -z "${DOCKER_UID}" ]; then
    echo "ProjectDocs requires passed DOCKER_UID and DOCKER_USER to handle generated file rights to match your user"
    exit 1
fi

echo "docker entry point ...."
adduser -u $DOCKER_UID -D -g '' $DOCKER_USER
adduser $DOCKER_USER sudo || true
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
# This will be uncommented once issue with switching rights fixed
#su -m $DOCKER_USER -c /opt/sphinxproject/clean_build_docker.sh
/opt/sphinxproject/clean_build_docker.sh
chown -R $DOCKER_USER:$DOCKER_USER /opt/sphinxproject/docs/html

