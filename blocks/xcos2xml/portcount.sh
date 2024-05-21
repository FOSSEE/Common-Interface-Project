#!/bin/bash

sqlite3 xcosblocks.sqlite3 < xcos2xml/portcount.sql > portcount.csv

while read line; do
    IFS=',' read -r block_name explicitInputPorts implicitInputPorts explicitOutputPorts implicitOutputPorts controlPorts commandPorts dummy <<< "$line"
    file=xcos2xml/blocks/$block_name.xsl
    if ! test -f $file; then
        echo "$file: not found"
        continue
    fi
    sed -i \
        -e "s,\\(<xsl:attribute name=\"explicitInputPorts\">\\).*\\(</xsl:attribute>\\),\\1$explicitInputPorts\\2," \
        -e "s,\\(<xsl:attribute name=\"implicitInputPorts\">\\).*\\(</xsl:attribute>\\),\\1$implicitInputPorts\\2," \
        -e "s,\\(<xsl:attribute name=\"explicitOutputPorts\">\\).*\\(</xsl:attribute>\\),\\1$explicitOutputPorts\\2," \
        -e "s,\\(<xsl:attribute name=\"implicitOutputPorts\">\\).*\\(</xsl:attribute>\\),\\1$implicitOutputPorts\\2," \
        -e "s,\\(<xsl:attribute name=\"controlPorts\">\\).*\\(</xsl:attribute>\\),\\1$controlPorts\\2," \
        -e "s,\\(<xsl:attribute name=\"commandPorts\">\\).*\\(</xsl:attribute>\\),\\1$commandPorts\\2," \
        $file
done < portcount.csv

rm -f portcount.csv
