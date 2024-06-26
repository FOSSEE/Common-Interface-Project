    <xsl:template match="*[@interfaceFunctionName = 'RFILE_f']">
      <xsl:element name="mxCell">
        <xsl:attribute name="style">
          <xsl:value-of select="@style" />
        </xsl:attribute>
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="vertex">1</xsl:attribute>
        <xsl:attribute name="connectable">0</xsl:attribute>
        <xsl:attribute name="CellType">Component</xsl:attribute>
        <xsl:attribute name="blockprefix">XCOS</xsl:attribute>
        <xsl:attribute name="explicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="implicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="explicitOutputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitOutputPorts">0</xsl:attribute>
        <xsl:attribute name="controlPorts">1</xsl:attribute>
        <!-- <xsl:attribute name="commandPorts">0</xsl:attribute> -->
        <xsl:variable name="value" select="(*[@as='exprs']/data[1]/@value)" />
        <xsl:attribute name="commandPorts">
          <xsl:choose>
            <xsl:when test="number($value) > 0">
              <xsl:value-of select="$value" />
            </xsl:when>
            <xsl:otherwise>
              <xsl:text>0</xsl:text>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="simulationFunction">
          <xsl:value-of select="@simulationFunctionName" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <Object>
          <xsl:attribute name="display_parameter">
            <xsl:value-of select="@value"/>
          </xsl:attribute>
          <xsl:attribute name="as">displayProperties</xsl:attribute>
        </Object>
        <Object>
          <xsl:for-each select="*[@as='exprs']/data">
            <xsl:attribute name="{concat('p', format-number(position() - 1, '000'), '_value')}">
              <xsl:value-of select="@value"/>
            </xsl:attribute>
          </xsl:for-each>
          <xsl:attribute name="as">parameter_values</xsl:attribute>
        </Object>
      </xsl:element>
    </xsl:template>
