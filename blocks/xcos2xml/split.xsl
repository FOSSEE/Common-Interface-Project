    <xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
    <xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
    <xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
    <xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />

    <xsl:key name="k-control" match="ControlPort" use="@parent" />
    <xsl:key name="k-command" match="CommandPort" use="@parent" />
    <xsl:key name="k-commandsrclink" match="CommandControlLink" use="@source" />
    <xsl:key name="k-commandtgtlink" match="CommandControlLink" use="@target" />

    <xsl:key name="k-implicitinput" match="ImplicitInputPort | ImplicitOutputPort" use="@parent" />
    <xsl:key name="k-implicitsrclink" match="ImplicitLink" use="@source | @target" />

    <xsl:template name="links">
      <xsl:param name="targetonelink" />
      <xsl:param name="sourceonelink" />
      <xsl:param name="sourcetwolink" />
      <xsl:param name="x" />
      <xsl:param name="y" />

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
        <mxGeometry relative="1" as="geometry">
          <Array as="points">
            <xsl:for-each select="$targetonelink/mxGeometry/Array/mxPoint">
              <xsl:copy-of select="." />
            </xsl:for-each>
            <xsl:for-each select="$sourceonelink/mxGeometry/Array/mxPoint">
              <xsl:copy-of select="." />
            </xsl:for-each>
          </Array>
        </mxGeometry>
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </xsl:element>

      <xsl:element name="mxCell">
        <xsl:attribute name="id">
          <xsl:value-of select="generate-id($targetonelink)" />
        </xsl:attribute>
        <xsl:attribute name="edge">1</xsl:attribute>
        <xsl:attribute name="sourceVertex">
          <xsl:value-of select="$sourcetwolink/@target" />
        </xsl:attribute>
        <xsl:attribute name="targetVertex">
          <xsl:value-of select="$newidone" />
        </xsl:attribute>
        <xsl:attribute name="tarx">
          <xsl:value-of select="$x" />
        </xsl:attribute>
        <xsl:attribute name="tary">
          <xsl:value-of select="$y" />
        </xsl:attribute>
        <xsl:attribute name="CellType">Unknown</xsl:attribute>
        <mxGeometry relative="1" as="geometry">
          <mxPoint>
            <xsl:attribute name="x">
              <xsl:value-of select="$x" />
            </xsl:attribute>
            <xsl:attribute name="y">
              <xsl:value-of select="$y" />
            </xsl:attribute>
            <xsl:attribute name="as">targetPoint</xsl:attribute>
          </mxPoint>
          <Array as="points">
            <xsl:for-each select="$sourcetwolink/mxGeometry/Array/mxPoint">
              <xsl:copy-of select="." />
            </xsl:for-each>
          </Array>
        </mxGeometry>
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
      </xsl:element>
    </xsl:template>

    <xsl:template match="SplitBlock">
      <xsl:variable name="InputPort" select="key('k-input', @id)" />
      <xsl:variable name="OutputPort" select="key('k-output', @id)" />

      <xsl:variable name="ControlPort" select="key('k-control', @id)" />
      <xsl:variable name="CommandPort" select="key('k-command', @id)" />

      <xsl:variable name="ImplicitPort" select="key('k-implicitinput', @id)" />

      <xsl:variable name="geometry" select="mxGeometry" />
      <xsl:variable name="x" select="$geometry/@x" />
      <xsl:variable name="y" select="$geometry/@y" />

      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:variable name="targetoneid" select="$InputPort[position()=1]/@id" />
          <xsl:variable name="sourceoneid" select="$OutputPort[position()=1]/@id" />
          <xsl:variable name="sourcetwoid" select="$OutputPort[position()=2]/@id" />
          <xsl:variable name="targetonelink" select="key('k-tgtlink', $targetoneid)" />
          <xsl:variable name="sourceonelink" select="key('k-srclink', $sourceoneid)" />
          <xsl:variable name="sourcetwolink" select="key('k-srclink', $sourcetwoid)" />

          <xsl:call-template name="links">
            <xsl:with-param name="targetonelink" select="$targetonelink"/>
            <xsl:with-param name="sourceonelink" select="$sourceonelink"/>
            <xsl:with-param name="sourcetwolink" select="$sourcetwolink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
          </xsl:call-template>
        </xsl:when>

        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:variable name="targetcommandoneid" select="$ControlPort[position()=1]/@id" />
          <xsl:variable name="sourcecommandoneid" select="$CommandPort[position()=1]/@id" />
          <xsl:variable name="sourcecommandtwoid" select="$CommandPort[position()=2]/@id" />
          <xsl:variable name="targetcommandonelink" select="key('k-commandtgtlink', $targetcommandoneid)" />
          <xsl:variable name="sourcecommandonelink" select="key('k-commandsrclink', $sourcecommandoneid)" />
          <xsl:variable name="sourcecommandtwolink" select="key('k-commandsrclink', $sourcecommandtwoid)" />

          <xsl:call-template name="links">
            <xsl:with-param name="targetonelink" select="$targetcommandonelink"/>
            <xsl:with-param name="sourceonelink" select="$sourcecommandonelink"/>
            <xsl:with-param name="sourcetwolink" select="$sourcecommandtwolink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
          </xsl:call-template>
        </xsl:when>

        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:variable name="targetimplicitoneid" select="$ImplicitPort[position()=1]/@id" />
          <xsl:variable name="sourceimplicitoneid" select="$ImplicitPort[position()=2]/@id" />
          <xsl:variable name="sourceimplicittwoid" select="$ImplicitPort[position()=3]/@id" />
          <xsl:variable name="targetimplicitonelink" select="key('k-implicitsrclink', $targetimplicitoneid)" />
          <xsl:variable name="sourceimplicitonelink" select="key('k-implicitsrclink', $sourceimplicitoneid)" />
          <xsl:variable name="sourceimplicittwolink" select="key('k-implicitsrclink', $sourceimplicittwoid)" />

          <xsl:call-template name="links">
            <xsl:with-param name="targetonelink" select="$targetimplicitonelink"/>
            <xsl:with-param name="sourceonelink" select="$sourceimplicitonelink"/>
            <xsl:with-param name="sourcetwolink" select="$sourceimplicittwolink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
          </xsl:call-template>
        </xsl:when>
      </xsl:choose>
    </xsl:template>

    <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
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

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort | ImplicitInputPort | ImplicitOutputPort | ControlPort | CommandPort">
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
