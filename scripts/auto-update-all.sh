#!/bin/bash

shopt -s nullglob

cd ${0%/*} || exit 1

# This script updates all docker images on the system.
# It pulls the latest images, recreates containers with the new images,
# and removes old images to free up space.

for conf in *.conf; do
  [ -f "$conf" ] || continue
  echo ">>> Processing configuration file: $conf"
  ./auto-update.sh "$conf"
done
