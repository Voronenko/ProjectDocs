#!/bin/sh
PROJECT=project
current_artefact=$(find ./$PROJECT*.tgz -type f -exec stat -c "%n" {} + | sort -r | head -n1)
echo Working with artefact: $current_artefact
tar xvzf $current_artefact
echo artefact unpacked: $current_artefact

