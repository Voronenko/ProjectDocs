#!/bin/bash

docker create -it -v $PWD:/opt/sphinxproject --name projectdocs softasap/sphinx:latest bash

# Now start it.
docker start projectdocs

docker exec -it projectdocs "cd /opt/sphinxproject && make --makefile Makefiledck"
