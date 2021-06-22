#!/bin/bash

find blocks/blocks/esimblocks/static -type f -name \*-1-A.svg |
    sort |
    xargs -r fgrep -H ' width=' |
    ./getsize.awk
