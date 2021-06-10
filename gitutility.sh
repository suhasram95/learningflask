#!/bin/bash
# This utility will push help in pushing the changes from the current branch to the repo
BRANCH=$(git rev-parse --abbrev-ref HEAD)
MESSAGE=$1
git add .
git commit -m "$MESSAGE"
git push origin $BRANCH
