    <xsl:template match="*[@interfaceFunctionName = 'SUMMATION']">
    <xsl:variable name="total" select="(*[@as='exprs']/data)" />
    <xsl:variable name="parameters1">
        <xsl:choose>
            <xsl:when test="count($total) = 1">1</xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="(*[@as='exprs']/data[1]/@value)" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:variable>

    <xsl:variable name="parameters2">
        <xsl:choose>
            <xsl:when test="count($total) = 1">
              <xsl:value-of select="(*[@as='exprs']/data[1]/@value)" />
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="(*[@as='exprs']/data[2]/@value)" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:variable>

    <xsl:variable name="parameters3">
        <xsl:choose>
            <xsl:when test="count($total) = 1">0</xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="(*[@as='exprs']/data[3]/@value)" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:variable>

    <!-- <xsl:variable name="total1" select="(*[@as='exprs']/data)" /> -->
    <!-- <xsl:variable name="value">
    <xsl:value-of select="parameter[1]" />
    </xsl:variable> -->

    <xsl:variable name="explicitInputPorts">
         
          <!-- <xsl:variable name="count" select="string-length($parameters2) - string-length(translate($parameters2, ';,', '')) + 1" /> -->
          <xsl:value-of select="string-length($parameters2) - string-length(translate($parameters2, ';,', '')) + 1" />
        </xsl:variable>
        <xsl:variable name="implicitInputPorts">0</xsl:variable>
        <xsl:variable name="explicitOutputPorts">1</xsl:variable>
        <xsl:variable name="implicitOutputPorts">0</xsl:variable>
        <xsl:variable name="controlPorts">0</xsl:variable>
        <xsl:variable name="commandPorts">0</xsl:variable>
        
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
          </xsl:attribute>
          <xsl:attribute name="as">displayProperties</xsl:attribute>
        </Object>
        <Object>
        

              <xsl:attribute name="{concat('p000', '_value')}">
                <xsl:value-of select="$parameters1"/>
              </xsl:attribute>
              <xsl:attribute name="{concat('p001', '_value')}">
                <xsl:value-of select="$parameters2"/>
              </xsl:attribute>
              <xsl:attribute name="{concat('p002', '_value')}">
                <xsl:value-of select="$parameters3"/>
              </xsl:attribute>
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

    
      
    


