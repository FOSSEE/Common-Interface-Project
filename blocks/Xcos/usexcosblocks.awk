#!/usr/bin/awk -f

/^[0-9]+ .*:[0-9]+$/ {
    lines[$1] = $2;
    next;
}

/^xcosblocks.py:[0-9]*:/ {
    linedata = gensub(/xcosblocks.py:([0-9]*):(.*)/, "\\1^\\2", "g", $0);
    split(linedata, line, "^")
    l = line[1]
    if (l in lines) {
        printf "%s:%s\n", lines[l], line[2];
    } else {
        print;
    }
}
