#!/bin/sh

HOME=$PWD
PROJECT=project
VERSIONFILE=_buildinfo.txt
SKIPLIST="--exclude=.git --exclude=*.sh  --exclude=*.tgz"

if [ -z "$1" ]
then
  SUFFIX=""
else
  SUFFIX="-$1"
fi

rm $PROJECT-*.tgz || true

VERSION=`cat version.txt`
GITCOMMIT=`git rev-parse --short HEAD`
GITBRANCH=`git rev-parse --abbrev-ref HEAD`
DATE=`date +%Y-%m-%d:%H:%M:%S`


echo "major_version=$VERSION" > $VERSIONFILE
echo "minor_version=$1" >> $VERSIONFILE
echo "git_hash=$GITCOMMIT" >> $VERSIONFILE
echo "git_branch" >> $VERSIONFILE
echo "built=$DATE" >> $VERSIONFILE
echo "ARTIFACT_VERSION=$VERSION" >> $VERSIONFILE

cp $VERSIONFILE ./out/html || true

cd ./out/html

echo tar cfz $PROJECT-$VERSION$SUFFIX.tgz . $SKIPLIST
tar cfz $HOME/$PROJECT-$VERSION$SUFFIX.tgz . $SKIPLIST || true
