#!/bin/bash

set -e

python3 -m venv env
. env/bin/activate
pip install -q -U pip setuptools wheel
pip install -q -r requirements.txt

sed -i \
  -e "s,\\(SCILAB_DIR = '\\).*\\('\\),\\1/usr/local\\2," \
  -e "s,\\(CELERY_BROKER_URL = '\\).*\\('\\),\\1redis://localhost:6379/1\\2," \
  -e "s,\\(CELERY_RESULT_BACKEND = '\\).*\\('\\),\\1redis://localhost:6379/1\\2," \
  Xcos/common/AAAAAA.py \
  blocks/settings.py

mkdir -p file_storage/uploads logs media/saves media/uploads
make -s
python manage.py migrate -v0
python manage.py loaddata -v0 saveAPI xcosblocks
python manage.py collectstatic -v0 --no-input --ignore=admin --ignore=rest_framework
find -type d \( -name __pycache__ \) -print0 | xargs -0 rm -rf
find env -type d \( -name docs -o -name tests \) -print0 | xargs -0 rm -rf
# remove directories that are not needed
rm -rf \
  env/lib/python*/site-packages/django/contrib/admin/static/admin \
  env/lib/python*/site-packages/django/contrib/{flatpages,gis,humanize,postgres,syndication} \
  env/lib/python*/site-packages/drf_yasg/static/drf-yasg \
  env/lib/python*/site-packages/rest_framework/static/rest_framework
find env -name locale -print0 |
  xargs -0 -I {} find {} -mindepth 1 -maxdepth 1 -type d ! -name en -print0 |
  xargs -0 rm -rf

sed -i \
  -e '1i\
map $http_x_forwarded_proto $scheme_override {\
    default $http_x_forwarded_proto;\
    '\'\''      $scheme;\
}\
\
map $http_host $host_override {\
    default $http_host;\
    '\'\''      $host;\
}\
' \
  -e '/^\s*location \/ {/,/^\s*}/c\
        location / {\
                try_files $uri /index.html;\
        }\
\
        location = /index.html {\
                add_header Cache-Control "no-cache, no-store, must-revalidate";\
                add_header Pragma "no-cache";\
                add_header Expires 0;\
        }\
\
        location /api/ {\
                proxy_pass http://127.0.0.1:8000;\
                proxy_buffering off;\
                proxy_cache off;\
        }\
\
        location /django_static/ {\
                alias /var/www/html/static/;\
                autoindex off;\
                expires 7d;\
        }\
\
        location ~ /exa[mp].* {\
                return 302 $scheme://$host/#/gallery;\
        }\
\
        location /files/ {\
                proxy_pass http://127.0.0.1:8000;\
        }\
\
        location /open {\
                if ($arg_efid) {\
                    return 302 $scheme://$host/#/editor?id=gallery$arg_efid;\
                }\
                return 302 $scheme://$host/#/editor;\
        }' \
  /etc/nginx/sites-enabled/default

cd eda-frontend
npm install --silent
npm run build
cp -r build/* /var/www/html/

cd ..
rm -rf eda-frontend

pip uninstall -q -y flake8 mccabe pip pycodestyle pyflakes wheel
rm -f .flake8 .srcflake8 Makefile requirements.txt xcosblocks.sed
