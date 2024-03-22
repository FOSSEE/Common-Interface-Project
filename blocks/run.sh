#!/bin/bash

set -e

service nginx start
service redis-server start

. env/bin/activate
celery -A blocks.celery_tasks worker --loglevel INFO --concurrency 1 &

cd eda-frontend
if test "$1" = 'prod'; then
    serve -l 3500 -n -s --no-port-switching build &
else
    npm start &
fi

cd ..
python manage.py runserver
