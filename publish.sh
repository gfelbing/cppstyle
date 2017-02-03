#!/bin/sh

set -e

BASEPATH=$(realpath "$(dirname $0)")
VERSION=$(cat "$BASEPATH/VERSION.txt")
DOCKERIMAGE="gfelbing/cppstyle"
GIT_TAG="v$VERSION"

echo -n "Running unit tests..."
python -m unittest tests
echo "done."

echo -n "Uploading to pypi..."
python setup.py sdist upload
echo "done."

echo -n "Creating docker image '$DOCKERIMAGE:$VERSION'..."
docker build -t "$DOCKERIMAGE:$VERSION" "$BASEPATH"
docker tag "$DOCKERIMAGE:$VERSION" "$DOCKERIMAGE:latest"
echo "done."
echo -n "Pushing docker image to registry..."
docker push "$DOCKERIMAGE:$VERSION"
docker push "$DOCKERIMAGE:latest"
echo "done."

echo -n "Tagging last commit with '$GIT_TAG'..."
git tag "$GIT_TAG"
echo "done."
echo -n "Pushing current branch and tag..."
git push
git push origin "$GIT_TAG"
echo "done."
