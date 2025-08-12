#!/bin/bash

set -e

service nginx start
service redis-server start

. env/bin/activate
celery -A blocks.celery_tasks worker -c 10 -l INFO -P gevent &

cd eda-frontend
if test "$1" = 'prod'; then
  serve -l 3500 -n -s --no-port-switching build &
else
  npm start &
fi

cd ..
python manage.py migrate
python manage.py loaddata saveAPI xcosblocks
python manage.py collectstatic --no-input
rm -rf /var/www/html/static/{admin,rest_framework}
python manage.py runserver
