#!/usr/bin/awk -f

BEGIN {
    STDERR = "/dev/stderr";
    PRINTCATEGORIESCSV = 0;
    PRINTBLOCKCATEGORIESCSV = 1;
    PRINTBLOCKSCSV = 0;
    PRINTBLOCKPORTSCSV = 0;
    PRINTMINMAXCSV = 0;
    categoryid = 0;
}

BEGINFILE {
    category = gensub(".*/([^/]*)\\.lib$", "\\1", "g", FILENAME);
    categoryid++;
    blockcount = 0;
}

/^DEF / {
    block = $2;
    idx = block;
    if (!(idx in blocks)) {
        blockcount++;
        blocks[idx] = $0;
        if (PRINTBLOCKCATEGORIESCSV) {
            printf "%s,%s\n", category, block;
        }
        if (PRINTBLOCKSCSV) {
            printf "%s\n", block;
        }
    } else {
        if (blocks[idx] == $0) {
            printf "duplicate block: %s\n", block > STDERR;
        } else {
            printf "not a duplicate block: %s: %s and %s\n", block, blocks[idx], $0 > STDERR;
        }
    }
}

/^X / {
    port_name = $2;
    port_number = $3;
    port_order = $3;
    port_orientation = $7;
    port_part = $10;
    port_dmg = $11;
    port_type = $12;
    idx = block SUBSEP port_number;
    if (!(idx in ports)) {
        ports[idx] = $0;
        if (PRINTBLOCKPORTSCSV) {
            printf "%s,%s,%s,%s,%s,%s\n", block, port_number, port_name, port_order, port_type, port_orientation;
        }
        if (block in minports) {
            if (minports[block] > port_number) {
                minports[block] = port_number;
            } else if (maxports[block] < port_number) {
                maxports[block] = port_number;
            }
        } else {
            minports[block] = port_number;
            maxports[block] = port_number;
        }
    } else {
        if (port_part == "2" || port_part == "3" || port_part == "4" || port_dmg == "2") {
            ;
        } else if (ports[idx] == $0) {
            printf "duplicate port: %s %s %s %s\n", block, port_number, port_part, port_dmg > STDERR;
        } else {
            printf "not a duplicate port: %s %s %s %s: %s and %s\n", block, port_number, port_part, port_dmg, ports[idx], $0 > STDERR;
        }
    }
}

/^ENDDEF/ {
    block = "";
}

ENDFILE {
    if (PRINTCATEGORIESCSV) {
        printf "%s,%s,%s,%s\n", categoryid, category, categoryid, blockcount;
    }

    category = "";
}

END {
    if (PRINTMINMAXCSV) {
        for (block in minports) {
            printf "%s,%s,%s\n", block, minports[block], maxports[block];
        }
    }
}
