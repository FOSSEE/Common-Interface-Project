#!/usr/bin/awk -f

BEGIN {
    GETSIZECSV = "getsize.csv";
}

# blocks/blocks/esimblocks/static/4xxx/U-4001-1-A.svg:     width="600" height="300" viewBox="-300.0 -150.0 600 300">

/\.svg: *width=".*" height=".*" / {
    name = gensub(".*/([^/]*/[^/]*)\\.svg:", "\\1", "g", $1);
    main_category = gensub("(.*)/([^-]*)-(.*)-1-A", "\\1", "g", name);
    blockprefix = gensub("(.*)/([^-]*)-(.*)-1-A", "\\2", "g", name);
    blockname = gensub("(.*)/([^-]*)-(.*)-1-A", "\\3", "g", name);
    width = gensub("width=\"(.*)\"", "\\1", "g", $2);
    height = gensub("height=\"(.*)\"", "\\1", "g", $3);
    printf "%s\t%s\t%s\t%s\n", main_category, blockname, width, height > GETSIZECSV;
}
