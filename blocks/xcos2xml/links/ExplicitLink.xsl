    <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
      <xsl:variable name="sourceId" select="@source"/>
      <xsl:variable name="sourceElement" select="//*[@id = $sourceId]"/>
      <xsl:variable name="sourceElemId" select="$sourceElement/@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $sourceElemId]"/>
      <xsl:variable name="targetId" select="@target"/>
      <xsl:variable name="targetElement" select="//*[@id = $targetId]"/>
      <xsl:variable name="targetElemId" select="$targetElement/@parent"/>
      <xsl:variable name="parentTargetElement" select="//*[@id = $targetElemId]"/>
      <mxCell>
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="edge">1</xsl:attribute>
        <xsl:attribute name="sourceVertex">
          <xsl:value-of select="$sourceId" />
        </xsl:attribute>
        <xsl:attribute name="targetVertex">
          <xsl:value-of select="$targetId" />
        </xsl:attribute>
        <xsl:attribute name="tarx">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='targetPoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='targetPoint']/@x" />
            </xsl:when>
            <xsl:when test="mxGeometry/mxPoint[@as='sourcePoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='sourcePoint']/@x" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="tary">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='targetPoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='targetPoint']/@y" />
            </xsl:when>
            <xsl:when test="mxGeometry/mxPoint[@as='sourcePoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='sourcePoint']/@y" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="CellType">Unknown</xsl:attribute>
        <xsl:copy-of select="node()"/>
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </mxCell>
    </xsl:template>
