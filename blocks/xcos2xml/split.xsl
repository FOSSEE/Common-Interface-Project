<xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
<xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
<xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
<xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />

    <xsl:template match="SplitBlock">
      <xsl:variable name="InputPorts" select="@inputPorts" />
        <xsl:variable name="OutputPorts" select="@outputPorts" />
        <xsl:variable name="InputPort" select="key('k-input', @id)" />
        <xsl:variable name="OutputPort" select="key('k-output', @id)" />
        <xsl:variable name="targetoneid" select="$InputPort/@id" />
        <xsl:variable name="sourceoneid" select="$OutputPort/@id" />
        <xsl:variable name="targetonelink" select="key('k-tgtlink', $targetoneid)" />
        <xsl:variable name="sourceonelink" select="key('k-srclink', $sourceoneid)" />
        <xsl:variable name="newidone" select="generate-id()" />

          <xsl:element name="mxCell">
            <xsl:attribute name="id">
              <xsl:value-of select="$newidone" />
            </xsl:attribute>
            <xsl:attribute name="edge">1</xsl:attribute>
            <xsl:attribute name="sourceVertex">
              <xsl:value-of select="$targetonelink/@source" />
            </xsl:attribute>
            <xsl:attribute name="targetVertex">
              <xsl:value-of select="$sourceonelink/@target" />
            </xsl:attribute>
            <xsl:attribute name="node">.null</xsl:attribute>
            <xsl:attribute name="CellType">Unknown</xsl:attribute>
            <xsl:attribute name="tarx">0</xsl:attribute>
            <xsl:attribute name="tary">0</xsl:attribute>
            <xsl:apply-templates select="node()"/>
            <xsl:apply-templates />
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <xsl:for-each select="$sourceonelink/mxGeometry/Array/mxPoint">
                  <xsl:copy-of select="." />
                </xsl:for-each>
                <xsl:for-each select="$targetonelink/mxGeometry/Array/mxPoint">
                  <xsl:copy-of select="." />
                </xsl:for-each>
              </Array>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>

        <xsl:choose>
          <xsl:when test="$OutputPorts = 2">
            <xsl:variable name="OutputtwoPort" select="$OutputPort[position()=2]" />
            <xsl:variable name="sourcetwoid" select="$OutputtwoPort/@id" />
            <xsl:variable name="sourcetwolink" select="key('k-srclink', $sourcetwoid)" />
              <xsl:element name="mxCell">
                <xsl:attribute name="id">
                  <xsl:value-of select="generate-id($targetonelink)" />
                </xsl:attribute>
                <xsl:attribute name="edge">1</xsl:attribute>
                <xsl:attribute name="sourceVertex">
                  <xsl:value-of select="$newidone" />
                </xsl:attribute>
                <xsl:attribute name="targetVertex">
                  <xsl:value-of select="$sourcetwolink/@target" />
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
          </xsl:when>

          <xsl:otherwise>
            <xsl:variable name="InputtwoPort" select="$InputPort[position()=2]" />
            <xsl:variable name="targettwoid" select="$InputtwoPort/@id" />
            <xsl:variable name="targettwolink" select="key('k-tgtlink', $targettwoid)" />
              <xsl:element name="mxCell">
                <xsl:attribute name="id">
                  <xsl:value-of select="generate-id($sourceonelink)" />
                </xsl:attribute>
                <xsl:attribute name="edge">1</xsl:attribute>
                <xsl:attribute name="sourceVertex">
                  <xsl:value-of select="$targettwolink/@source" />
                </xsl:attribute>
                <xsl:attribute name="targetVertex">
                  <xsl:value-of select="$newidone" />
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
          </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ExplicitLink">
      <xsl:variable name="sourceId" select="@source"/>
      <xsl:variable name="sourceElement" select="//*[@id = $sourceId]"/>
      <xsl:variable name="sourceElemId" select="$sourceElement/@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $sourceElemId]"/>
      <xsl:variable name="targetId" select="@target"/>
      <xsl:variable name="targetElement" select="//*[@id = $targetId]"/>
      <xsl:variable name="targetElemId" select="$targetElement/@parent"/>
      <xsl:variable name="parentTargetElement" select="//*[@id = $targetElemId]"/>

      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock' and name($parentTargetElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $parentId]"/>
      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>
