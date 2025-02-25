    <xsl:template match="SuperBlock">
      <xsl:variable name="explicitInputPorts" select="count(SuperBlockDiagram/mxGraphModel/root/ExplicitOutBlock)"/>
    <xsl:variable name="implicitInputPorts" select="count(SuperBlockDiagram/mxGraphModel/root/ImplicitOutBlock)"/>
    <xsl:variable name="explicitOutputPorts" select="count(SuperBlockDiagram/mxGraphModel/root/ExplicitInBlock)"/>
    <xsl:variable name="implicitOutputPorts" select="count(SuperBlockDiagram/mxGraphModel/root/ImplicitInBlock)"/>
    <xsl:variable name="controlPorts" select="count(SuperBlockDiagram/mxGraphModel/root/EventInBlock)"/>
    <xsl:variable name="commandPorts" select="count(SuperBlockDiagram/mxGraphModel/root/EventOutBlock)"/>
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
        <xsl:apply-templates select="mxGeometry"/>
        <Object display_parameter="" as="displayProperties"/>
        <Object as="parameter_values"/>
        <xsl:apply-templates select="SuperBlockDiagram/node()"/>
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
