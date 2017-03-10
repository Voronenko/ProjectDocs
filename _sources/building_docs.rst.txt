Building docs project
=====================

You have two options:

- build locally with diagramming software installed separately
- using dockerized image

local setup
-----------

You would need:

number of languages:

- python 2.7 , virtualenv, make
- java 6-7-8 for plantUML


diagramming software

- plantUML (http://plantuml.com/ , recipe https://github.com/Voronenko/ansible-developer_recipes/blob/master/tools/tasks_plantuml.yml)
- blockdiag (http://blockdiag.com/en/ , installed via requirements.txt)


running the local build
~~~~~~~~~~~~~~~~~~~~~~~

At this moment it is enough to run ./clean_build.sh
Result will be produced in out/html



docker setup
------------

You need to have docker installed

.. code-block:: shell

  #!/bin/bash

  docker create -it -v $PWD:/opt/sphinxproject --name projectdocs softasap/sphinx:latest bash

  # Now start it.
  docker start projectdocs

  docker exec -it projectdocs "cd /opt/sphinxproject && make --makefile Makefiledck"
