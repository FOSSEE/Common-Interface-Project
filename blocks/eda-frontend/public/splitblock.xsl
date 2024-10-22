<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
    <xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
    <xsl:key name="k-link" match="ExplicitLink" use="@source | @target" />
    <xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
    <xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />

    <xsl:key name="k-control" match="ControlPort" use="@parent" />
    <xsl:key name="k-command" match="CommandPort" use="@parent" />
    <xsl:key name="k-commandlink" match="CommandControlLink" use="@source | @target" />
    <xsl:key name="k-commandsrclink" match="CommandControlLink" use="@source" />
    <xsl:key name="k-commandtgtlink" match="CommandControlLink" use="@target" />

    <xsl:key name="k-implicitinput" match="ImplicitInputPort | ImplicitOutputPort" use="@parent" />
    <xsl:key name="k-implicitlink" match="ImplicitLink" use="@source | @target" />
    <xsl:key name="k-implicitsrclink" match="ImplicitLink" use="@source" />
    <xsl:key name="k-implicittgtlink" match="ImplicitLink" use="@target" />

    <xsl:template name="links">
      <xsl:param name="linktype" />
      <xsl:param name="targetonelink" />
      <xsl:param name="targetonelinksrcortgt" />
      <xsl:param name="sourceonelink" />
      <xsl:param name="sourceonelinksrcortgt" />
      <xsl:param name="sourcetwolink" />
      <xsl:param name="sourcetwolinksrcortgt" />
      <xsl:param name="sourcethreelink" />
      <xsl:param name="sourcethreelinksrcortgt" />
      <xsl:param name="targetonesrcsecondlink" />
      <xsl:param name="targetonetgtsecondlink" />
      <xsl:param name="sourceonesrcsecondlink" />
      <xsl:param name="sourceonetgtsecondlink" />
      <xsl:param name="sourcetwosrcsecondlink" />
      <xsl:param name="sourcetwotgtsecondlink" />
      <xsl:param name="sourcethreesrcsecondlink" />
      <xsl:param name="sourcethreetgtsecondlink" />
      <xsl:param name="x" />
      <xsl:param name="y" />
      <xsl:param name="parent" />

    <!-- generate new primary link one id -->
      <xsl:variable name="newidone" >
        <xsl:choose>
          <xsl:when test="$targetonelink/@id != '' and $sourceonelink/@id != ''">       
            <xsl:value-of select="concat($targetonelink/@id, generate-id())" />
          </xsl:when>
          <xsl:when test="$targetonelink/@id != ''">
            <xsl:value-of select="$targetonelink/@id" />
          </xsl:when>
          <xsl:when test="$sourceonelink/@id != ''">
            <xsl:value-of select="$sourceonelink/@id" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:text>No match found</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

