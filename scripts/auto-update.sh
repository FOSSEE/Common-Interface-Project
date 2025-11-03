#!/bin/bash

if [[ "$ALREADY_SOURCED" = "yes" ]]; then
  return
fi
ALREADY_SOURCED=yes

# Configuration
DOCKER="docker" # or "podman"
IMAGE=""
CONTAINER=""
DOCKER_OPTIONS=""
PODMAN_OPTIONS="--cap-add=NET_RAW --network=slirp4netns:allow_host_loopback=true"

ENV_VARS=()
ENV_VALS=()
HOST_PORTS=()
DOCKER_PORTS=()
HOST_FILES=()
DOCKER_FILES=()
HOST_DIRECTORIES=()
DOCKER_DIRECTORIES=()

LOG_LINES=30
# End Configuration

cd ${0%/*} || exit 1
test "$#" -ge 1 -a "$#" -le 2 || {
  echo "Usage: $0 ${DOCKER}_config_file.conf mode"
  exit 1
}
test -n "$1" -a "${1%.conf}" != "$1" -a -f "$1" || {
  echo "Usage: $0 ${DOCKER}_config_file.conf mode"
  exit 1
}
. "$1" || exit 2
test -n "$IMAGE" -a -n "$CONTAINER" || {
  echo "IMAGE and CONTAINER must be set"
  exit 3
}
MODE="${2:-update}"

for i in "${!ENV_VARS[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -e ${ENV_VARS[i]}=${ENV_VALS[i]}"
done
for i in "${!HOST_PORTS[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -p ${HOST_PORTS[i]}:${DOCKER_PORTS[i]}"
done
for i in "${!HOST_FILES[@]}"; do
  test -f "${HOST_FILES[i]}" || touch "${HOST_FILES[i]}"
  DOCKER_OPTIONS="$DOCKER_OPTIONS -v ${HOST_FILES[i]}:${DOCKER_FILES[i]}"
done
for i in "${!HOST_DIRECTORIES[@]}"; do
  DOCKER_OPTIONS="$DOCKER_OPTIONS -v ${HOST_DIRECTORIES[i]}:${DOCKER_DIRECTORIES[i]}"
done
if test "$DOCKER" = 'podman'; then
  DOCKER_OPTIONS="$DOCKER_OPTIONS $PODMAN_OPTIONS"
fi

set -euo pipefail

start() {
  echo ">>> Starting container $CONTAINER..."
  $DOCKER run -d --name "$CONTAINER" $DOCKER_OPTIONS "$IMAGE"
  echo "$DOCKER_OPTIONS" >"${CONTAINER}.options"
}

stop() {
  echo ">>> Stopping container $CONTAINER..."
  $DOCKER stop "$CONTAINER" || true
  $DOCKER rm "$CONTAINER" || true
  rm -f "${CONTAINER}.options" || true
}

restart() {
  stop
  start
}

reload() {
  LAST_DOCKER_OPTIONS=$(cat "${CONTAINER}.options" 2>/dev/null || echo)
  if [ "$LAST_DOCKER_OPTIONS" = "$DOCKER_OPTIONS" ]; then
    echo ">>> No changes in $CONTAINER options, reload not needed."
    exit 0
  fi
  echo ">>> Reloading container $CONTAINER with new options..."
  stop
  start
}

status() {
  echo ">>> Status of container $CONTAINER:"
  $DOCKER ps --filter "name=$CONTAINER" -a -s
  $DOCKER logs --tail $LOG_LINES "$CONTAINER"
}

update() {
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
    echo ">>> Image $IMAGE is unchanged."
    reload
    exit 0
  fi

  echo ">>> New image detected. Restarting container $CONTAINER..."

  # Stop and remove old container if exists
  if [[ -n "$OLD_IMAGE_ID" ]]; then
    stop
  fi

  start

  sleep 15

  # Verify container is running
  if ! $DOCKER ps --format '{{.Names}}' | grep -q "^$CONTAINER\$"; then
    echo "!!! Container $CONTAINER failed to start with new image."
    exit 1
  fi

  status

  # Clean up old images
  $DOCKER system prune -f || true

  echo ">>> Update complete. Running container uses $NEW_IMAGE_ID"
}

case "$MODE" in
start) start ;;
stop) stop ;;
restart) restart ;;
reload) reload ;;
update) update ;;
status) status ;;
*)
  echo "Invalid mode: $MODE"
  echo "Usage: $0 ${DOCKER}_config_file.conf mode"
  echo "mode: start | stop | restart | reload | update | status"
  exit 4
  ;;
esac
