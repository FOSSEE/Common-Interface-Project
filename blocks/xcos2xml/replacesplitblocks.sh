#!/bin/bash

usage() {
  echo "Usage:" >&2
  echo "    $0 input-file.xcos [workspace.dat] [context]" >&2
  echo "    $0 input-file.xml [workspace.dat] [context]" >&2
  exit 101
}

if test $# -lt 1 -o $# -gt 3; then
  usage
fi

make -s >&2

SPLITXSL="eda-frontend/public/splitblock.xsl"
if test ! -f "$SPLITXSL"; then
  echo "$SPLITXSL: not found" >&2
  usage
fi
if test "${SPLITXSL%.xsl}" = "$SPLITXSL"; then
  echo "$SPLITXSL: not xsl" >&2
  usage
fi

XSL="eda-frontend/public/xcos2xml.xsl"
if test ! -f "$XSL"; then
  echo "$XSL: not found" >&2
  usage
fi
if test "${XSL%.xsl}" = "$XSL"; then
  echo "$XSL: not xsl" >&2
  usage
fi

GEOMETRYXSL="eda-frontend/public/geometry.xsl"
if test ! -f "$GEOMETRYXSL"; then
  echo "$GEOMETRYXSL: not found" >&2
  usage
fi
if test "${GEOMETRYXSL%.xsl}" = "$GEOMETRYXSL"; then
  echo "$GEOMETRYXSL: not xsl" >&2
  usage
fi

INPUT="$1"
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

WORKSPACE="$2"
if test -n "$WORKSPACE"; then
  if test ! -f "$WORKSPACE"; then
    echo "$WORKSPACE: not found" >&2
    usage
  fi
  if test "${WORKSPACE%.dat}" = "$WORKSPACE"; then
    echo "$WORKSPACE: not dat" >&2
    usage
  fi
fi

CONTEXT="$3"

set -e

TMPFILE1="$(mktemp -t XXXXXX.xml)"
TMPFILE2="$(mktemp -t XXXXXX.xml)"
trap "rm -f $TMPFILE1 $TMPFILE2" 0 1 2 15

if test -n "$INPUTXML"; then
  xmllint --format "$INPUTXML" >"$TMPFILE2"
  if ! diff -q "$TMPFILE2" "$INPUTXML" >&2; then
    cp -f "$TMPFILE2" "$INPUTXML"
    echo "$INPUTXML updated" >&2
  fi

  # MxGraphParser creates $INPUT
  echo "Running Xcos/MxGraphParser.py $INPUTXML $WORKSPACE $CONTEXT" >&2
  Xcos/MxGraphParser.py "$INPUTXML" "$WORKSPACE" "$CONTEXT" >&2
fi

count=$(grep -c '^      <SplitBlock' "$INPUT") || :
INPUT1="$BASE-$count.xml"
echo "Creating $INPUT1" >&2
cp -f "$INPUT" "$INPUT1"

while test $count -gt 0; do
  oldcount=$count

  xsltproc "$SPLITXSL" "$INPUT1" >"$TMPFILE1"
  xmllint --format "$TMPFILE1" >"$TMPFILE2"
  count=$(grep -c '^      <SplitBlock' "$TMPFILE2") || :
  INPUT1="$BASE-$count.xml"
  echo "Creating $INPUT1" >&2
  cp -f "$TMPFILE2" "$INPUT1"

  if ((count != oldcount - 1)); then
    echo "ERROR: $count != $oldcount - 1" >&2
    exit 2
  fi
done

xsltproc "$XSL" "$INPUT1" >"$TMPFILE1"
xmllint --format "$TMPFILE1" >"$TMPFILE2"
INPUT1="$BASE-xcos2xml.xml"
echo "Creating $INPUT1" >&2
cp -f "$TMPFILE2" "$INPUT1"

# Change BASE
BASE="$BASE-geometry"

xsltproc "$GEOMETRYXSL" "$INPUT1" >"$TMPFILE1"
xmllint --format "$TMPFILE1" >"$TMPFILE2"
INPUT1="$BASE.xml"
echo "Creating $INPUT1" >&2
cp -f "$TMPFILE2" "$INPUT1"

rm -f "$BASE-"*.xml

oldrv=100

echo "Running Xcos/XmlParser.py $INPUT1" >&2
Xcos/XmlParser.py "$INPUT1" >&2 && rv=$? || rv=$?

if ((rv >= oldrv)); then
  echo "ERROR: $rv >= $oldrv" >&2
  exit 102
fi

while test $rv -gt 0; do
  oldrv=$rv

  INPUT1="$BASE-$rv.xml"
  xmllint --format "$INPUT1" >"$TMPFILE2"
  cp -f "$TMPFILE2" "$INPUT1"
  echo "Running Xcos/XmlParser.py $INPUT1" >&2
  Xcos/XmlParser.py "$INPUT1" >&2 && rv=$? || rv=$?

  if ((rv >= oldrv)); then
    echo "ERROR: $rv >= $oldrv" >&2
    exit 102
  fi
done

INPUT1="$BASE-$rv.xml"
xmllint --format "$INPUT1" >"$TMPFILE2"
cp -f "$TMPFILE2" "$INPUT1"

echo "Running Xcos/MxGraphParser.py $INPUT1 $WORKSPACE $CONTEXT" >&2
Xcos/MxGraphParser.py "$INPUT1" "$WORKSPACE" "$CONTEXT" >&2
INPUT1="$BASE.xcos"
echo "Created $INPUT1" >&2

exit 0
