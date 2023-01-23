#!/usr/bin/awk -f

/^# BEGIN / {
    file = $3;
    line = -2;
    next;
}

/^# END / {
    line = -2;
    next;
}

{
    if (++line > 0)
        printf "%s %s:%s\n", NR, file, line;
}
