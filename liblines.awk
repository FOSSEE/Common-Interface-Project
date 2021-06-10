#!/usr/bin/awk -f

BEGINFILE {
    lines = 0;
    sum = 0;
    common[0] = 0;
    common[1] = 0;
}

/^DEF / {
    block = $2;
    parts = $8;
    lines++;
    sum += parts;
    maxpart = 0;
    maxdmg = 0;
    hascommon = 0;
}

/^[BP] / { part = $3; dmg = $4; }
/^C / { part = $5; dmg = $6; }
/^S / { part = $6; dmg = $7; }
/^[AT] / { part = $7; dmg = $8; }
/^X / { part = $10; dmg = $11; }

/^[ABCPSTX] / {
    if (part == 0) {
        maxpart = parts;
        if (parts > 1 && !(block in duplicateblocks)) {
            #print block, $1, parts;
            duplicateblocks[block] = 1;
            hascommon = 1;
        }
    } else if (maxpart < part)
        maxpart = part;
    if (dmg == 0)
        maxdmg = 2;
    else if (maxdmg < dmg)
        maxdmg = dmg;
    print block, part > "blockpart.out";
}

/^ENDDEF$/ {
    if (maxpart > 1) {
        print block, maxpart, hascommon > "blockenddef.out";
        common[hascommon]++;
    }
}

ENDFILE {
    if (common[0] > 0 || common[1] > 0)
        print FILENAME, lines, sum, common[0], common[1];
}
