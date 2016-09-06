# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM softasap/alpine:full
MAINTAINER Vyacheslav Voronenko <git@voronenko.info>

# Graphviz
RUN mkdir /graphviz && \
  apk add --update graphviz && \
  rm -rf /var/cache/apk/*

# PlantUML

RUN apk add --update curl && \
    mkdir -p /opt/plantuml/ && \
    curl  http://sourceforge.net/projects/plantuml/files/plantuml.jar/download > /opt/plantuml/plantuml.jar && \
    rm -rf /var/cache/apk/*

COPY docker/plantuml /usr/bin/plantuml

# Sphinx
COPY requirements.txt /requirements.txt

RUN  apk add --no-cache python && \
     apk add --no-cache build-base && \
     apk add --no-cache python-dev && \
     apk add --no-cache git && \
     apk add --no-cache zlib-dev && \
     apk add --no-cache g++ && \
     apk add --no-cache libjpeg-turbo-dev && \
     apk add --no-cache musl-dev && \
     python -m ensurepip && \
     rm -r /usr/lib/python*/ensurepip && \
     pip install -r /requirements.txt && \
     rm -r /root/.cache
