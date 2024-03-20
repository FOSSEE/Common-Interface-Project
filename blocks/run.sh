#!/bin/bash

set -e

service nginx start

. env/bin/activate

cd eda-frontend
npm start &

cd ..
python manage.py runserver
