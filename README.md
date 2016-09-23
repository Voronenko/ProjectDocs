Known issues:
=============

## "BlockDiag not found"

Most likely you are hitting:

### ubuntu 14.04, 

error  ValueError: --enable-jpeg requested but jpeg not found, aborting

solution: `sudo apt-get install libjpeg-dev`


### MacOS

zlib not found or libjpeg not found

solution: install dev packages using `xcode-select --install`  ,
install jpeg-devel using `brew install libjpeg`

### Other clues

Take a look on  https://github.com/Voronenko/projectdocs/blob/master/Dockerfile
it has listed all binary packages required. Check you have all of them or alternatives.


useful tools 
============

Formats convertor:  https://github.com/jgm/pandoc

Example, to convert docs artifact:

```

pandoc -s flow.docx -t rst -o product_flow.rst

```

Online work pad for diagramming construction
http://interactive.blockdiag.com/

Online work pad for UML diagrams construction

http://plantuml.com/plantuml/uml/


Generate pgsql schema diagram with schemacrawler  http://sualeh.github.io/SchemaCrawler/ , example:

```

schemacrawler -server=postgresql -database=demo_test -user=postgres -password=postgres -infolevel=maximum -command=graph -outputformat=pdf -outputfile=database-diagram.pdf

```

Generate pgsql schema diagram portal with schemaspy http://schemaspy.sourceforge.net/ , example:

```
schemaspy -t pgsql -db demo_test -host localhost -port 5432 -s public -u postgres -p postgres  -o output
```



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
-----------------------

At this moment it is enough to run ./clean_build.sh
Result will be produced in docs/html



docker setup
------------

You need to have docker installed. File ./docker_build.sh does similar task as clean_build.sh

```

  #!/bin/bash

  docker create -it -v $PWD:/opt/sphinxproject --name projectdocs softasap/sphinx:latest bash

  # Now start it.
  docker start projectdocs

  docker exec -it projectdocs "cd /opt/sphinxproject && make --makefile Makefiledck"
```
