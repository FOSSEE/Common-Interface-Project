#!/bin/bash

mysql --login-path=local -B -N esimblocks < create-style-json.sql |
    sed -e 's/\\n/\n/g' |
    tac |
    sed '1,/^  },/s/^  },/  }/' |
    tac > blocks/eda-frontend/src/static/eSim-style.json

