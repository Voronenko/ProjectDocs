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

Converting markdown artifact:

```

pandoc --from=markdown --to=rst --output=README.rst README.md

```

PandaDoc online:  https://pandoc.org/try/

Online work pad for diagramming construction
http://interactive.blockdiag.com/

Online work pad for UML diagrams construction

http://plantuml.com/plantuml/uml/

PlantUML learning pad with examples:

http://www.planttext.com/planttext


Generate pgsql schema diagram with schemacrawler  http://sualeh.github.io/SchemaCrawler/ , example:

```

schemacrawler -server=postgresql -database=demo_test -user=postgres -password=postgres -infolevel=maximum -command=graph -outputformat=pdf -outputfile=database-diagram.pdf

```

Generate pgsql schema diagram portal with schemaspy http://schemaspy.sourceforge.net/ , example:

```
schemaspy -t pgsql -db demo_test -host localhost -port 5432 -s public -u postgres -p postgres  -o output
```

Incorporate static code analysis into your project:

Doxygen:

https://github.com/michaeljones/breathe/tree/master


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

DOCKER_UID=$(id -u)

DOCKER_USER=$(whoami)

RUNNING=$(docker inspect --format="{{ .State.Running }}" projectdocs 2> /dev/null)

if [ $? -eq 1 ]; then
  echo "PROJECTDOCS CONTAINER DOES NOT EXIST - CREATE IT"
  docker create -it -v $PWD:/opt/sphinxproject --name projectdocs softasap/sphinx-projectdocs:latest bash
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

```


Building epub project
=====================

make epub


Building kindle project
=======================

make mobi

The following configuration values can be used in `conf.py`. At a minimum, you must set the *mobi\_theme* option:

mobi\_add\_visible\_links  
Whether or not to write out the full text of a hyperlink next to the link itself. If the document will be read on paper (or printed), it is a good idea to set this to `True`.

Default: `True`

mobi\_author  
The author of the book.

> Default: `'unknown'`

mobi\_basename  
The basename of the output file (the part of the filename that precedes `.mobi`)

> Default: The project name, with spaces removed.

mobi\_copyright  
The copyright holder of the book.

> Default: The value of **copyright** in `conf.py`

mobi\_cover  
The cover image for the book. This should be in `.jpg` format.

> Default: No cover image is used.

mobi\_exclude\_files  

> Default: no files are excluded.

mobi\_identifier  

> Default: `'unknown'`

mobi\_language  

> Default: The value of *language* in `conf.py`, or `'en'` if *language* is not set.

mobi\_post\_files  

> Default: no post files are used.

mobi\_pre\_files  

> Default: no pre files are used.

mobi\_publisher  
The publisher name for the book.

> Default: `'unknown'`

mobi\_scheme  

> Default: `'unknown'`

mobi\_theme  
*Required*. The mobi theme-file to use. If you don’t have a theme of your own, use the `epub` theme:

    mobi_theme = 'epub'

mobi\_title  

> Default: The value of *html\_title* in `conf.py`.

mobi\_tocdepth  

> Default: `3`.

mobi\_tocdup  

> Default: `True`

mobi\_uid  

> Default: `'unknown'`
