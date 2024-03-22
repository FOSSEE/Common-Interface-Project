#!/bin/bash

set -e

service nginx start
service redis-server start

. env/bin/activate
celery -A blocks.celery_tasks worker --loglevel INFO --concurrency 1 &

cd eda-frontend
npm start &

cd ..
python manage.py runserver
