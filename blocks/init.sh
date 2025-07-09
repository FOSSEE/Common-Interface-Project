#!/bin/bash

### SETTINGS: Modify as required ###
EMAIL='sunilshetye@rocketmail.com'
PASSWORD=''
### END OF SETTINGS ###

rm -f xcosblocks.sqlite3

python manage.py migrate -v0
python manage.py loaddata -v0 saveAPI xcosblocks

echo "from authAPI.models import User; User.objects.create_superuser('$EMAIL', '$EMAIL', '$PASSWORD')" |
  python manage.py shell
