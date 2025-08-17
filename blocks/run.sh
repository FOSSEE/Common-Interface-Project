#!/bin/bash

set -e

service nginx start
service redis-server start

. env/bin/activate
celery -A blocks.celery_tasks worker -c 10 -l INFO -P gevent &

if test "$1" = 'prod'; then
  :
else
  cd eda-frontend
  npm start &
  cd ..
fi

python manage.py migrate
python manage.py loaddata saveAPI xcosblocks
python manage.py runserver
