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

  <xsl:template name="get-port">
    <xsl:param name="style" />

    <xsl:choose>
      <xsl:when test="contains($style, ';')">
        <xsl:value-of select="substring-before($style, ';')" />
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$style" />
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

  <!-- sourcePoint {{{2 -->
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@x" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@x + @width" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort' or $port = 'CommandPort'">
                  <xsl:value-of select="@x + @width * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="x">
        <xsl:choose>
          <xsl:when test="$newx = ''">
            <xsl:value-of select="@x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newx" />
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="($port = 'ExplicitInputPort' or $port = 'ImplicitInputPort') or ($port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort')">
                  <xsl:value-of select="@y + @height * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@y" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@y + @height" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="y">
        <xsl:choose>
          <xsl:when test="$newy = ''">
            <xsl:value-of select="@y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newy" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}2 -->

  <!-- targetpoint {{{3 -->
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@x" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@x + @width" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort' or $port = 'CommandPort'">
                  <xsl:value-of select="@x + @width * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="x">
        <xsl:choose>
          <xsl:when test="$newx = ''">
            <xsl:value-of select="@x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newx" />
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="($port = 'ExplicitInputPort' or $port = 'ImplicitInputPort') or ($port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort')">
                  <xsl:value-of select="@y + @height * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@y" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@y + @height" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="y">
        <xsl:choose>
          <xsl:when test="$newy = ''">
            <xsl:value-of select="@y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newy" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <!-- }}} -->

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}3 -->

  <!-- mxcell tarx & tary & tar2x & tar2y {{{4 -->
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Get parent mxCell with port count -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@x" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@x + @width" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort' or $port = 'CommandPort'">
                  <xsl:value-of select="@x + @width * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tarx">
        <xsl:choose>
          <xsl:when test="$newtarx = ''">
            <xsl:value-of select="@tarx" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newtarx" />
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Find the mxCell whose id matches sourceVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="($port = 'ExplicitInputPort' or $port = 'ImplicitInputPort') or ($port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort')">
                  <xsl:value-of select="@y + @height * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@y" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@y + @height" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tary">
        <xsl:choose>
          <xsl:when test="$newtary = ''">
            <xsl:value-of select="@tary" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newtary" />
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Find the mxCell whose id matches sourceVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@x" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@x + @width" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort' or $port = 'CommandPort'">
                  <xsl:value-of select="@x + @width * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tar2x">
        <xsl:choose>
          <xsl:when test="$newtar2x = ''">
            <xsl:value-of select="@tar2x" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newtar2x" />
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
            <xsl:choose>
              <xsl:when test="contains(@style, ';')">
                <xsl:value-of select="substring-before(@style, ';')" />
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="@style" />
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>

          <!-- Find the mxCell whose id matches targetVertex -->
          <xsl:for-each select="key('k-cell', @ParentComponent)">
            <!-- Get the number of ports for calculating position -->
            <xsl:variable name="noofport">
              <xsl:choose>
                <xsl:when test="$port = 'ExplicitInputPort' or $port = 'ImplicitInputPort'">
                  <xsl:value-of select="@explicitInputPorts + @implicitInputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort'">
                  <xsl:value-of select="@explicitOutputPorts + @implicitOutputPorts" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@controlPorts" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@commandPorts" />
                </xsl:when>
              </xsl:choose>
            </xsl:variable>

            <xsl:for-each select="mxGeometry">
              <xsl:choose>
                <xsl:when test="($port = 'ExplicitInputPort' or $port = 'ImplicitInputPort') or ($port = 'ExplicitOutputPort' or $port = 'ImplicitOutputPort')">
                  <xsl:value-of select="@y + @height * (2 * $ordering - 1) div (2 * $noofport)" />
                </xsl:when>
                <xsl:when test="$port = 'ControlPort'">
                  <xsl:value-of select="@y" />
                </xsl:when>
                <xsl:when test="$port = 'CommandPort'">
                  <xsl:value-of select="@y + @height" />
                </xsl:when>
              </xsl:choose>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:variable>

      <xsl:attribute name="tar2y">
        <xsl:choose>
          <xsl:when test="$newtar2y = ''">
            <xsl:value-of select="@tar2y" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$newtar2y" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>

      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}4 -->

</xsl:stylesheet>
