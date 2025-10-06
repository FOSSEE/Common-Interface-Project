#!/bin/bash

if [[ "$ALREADY_SOURCED" = "yes" ]]; then
  return
fi
ALREADY_SOURCED=yes

# Configuration
DOCKER="docker" # or "podman"
IMAGE=""
CONTAINER=""

ENV_VARS=()
ENV_VALS=()
HOST_PORTS=()
DOCKER_PORTS=()
HOST_FILES=()
DOCKER_FILES=()
# End Configuration

cd ${0%/*} || exit 1
test "$#" -eq 1 -a -n "$1" -a -f "$1" || {
  echo "Usage: $0 ${DOCKER}_config_file"
  exit 1
}
. "$1" || exit 2
test -n "$IMAGE" -a -n "$CONTAINER" || {
  echo "IMAGE and CONTAINER must be set"
  exit 3
}

DOCKER_OPTIONS=""
for i in "${!ENV_VARS[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -e ${ENV_VARS[i]}=${ENV_VALS[i]}"
done
for i in "${!HOST_PORTS[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -p ${HOST_PORTS[i]}:${DOCKER_PORTS[i]}"
done
for i in "${!HOST_FILES[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -v ${HOST_FILES[i]}:${DOCKER_FILES[i]}"
done

set -euo pipefail

echo ">>> Checking for updates to $IMAGE..."

# Get currently running image ID (if container exists)
if $DOCKER ps -a --format '{{.Names}}' | grep -q "^$CONTAINER\$"; then
  OLD_IMAGE_ID=$($DOCKER inspect --format='{{.Image}}' "$CONTAINER")
else
  OLD_IMAGE_ID=""
fi

# Pull latest image
$DOCKER pull "$IMAGE" >/tmp/$DOCKER-pull.log 2>&1 || {
  echo "!!! Failed to pull image $IMAGE"
  cat /tmp/$DOCKER-pull.log
  exit 1
}

NEW_IMAGE_ID=$($DOCKER inspect --format='{{.Id}}' "$IMAGE")

if [ "$OLD_IMAGE_ID" = "$NEW_IMAGE_ID" ]; then
  echo ">>> Image is unchanged, no restart needed."
  exit 0
fi

echo ">>> New image detected. Restarting container $CONTAINER..."

# Stop and remove old container if exists
if [[ -n "$OLD_IMAGE_ID" ]]; then
  $DOCKER stop "$CONTAINER" || true
  $DOCKER rm "$CONTAINER" || true
fi

# Run new container (adjust options as needed)
$DOCKER run -d --name "$CONTAINER" $DOCKER_OPTIONS "$IMAGE"

sleep 20

# Verify container is running
$DOCKER ps --filter "name=$CONTAINER" -a -s
$DOCKER logs --tail 60 "$CONTAINER"

# Clean up old images
$DOCKER system prune -f || true

echo ">>> Update complete. Running container uses $NEW_IMAGE_ID"
