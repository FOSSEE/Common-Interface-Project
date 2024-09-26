<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

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

    <xsl:template match="SplitBlock[position() = 1]"> <!-- Only process the first SplitBlock -->
        <xsl:variable name="InputPort" select="key('k-input', @id)" />
        <xsl:variable name="OutputPort" select="key('k-output', @id)" />
        <xsl:variable name="InputPorts" select="count($InputPort)" />
        <xsl:variable name="OutputPorts" select="count($OutputPort)" />
        <xsl:variable name="targetoneid" select="$InputPort/@id" />
        <xsl:variable name="sourceoneid" select="$OutputPort/@id" />
        <xsl:variable name="targetonelink" select="key('k-tgtlink', $targetoneid)" />
        <xsl:variable name="sourceonelink" select="key('k-srclink', $sourceoneid)" />

        <xsl:variable name="ControlPort" select="key('k-control', @id)" />
        <xsl:variable name="CommandPort" select="key('k-command', @id)" />
        <xsl:variable name="ControlPorts" select="count($ControlPort)" />
        <xsl:variable name="CommandPorts" select="count($CommandPort)" />
        <xsl:variable name="targetcommandoneid" select="$ControlPort/@id" />
        <xsl:variable name="sourcecommandoneid" select="$CommandPort/@id" />
        <xsl:variable name="targetcommandonelink" select="key('k-commandtgtlink', $targetcommandoneid)" />
        <xsl:variable name="sourcecommandonelink" select="key('k-commandsrclink', $sourcecommandoneid)" />

        <xsl:variable name="ImplicitPort" select="key('k-implicitinput', @id)" />
        <xsl:variable name="ImplicitPorts" select="count($ImplicitPort)" />
        <xsl:variable name="targetimplicitoneid" select="$ImplicitPort[position()=1]/@id" />
        <xsl:variable name="sourceimplicitoneid" select="$ImplicitPort[position()=2]/@id" />
        <xsl:variable name="targetimplicitonelink" select="key('k-implicitsrclink', $targetimplicitoneid)" />
        <xsl:variable name="sourceimplicitonelink" select="key('k-implicitsrclink', $sourceimplicitoneid)" />
        <xsl:variable name="newidone" select="generate-id()" />

        <xsl:variable name="geometry" select="mxGeometry" />
        <xsl:variable name="x" select="$geometry/@x" />
        <xsl:variable name="y" select="$geometry/@y" />

        <xsl:choose>
            <xsl:when test="($InputPorts + $OutputPorts) > 0">
                <xsl:element name="ExplicitLink">
                    <xsl:attribute name="id"><xsl:value-of select="$newidone" /></xsl:attribute>
                    <xsl:attribute name="parent"><xsl:value-of select="@parent" /></xsl:attribute>
                    <xsl:attribute name="source"><xsl:value-of select="$targetonelink/@source" /></xsl:attribute>
                    <xsl:attribute name="target"><xsl:value-of select="$sourceonelink/@target" /></xsl:attribute>
                    <xsl:attribute name="style">ExplicitLink</xsl:attribute>
                    <xsl:attribute name="value"></xsl:attribute>

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
                </xsl:element>

                <xsl:choose>
                    <xsl:when test="$OutputPorts >= 2">
                        <xsl:variable name="OutputtwoPort" select="$OutputPort[position()=2]" />
                        <xsl:variable name="sourcetwoid" select="$OutputtwoPort/@id" />
                        <xsl:variable name="sourcetwolink" select="key('k-srclink', $sourcetwoid)" />
                        <xsl:element name="ExplicitLink">
                            <xsl:attribute name="id"><xsl:value-of select="generate-id($targetonelink)" /></xsl:attribute>
                            <xsl:attribute name="parent"><xsl:value-of select="@parent" /></xsl:attribute>
                            <xsl:attribute name="source"><xsl:value-of select="$sourcetwolink/@target" /></xsl:attribute>
                            <xsl:attribute name="target"><xsl:value-of select="$newidone" /></xsl:attribute>
                            <xsl:attribute name="style">ExplicitLink</xsl:attribute>
                            <xsl:attribute name="value"></xsl:attribute>
                        </xsl:element>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:variable name="InputtwoPort" select="$InputPort[position()=2]" />
                        <xsl:variable name="targettwoid" select="$InputtwoPort/@id" />
                        <xsl:variable name="targettwolink" select="key('k-tgtlink', $targettwoid)" />
                        <xsl:element name="ExplicitLink">
                            <xsl:attribute name="id"><xsl:value-of select="generate-id($sourceonelink)" /></xsl:attribute>
                            <xsl:attribute name="parent"><xsl:value-of select="@parent" /></xsl:attribute>
                            <xsl:attribute name="source"><xsl:value-of select="$targettwolink/@source" /></xsl:attribute>
                            <xsl:attribute name="target"><xsl:value-of select="$newidone" /></xsl:attribute>
                            <xsl:attribute name="style">ExplicitLink</xsl:attribute>
                            <xsl:attribute name="value"></xsl:attribute>
                        </xsl:element>
                    </xsl:otherwise>
                </xsl:choose>
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
        <xsl:variable name="SPLITLINK" select="//SplitBlock[position() = 1]"/>
        <xsl:choose>

        <xsl:when test="$sourceElemId != $SPLITLINK/@id and $targetElemId != $SPLITLINK/@id">
            <!-- Copy the link element and its attributes only if it should not be removed -->
            <xsl:copy>
                <xsl:copy-of select="@*"/>
                <xsl:copy-of select="node()"/>
            </xsl:copy>
        </xsl:when>

    </xsl:choose>
    </xsl:template>

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort | ImplicitInputPort | ImplicitOutputPort | ControlPort | CommandPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $parentId]"/>
      <xsl:variable name="PortId" select="@id"/>

      <xsl:variable name="SPLIT" select="//SplitBlock[position() = 1]"/>
      <xsl:choose>
        <xsl:when test="$parentId != $SPLIT/@id" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
    </xsl:template>


</xsl:stylesheet>
