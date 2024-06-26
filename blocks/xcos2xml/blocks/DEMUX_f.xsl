    <xsl:template match="*[@interfaceFunctionName = 'DEMUX_f']">
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
        <!-- <xsl:variable name="explicitOutputPorts">2</xsl:variable> -->
        <xsl:variable name="explicitOutputPorts">
          <xsl:value-of select="*[@as='exprs']/data[1]/@value"/>
        </xsl:variable>
        <xsl:variable name="implicitOutputPorts">0</xsl:variable>
        <xsl:variable name="controlPorts">0</xsl:variable>
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
        <Object>
          <xsl:attribute name="display_parameter">
            <xsl:value-of select="*[@as='exprs']/data/@value"/>
          </xsl:attribute>
          <xsl:attribute name="as">displayProperties</xsl:attribute>
        </Object>
        <Object>
          <xsl:attribute name="p000_value">
            <xsl:value-of select="*[@as='exprs']/data/@value"/>
          </xsl:attribute>
          <xsl:attribute name="as">parameter_values</xsl:attribute>
        </Object>
      </xsl:element>
    </xsl:template>
