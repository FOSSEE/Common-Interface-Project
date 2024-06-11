    <xsl:template match="ControlPort">
      <xsl:element name="mxCell">
        <xsl:attribute name="style">
          <xsl:value-of select="@style" />
        </xsl:attribute>
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="vertex">1</xsl:attribute>
        <xsl:attribute name="CellType">Pin</xsl:attribute>
        <xsl:attribute name="ParentComponent">
          <xsl:value-of select="@parent" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <mxGeometry x="0.5" width="8" height="8" relative="1" as="geometry">
          <mxPoint x="-4" y="-8" as="offset"/>
        </mxGeometry>
        <xsl:apply-templates select="node()"/>
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </xsl:element>
    </xsl:template>
