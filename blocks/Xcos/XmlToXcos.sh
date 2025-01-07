#!/bin/bash

usage() {
  echo "Usage:" >&2
  echo "    $0 input-file.xml" >&2
  exit 101
}

if test $# -ne 1; then
  usage
fi

INPUT="$1"
if test ! -f "$INPUT"; then
  echo "$INPUT: not found" >&2
  usage
fi
if test "${INPUT%.xml}" != "$INPUT"; then
  BASE="${INPUT%.xml}"
  INPUT1="$INPUT"
else
  echo "$INPUT: not xml" >&2
  usage
fi

set -e

TMPFILE2="$(mktemp -t XXXXXX.xml)"
trap "rm -f $TMPFILE2" 0 1 2 15

rm -f "$BASE."*.xml

oldrv=100

echo "Running Xcos/XmlParser.py $INPUT1" >&2
Xcos/XmlParser.py "$INPUT1" >&2 && rv=$? || rv=$?

if ((rv >= oldrv)); then
  echo "ERROR: $rv >= $oldrv" >&2
  exit 102
fi

while test $rv -gt 0; do
  oldrv=$rv

  INPUT1="$BASE.$rv.xml"
  echo "Created $INPUT1" >&2
  xmllint --format "$INPUT1" >"$TMPFILE2"
  cp -f "$TMPFILE2" "$INPUT1"
  echo "Running Xcos/XmlParser.py $INPUT1" >&2
  Xcos/XmlParser.py "$INPUT1" >&2 && rv=$? || rv=$?

  if ((rv >= oldrv)); then
    echo "ERROR: $rv >= $oldrv" >&2
    exit 102
  fi
done

INPUT1="$BASE.$rv.xml"
echo "Created $INPUT1" >&2
xmllint --format "$INPUT1" >"$TMPFILE2"
cp -f "$TMPFILE2" "$INPUT1"

echo "Running Xcos/MxGraphParser.py $INPUT1" >&2
Xcos/MxGraphParser.py "$INPUT1" >&2
INPUT1="$BASE.$rv.xcos"
echo "Created $INPUT1" >&2

exit 0
