    <xsl:template match="*[@interfaceFunctionName = 'CLR']">
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
        <xsl:attribute name="explicitInputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="explicitOutputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitOutputPorts">0</xsl:attribute>
        <xsl:attribute name="controlPorts">0</xsl:attribute>
        <xsl:attribute name="commandPorts">0</xsl:attribute>
        <xsl:attribute name="simulationFunction">
          <xsl:value-of select="@simulationFunctionName" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <Object display_parameter="100,s&lt;SUP&gt;2&lt;/SUP&gt;+ 12*s + 100" as="displayProperties"/>
        <Object p000_value="100" p001_value="s^2 + 12*s + 100" as="parameter_values"/>
      </xsl:element>
    </xsl:template>
