#!/bin/bash

set -e

python3 -m venv env
. env/bin/activate
pip install -q -U pip setuptools wheel
pip install -q -r requirements.txt
pip uninstall -q -y pip wheel

make -s
python manage.py makemigrations -v0 simulationAPI xcosblocks
python manage.py migrate -v0
python manage.py loaddata -v0 xcosblocks

sed -i \
    -e "s/\\(SCILAB_DIR = \\).*/\\1'\/usr\/local'/" \
    -e "s/\\(CELERY_BROKER_URL = \\).*/\\1'redis:\\/\\/localhost:6379\\/1'/" \
    -e "s/\\(CELERY_RESULT_BACKEND = \\).*/\\1'redis:\\/\\/localhost:6379\\/1'/" \
    blocks/settings.py

sed -i -e '/^\s*location \/ {/,/^\s*}/c\
        location / {\
                proxy_pass http://127.0.0.1:3500;\
        }\
\
        location /api/ {\
                proxy_pass http://127.0.0.1:8000;\
                proxy_buffering off;\
                proxy_cache off;\
        }\
\
        location /django_static/ {\
                proxy_pass http://127.0.0.1:8000;\
        }\
\
        location /ws {\
                proxy_pass http://127.0.0.1:3500;\
                proxy_http_version 1.1;\
                proxy_set_header Upgrade $http_upgrade;\
                proxy_set_header Connection "Upgrade";\
                proxy_set_header Host $host;\
                proxy_buffering off;\
                proxy_cache off;\
        }' /etc/nginx/sites-enabled/default

cd eda-frontend
if test "$1" = 'prod'; then
    npm install -g serve
fi
npm install --silent
if test "$1" = 'prod'; then
    npm run build
    rm -rf node_modules public src
fi
echo 'WDS_SOCKET_PORT=8000' > .env.local
