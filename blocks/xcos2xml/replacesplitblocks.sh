#!/bin/bash

usage() {
    echo "Usage:" >&2
    echo "    $0 split-file.xsl file.xsl input-file.xcos > output-file.xml" >&2
    echo "    $0 split-file.xsl file.xsl input-file.xml > output-file.xml" >&2
    exit 1
}

if test $# -ne 3; then
    usage
fi

make -s >&2

SPLITXSL="$1"
if test ! -f "$SPLITXSL"; then
    echo "$SPLITXSL: not found" >&2
    usage
fi
if test "${SPLITXSL%.xsl}" = "$SPLITXSL"; then
    echo "$SPLITXSL: not xsl" >&2
    usage
fi

XSL="$2"
if test ! -f "$XSL"; then
    echo "$XSL: not found" >&2
    usage
fi
if test "${XSL%.xsl}" = "$XSL"; then
    echo "$XSL: not xsl" >&2
    usage
fi

INPUT="$3"
if test ! -f "$INPUT"; then
    echo "$INPUT: not found" >&2
    usage
fi
if test "${INPUT%.xml}" != "$INPUT"; then
    INPUTXML="$INPUT"
    BASE="${INPUT%.xml}"
    INPUT="$BASE.xcos"
elif test "${INPUT%.xcos}" != "$INPUT"; then
    INPUTXML=
    BASE="${INPUT%.xcos}"
else
    echo "$INPUT: not xml / xcos" >&2
    usage
fi

set -e

TMPFILE1="$( mktemp -t XXXXXX.xml )"
TMPFILE2="$( mktemp -t XXXXXX.xml )"
trap "cat $TMPFILE2; rm -f $TMPFILE1 $TMPFILE2" 0 1 2 15

if test -n "$INPUTXML"; then
    xmllint --format "$INPUTXML" > "$TMPFILE2"
    if ! diff -q "$TMPFILE2" "$INPUTXML" >&2; then
        cp -f "$TMPFILE2" "$INPUTXML"
        echo "$INPUTXML updated" >&2
    fi

    # MxGraphParser creates $INPUT
    echo "Running Xcos/MxGraphParser.py $INPUTXML" >&2
    Xcos/MxGraphParser.py "$INPUTXML" >&2
fi

count=$( grep -c '^      <SplitBlock' "$INPUT" ) || :
INPUT1="$BASE-$count.xml"
echo "Creating $INPUT1" >&2
cp -f "$INPUT" "$INPUT1"

while test $count -gt 0; do
    oldcount=$count

    xsltproc "$SPLITXSL" "$INPUT1" > "$TMPFILE1"
    xmllint --format "$TMPFILE1" > "$TMPFILE2"
    count=$( grep -c '^      <SplitBlock' "$TMPFILE2" ) || :
    INPUT1="$BASE-$count.xml"
    echo "Creating $INPUT1" >&2
    cp -f "$TMPFILE2" "$INPUT1"

    if (( count != oldcount - 1 )); then
        echo "ERROR: $count != $oldcount - 1" >&2
        exit 2
    fi
done

xsltproc "$XSL" "$INPUT1" > "$TMPFILE1"
xmllint --format "$TMPFILE1" > "$TMPFILE2"
cp -f "$TMPFILE2" "$TMPFILE1"

exit 0
