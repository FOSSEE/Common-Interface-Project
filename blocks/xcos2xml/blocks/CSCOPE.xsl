    <xsl:template match="*[@interfaceFunctionName = 'CSCOPE']">
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
        <xsl:variable name="explicitInputPorts">1</xsl:variable>
        <xsl:variable name="implicitInputPorts">0</xsl:variable>
        <xsl:variable name="explicitOutputPorts">0</xsl:variable>
        <xsl:variable name="implicitOutputPorts">0</xsl:variable>
        <!-- <xsl:variable name="controlPorts">1</xsl:variable> -->
        <xsl:variable name="value" select="(*[@as='exprs']/data[9]/@value)" />
        <xsl:variable name="controlPorts">
          <xsl:choose>
            <xsl:when test="$value = 0">
              <xsl:text>1</xsl:text>
            </xsl:when>
          </xsl:choose>
        </xsl:variable>
        <xsl:variable name="commandPorts">0</xsl:variable>
        <xsl:variable name="inputPortNumber">0</xsl:variable>
        <xsl:variable name="outputPortNumber">0</xsl:variable>
        <xsl:variable name="controlPortNumber">0</xsl:variable>
        <xsl:variable name="commandPortNumber">0</xsl:variable>
        <xsl:attribute name="explicitInputPorts">
          <xsl:value-of select="$explicitInputPorts" />
        </xsl:attribute>
        <xsl:attribute name="implicitInputPorts">
          <xsl:value-of select="$implicitInputPorts" />
        </xsl:attribute>
        <xsl:attribute name="explicitOutputPorts">
          <xsl:value-of select="$explicitOutputPorts" />
        </xsl:attribute>
        <xsl:attribute name="implicitOutputPorts">
          <xsl:value-of select="$implicitOutputPorts" />
        </xsl:attribute>
        <xsl:attribute name="controlPorts">
          <xsl:value-of select="$controlPorts" />
        </xsl:attribute>
        <xsl:attribute name="commandPorts">
          <xsl:value-of select="$commandPorts" />
        </xsl:attribute>
        <xsl:attribute name="simulationFunction">
          <xsl:value-of select="@simulationFunctionName" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <Object display_parameter="" as="displayProperties"/>
        <Object p000_value="1 3 5 7 9 11 13 15" p001_value="-1" p002_value="[]" p003_value="[600;400]" p004_value="-2" p005_value="2" p006_value="30" p007_value="20" p008_value="0" p009_value="" as="parameter_values"/>
      </xsl:element>
    </xsl:template>
