#!/usr/bin/sed -f

/<xsl:attribute name="simulationFunction">/i\
        <xsl:variable name="inputPortNumber">0</xsl:variable>\
        <xsl:variable name="outputPortNumber">0</xsl:variable>\
        <xsl:variable name="controlPortNumber">0</xsl:variable>\
        <xsl:variable name="commandPortNumber">0</xsl:variable>\
        <xsl:attribute name="explicitInputPorts">\
          <xsl:value-of select="$explicitInputPorts" />\
        </xsl:attribute>\
        <xsl:attribute name="implicitInputPorts">\
          <xsl:value-of select="$implicitInputPorts" />\
        </xsl:attribute>\
        <xsl:attribute name="explicitOutputPorts">\
          <xsl:value-of select="$explicitOutputPorts" />\
        </xsl:attribute>\
        <xsl:attribute name="implicitOutputPorts">\
          <xsl:value-of select="$implicitOutputPorts" />\
        </xsl:attribute>\
        <xsl:attribute name="controlPorts">\
          <xsl:value-of select="$controlPorts" />\
        </xsl:attribute>\
        <xsl:attribute name="commandPorts">\
          <xsl:value-of select="$commandPorts" />\
        </xsl:attribute>
