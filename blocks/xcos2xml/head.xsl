<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
>

  <xsl:template name="log2">
     <xsl:param name="pX" />
     <xsl:param name="count" select="0" />

     <xsl:choose>
       <xsl:when test="$pX &lt;= 1">
         <xsl:value-of select="$count" />
       </xsl:when>
       <xsl:otherwise>
         <xsl:call-template name="log2">
           <xsl:with-param name="pX" select="$pX div 2" />
           <xsl:with-param name="count" select="$count + 1" />
         </xsl:call-template>
       </xsl:otherwise>
     </xsl:choose>
  </xsl:template>

  <xsl:template name="eval-rational">
    <xsl:param name="expr"/>

    <xsl:choose>
      <xsl:when test="contains($expr, '/')">
        <xsl:variable name="num" select="number(substring-before($expr, '/'))" />
        <xsl:variable name="den" select="number(substring-after($expr, '/'))" />
        <xsl:value-of select="$num div $den" />
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="number($expr)" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="si-format">
    <xsl:param name="expr" />

    <xsl:variable name="num">
      <xsl:call-template name="eval-rational">
        <xsl:with-param name="expr" select="$expr" />
      </xsl:call-template>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="number($num) &gt;= 1000000000000">
        <xsl:value-of select="format-number($num div 1000000000000, '#.##')" />
        <xsl:text> T</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 1000000000">
        <xsl:value-of select="format-number($num div 1000000000, '#.##')" />
        <xsl:text> G</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 1000000">
        <xsl:value-of select="format-number($num div 1000000, '#.##')" />
        <xsl:text> M</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 1000">
        <xsl:value-of select="format-number($num div 1000, '#.##')" />
        <xsl:text> k</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 1">
        <xsl:value-of select="format-number($num, '#.##')" />
      </xsl:when>
      <xsl:when test="number($num) &gt;= 0.001">
        <xsl:value-of select="format-number($num div 0.001, '#.##')" />
        <xsl:text> m</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 0.000001">
        <xsl:value-of select="format-number($num div 0.000001, '#.##')" />
        <xsl:text> &#956;</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 0.000000001">
        <xsl:value-of select="format-number($num div 0.000000001, '#.##')" />
        <xsl:text> n</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 0.000000000001">
        <xsl:value-of select="format-number($num div 0.000000000001, '#.##')" />
        <xsl:text> p</xsl:text>
      </xsl:when>
      <xsl:when test="number($num) &gt;= 0.000000000000001">
        <xsl:value-of select="format-number($num div 0.000000000000001, '#.##')" />
        <xsl:text> f</xsl:text>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="format-number($num, '#.##')" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:output method="xml" indent="no" />
  <xsl:key name="k-in" match="ExplicitInputPort | ImplicitInputPort" use="@parent" />
  <xsl:key name="k-out" match="ExplicitOutputPort | ImplicitOutputPort" use="@parent" />
  <xsl:key name="k-command" match="CommandPort" use="@parent" />
  <xsl:key name="k-control" match="ControlPort" use="@parent" />

  <xsl:variable name="originx">
    <xsl:choose>
      <xsl:when test="/XcosDiagram/mxPoint[@as='origin']/@x">
        <xsl:value-of select="/XcosDiagram/mxPoint[@as='origin']/@x" />
      </xsl:when>
      <xsl:otherwise>0</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <xsl:variable name="originy">
    <xsl:choose>
      <xsl:when test="/XcosDiagram/mxPoint[@as='origin']/@y">
        <xsl:value-of select="/XcosDiagram/mxPoint[@as='origin']/@y" />
      </xsl:when>
      <xsl:otherwise>0</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
  <xsl:template match="comment()" />
  <xsl:template match="XcosDiagram">
    <xsl:copy>
      <xsl:apply-templates select="@* | node()" />
    </xsl:copy>
  </xsl:template>

  <xsl:template match="SuperBlockDiagram">
    <xsl:copy>
      <xsl:apply-templates select="@* | node()" />
    </xsl:copy>
  </xsl:template>

  <xsl:template match="Array[@as='context']">
    <xsl:copy>
      <xsl:apply-templates select="@* | node()" />
    </xsl:copy>
  </xsl:template>
  
  <xsl:template match="mxGraphModel">
    <xsl:copy>
      <xsl:apply-templates select="@*[name(.)!='as']" />
      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <xsl:template match="mxCell[position()=1]">
    <xsl:copy>
      <xsl:attribute name="id">
        <xsl:value-of select="@id" />
      </xsl:attribute>
      <xsl:attribute name="appname">Xcos</xsl:attribute>
      <xsl:attribute name="description"></xsl:attribute>
      <xsl:attribute name="CellType">Unknown</xsl:attribute>
      <xsl:attribute name="sourceVertex">0</xsl:attribute>
      <xsl:attribute name="targetVertex">0</xsl:attribute>
      <xsl:attribute name="tarx">0</xsl:attribute>
      <xsl:attribute name="tary">0</xsl:attribute>
      <Object as="parameter_values" />
      <Object as="displayProperties" />
      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <xsl:template match="mxCell[position()=2]">
    <xsl:copy>
      <xsl:attribute name="id">
        <xsl:value-of select="@id" />
      </xsl:attribute>
      <xsl:attribute name="CellType">Unknown</xsl:attribute>
      <xsl:attribute name="sourceVertex">0</xsl:attribute>
      <xsl:attribute name="targetVertex">0</xsl:attribute>
      <xsl:attribute name="tarx">0</xsl:attribute>
      <xsl:attribute name="tary">0</xsl:attribute>
      <Object as="parameter_values" />
      <Object as="displayProperties" />
      <xsl:apply-templates select="node()" />
    </xsl:copy>
  </xsl:template>
  <xsl:template name="mxGeometry" match="mxGeometry">
    <xsl:element name="mxGeometry">
      <xsl:attribute name="x">
            <xsl:choose>
                <xsl:when test="@x">
                    <xsl:value-of select="format-number(@x + $originx, '0.0')" />
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>0.0</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>

      <xsl:attribute name="y">
            <xsl:choose>
                <xsl:when test="@y">
                    <xsl:value-of select="format-number(@y + $originy, '0.0')" />
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>0.0</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>

      <xsl:if test="@width">
        <xsl:attribute name="width">
          <xsl:value-of select="@width" />
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="@height">
        <xsl:attribute name="height">
          <xsl:value-of select="@height" />
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="@relative">
        <xsl:attribute name="relative">
          <xsl:value-of select="@relative" />
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="@as">
        <xsl:attribute name="as">
          <xsl:value-of select="@as" />
        </xsl:attribute>
      </xsl:if>
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>
  <xsl:template name="mxPoint" match="mxPoint">
    <xsl:element name="mxPoint">
      <xsl:attribute name="x">
        <xsl:choose>
          <xsl:when test="@x = '0.0'">
            <xsl:value-of select="format-number(@x, '0.0')" />
          </xsl:when>
          <xsl:when test="@x">
            <xsl:value-of select="format-number(@x+$originx,'0.0')" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($originx,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <xsl:attribute name="y">
        <xsl:choose>
          <xsl:when test="@y = '0.0'">
            <xsl:value-of select="format-number(@y, '0.0')" />
          </xsl:when>
          <xsl:when test="@y">
            <xsl:value-of select="format-number(@y+$originy,'0.0')" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="format-number($originy,'0.0')" />
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <xsl:if test="@as">
        <xsl:attribute name="as">
          <xsl:value-of select="@as" />
        </xsl:attribute>
      </xsl:if>
    </xsl:element>
  </xsl:template>
  <xsl:template name="Array" match="Array[@as = 'points']">
    <xsl:element name="Array">
      <xsl:if test="@as">
        <xsl:attribute name="as">
          <xsl:value-of select="@as" />
        </xsl:attribute>
      </xsl:if>
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>

  <xsl:template name="generate-block">
    <xsl:param name="style"/>
    <xsl:param name="id"/>
    <xsl:param name="explicitInputPorts"/>
    <xsl:param name="implicitInputPorts"/>
    <xsl:param name="explicitOutputPorts"/>
    <xsl:param name="implicitOutputPorts"/>
    <xsl:param name="controlPorts"/>
    <xsl:param name="commandPorts"/>
    <xsl:param name="simulationFunction"/>
    <xsl:param name="display_parameter"/>
    <xsl:param name="data"/>

    <xsl:element name="mxCell">
      <xsl:attribute name="style"><xsl:value-of select="$style"/></xsl:attribute>
      <xsl:attribute name="id"><xsl:value-of select="$id"/></xsl:attribute>
      <xsl:attribute name="vertex">1</xsl:attribute>
      <xsl:attribute name="connectable">0</xsl:attribute>
      <xsl:attribute name="CellType">Component</xsl:attribute>
      <xsl:attribute name="blockprefix">XCOS</xsl:attribute>
      <xsl:attribute name="explicitInputPorts"><xsl:value-of select="$explicitInputPorts"/></xsl:attribute>
      <xsl:attribute name="implicitInputPorts"><xsl:value-of select="$implicitInputPorts"/></xsl:attribute>
      <xsl:attribute name="explicitOutputPorts"><xsl:value-of select="$explicitOutputPorts"/></xsl:attribute>
      <xsl:attribute name="implicitOutputPorts"><xsl:value-of select="$implicitOutputPorts"/></xsl:attribute>
      <xsl:attribute name="controlPorts"><xsl:value-of select="$controlPorts"/></xsl:attribute>
      <xsl:attribute name="commandPorts"><xsl:value-of select="$commandPorts"/></xsl:attribute>
      <xsl:attribute name="simulationFunction"><xsl:value-of select="$simulationFunction"/></xsl:attribute>
      <xsl:attribute name="sourceVertex">0</xsl:attribute>
      <xsl:attribute name="targetVertex">0</xsl:attribute>
      <xsl:attribute name="tarx">0</xsl:attribute>
      <xsl:attribute name="tary">0</xsl:attribute>

      <xsl:apply-templates select="mxGeometry"/>

      <Object as="displayProperties">
        <xsl:attribute name="display_parameter">
          <xsl:value-of select="$display_parameter"/>
        </xsl:attribute>
      </Object>

      <Object as="parameter_values">
        <xsl:for-each select="$data">
          <xsl:attribute name="{concat('p', format-number(position() - 1, '000'), '_value')}">
            <xsl:value-of select="@value" />
          </xsl:attribute>
        </xsl:for-each>
      </Object>
    </xsl:element>

    <xsl:call-template name="port">
      <xsl:with-param name="id" select="$id"/>
      <xsl:with-param name="explicitInputPorts" select="$explicitInputPorts"/>
      <xsl:with-param name="explicitOutputPorts" select="$explicitOutputPorts"/>
      <xsl:with-param name="implicitInputPorts" select="$implicitInputPorts"/>
      <xsl:with-param name="implicitOutputPorts" select="$implicitOutputPorts"/>
      <xsl:with-param name="controlPorts" select="$controlPorts"/>
      <xsl:with-param name="commandPorts" select="$commandPorts"/>
    </xsl:call-template>
  </xsl:template>
