#!/bin/bash


SOURCE_IMAGE="testoo"
docker build . -t $SOURCE_IMAGE

GOOGLE_PROJECT_ID="sturdy-spanner-370810"
TARGET_IMAGE="asia-southeast2-docker.pkg.dev/$GOOGLE_PROJECT_ID/another-you/manual_matcher_tool"
docker tag $SOURCE_IMAGE \
$TARGET_IMAGE
docker push $TARGET_IMAGE