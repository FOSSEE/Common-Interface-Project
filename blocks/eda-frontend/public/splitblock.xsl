<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:ext="http://exslt.org/common"
  exclude-result-prefixes="xsl ext">

  <!-- copy all other nodes {{{1 -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}1 -->

  <!-- keys {{{1 -->
  <xsl:key name="k-explicitinput" match="ExplicitInputPort" use="@parent" />
  <xsl:key name="k-explicitoutput" match="ExplicitOutputPort" use="@parent" />

  <xsl:key name="k-control" match="ControlPort" use="@parent" />
  <xsl:key name="k-command" match="CommandPort" use="@parent" />

  <xsl:key name="k-implicit" match="ImplicitInputPort | ImplicitOutputPort" use="@parent" />

  <xsl:key name="k-block" match="AfficheBlock | BasicBlock | BigSom | EventInBlock | EventOutBlock | ExplicitInBlock | ExplicitOutBlock | GroundBlock | ImplicitInBlock | ImplicitOutBlock | Product | RoundBlock | SplitBlock | Summation | SuperBlock | TextBlock | VoltageSensorBlock" use="@id" />
  <xsl:key name="k-port" match="ExplicitInputPort | ExplicitOutputPort | ControlPort | CommandPort | ImplicitInputPort | ImplicitOutputPort" use="@id" />
  <xsl:key name="k-portorlink" match="ExplicitInputPort | ExplicitOutputPort | ExplicitLink | ControlPort | CommandPort | CommandControlLink | ImplicitInputPort | ImplicitOutputPort | ImplicitLink" use="@id" />
  <xsl:key name="k-link" match="ExplicitLink | CommandControlLink | ImplicitLink" use="@source | @target" />
  <xsl:key name="k-linksrc" match="ExplicitLink | CommandControlLink | ImplicitLink" use="@source" />
  <xsl:key name="k-linktgt" match="ExplicitLink | CommandControlLink | ImplicitLink" use="@target" />
  <!-- }}}1 -->

  <!-- links template {{{1 -->
  <xsl:template name="links">

    <!-- links template parameters {{{ -->
    <xsl:param name="x" />
    <xsl:param name="y" />
    <xsl:param name="parent" />

    <xsl:param name="linktype" />

    <xsl:param name="tgtonelink" />
    <xsl:param name="tgtonelinkwaypoints" />
    <xsl:param name="tgtoneotherportid" />
    <xsl:param name="tgtoneotherblockx" />
    <xsl:param name="tgtoneotherblocky" />
    <xsl:param name="tgtonesrcsecondlink" />
    <xsl:param name="tgtonetgtsecondlink" />

    <xsl:param name="srconelink" />
    <xsl:param name="srconelinkwaypoints" />
    <xsl:param name="srconeotherportid" />
    <xsl:param name="srconeotherblockx" />
    <xsl:param name="srconeotherblocky" />
    <xsl:param name="srconesrcsecondlink" />
    <xsl:param name="srconetgtsecondlink" />

    <xsl:param name="srctwolink" />
    <xsl:param name="srctwolinkwaypoints" />
    <xsl:param name="srctwootherportid" />
    <xsl:param name="srctwootherblockx" />
    <xsl:param name="srctwootherblocky" />
    <xsl:param name="srctwosrcsecondlink" />
    <xsl:param name="srctwotgtsecondlink" />

    <xsl:param name="srcthreelink" />
    <xsl:param name="srcthreelinkwaypoints" />
    <xsl:param name="srcthreeotherportid" />
    <xsl:param name="srcthreeotherblockx" />
    <xsl:param name="srcthreeotherblocky" />
    <xsl:param name="srcthreesrcsecondlink" />
    <xsl:param name="srcthreetgtsecondlink" />
    <!-- }}} -->

    <!-- generate new primary link one id {{{ -->
    <xsl:variable name="newidone">
      <xsl:choose>
        <xsl:when test="$tgtonelink/@id != '' and $srconelink/@id != ''">
          <xsl:value-of select="concat($tgtonelink/@id, generate-id())" />
        </xsl:when>
        <xsl:when test="$tgtonelink/@id != ''">
          <xsl:value-of select="$tgtonelink/@id" />
        </xsl:when>
        <xsl:when test="$srconelink/@id != ''">
          <xsl:value-of select="$srconelink/@id" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- generate new primary link one {{{ -->
    <xsl:if test="$tgtonelink/@id != '' and $srconelink/@id != ''">
      <xsl:element name="{$linktype}">
        <xsl:attribute name="id">
          <xsl:value-of select="$newidone" />
        </xsl:attribute>
        <xsl:attribute name="parent">
          <xsl:value-of select="$parent" />
        </xsl:attribute>
        <xsl:attribute name="source">
          <xsl:value-of select="$tgtoneotherportid" />
        </xsl:attribute>
        <xsl:attribute name="target">
          <xsl:value-of select="$srconeotherportid" />
        </xsl:attribute>
        <xsl:attribute name="style">
          <xsl:value-of select="$linktype" />
        </xsl:attribute>
        <xsl:attribute name="value"></xsl:attribute>
        <mxGeometry relative="1" as="geometry">
          <mxPoint>
            <xsl:attribute name="x">
              <xsl:value-of select="$tgtoneotherblockx" />
            </xsl:attribute>
            <xsl:attribute name="y">
              <xsl:value-of select="$tgtoneotherblocky" />
            </xsl:attribute>
            <xsl:attribute name="as">sourcePoint</xsl:attribute>
          </mxPoint>
          <mxPoint>
            <xsl:attribute name="x">
              <xsl:value-of select="$srconeotherblockx" />
            </xsl:attribute>
            <xsl:attribute name="y">
              <xsl:value-of select="$srconeotherblocky" />
            </xsl:attribute>
            <xsl:attribute name="as">targetPoint</xsl:attribute>
          </mxPoint>   
          <Array as="points">
            <xsl:for-each select="$tgtonelinkwaypoints">
              <xsl:copy-of select="." />
            </xsl:for-each>
            <xsl:for-each select="$srconelinkwaypoints">
              <xsl:copy-of select="." />
            </xsl:for-each>
          </Array>
        </mxGeometry>
      </xsl:element>
    </xsl:if>
    <!-- }}} -->

    <!-- generate new primary link two id {{{ -->
    <xsl:variable name="newidtwo">
      <xsl:choose>
        <xsl:when test="($tgtonelink/@id != '' or $srconelink/@id != '') and $srctwolink/@id != ''">
          <xsl:value-of select="concat($srctwolink/@id, generate-id($srctwolink))" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- generate new primary link three id {{{ -->
    <xsl:variable name="newidthree">
      <xsl:choose>
        <xsl:when test="$tgtonelink/@id != '' and $srconelink/@id != ''">
          <xsl:value-of select="$newidone" />
        </xsl:when>
        <xsl:when test="$tgtonelink/@id != ''">
          <xsl:value-of select="$tgtoneotherportid" />
        </xsl:when>
        <xsl:when test="$srconelink/@id != ''">
          <xsl:value-of select="$srconeotherportid" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- generate new primary link four id {{{ -->
    <xsl:variable name="newidfour">
      <xsl:choose>
        <xsl:when test="$tgtonelink/@id != '' and $srconelink/@id != ''">
          <xsl:value-of select="$newidone" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$newidtwo" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- generate new primary link two {{{ -->
    <xsl:if test="$newidthree != 'No match found' and $srctwolink/@id != ''">
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
        <xsl:value-of select="$srctwootherportid" />
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
        <mxPoint>
          <xsl:attribute name="x">
            <xsl:value-of select="$srctwootherblockx" />
          </xsl:attribute>
          <xsl:attribute name="y">
            <xsl:value-of select="$srctwootherblocky" />
          </xsl:attribute>
          <xsl:attribute name="as">targetPoint</xsl:attribute>
        </mxPoint>
        <Array as="points">
          <xsl:for-each select="$srctwolinkwaypoints">
            <xsl:copy-of select="." />
          </xsl:for-each>
        </Array>
      </mxGeometry>
    </xsl:element>
    </xsl:if>


    <xsl:element name="DEBUG">
      <xsl:attribute name="tgtonelink">
          <xsl:value-of select="$tgtonelink/@id" />
        </xsl:attribute>
        <xsl:attribute name="srconelink">
          <xsl:value-of select="$srconelink/@id" />
        </xsl:attribute>
        <xsl:attribute name="srctwolink">
          <xsl:value-of select="$srctwolink/@id" />
        </xsl:attribute>
        <xsl:attribute name="newidone">
          <xsl:value-of select="$newidone" />
        </xsl:attribute>
        <xsl:attribute name="newidtwo">
          <xsl:value-of select="$newidtwo" />
        </xsl:attribute>
        <xsl:attribute name="newidthree">
          <xsl:value-of select="$newidthree" />
        </xsl:attribute>
        <xsl:attribute name="newidfour">
          <xsl:value-of select="$newidfour" />
        </xsl:attribute>
    </xsl:element>
    <!-- }}} -->

    <!-- change source or target of secondary link: foreach loop, link copy, source change {{{ -->
    <xsl:for-each select="$tgtonesrcsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="source">
          <xsl:value-of select="$newidfour" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <xsl:for-each select="$tgtonetgtsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="target">
          <xsl:value-of select="$newidfour" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <xsl:for-each select="$srconesrcsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="source">
          <xsl:value-of select="$newidfour" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <xsl:for-each select="$srconetgtsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="target">
          <xsl:value-of select="$newidfour" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <xsl:for-each select="$srctwosrcsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="source">
          <xsl:value-of select="$newidtwo" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <xsl:for-each select="$srctwotgtsecondlink">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:attribute name="target">
          <xsl:value-of select="$newidtwo" />
        </xsl:attribute>
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:for-each>
    <!-- }}} -->

  </xsl:template>
  <!-- }}}1 -->

  <!-- checklinks template {{{1 -->
  <xsl:template name="checklinks">

    <!-- checklinks template parameters {{{ -->
    <xsl:param name="x" />
    <xsl:param name="y" />
    <xsl:param name="parent" />

    <xsl:param name="linktype" />

    <xsl:param name="tgtonelink" />
    <xsl:param name="tgtonelinkwaypoints" />
    <xsl:param name="tgtoneotherportid" />
    <xsl:param name="tgtoneotherblockx" />
    <xsl:param name="tgtoneotherblocky" />
    <xsl:param name="tgtonesrcsecondlink" />
    <xsl:param name="tgtonetgtsecondlink" />

    <xsl:param name="srconelink" />
    <xsl:param name="srconelinkwaypoints" />
    <xsl:param name="srconeotherportid" />
    <xsl:param name="srconeotherblockx" />
    <xsl:param name="srconeotherblocky" />
    <xsl:param name="srconesrcsecondlink" />
    <xsl:param name="srconetgtsecondlink" />

    <xsl:param name="srctwolink" />
    <xsl:param name="srctwolinkwaypoints" />
    <xsl:param name="srctwootherportid" />
    <xsl:param name="srctwootherblockx" />
    <xsl:param name="srctwootherblocky" />
    <xsl:param name="srctwosrcsecondlink" />
    <xsl:param name="srctwotgtsecondlink" />

    <xsl:param name="srcthreelink" />
    <xsl:param name="srcthreelinkwaypoints" />
    <xsl:param name="srcthreeotherportid" />
    <xsl:param name="srcthreeotherblockx" />
    <xsl:param name="srcthreeotherblocky" />
    <xsl:param name="srcthreesrcsecondlink" />
    <xsl:param name="srcthreetgtsecondlink" />
    <!-- }}} -->

    <!-- call the links template {{{ -->
    <xsl:choose>
      <!-- tgtonelink, srconelink {{{ -->
      <xsl:when test="$tgtonelink/@id != '' and $srconelink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$tgtonelink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srconelink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srconeotherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srconetgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$srctwolink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$srctwootherportid" />
          <xsl:with-param name="srctwootherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$srctwotgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srcthreelink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srcthreetgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
      <!-- tgtonelink, srctwolink {{{ -->
      <xsl:when test="$tgtonelink/@id != '' and $srctwolink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$tgtonelink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srctwolink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srctwootherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srctwotgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$srconelink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$srconeotherportid" />
          <xsl:with-param name="srctwootherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$srconetgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srcthreelink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srcthreetgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
      <!-- tgtonelink, srcthreelink {{{ -->
      <xsl:when test="$tgtonelink/@id != '' and $srcthreelink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$tgtonelink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srcthreelink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srcthreetgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$srconelink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$srconeotherportid" />
          <xsl:with-param name="srctwootherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$srconetgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srctwolink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srctwootherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srctwotgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
      <!-- srconelink, srctwolink {{{ -->
      <xsl:when test="$srconelink/@id != '' and $srctwolink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$srconelink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$srconeotherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$srconetgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srctwolink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srctwootherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srctwotgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$tgtonelink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="srctwootherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srcthreelink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srcthreetgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
      <!-- srconelink, srcthreelink {{{ -->
      <xsl:when test="$srconelink/@id != '' and $srcthreelink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$srconelink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$srconeotherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$srconetgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srcthreelink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srcthreetgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$tgtonelink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="srctwootherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srctwolink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srctwootherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srctwotgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
      <!-- srctwolink, srcthreelink {{{ -->
      <xsl:when test="$srctwolink/@id != '' and $srcthreelink/@id != ''">
        <xsl:call-template name="links">
          <xsl:with-param name="x" select="$x" />
          <xsl:with-param name="y" select="$y" />
          <xsl:with-param name="parent" select="$parent" />

          <xsl:with-param name="linktype" select="$linktype" />

          <xsl:with-param name="tgtonelink" select="$srctwolink" />
          <xsl:with-param name="tgtonelinkwaypoints" select="$srctwolinkwaypoints" />
          <xsl:with-param name="tgtoneotherportid" select="$srctwootherportid" />
          <xsl:with-param name="tgtoneotherblockx" select="$srctwootherblockx" />
          <xsl:with-param name="tgtoneotherblocky" select="$srctwootherblocky" />
          <xsl:with-param name="tgtonesrcsecondlink" select="$srctwosrcsecondlink" />
          <xsl:with-param name="tgtonetgtsecondlink" select="$srctwotgtsecondlink" />

          <xsl:with-param name="srconelink" select="$srcthreelink" />
          <xsl:with-param name="srconelinkwaypoints" select="$srcthreelinkwaypoints" />
          <xsl:with-param name="srconeotherportid" select="$srcthreeotherportid" />
          <xsl:with-param name="srconeotherblockx" select="$srcthreeotherblockx" />
          <xsl:with-param name="srconeotherblocky" select="$srcthreeotherblocky" />
          <xsl:with-param name="srconesrcsecondlink" select="$srcthreesrcsecondlink" />
          <xsl:with-param name="srconetgtsecondlink" select="$srcthreetgtsecondlink" />

          <xsl:with-param name="srctwolink" select="$tgtonelink" />
          <xsl:with-param name="srctwolinkwaypoints" select="$tgtonelinkwaypoints" />
          <xsl:with-param name="srctwootherportid" select="$tgtoneotherportid" />
          <xsl:with-param name="srctwootherblockx" select="$tgtoneotherblockx" />
          <xsl:with-param name="srctwootherblocky" select="$tgtoneotherblocky" />
          <xsl:with-param name="srctwosrcsecondlink" select="$tgtonesrcsecondlink" />
          <xsl:with-param name="srctwotgtsecondlink" select="$tgtonetgtsecondlink" />

          <xsl:with-param name="srcthreelink" select="$srconelink" />
          <xsl:with-param name="srcthreelinkwaypoints" select="$srconelinkwaypoints" />
          <xsl:with-param name="srcthreeotherportid" select="$srconeotherportid" />
          <xsl:with-param name="srcthreeotherblockx" select="$srconeotherblockx" />
          <xsl:with-param name="srcthreeotherblocky" select="$srconeotherblocky" />
          <xsl:with-param name="srcthreesrcsecondlink" select="$srconesrcsecondlink" />
          <xsl:with-param name="srcthreetgtsecondlink" select="$srconetgtsecondlink" />
        </xsl:call-template>
      </xsl:when>
      <!-- }}} -->
    </xsl:choose>
    <!-- }}} -->

  </xsl:template>
  <!-- }}}1 -->

  <!-- SplitBlock template {{{1 -->
  <xsl:template match="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]">
    <xsl:variable name="InputPort" select="key('k-explicitinput', @id)" />
    <xsl:variable name="OutputPort" select="key('k-explicitoutput', @id)" />

    <xsl:variable name="ControlPort" select="key('k-control', @id)" />
    <xsl:variable name="CommandPort" select="key('k-command', @id)" />

    <xsl:variable name="ImplicitPort" select="key('k-implicit', @id)" />

    <!-- x, y, parent: set (value) {{{ -->
    <xsl:variable name="geometry" select="mxGeometry" />
    <xsl:variable name="x" select="$geometry/@x" />
    <xsl:variable name="y" select="$geometry/@y" />
    <xsl:variable name="parent" select="@parent" />
    <!-- }}} -->

    <!-- linktype: set (value) {{{ -->
    <xsl:variable name="linktype">
      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">ExplicitLink</xsl:when>
        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">CommandControlLink</xsl:when>
        <xsl:when test="count($ImplicitPort) >= 3">ImplicitLink</xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- tgtoneid, srconeid: find ports connected to splitblock (value) {{{ -->
    <xsl:variable name="tgtoneid">
      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:value-of select="$InputPort[position()=1]/@id" />
        </xsl:when>
        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:value-of select="$ControlPort[position()=1]/@id" />
        </xsl:when>
        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:value-of select="$ImplicitPort[position()=1]/@id" />
        </xsl:when>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srconeid">
      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:value-of select="$OutputPort[position()=1]/@id" />
        </xsl:when>
        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:value-of select="$CommandPort[position()=1]/@id" />
        </xsl:when>
        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:value-of select="$ImplicitPort[position()=2]/@id" />
        </xsl:when>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srctwoid">
      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:value-of select="$OutputPort[position()=2]/@id" />
        </xsl:when>
        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:value-of select="$CommandPort[position()=2]/@id" />
        </xsl:when>
        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:value-of select="$ImplicitPort[position()=3]/@id" />
        </xsl:when>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srcthreeid">
      <xsl:choose>
        <xsl:when test="count($InputPort) >= 1 and count($OutputPort) >= 2">
          <xsl:value-of select="$OutputPort[position()=3]/@id" />
        </xsl:when>
        <xsl:when test="count($ControlPort) >= 1 and count($CommandPort) >= 2">
          <xsl:value-of select="$CommandPort[position()=3]/@id" />
        </xsl:when>
        <xsl:when test="count($ImplicitPort) >= 3">
          <xsl:value-of select="$ImplicitPort[position()=4]/@id" />
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- tgtonelink, srconelink: find links connected to ports connected to splitblock (node-set) {{{ -->
    <xsl:variable name="tgtonelink" select="key('k-link', $tgtoneid)" />
    <xsl:variable name="srconelink" select="key('k-link', $srconeid)" />
    <xsl:variable name="srctwolink" select="key('k-link', $srctwoid)" />
    <xsl:variable name="srcthreelink" select="key('k-link', $srcthreeid)" />
    <!-- }}} -->

    <!-- tgtoneotherportid, srconeotherportid: find other (tgt|src) ports connected to links connected to (src|tgt) ports connected to splitblock (value) {{{ -->
    <xsl:variable name="tgtoneotherportid">
      <xsl:choose>
        <xsl:when test="$tgtoneid = $tgtonelink/@source">
          <xsl:value-of select="$tgtonelink/@target" />
        </xsl:when>
        <xsl:when test="$tgtoneid = $tgtonelink/@target">
          <xsl:value-of select="$tgtonelink/@source" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srconeotherportid">
      <xsl:choose>
        <xsl:when test="$srconeid = $srconelink/@source">
          <xsl:value-of select="$srconelink/@target" />
        </xsl:when>
        <xsl:when test="$srconeid = $srconelink/@target">
          <xsl:value-of select="$srconelink/@source" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srctwootherportid">
      <xsl:choose>
        <xsl:when test="$srctwoid = $srctwolink/@source">
          <xsl:value-of select="$srctwolink/@target" />
        </xsl:when>
        <xsl:when test="$srctwoid = $srctwolink/@target">
          <xsl:value-of select="$srctwolink/@source" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srcthreeotherportid">
      <xsl:choose>
        <xsl:when test="$srcthreeid = $srcthreelink/@source">
          <xsl:value-of select="$srcthreelink/@target" />
        </xsl:when>
        <xsl:when test="$srcthreeid = $srcthreelink/@target">
          <xsl:value-of select="$srcthreelink/@source" />
        </xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- }}} -->

    <!-- tgtoneotherblockx, tgtoneotherblocky, srconeotherblockx, srconeotherblocky: find x, y position of other (tgt|src) ports connected to links connected to (src|tgt) ports connected to splitblock (value) {{{ -->
    <xsl:variable name="tgtoneotherportsort">
      <xsl:choose>
        <xsl:when test="$tgtoneid = $tgtonelink/@source">targetPoint</xsl:when>
        <xsl:when test="$tgtoneid = $tgtonelink/@target">sourcePoint</xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="tgtoneotherport" select="key('k-port', $tgtoneotherportid)" />
    <xsl:variable name="tgtoneotherblock" select="key('k-block', $tgtoneotherport/@parent)" />

    <xsl:variable name="tgtoneotherblockx">
      <xsl:choose>
        <xsl:when test="$tgtonelink/mxGeometry/mxPoint[@as=$tgtoneotherportsort]">
          <xsl:value-of select="$tgtonelink/mxGeometry/mxPoint[@as=$tgtoneotherportsort]/@x" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$tgtoneotherblock/mxGeometry/@x" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="tgtoneotherblocky" >
        <xsl:choose>
        <xsl:when test="$tgtonelink/mxGeometry/mxPoint[@as=$tgtoneotherportsort]">
          <xsl:value-of select="$tgtonelink/mxGeometry/mxPoint[@as=$tgtoneotherportsort]/@y" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$tgtoneotherblock/mxGeometry/@y" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srconeotherportsort">
      <xsl:choose>
        <xsl:when test="$srconeid = $srconelink/@source">targetPoint</xsl:when>
        <xsl:when test="$srconeid = $srconelink/@target">sourcePoint</xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srconeotherport" select="key('k-port', $srconeotherportid)" />
    <xsl:variable name="srconeotherblock" select="key('k-block', $srconeotherport/@parent)" />

    <xsl:variable name="srconeotherblockx">
      <xsl:choose>
        <xsl:when test="$srconelink/mxGeometry/mxPoint[@as=$srconeotherportsort]">
          <xsl:value-of select="$srconelink/mxGeometry/mxPoint[@as=$srconeotherportsort]/@x" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srconeotherblock/mxGeometry/@x" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srconeotherblocky" >
        <xsl:choose>
        <xsl:when test="$srconelink/mxGeometry/mxPoint[@as=$srconeotherportsort]">
          <xsl:value-of select="$srconelink/mxGeometry/mxPoint[@as=$srconeotherportsort]/@y" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srconeotherblock/mxGeometry/@y" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srctwootherportsort">
      <xsl:choose>
        <xsl:when test="$srctwoid = $srctwolink/@source">targetPoint</xsl:when>
        <xsl:when test="$srctwoid = $srctwolink/@target">sourcePoint</xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srctwootherport" select="key('k-port', $srctwootherportid)" />
    <xsl:variable name="srctwootherblock" select="key('k-block', $srctwootherport/@parent)" />

    <xsl:variable name="srctwootherblockx">
      <xsl:choose>
        <xsl:when test="$srctwolink/mxGeometry/mxPoint[@as=$srctwootherportsort]">
          <xsl:value-of select="$srctwolink/mxGeometry/mxPoint[@as=$srctwootherportsort]/@x" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srctwootherblock/mxGeometry/@x" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srctwootherblocky" >
        <xsl:choose>
        <xsl:when test="$srctwolink/mxGeometry/mxPoint[@as=$srctwootherportsort]">
          <xsl:value-of select="$srctwolink/mxGeometry/mxPoint[@as=$srctwootherportsort]/@y" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srctwootherblock/mxGeometry/@y" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srcthreeotherportsort">
      <xsl:choose>
        <xsl:when test="$srcthreeid = $srcthreelink/@source">targetPoint</xsl:when>
        <xsl:when test="$srcthreeid = $srcthreelink/@target">sourcePoint</xsl:when>
        <xsl:otherwise>No match found</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srcthreeotherport" select="key('k-port', $srcthreeotherportid)" />
    <xsl:variable name="srcthreeotherblock" select="key('k-block', $srcthreeotherport/@parent)" />
    <xsl:variable name="srcthreeotherblockx">
      <xsl:choose>
        <xsl:when test="$srcthreelink/mxGeometry/mxPoint[@as=$srcthreeotherportsort]">
          <xsl:value-of select="$srcthreelink/mxGeometry/mxPoint[@as=$srcthreeotherportsort]/@x" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srcthreeotherblock/mxGeometry/@x" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:variable name="srcthreeotherblocky" >
        <xsl:choose>
        <xsl:when test="$srcthreelink/mxGeometry/mxPoint[@as=$srcthreeotherportsort]">
          <xsl:value-of select="$srcthreelink/mxGeometry/mxPoint[@as=$srcthreeotherportsort]/@y" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$srcthreeotherblock/mxGeometry/@y" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <!-- <xsl:element name="variables">
      <xsl:attribute name="tgtoneotherportsort">
        <xsl:value-of select="$tgtoneotherportsort" />
      </xsl:attribute>
      <xsl:attribute name="tgtoneotherblockx">
        <xsl:value-of select="$tgtoneotherblockx" />
      </xsl:attribute>
      <xsl:attribute name="tgtoneotherblocky">
        <xsl:value-of select="$tgtoneotherblocky" />
      </xsl:attribute>
      <xsl:attribute name="srconeotherportsort">
        <xsl:value-of select="$srconeotherportsort" />
      </xsl:attribute>
      <xsl:attribute name="srconeotherblockx">
        <xsl:value-of select="$srconeotherblockx" />
      </xsl:attribute>
      <xsl:attribute name="srconeotherblocky">
        <xsl:value-of select="$srconeotherblocky" />
      </xsl:attribute>
      <xsl:attribute name="srctwootherportsort">
        <xsl:value-of select="$srctwootherportsort" />
      </xsl:attribute>
      <xsl:attribute name="srctwootherblockx">
        <xsl:value-of select="$srctwootherblockx" />
      </xsl:attribute>
      <xsl:attribute name="srctwootherblocky">
        <xsl:value-of select="$srctwootherblocky" />
      </xsl:attribute>
    </xsl:element> -->
    <!-- }}} -->

    <!-- tgtonelinkwaypoints, srconelinkwaypoints: find waypoints of links connected to ports connected to splitblock (node-set) {{{ -->
    <xsl:variable name="tmptgtonelinkwaypoints">
      <waypoints>
        <xsl:choose>
          <xsl:when test="$tgtoneid = $tgtonelink/@source">
            <xsl:for-each select="$tgtonelink/mxGeometry/Array/mxPoint">
              <xsl:sort select="position()" order="descending"/>
              <xsl:copy-of select="."/>
            </xsl:for-each>
          </xsl:when>
          <xsl:when test="$tgtoneid = $tgtonelink/@target">
            <xsl:copy-of select="$tgtonelink/mxGeometry/Array/mxPoint" />
          </xsl:when>
          <xsl:otherwise>No match found</xsl:otherwise>
        </xsl:choose>
      </waypoints>
    </xsl:variable>
    <xsl:variable name="tgtonelinkwaypoints" select="ext:node-set($tmptgtonelinkwaypoints)/waypoints/mxPoint" />

    <xsl:variable name="tmpsrconelinkwaypoints">
      <waypoints>
        <xsl:choose>
          <xsl:when test="$srconeid = $srconelink/@target">
            <xsl:for-each select="$srconelink/mxGeometry/Array/mxPoint">
              <xsl:sort select="position()" order="descending"/>
              <xsl:copy-of select="."/>
            </xsl:for-each>
          </xsl:when>
          <xsl:when test="$srconeid = $srconelink/@source">
            <xsl:copy-of select="$srconelink/mxGeometry/Array/mxPoint" />
          </xsl:when>
          <xsl:otherwise>No match found</xsl:otherwise>
        </xsl:choose>
      </waypoints>
    </xsl:variable>
    <xsl:variable name="srconelinkwaypoints" select="ext:node-set($tmpsrconelinkwaypoints)/waypoints/mxPoint" />

    <xsl:variable name="tmpsrctwolinkwaypoints">
      <waypoints>
        <xsl:choose>
          <xsl:when test="$srctwoid = $srctwolink/@target">
            <xsl:for-each select="$srctwolink/mxGeometry/Array/mxPoint">
              <xsl:sort select="position()" order="descending"/>
              <xsl:copy-of select="."/>
            </xsl:for-each>
          </xsl:when>
          <xsl:when test="$srctwoid = $srctwolink/@source">
            <xsl:copy-of select="$srctwolink/mxGeometry/Array/mxPoint" />
          </xsl:when>
          <xsl:otherwise>No match found</xsl:otherwise>
        </xsl:choose>
      </waypoints>
    </xsl:variable>
    <xsl:variable name="srctwolinkwaypoints" select="ext:node-set($tmpsrctwolinkwaypoints)/waypoints/mxPoint" />

    <xsl:variable name="tmpsrcthreelinkwaypoints">
      <waypoints>
        <xsl:choose>
          <xsl:when test="$srcthreeid = $srcthreelink/@target">
            <xsl:for-each select="$srcthreelink/mxGeometry/Array/mxPoint">
              <xsl:sort select="position()" order="descending"/>
              <xsl:copy-of select="."/>
            </xsl:for-each>
          </xsl:when>
          <xsl:when test="$srcthreeid = $srcthreelink/@source">
            <xsl:copy-of select="$srcthreelink/mxGeometry/Array/mxPoint" />
          </xsl:when>
          <xsl:otherwise>No match found</xsl:otherwise>
        </xsl:choose>
      </waypoints>
    </xsl:variable>
    <xsl:variable name="srcthreelinkwaypoints" select="ext:node-set($tmpsrcthreelinkwaypoints)/waypoints/mxPoint" />
    <!-- }}} -->

    <!-- tgtonesrcsecondlink, tgtonetgtsecondlink, srconesrcsecondlink, srconetgtsecondlink: find secondary links connected to links connected to ports connected to splitblock (node-set) {{{ -->
    <xsl:variable name="tgtonesrcsecondlink" select="key('k-linksrc', $tgtonelink/@id)" />
    <xsl:variable name="tgtonetgtsecondlink" select="key('k-linktgt', $tgtonelink/@id)" />
    <xsl:variable name="srconesrcsecondlink" select="key('k-linksrc', $srconelink/@id)" />
    <xsl:variable name="srconetgtsecondlink" select="key('k-linktgt', $srconelink/@id)" />
    <xsl:variable name="srctwosrcsecondlink" select="key('k-linksrc', $srctwolink/@id)" />
    <xsl:variable name="srctwotgtsecondlink" select="key('k-linktgt', $srctwolink/@id)" />
    <xsl:variable name="srcthreesrcsecondlink" select="key('k-linksrc', $srcthreelink/@id)" />
    <xsl:variable name="srcthreetgtsecondlink" select="key('k-linktgt', $srcthreelink/@id)" />
    <!-- }}} -->

    <!-- call the checklinks template {{{ -->
    <xsl:call-template name="checklinks">
      <xsl:with-param name="x" select="$x" />
      <xsl:with-param name="y" select="$y" />
      <xsl:with-param name="parent" select="$parent" />

      <xsl:with-param name="linktype" select="$linktype" />

      <xsl:with-param name="tgtonelink" select="$tgtonelink" />
      <xsl:with-param name="tgtonelinkwaypoints" select="$tgtonelinkwaypoints" />
      <xsl:with-param name="tgtoneotherportid" select="$tgtoneotherportid" />
      <xsl:with-param name="tgtoneotherblockx" select="$tgtoneotherblockx" />
      <xsl:with-param name="tgtoneotherblocky" select="$tgtoneotherblocky" />
      <xsl:with-param name="tgtonesrcsecondlink" select="$tgtonesrcsecondlink" />
      <xsl:with-param name="tgtonetgtsecondlink" select="$tgtonetgtsecondlink" />

      <xsl:with-param name="srconelink" select="$srconelink" />
      <xsl:with-param name="srconelinkwaypoints" select="$srconelinkwaypoints" />
      <xsl:with-param name="srconeotherportid" select="$srconeotherportid" />
      <xsl:with-param name="srconeotherblockx" select="$srconeotherblockx" />
      <xsl:with-param name="srconeotherblocky" select="$srconeotherblocky" />
      <xsl:with-param name="srconesrcsecondlink" select="$srconesrcsecondlink" />
      <xsl:with-param name="srconetgtsecondlink" select="$srconetgtsecondlink" />

      <xsl:with-param name="srctwolink" select="$srctwolink" />
      <xsl:with-param name="srctwolinkwaypoints" select="$srctwolinkwaypoints" />
      <xsl:with-param name="srctwootherportid" select="$srctwootherportid" />
      <xsl:with-param name="srctwootherblockx" select="$srctwootherblockx" />
      <xsl:with-param name="srctwootherblocky" select="$srctwootherblocky" />
      <xsl:with-param name="srctwosrcsecondlink" select="$srctwosrcsecondlink" />
      <xsl:with-param name="srctwotgtsecondlink" select="$srctwotgtsecondlink" />

      <xsl:with-param name="srcthreelink" select="$srcthreelink" />
      <xsl:with-param name="srcthreelinkwaypoints" select="$srcthreelinkwaypoints" />
      <xsl:with-param name="srcthreeotherportid" select="$srcthreeotherportid" />
      <xsl:with-param name="srcthreeotherblockx" select="$srcthreeotherblockx" />
      <xsl:with-param name="srcthreeotherblocky" select="$srcthreeotherblocky" />
      <xsl:with-param name="srcthreesrcsecondlink" select="$srcthreesrcsecondlink" />
      <xsl:with-param name="srcthreetgtsecondlink" select="$srcthreetgtsecondlink" />
    </xsl:call-template>
    <!-- }}} -->

  </xsl:template>
  <!-- }}}1 -->

  <!-- Port template {{{1 -->
  <xsl:template match="ExplicitInputPort | ExplicitOutputPort | ImplicitInputPort | ImplicitOutputPort | ControlPort | CommandPort">
    <xsl:variable name="parentId" select="@parent" />
    <xsl:variable name="SPLIT" select="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]" />

    <xsl:if test="$parentId != $SPLIT/@id">
      <xsl:copy>
        <xsl:copy-of select="@*" />
        <xsl:copy-of select="node()" />
      </xsl:copy>
    </xsl:if>
  </xsl:template>
  <!-- }}}1 -->

  <!-- Link template {{{1 -->
  <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
    <xsl:variable name="sourceElement" select="key('k-portorlink', @source)" />
    <xsl:variable name="targetElement" select="key('k-portorlink', @target)" />
    <xsl:variable name="SPLITID" select="/XcosDiagram/mxGraphModel/root/SplitBlock[position() = 1]/@id" />
    <xsl:if test="$sourceElement/@parent != $SPLITID and $targetElement/@parent != $SPLITID">
      <xsl:variable name="srcsrcid" select="key('k-portorlink', $sourceElement/@source)/@parent" />
      <xsl:variable name="srctgtid" select="key('k-portorlink', $sourceElement/@target)/@parent" />
      <xsl:variable name="tgtsrcid" select="key('k-portorlink', $targetElement/@source)/@parent" />
      <xsl:variable name="tgttgtid" select="key('k-portorlink', $targetElement/@target)/@parent" />

      <xsl:if test="(string-length($tgtsrcid) = 0 or $tgtsrcid != $SPLITID) and (string-length($tgttgtid) = 0 or $tgttgtid != $SPLITID) and (string-length($srctgtid) = 0 or $srctgtid != $SPLITID) and (string-length($srcsrcid) = 0 or $srcsrcid != $SPLITID)">
        <xsl:copy>
          <xsl:copy-of select="@*" />
          <xsl:copy-of select="node()" />
        </xsl:copy>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!-- }}}1 -->

</xsl:stylesheet>
