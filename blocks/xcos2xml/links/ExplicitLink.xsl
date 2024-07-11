    <xsl:key name="k-explicitin" match="ExplicitInputPort" use="@id" />
<xsl:key name="k-explicitout" match="ExplicitOutputPort" use="@id" />
<xsl:key name="k-splitblock" match="SplitBlock" use="@id" />


    <xsl:template match="ExplicitLink">
    <xsl:choose>
    <xsl:when test="not(key('k-explicitout', @source) | key('k-explicitin', @target))">
      <!-- If the condition is not met, apply templates to process the element -->
      
    <!-- <xsl:for-each select="key('k-explicitout', @source) | key('k-explicitin', @target)">
    <new>
    <xsl:attribute name="test1">
          <xsl:value-of select="name(.)"/>
        </xsl:attribute>
        <xsl:attribute name="test11">
          <xsl:value-of select="@id"/>
        </xsl:attribute>
      <xsl:for-each select="key('k-splitblock', @parent)">
      
        <xsl:attribute name="test">
          <xsl:value-of select="name(.)"/>
        </xsl:attribute>
        <xsl:attribute name="test12">
          <xsl:value-of select="@id"/>
        </xsl:attribute>
     

      </xsl:for-each>
      </new>
      </xsl:for-each> -->

    <!-- <xsl:variable name="sourceId" select="@source"/>
    <xsl:variable name="portId" select="//*[@id=$sourceId]"/>
    <xsl:variable name="parentId" select="$portId/@parent"/>
    <xsl:variable name="parentElem" select="//*[@id=$parentId]"/> -->


    <!-- <BlockName>

      <xsl:value-of select="name($parentElem)"/>
    </BlockName> -->
    <!-- <xsl:if test="name($parentElem) != 'SplitBlock'"> -->

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
      <xsl:apply-templates select="."/>
    </xsl:when>
    <!-- Add additional conditions or behavior as needed -->
  </xsl:choose>
      <!-- </xsl:if> -->
    </xsl:template>
