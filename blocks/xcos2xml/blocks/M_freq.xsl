    <xsl:template match="*[@interfaceFunctionName = 'M_freq']">
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
        <xsl:variable name="explicitInputPorts">0</xsl:variable>
        <xsl:variable name="implicitInputPorts">0</xsl:variable>
        <xsl:variable name="explicitOutputPorts">0</xsl:variable>
        <xsl:variable name="implicitOutputPorts">0</xsl:variable>
        <xsl:variable name="controlPorts">1</xsl:variable>
        <xsl:variable name="commandPorts">
          <xsl:variable name="value" select="(*[@as='exprs']/data[1]/@value)" />
          <xsl:variable name="count" select="string-length($value) - string-length(translate($value, ';, ', '')) + 1" />
          <xsl:variable name="power">
            <xsl:call-template name="pow">
              <xsl:with-param name="pBase" select="2"/>
              <xsl:with-param name="pPower" select="$count"/>
            </xsl:call-template>
          </xsl:variable>
          <xsl:variable name="integer-power" select="floor($power)"/>
          <xsl:value-of select="$integer-power - 1"/>
        </xsl:variable>
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
      <xsl:call-template name="port">
        <xsl:with-param name="id" select="@id"/>
        <xsl:with-param name="explicitInputPorts" select="$explicitInputPorts"/>
        <xsl:with-param name="explicitOutputPorts" select="$explicitOutputPorts"/>
        <xsl:with-param name="implicitInputPorts" select="$implicitInputPorts"/>
        <xsl:with-param name="implicitOutputPorts" select="$implicitOutputPorts"/>
        <xsl:with-param name="controlPorts" select="$controlPorts"/>
        <xsl:with-param name="commandPorts" select="$commandPorts"/>
      </xsl:call-template>
    </xsl:template>
