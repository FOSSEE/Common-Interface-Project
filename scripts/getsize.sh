#!/bin/bash

find blocks/blocks/xcosblocks/static -type f -name \*-1-A.svg |
    sort |
    xargs -r fgrep -H ' width=' |
    ./scripts/getsize.awk
