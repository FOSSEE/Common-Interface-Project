    <xsl:template match="CommandControlLink">
      <xsl:element name="mxCell">
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="edge">1</xsl:attribute>
        <xsl:attribute name="sourceVertex">
          <xsl:value-of select="@source" />
        </xsl:attribute>
        <xsl:attribute name="targetVertex">
          <xsl:value-of select="@target" />
        </xsl:attribute>
        <xsl:attribute name="node">.null</xsl:attribute>
        <xsl:attribute name="CellType">Unknown</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <xsl:apply-templates />
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </xsl:element>
    </xsl:template>
