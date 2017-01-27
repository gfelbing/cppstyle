#!/bin/sh

set -e
set -x

BASEPATH=$(realpath "$(dirname $0)")
VERSION=$(cat "$BASEPATH/VERSION.txt")
DOCKERIMAGE="gfelbing/cppstyle"

# Upload to pypi
python setup.py sdist upload

# create docker image
docker build -t "$DOCKERIMAGE:$VERSION" "$BASEPATH"
# upload docker image
docker push "$DOCKERIMAGE:$VERSION"

# git tag version
git tag "v$VERSION"
# git push
git push
