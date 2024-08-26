#!/bin/bash

### SETTINGS: Modify as required ###
EMAIL='sunilshetye@rocketmail.com'
PASSWORD=''
### END OF SETTINGS ###

rm -f xcosblocks.sqlite3

./manage.py makemigrations -v0
./manage.py migrate -v0
./manage.py loaddata xcosblocks

echo "from authAPI.models import User; User.objects.create_superuser('$EMAIL', '$EMAIL', '$PASSWORD')" |
    ./manage.py shell
