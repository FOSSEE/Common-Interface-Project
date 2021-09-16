#!/bin/bash

mysql -p"$( cat ~/.mysql.pwd )" -B -N esimblocks < scripts/create-style-json.sql |
    sed -e 's/\\n/\n/g' |
    tac |
    sed '1,/^  },/s/^  },/  }/' |
    tac > blocks/eda-frontend/src/static/style.json
