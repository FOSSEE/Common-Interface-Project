#!/bin/bash

set -e

cd eda-frontend
npm install --silent
echo 'WDS_SOCKET_PORT=8000' > .env.local

cd ..
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
