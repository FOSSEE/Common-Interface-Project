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
      <!-- <xsl:choose> -->
        <!-- <xsl:when test="name($parentElement) != 'SplitBlock' and name($parentTargetElement) != 'SplitBlock'" > -->
          <!-- <xsl:copy> -->
          
            <!-- <xsl:copy-of select="@*"/> -->
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
          <!-- </xsl:copy> -->
        <!-- </xsl:when> -->

      <!-- </xsl:choose> -->
      </mxCell>
     </xsl:template>
<!-- <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
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
          <mxGeometry relative="1" as="geometry" />
          <Object as="parameter_values"/>
          <Object as="displayProperties"/>
        </xsl:element>
      </xsl:if>
    </xsl:template> -->