#!/bin/sh

set -e
set -x

BASEPATH=$(realpath "$(dirname $0)")
VERSION=$(cat "$BASEPATH/VERSION.txt")
DOCKERIMAGE="gfelbing/cppstyle"
GIT_TAG="v$VERSION"

# Upload to pypi
python setup.py sdist upload

# create docker image
docker build -t "$DOCKERIMAGE:$VERSION" "$BASEPATH"
# upload docker image
docker push "$DOCKERIMAGE:$VERSION"

# git tag version
git tag "$GIT_TAG"
# git push
git push
git push origin "$GIT_TAG"
