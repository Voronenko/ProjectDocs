#!/bin/bash

DOCKER_UID=$(id -u)

DOCKER_USER=$(whoami)

RUNNING=$(docker inspect --format="{{ .State.Running }}" projectdocs 2> /dev/null)

if [ $? -eq 1 ]; then
  echo "PROJECTDOCS CONTAINER DOES NOT EXIST - CREATE IT"
  docker create -it -v $PWD:/opt/sphinxproject --name projectdocs softasap/sphinx-projectdocs:0.2.0 bash
  docker start projectdocs
  echo projectdocs container created
fi

if [ "$RUNNING" == "false" ]; then
  echo "RUN PROJECTDOCS CONTAINER"
  docker start projectdocs
  echo projectdocs container running
fi

echo "building docs"
echo docker exec -it projectdocs bash -c "export DOCKER_UID=${DOCKER_UID} && export DOCKER_USER=${DOCKER_USER} && /opt/sphinxproject/docker_entry_point.sh"
docker exec -it projectdocs bash -c "export DOCKER_UID=${DOCKER_UID} && export DOCKER_USER=${DOCKER_USER} && /opt/sphinxproject/docker_entry_point.sh"
