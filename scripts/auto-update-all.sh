#!/bin/bash

shopt -s nullglob

cd ${0%/*} || exit 1

# This script manages all docker images on the system.
# supported modes:
# start
# stop
# restart
# reload
# update (default)
#   It pulls the latest images, recreates containers with the new images, and removes old images to free up space.
# status
MODE="${1:-update}"
echo ">>> Processing: $MODE at $(date)"

for conf in *.conf; do
  [ -f "$conf" ] || continue
  echo ">>> Processing configuration file: $conf $MODE"
  ./auto-update.sh "$conf" "$MODE"
done
