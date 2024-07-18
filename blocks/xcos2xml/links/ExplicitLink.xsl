<xsl:template match="ExplicitLink">
      <xsl:variable name="sourceId" select="@source" />
      <xsl:variable name="sourceParentId" select="//*[@id = $sourceId]/@parent" />
      <xsl:variable name="sourceParentName" select="name(//*[@id = $sourceParentId])" />
      <xsl:variable name="targetId" select="@target" />
      <xsl:variable name="targetParentId" select="//*[@id = $targetId]/@parent" />
      <xsl:variable name="targetParentName" select="name(//*[@id = $targetParentId])" />
      <xsl:if test="$sourceParentName != 'SplitBlock' and $targetParentName != 'SplitBlock'">
        <xsl:element name="mxCell">
          <xsl:attribute name="id">
            <xsl:value-of select="@id" />
          </xsl:attribute>
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
          <!-- <xsl:apply-templates select="node()"/> -->
          <!-- <xsl:apply-templates /> -->
          <mxGeometry relative="1" as="geometry" />
          <Object as="parameter_values"/>
          <Object as="displayProperties"/>
        </xsl:element>
      </xsl:if>
    </xsl:template>