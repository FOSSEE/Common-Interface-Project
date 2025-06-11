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

  <xsl:key name="k-cell" match="mxCell" use="@id" />

  <!-- templates {{{2 -->
  <xsl:template name="get-port">
    <xsl:param name="style" />

    <xsl:variable name="first" select="substring-before($style, ';')" />
    <xsl:choose>
      <xsl:when test="$first = ''">
        <xsl:value-of select="$style" />
      </xsl:when>
      <xsl:when test="not(contains($first, '='))">
        <xsl:value-of select="$first" />
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="rest" select="substring-after($style, ';')" />
        <xsl:call-template name="get-port">
          <xsl:with-param name="style" select="$rest" />
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="get-noofports">
    <xsl:param name="port" />
    <xsl:param name="context" />

    <xsl:choose>
      <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
        <xsl:value-of select="$context/@explicitInputPorts + $context/@implicitInputPorts" />
      </xsl:when>
      <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
        <xsl:value-of select="$context/@explicitOutputPorts + $context/@implicitOutputPorts" />
      </xsl:when>
      <xsl:when test="$port = 'ControlPort'">
        <xsl:value-of select="$context/@controlPorts" />
      </xsl:when>
      <xsl:when test="$port = 'CommandPort'">
        <xsl:value-of select="$context/@commandPorts" />
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="get-x-position">
    <xsl:param name="port" />
    <xsl:param name="ordering" />
    <xsl:param name="noofport" />
    <xsl:param name="geometry" />

    <xsl:choose>
      <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
        <xsl:value-of select="$geometry/@x" />
      </xsl:when>
      <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
        <xsl:value-of select="$geometry/@x + $geometry/@width" />
      </xsl:when>
      <xsl:when test="$port = 'ControlPort' or $port = 'CommandPort'">
        <xsl:value-of select="$geometry/@x + $geometry/@width * (2 * $ordering - 1) div (2 * $noofport)" />
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="get-y-position">
    <xsl:param name="port" />
    <xsl:param name="ordering" />
    <xsl:param name="noofport" />
    <xsl:param name="geometry" />

    <xsl:choose>
      <xsl:when test="($port = 'ExplicitInputPort' or $port = 'ImplicitInputPort') or ($port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort')">
        <xsl:value-of select="$geometry/@y + $geometry/@height * (2 * $ordering - 1) div (2 * $noofport)" />
      </xsl:when>
      <xsl:when test="$port = 'ControlPort'">
        <xsl:value-of select="$geometry/@y" />
      </xsl:when>
      <xsl:when test="$port = 'CommandPort'">
        <xsl:value-of select="$geometry/@y + $geometry/@height" />
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!-- }}}2 -->

  <!-- sourcePoint {{{3 -->
  <xsl:template match="mxPoint[@as='sourcePoint']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />

      <!-- x {{{ -->
      <xsl:variable name="newx">
        <!-- Get mxCell with sourceVertex of parent -->
        <xsl:for-each select="key('k-cell', ancestor::mxCell/@sourceVertex)">
          <!-- Get the port number for calculating position -->
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <!-- Get the port type from the style attribute -->
          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="x-pos">
              <xsl:call-template name="get-x-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$x-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="x">
        <xsl:choose>
          <xsl:when test="$newx = ''">
            <xsl:value-of select="@x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newx,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <!-- y {{{ -->
      <xsl:variable name="newy">
        <!-- Get mxCell with sourceVertex of parent -->
        <xsl:for-each select="key('k-cell', ancestor::mxCell/@sourceVertex)">
          <!-- Get the port number for calculating position -->
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <!-- Get the port type from the style attribute -->
          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="y-pos">
              <xsl:call-template name="get-y-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$y-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="y">
        <xsl:choose>
          <xsl:when test="$newy = ''">
            <xsl:value-of select="@y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newy,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}3 -->

  <!-- targetpoint {{{4 -->
  <xsl:template match="mxPoint[@as='targetPoint']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />

      <!-- x {{{ -->
      <xsl:variable name="newx">
        <!-- Get mxCell with targetVertex of parent -->
        <xsl:for-each select="key('k-cell', ancestor::mxCell/@targetVertex)">
          <!-- Get the port number for calculating position -->
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <!-- Get the port type from the style attribute -->
          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="x-pos">
              <xsl:call-template name="get-x-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$x-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="x">
        <xsl:choose>
          <xsl:when test="$newx = ''">
            <xsl:value-of select="@x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newx,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <!-- y {{{ -->
      <xsl:variable name="newy">
        <!-- Get mxCell with targetVertex of parent -->
        <xsl:for-each select="key('k-cell', ancestor::mxCell/@targetVertex)">
          <!-- Get the port number for calculating position -->
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <!-- Get the port type from the style attribute -->
          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="y-pos">
              <xsl:call-template name="get-y-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$y-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="y">
        <xsl:choose>
          <xsl:when test="$newy = ''">
            <xsl:value-of select="@y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newy,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}4 -->

  <!-- mxcell tarx & tary & tar2x & tar2y {{{5 -->
  <xsl:template match="mxCell[@edge='1']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />

      <xsl:variable name="newtarx">
        <!-- Get mxCell with sourceVertex -->
        <xsl:for-each select="key('k-cell', @sourceVertex)">
          <!-- Get the port number for calculating position -->
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <!-- Get the port type from the style attribute -->
          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="x-pos">
              <xsl:call-template name="get-x-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$x-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tarx">
        <xsl:choose>
          <xsl:when test="$newtarx = ''">
            <xsl:value-of select="@tarx" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newtarx,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>

      <xsl:variable name="newtary">
        <!-- Check for mxCell with sourceVertex -->
        <xsl:for-each select="key('k-cell', @sourceVertex)">
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Find the mxCell whose id matches sourceVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="y-pos">
              <xsl:call-template name="get-y-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$y-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tary">
        <xsl:choose>
          <xsl:when test="$newtary = ''">
            <xsl:value-of select="@tary" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newtary,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>

      <!-- tar2x & tar2y -->
      <xsl:variable name="newtar2x">
        <!-- Check for mxCell with sourceVertex -->
        <xsl:for-each select="key('k-cell', @targetVertex)">
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Find the mxCell whose id matches sourceVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="x-pos">
              <xsl:call-template name="get-x-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$x-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tar2x">
        <xsl:choose>
          <xsl:when test="$newtar2x = ''">
            <xsl:value-of select="@tar2x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newtar2x,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>

      <xsl:variable name="newtar2y">
        <!-- Check for mxCell with targetVertex -->
        <xsl:for-each select="key('k-cell', @targetVertex)">
          <xsl:variable name="ordering">
            <xsl:value-of select="@ordering" />
          </xsl:variable>

          <xsl:variable name="port">
            <xsl:call-template name="get-port">
              <xsl:with-param name="style" select="@style" />
            </xsl:call-template>
          </xsl:variable>

          <!-- Find the mxCell whose id matches targetVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:call-template name="get-noofports">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="context" select="." />
              </xsl:call-template>
            </xsl:variable>

            <xsl:variable name="y-pos">
              <xsl:call-template name="get-y-position">
                <xsl:with-param name="port" select="$port" />
                <xsl:with-param name="ordering" select="$ordering" />
                <xsl:with-param name="noofport" select="$noofport" />
                <xsl:with-param name="geometry" select="mxGeometry" />
              </xsl:call-template>
            </xsl:variable>
            <xsl:value-of select="$y-pos" />
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tar2y">
        <xsl:choose>
          <xsl:when test="$newtar2y = ''">
            <xsl:value-of select="@tar2y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($newtar2y,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}5 -->

</xsl:stylesheet>
