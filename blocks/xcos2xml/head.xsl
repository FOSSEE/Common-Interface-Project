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

  <xsl:template name="si-format">
        <xsl:param name="num" />

        <!-- Compute absolute value manually -->
        <xsl:variable name="absNum">
            <xsl:choose>
                <xsl:when test="$num &lt; 0"><xsl:value-of select="-$num" /></xsl:when>
                <xsl:otherwise><xsl:value-of select="$num" /></xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <!-- Compute exponent -->
        <xsl:variable name="exponent">
            <xsl:choose>
                <xsl:when test="$absNum = 0">0</xsl:when>
                <xsl:otherwise>
                    <xsl:call-template name="compute-exp">
                        <xsl:with-param name="n" select="$absNum" />
                        <xsl:with-param name="exp" select="0" />
                    </xsl:call-template>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <!-- Define SI prefixes -->
        <xsl:choose>
            <xsl:when test="$exponent &gt;= -2 and $exponent &lt;= 0">
                <xsl:value-of select="round($num div 1E-3)" /> m
            </xsl:when>
            <xsl:when test="$exponent &gt;= -5 and $exponent &lt;= -3">
                <xsl:value-of select="round($num div 1E-6)" /> &#956;  <!-- Unicode for μ -->
            </xsl:when>
            <xsl:when test="$exponent &gt;= -8 and $exponent &lt;= -6">
                <xsl:value-of select="round($num div 1E-9)" /> n
            </xsl:when>
            <xsl:when test="$exponent &gt;= -11 and $exponent &lt;= -9">
                <xsl:value-of select="round($num div 1E-12)" /> p
            </xsl:when>
            <xsl:when test="$exponent &gt;= 1 and $exponent &lt;= 3">
                <xsl:value-of select="round($num div 1)" />
            </xsl:when>
            <xsl:when test="$exponent &gt;= 4 and $exponent &lt;= 6">
                <xsl:value-of select="round($num div 1E3)" /> k</xsl:when>
            <xsl:when test="$exponent &gt;= 7 and $exponent &lt;= 9">
                <xsl:value-of select="round($num div 1E6)" /> M
            </xsl:when>
            <xsl:when test="$exponent &gt;= 10 and $exponent &lt;= 12">
                <xsl:value-of select="round($num div 1E9)" /> G
            </xsl:when>
            <xsl:when test="$exponent &gt;= 13 and $exponent &lt;= 15">
                <xsl:value-of select="round($num div 1E12)" /> T
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$num" /> 10^<xsl:value-of select="$exponent " />
            </xsl:otherwise>
        </xsl:choose>
  </xsl:template>
    <!-- Recursive template to compute the exponent -->
  <xsl:template name="compute-exp">
        <xsl:param name="n" />
        <xsl:param name="exp" />

        <xsl:choose>
            <xsl:when test="$n &lt; 1">
                <xsl:call-template name="compute-exp">
                    <xsl:with-param name="n" select="$n * 10" />
                    <xsl:with-param name="exp" select="$exp - 1" />
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="$n &gt;= 10">
                <xsl:call-template name="compute-exp">
                    <xsl:with-param name="n" select="$n div 10" />
                    <xsl:with-param name="exp" select="$exp + 1" />
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$exp" />
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
    <xsl:param name="explicitInputPorts"/>
    <xsl:param name="implicitInputPorts"/>
    <xsl:param name="explicitOutputPorts"/>
    <xsl:param name="implicitOutputPorts"/>
    <xsl:param name="controlPorts"/>
    <xsl:param name="commandPorts"/>
    <xsl:param name="blockId"/>
    <xsl:param name="style"/>
    <xsl:param name="simulationFunction"/>

    <xsl:element name="mxCell">
        <xsl:attribute name="style"><xsl:value-of select="$style"/></xsl:attribute>
        <xsl:attribute name="id"><xsl:value-of select="$blockId"/></xsl:attribute>
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
            <xsl:value-of select="*[@as='exprs']/data/@value"/>
        </xsl:attribute>
        </Object>
        <Object as="parameter_values">
        <xsl:attribute name="p000_value">
            <xsl:value-of select="*[@as='exprs']/data/@value"/>
        </xsl:attribute>
        </Object>
    </xsl:element>

    <xsl:call-template name="port">
        <xsl:with-param name="id" select="$blockId"/>
        <xsl:with-param name="explicitInputPorts" select="$explicitInputPorts"/>
        <xsl:with-param name="explicitOutputPorts" select="$explicitOutputPorts"/>
        <xsl:with-param name="implicitInputPorts" select="$implicitInputPorts"/>
        <xsl:with-param name="implicitOutputPorts" select="$implicitOutputPorts"/>
        <xsl:with-param name="controlPorts" select="$controlPorts"/>
        <xsl:with-param name="commandPorts" select="$commandPorts"/>
    </xsl:call-template>
  </xsl:template>