<!-- generate new primary link one -->
        <xsl:if test="$targetonelink/@id != '' and $sourceonelink/@id != ''">

      <xsl:element name="{$linktype}">
        <xsl:attribute name="id">
          <xsl:value-of select="$newidone" />
        </xsl:attribute>
        <xsl:attribute name="parent">
          <xsl:value-of select="$parent" />
        </xsl:attribute>
        <xsl:attribute name="source">
          <xsl:value-of select="$targetonelinksrcortgt" /> <!-- removed by suchita $targetonelink/@source-->
        </xsl:attribute>
        <xsl:attribute name="target">
          <xsl:value-of select="$sourceonelinksrcortgt" /> <!-- removed by suchita sourceonelink/@target-->
        </xsl:attribute>
        <xsl:attribute name="style">
          <xsl:value-of select="$linktype" />
        </xsl:attribute>
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
          <xsl:for-each select="$targetonelink/mxGeometry/mxPoint">
            <xsl:copy>
              <xsl:copy-of select="@*"/>
            </xsl:copy>
          </xsl:for-each>
        </mxGeometry>
      </xsl:element>
      </xsl:if>

      <!-- generate new primary link two id -->
      <xsl:variable name="newidtwo" >
        <xsl:choose>
          <xsl:when test="($targetonelink/@id != '' or $sourceonelink/@id != '') and $sourcetwolink/@id != ''">       
            <xsl:value-of select="concat($sourcetwolink/@id, generate-id($sourcetwolink))" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:text>No match found</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

      <xsl:variable name="newidthree" >
        <xsl:choose>
          <xsl:when test="$targetonelink/@id != '' and $sourceonelink/@id != ''">       
            <xsl:value-of select="$newidone" />
          </xsl:when>
          <xsl:when test="$targetonelink/@id != ''">
            <xsl:value-of select="$targetonelinksrcortgt" />
          </xsl:when>
          <xsl:when test="$sourceonelink/@id != ''">
            <xsl:value-of select="$sourceonelinksrcortgt" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:text>No match found</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

      <xsl:variable name="newidfour" >
        <xsl:choose>
          <xsl:when test="$targetonelink/@id != '' and $sourceonelink/@id != ''">       
            <xsl:value-of select="$newidone" />
          </xsl:when>
          
          <xsl:otherwise>
            <xsl:value-of select="$newidtwo" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

      <!-- generate new primary link two -->
      <xsl:if test="$newidthree != 'No match found' and $sourcetwolink/@id != ''">
      <xsl:element name="{$linktype}">
        <xsl:attribute name="id">
          <xsl:value-of select="$newidtwo" />
        </xsl:attribute>
        <xsl:attribute name="parent">
          <xsl:value-of select="$parent" />
        </xsl:attribute>
        <xsl:attribute name="source">
          <xsl:value-of select="$newidthree" />
        </xsl:attribute>
        <xsl:attribute name="target">
          <xsl:value-of select="$sourcetwolinksrcortgt" />
        </xsl:attribute>
        <xsl:attribute name="style">
          <xsl:value-of select="$linktype" />
        </xsl:attribute>
        <xsl:attribute name="value"></xsl:attribute>
        <mxGeometry relative="1" as="geometry">
          <mxPoint>
            <xsl:attribute name="x">
              <xsl:value-of select="$x" />
            </xsl:attribute>
            <xsl:attribute name="y">
              <xsl:value-of select="$y" />
            </xsl:attribute>
            <xsl:attribute name="as">sourcePoint</xsl:attribute>
          </mxPoint>
          <Array as="points">
            <xsl:for-each select="$sourcetwolink/mxGeometry/Array/mxPoint">
              <xsl:copy-of select="." />
            </xsl:for-each>
          </Array>
        </mxGeometry>
      </xsl:element>
      </xsl:if>
      <!-- change source or target of secondary link -->
      <!-- foreach loop, link copy, source change -->
      <xsl:for-each select="$targetonesrcsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="source">
            <xsl:value-of select="$newidfour" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
      <xsl:for-each select="$targetonetgtsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="target">
            <xsl:value-of select="$newidfour" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
      <xsl:for-each select="$sourceonesrcsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="source">
            <xsl:value-of select="$newidfour" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
      <xsl:for-each select="$sourceonetgtsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="target">
            <xsl:value-of select="$newidfour" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
      <xsl:for-each select="$sourcetwosrcsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="source">
            <xsl:value-of select="$newidtwo" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
      <xsl:for-each select="$sourcetwotgtsecondlink">
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="target">
            <xsl:value-of select="$newidtwo" />
          </xsl:attribute>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:for-each>
    </xsl:template>

    <xsl:template match="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]">
      <xsl:variable name="InputPort" select="key('k-input', @id)" />
      <xsl:variable name="OutputPort" select="key('k-output', @id)" />

      <xsl:variable name="ControlPort" select="key('k-control', @id)" />
      <xsl:variable name="CommandPort" select="key('k-command', @id)" />

      <xsl:variable name="ImplicitPort" select="key('k-implicitinput', @id)" />

      <xsl:variable name="geometry" select="mxGeometry" />
      <xsl:variable name="x" select="$geometry/@x" />
      <xsl:variable name="y" select="$geometry/@y" />
      <xsl:variable name="parent" select="@parent" />

      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:variable name="linktype">ExplicitLink</xsl:variable>
          <xsl:variable name="targetoneid" select="$InputPort[position()=1]/@id" />
          <xsl:variable name="sourceoneid" select="$OutputPort[position()=1]/@id" />
          <xsl:variable name="sourcetwoid" select="$OutputPort[position()=2]/@id" />
          <xsl:variable name="sourcethreeid" select="$OutputPort[position()=3]/@id" />
          <xsl:variable name="targetonelink" select="key('k-link', $targetoneid)" />
          <xsl:variable name="sourceonelink" select="key('k-link', $sourceoneid)" />
          <xsl:variable name="sourcetwolink" select="key('k-link', $sourcetwoid)" />
          <xsl:variable name="sourcethreelink" select="key('k-link', $sourcethreeid)" />
          <xsl:variable name="targetonesrcsecondlink" select="key('k-srclink', $targetonelink/@id)" />
          <xsl:variable name="targetonetgtsecondlink" select="key('k-tgtlink', $targetonelink/@id)" />
          <xsl:variable name="sourceonesrcsecondlink" select="key('k-srclink', $sourceonelink/@id)" />
          <xsl:variable name="sourceonetgtsecondlink" select="key('k-tgtlink', $sourceonelink/@id)" />
          <xsl:variable name="sourcetwosrcsecondlink" select="key('k-srclink', $sourcetwolink/@id)" />
          <xsl:variable name="sourcetwotgtsecondlink" select="key('k-tgtlink', $sourcetwolink/@id)" />
          <xsl:variable name="sourcethreesrcsecondlink" select="key('k-srclink', $sourcethreelink/@id)" />
          <xsl:variable name="sourcethreetgtsecondlink" select="key('k-tgtlink', $sourcethreelink/@id)" />

          <xsl:call-template name="links">
            <xsl:with-param name="linktype" select="$linktype"/>
            <xsl:with-param name="targetonelink" select="$targetonelink"/>
            <xsl:with-param name="targetonelinksrcortgt" select="$targetonelink/@source"/>
            <xsl:with-param name="sourceonelink" select="$sourceonelink"/>
            <xsl:with-param name="sourceonelinksrcortgt" select="$sourceonelink/@target"/>
            <xsl:with-param name="sourcetwolink" select="$sourcetwolink"/>
            <xsl:with-param name="sourcetwolinksrcortgt" select="$sourcetwolink/@target"/>
            <xsl:with-param name="sourcethreelink" select="$sourcethreelink"/>
            <xsl:with-param name="sourcethreelinksrcortgt" select="$sourcethreelink/@target"/>
            <xsl:with-param name="targetonesrcsecondlink" select="$targetonesrcsecondlink"/>
             <xsl:with-param name="targetonetgtsecondlink" select="$targetonetgtsecondlink"/>
            <xsl:with-param name="sourceonesrcsecondlink" select="$sourceonesrcsecondlink"/>
            <xsl:with-param name="sourceonetgtsecondlink" select="$sourceonetgtsecondlink"/>
            <xsl:with-param name="sourcetwosrcsecondlink" select="$sourcetwosrcsecondlink"/>
            <xsl:with-param name="sourcetwotgtsecondlink" select="$sourcetwotgtsecondlink"/>
            <xsl:with-param name="sourcethreesrcsecondlink" select="$sourcethreesrcsecondlink"/>
            <xsl:with-param name="sourcethreetgtsecondlink" select="$sourcethreetgtsecondlink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
            <xsl:with-param name="parent" select="$parent"/>
          </xsl:call-template>
        </xsl:when>

        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:variable name="linktype">CommandControlLink</xsl:variable>
          <xsl:variable name="targetcommandoneid" select="$ControlPort[position()=1]/@id" />
          <xsl:variable name="sourcecommandoneid" select="$CommandPort[position()=1]/@id" />
          <xsl:variable name="sourcecommandtwoid" select="$CommandPort[position()=2]/@id" />
          <xsl:variable name="sourcecommandthreeid" select="$CommandPort[position()=3]/@id" />
          <xsl:variable name="targetcommandonelink" select="key('k-commandlink', $targetcommandoneid)" />
          <xsl:variable name="sourcecommandonelink" select="key('k-commandlink', $sourcecommandoneid)" />
          <xsl:variable name="sourcecommandtwolink" select="key('k-commandlink', $sourcecommandtwoid)" />
          <xsl:variable name="sourcecommandthreelink" select="key('k-commandlink', $sourcecommandthreeid)" />
          <xsl:variable name="targetonesrcsecondlink" select="key('k-commandsrclink', $targetcommandonelink/@id)" />
          <xsl:variable name="targetonetgtsecondlink" select="key('k-commandtgtlink', $targetcommandonelink/@id)" />
          <xsl:variable name="sourceonesrcsecondlink" select="key('k-commandsrclink', $sourcecommandonelink/@id)" />
          <xsl:variable name="sourceonetgtsecondlink" select="key('k-commandtgtlink', $sourcecommandonelink/@id)" />
          <xsl:variable name="sourcetwosrcsecondlink" select="key('k-commandsrclink', $sourcecommandtwolink/@id)" />
          <xsl:variable name="sourcetwotgtsecondlink" select="key('k-commandtgtlink', $sourcecommandtwolink/@id)" />
          <xsl:variable name="sourcethreesrcsecondlink" select="key('k-commandsrclink', $sourcecommandthreelink/@id)" />
          <xsl:variable name="sourcethreetgtsecondlink" select="key('k-commandtgtlink', $sourcecommandthreelink/@id)" />

          <xsl:call-template name="links">
            <xsl:with-param name="linktype" select="$linktype"/>
            <xsl:with-param name="targetonelink" select="$targetcommandonelink"/>
            <xsl:with-param name="targetonelinksrcortgt" select="$targetcommandonelink/@source"/>
            <xsl:with-param name="sourceonelink" select="$sourcecommandonelink"/>
            <xsl:with-param name="sourceonelinksrcortgt" select="$sourcecommandonelink/@target"/>
            <xsl:with-param name="sourcetwolink" select="$sourcecommandtwolink"/>
            <xsl:with-param name="sourcetwolinksrcortgt" select="$sourcecommandtwolink/@target"/>
            <xsl:with-param name="sourcethreelink" select="$sourcecommandthreelink"/>
            <xsl:with-param name="sourcethreelinksrcortgt" select="$sourcecommandthreelink/@target"/>
            <xsl:with-param name="targetonesrcsecondlink" select="$targetonesrcsecondlink"/>
            <xsl:with-param name="targetonetgtsecondlink" select="$targetonetgtsecondlink"/>
            <xsl:with-param name="sourceonesrcsecondlink" select="$sourceonesrcsecondlink"/>
            <xsl:with-param name="sourceonetgtsecondlink" select="$sourceonetgtsecondlink"/>
            <xsl:with-param name="sourcetwosrcsecondlink" select="$sourcetwosrcsecondlink"/>
            <xsl:with-param name="sourcetwotgtsecondlink" select="$sourcetwotgtsecondlink"/>
            <xsl:with-param name="sourcethreesrcsecondlink" select="$sourcethreesrcsecondlink"/>
            <xsl:with-param name="sourcethreetgtsecondlink" select="$sourcethreetgtsecondlink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
            <xsl:with-param name="parent" select="$parent"/>
          </xsl:call-template>
        </xsl:when>

        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:variable name="linktype">ImplicitLink</xsl:variable>
          <xsl:variable name="targetimplicitoneid" select="$ImplicitPort[position()=1]/@id" />
          <xsl:variable name="sourceimplicitoneid" select="$ImplicitPort[position()=2]/@id" />
          <xsl:variable name="sourceimplicittwoid" select="$ImplicitPort[position()=3]/@id" />
          <xsl:variable name="sourceimplicitthreeid" select="$ImplicitPort[position()=4]/@id" />
          <xsl:variable name="targetimplicitonelink" select="key('k-implicitlink', $targetimplicitoneid)" />
          <xsl:variable name="sourceimplicitonelink" select="key('k-implicitlink', $sourceimplicitoneid)" />
          <xsl:variable name="sourceimplicittwolink" select="key('k-implicitlink', $sourceimplicittwoid)" />
          <xsl:variable name="sourceimplicitthreelink" select="key('k-implicitlink', $sourceimplicitthreeid)" />
          <xsl:variable name="targetonesrcsecondlink" select="key('k-implicitsrclink', $targetimplicitonelink/@id)" />
          <xsl:variable name="targetonetgtsecondlink" select="key('k-implicittgtlink', $targetimplicitonelink/@id)" />
          <xsl:variable name="sourceonesrcsecondlink" select="key('k-implicitsrclink', $sourceimplicitonelink/@id)" />
          <xsl:variable name="sourceonetgtsecondlink" select="key('k-implicittgtlink', $sourceimplicitonelink/@id)" />
          <xsl:variable name="sourcetwosrcsecondlink" select="key('k-implicitsrclink', $sourceimplicittwolink/@id)" />
          <xsl:variable name="sourcetwotgtsecondlink" select="key('k-implicittgtlink', $sourceimplicittwolink/@id)" />
          <xsl:variable name="sourcethreesrcsecondlink" select="key('k-implicitsrclink', $sourceimplicitthreelink/@id)" />
          <xsl:variable name="sourcethreetgtsecondlink" select="key('k-implicittgtlink', $sourceimplicitthreelink/@id)" />
          <xsl:variable name="targetonelinksort" >
            <xsl:choose>
              <xsl:when test="$targetimplicitoneid = $targetimplicitonelink/@source">
                <xsl:value-of select="$targetimplicitonelink/@target"/>
              </xsl:when>
              <xsl:when test="$targetimplicitoneid = $targetimplicitonelink/@target">
                <xsl:value-of select="$targetimplicitonelink/@source"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>No match found</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <xsl:variable name="sourceonelinksort" >
            <xsl:choose>
              <xsl:when test="$sourceimplicitoneid = $sourceimplicitonelink/@source">
                <xsl:value-of select="$sourceimplicitonelink/@target"/>
              </xsl:when>
              <xsl:when test="$sourceimplicitoneid = $sourceimplicitonelink/@target">
                <xsl:value-of select="$sourceimplicitonelink/@source"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>No match found</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <xsl:variable name="sourcetwolinksort" >
            <xsl:choose>
              <xsl:when test="$sourceimplicittwoid = $sourceimplicittwolink/@source">
                <xsl:value-of select="$sourceimplicittwolink/@target"/>
              </xsl:when>
              <xsl:when test="$sourceimplicittwoid = $sourceimplicittwolink/@target">
                <xsl:value-of select="$sourceimplicittwolink/@source"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>No match found</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <xsl:variable name="sourcethreelinksort" >
            <xsl:choose>
              <xsl:when test="$sourceimplicitthreeid = $sourceimplicitthreelink/@source">
                <xsl:value-of select="$sourceimplicitthreelink/@target"/>
              </xsl:when>
              <xsl:when test="$sourceimplicitthreeid = $sourceimplicitthreelink/@target">
                <xsl:value-of select="$sourceimplicitthreelink/@source"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>No match found</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>
          
          <xsl:call-template name="links">
            <xsl:with-param name="linktype" select="$linktype"/>
            <xsl:with-param name="targetonelink" select="$targetimplicitonelink"/>
            <xsl:with-param name="targetonelinksrcortgt" select="$targetonelinksort"/>
            <xsl:with-param name="sourceonelink" select="$sourceimplicitonelink"/>
            <xsl:with-param name="sourceonelinksrcortgt" select="$sourceonelinksort"/>
            <xsl:with-param name="sourcetwolink" select="$sourceimplicittwolink"/>
            <xsl:with-param name="sourcetwolinksrcortgt" select="$sourcetwolinksort"/>
            <xsl:with-param name="sourcethreelink" select="$sourceimplicitthreelink"/>
            <xsl:with-param name="sourcethreelinksrcortgt" select="$sourcethreelinksort"/>
            <xsl:with-param name="targetonesrcsecondlink" select="$targetonesrcsecondlink"/>
            <xsl:with-param name="targetonetgtsecondlink" select="$targetonetgtsecondlink"/>
            <xsl:with-param name="sourceonesrcsecondlink" select="$sourceonesrcsecondlink"/>
            <xsl:with-param name="sourceonetgtsecondlink" select="$sourceonetgtsecondlink"/>
            <xsl:with-param name="sourcetwosrcsecondlink" select="$sourcetwosrcsecondlink"/>
            <xsl:with-param name="sourcetwotgtsecondlink" select="$sourcetwotgtsecondlink"/>
            <xsl:with-param name="sourcethreesrcsecondlink" select="$sourcethreesrcsecondlink"/>
            <xsl:with-param name="sourcethreetgtsecondlink" select="$sourcethreetgtsecondlink"/>
            <xsl:with-param name="x" select="$x"/>
            <xsl:with-param name="y" select="$y"/>
            <xsl:with-param name="parent" select="$parent"/>
          </xsl:call-template>
        </xsl:when>
      </xsl:choose>
    </xsl:template>

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort | ImplicitInputPort | ImplicitOutputPort | ControlPort | CommandPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="SPLIT" select="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]"/>

      <xsl:if test="$parentId != $SPLIT/@id" >
        <xsl:copy>
          <xsl:copy-of select="@*"/>
          <xsl:copy-of select="node()"/>
        </xsl:copy>
      </xsl:if>
    </xsl:template>

    <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
      <xsl:variable name="sourceId" select="@source"/>
      <xsl:variable name="sourceElement" select="//*[@id = $sourceId]"/>
      <xsl:variable name="sourceElemId" select="$sourceElement/@parent"/>
      <xsl:variable name="targetId" select="@target"/>
      <xsl:variable name="targetElement" select="//*[@id = $targetId]"/>
      <xsl:variable name="targetElemId" select="$targetElement/@parent"/>
      <xsl:variable name="SPLITID" select="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]/@id"/>

      <xsl:if test="$sourceElemId != $SPLITID and $targetElemId != $SPLITID">
        <xsl:variable name="tgtsrcid" select="//*[@id = $targetElement/@source]/@parent"/>
        <xsl:variable name="srctgtid" select="//*[@id = $sourceElement/@target]/@parent"/>
        <xsl:variable name="srcsrcid" select="//*[@id = $sourceElement/@source]/@parent"/>
        <xsl:variable name="tgttgtid" select="//*[@id = $targetElement/@target]/@parent"/>
        
        <xsl:if test="(string-length($tgtsrcid) = 0 or $tgtsrcid != $SPLITID) and (string-length($tgttgtid) = 0 or $tgttgtid != $SPLITID) and (string-length($srctgtid) = 0 or $srctgtid != $SPLITID) and (string-length($srcsrcid) = 0 or $srcsrcid != $SPLITID)">
          <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:copy-of select="node()"/>
          </xsl:copy>
        </xsl:if>
      </xsl:if>
    </xsl:template>
</xsl:stylesheet>
