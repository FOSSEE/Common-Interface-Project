#!/bin/bash

set -e

service nginx start
service redis-server start

. env/bin/activate
celery -A blocks.celery_tasks -q worker -c 10 -l INFO -P gevent &
PIDS=($!)

python manage.py migrate
python manage.py loaddata saveAPI xcosblocks
gunicorn blocks.wsgi:application -b 0.0.0.0:8000 -k gevent -w 10 &
PIDS+=($!)

# Handle SIGTERM properly
term_handler() {
  echo "$(date +'%H:%M:%S') Stopping services with PIDs: ${PIDS[@]}"
  kill -TERM "${PIDS[@]}" || true
  service redis-server stop || true
  service nginx stop || true
  wait "${PIDS[@]}"
  echo "$(date +'%H:%M:%S') All services stopped."
  exit 0
}

trap 'echo SIGTERM received; term_handler' SIGTERM SIGINT

echo "$(date +'%H:%M:%S') Services started with PIDs: ${PIDS[@]}"
wait -n
echo "A service has exited, initiating shutdown..."
term_handler
