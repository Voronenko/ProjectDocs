Known issues:
=============

## "BlockDiag not found"

Most likely you are hitting:

### ubuntu ,

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


- python 3.7 , pipenv, make
- java 6-7-8 for plantUML


diagramming software

- plantUML (http://plantuml.com/ , recipe https://github.com/Voronenko/ansible-developer_recipes/blob/master/tools/tasks_plantuml.yml)
- blockdiag (http://blockdiag.com/en/ , installed via requirements.txt)


running the local build
-----------------------

At this moment it is enough to run ./clean_build.sh
Result will be produced out/html



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


Options for epub output
These options influence the epub output. As this builder derives from the HTML builder, the HTML options also apply where appropriate. The actual values for some of the options is not really important, they just have to be entered into the Dublin Core metadata.

epub\_basename
The basename for the epub file. It defaults to the project name.

epub\_theme
The HTML theme for the epub output. Since the default themes are not optimized for small screen space, using the same theme for HTML and epub output is usually not wise. This defaults to 'epub', a theme designed to save visual space.

epub\_title
The title of the document. It defaults to the html_title option but can be set independently for epub creation.

epub\_author
The author of the document. This is put in the Dublin Core metadata. The default value is 'unknown'.

epub\_language
The language of the document. This is put in the Dublin Core metadata. The default is the language option or 'en' if unset.

epub\_publisher
The publisher of the document. This is put in the Dublin Core metadata. You may use any sensible string, e.g. the project homepage. The default value is 'unknown'.

epub\_copyright
The copyright of the document. It defaults to the copyright option but can be set independently for epub creation.

epub\_identifier
An identifier for the document. This is put in the Dublin Core metadata. For published documents this is the ISBN number, but you can also use an alternative scheme, e.g. the project homepage. The default value is 'unknown'.

epub\_scheme
The publication scheme for the epub_identifier. This is put in the Dublin Core metadata. For published books the scheme is 'ISBN'. If you use the project homepage, 'URL' seems reasonable. The default value is 'unknown'.

epub\_uid
A unique identifier for the document. This is put in the Dublin Core metadata. You may use a random string. The default value is 'unknown'.

epub\_cover
The cover page information. This is a tuple containing the filenames of the cover image and the html template. The rendered html cover page is inserted as the first item in the spine in content.opf. If the template filename is empty, no html cover page is created. No cover at all is created if the tuple is empty. Examples:

epub\_cover = ('_static/cover.png', 'epub-cover.html')
epub\_cover = ('_static/cover.png', '')
epub\_cover = ()
The default value is ().

New in version 1.1.

epub\_pre\_files
Additional files that should be inserted before the text generated by Sphinx. It is a list of tuples containing the file name and the title. If the title is empty, no entry is added to toc.ncx. Example:

epub\_pre\_files = [
    ('index.html', 'Welcome'),
]
The default value is [].

epub\_post\_files
Additional files that should be inserted after the text generated by Sphinx. It is a list of tuples containing the file name and the title. This option can be used to add an appendix. If the title is empty, no entry is added to toc.ncx. The default value is [].

epub\_exclude\_files
A list of files that are generated/copied in the build directory but should not be included in the epub file. The default value is [].

epub\_tocdepth
The depth of the table of contents in the file toc.ncx. It should be an integer greater than zero. The default value is 3. Note: A deeply nested table of contents may be difficult to navigate.

epub\_tocdup
This flag determines if a toc entry is inserted again at the beginning of it’s nested toc listing. This allows easier navitation to the top of a chapter, but can be confusing because it mixes entries of differnet depth in one list. The default value is True.


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



# Additional resources


https://github.com/yoloseem/awesome-sphinxdoc
