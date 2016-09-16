FROM softasap/alpine:full
MAINTAINER Vyacheslav Voronenko <git@voronenko.info>

env USER_ID 1000  # to correctly remap user rights
env GROUP_ID 1000 # to correctly remap user rights

# Graphviz
RUN mkdir /graphviz && \
  apk add --update graphviz && \
  rm -rf /var/cache/apk/*

# PlantUML

RUN apk add --update curl && \
    mkdir -p /opt/plantuml/ && \
    curl -L  https://sourceforge.net/projects/plantuml/files/plantuml.jar/download > /opt/plantuml/plantuml.jar && \
    rm -rf /var/cache/apk/*

COPY docker/plantuml /usr/bin/plantuml
RUN chmod +x /usr/bin/plantuml

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
     apk add --update bash && \
     python -m ensurepip && \
     rm -r /usr/lib/python*/ensurepip && \
     pip install -r /requirements.txt && \
     rm -r /root/.cache
