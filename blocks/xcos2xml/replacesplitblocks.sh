#!/bin/bash

usage() {
    echo "Usage:" >&2
    echo "    $0 file.xsl input-file.xml > output-file.xml" >&2
    echo "    $0 file.xsl input-file.xcos > output-file.xml" >&2
    exit 1
}

if test $# -ne 2; then
    usage
fi

XSL="$1"
if test "${XSL%.xsl}" = "$XSL"; then
    usage
fi
if test ! -f "$XSL"; then
    usage
fi

INPUT="$2"
if test "${INPUT%.xml}" = "$$INPUT" -a "${INPUT%.xcos}" = "$$INPUT"; then
    usage
fi
if test ! -f "$INPUT"; then
    usage
fi

set -e

TMPFILE1="$( mktemp -t XXXXXX.xml )"
TMPFILE2="$( mktemp -t XXXXXX.xml )"
trap "cat $TMPFILE1; rm -f $TMPFILE1 $TMPFILE2" 0 1 2 15

cp "$INPUT" "$TMPFILE1"

count=$( grep -c '<SplitBlock' "$TMPFILE1" ) || :
echo $count >&2

while test $count -gt 0; do
    oldcount=$count

    xsltproc "$XSL" "$TMPFILE1" > "$TMPFILE2"
    mv -f "$TMPFILE2" "$TMPFILE1"
    count=$( grep -c '<SplitBlock' "$TMPFILE1" ) || :
    echo $count >&2

    if let 'count!=oldcount-1'; then
        echo "ERROR: $count != $oldcount - 1" >&2
        exit 2
    fi
done

xmllint --format "$TMPFILE1" > "$TMPFILE2"
mv -f "$TMPFILE2" "$TMPFILE1"
exit 0
