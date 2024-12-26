    <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
      <mxCell>
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
        <xsl:attribute name="tarx">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='sourcePoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='sourcePoint']/@x" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="tary">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='sourcePoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='sourcePoint']/@y" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="tar2x">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='targetPoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='targetPoint']/@x" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="tar2y">
          <xsl:choose>
            <xsl:when test="mxGeometry/mxPoint[@as='targetPoint']">
              <xsl:value-of select="mxGeometry/mxPoint[@as='targetPoint']/@y" />
            </xsl:when>
            <xsl:otherwise>0</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:attribute name="CellType">Unknown</xsl:attribute>
        <xsl:apply-templates />
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </mxCell>
    </xsl:template>
