<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="no" />
    <xsl:template match="@*|node()">
      <xsl:copy>
         <xsl:apply-templates select="@*|node()"/>
      </xsl:copy>
    </xsl:template>
    <xsl:template match="comment()"/>
    <xsl:template match="XcosDiagram">
      <xsl:apply-templates select="node()"/>
    </xsl:template>
    <xsl:template match="mxGraphModel">
      <xsl:copy>
         <xsl:apply-templates select="@*[name(.)!='as']"/>
         <xsl:apply-templates select="node()"/>
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
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
        <xsl:apply-templates select="node()"/>
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
        <Object as="parameter_values"/>
        <Object as="displayProperties"/>
        <xsl:apply-templates select="node()"/>
      </xsl:copy>
    </xsl:template>
    <xsl:template match="BasicBlock[@interfaceFunctionName = 'STEP_FUNCTION']">
      <xsl:element name="mxCell">
        <xsl:attribute name="style">
          <xsl:value-of select="@style" />
        </xsl:attribute>
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="vertex">1</xsl:attribute>
        <xsl:attribute name="connectable">0</xsl:attribute>
        <xsl:attribute name="CellType">Component</xsl:attribute>
        <xsl:attribute name="blockprefix">XCOS</xsl:attribute>
        <xsl:attribute name="explicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="implicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="explicitOutputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitOutputPorts">0</xsl:attribute>
        <xsl:attribute name="controlPorts">0</xsl:attribute>
        <xsl:attribute name="commandPorts">0</xsl:attribute>
        <xsl:attribute name="simulationFunction">
          <xsl:value-of select="@simulationFunctionName" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <Object display_parameter="" as="displayProperties"/>
        <Object p000_value="1" p001_value="0" p002_value="1" as="parameter_values"/>
        
      </xsl:element>
    </xsl:template>
    <xsl:template name="mxGeometry" match="mxGeometry">
        <xsl:copy>
          <xsl:attribute name="x">
            <xsl:value-of select="@x" />
          </xsl:attribute>
          <xsl:attribute name="y">
            <xsl:value-of select="@y" />
          </xsl:attribute>
          <xsl:attribute name="width">
            <xsl:value-of select="@width" />
          </xsl:attribute>
          <xsl:attribute name="height">
            <xsl:value-of select="@height" />
          </xsl:attribute>
          <xsl:attribute name="as">
            <xsl:value-of select="@as" />
          </xsl:attribute>
          <xsl:apply-templates />
        </xsl:copy>
    </xsl:template>
<!-- for no param -->
    <xsl:template match="BasicBlock[@interfaceFunctionName = 'DERIV' or @interfaceFunctionName = 'GAINBLK_f']">
      <xsl:element name="mxCell">
        <xsl:attribute name="style">
          <xsl:value-of select="@style" />
        </xsl:attribute>
        <xsl:attribute name="id">
          <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:attribute name="vertex">1</xsl:attribute>
        <xsl:attribute name="connectable">0</xsl:attribute>
        <xsl:attribute name="CellType">Component</xsl:attribute>
        <xsl:attribute name="blockprefix">XCOS</xsl:attribute>
        <xsl:attribute name="explicitInputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitInputPorts">0</xsl:attribute>
        <xsl:attribute name="explicitOutputPorts">1</xsl:attribute>
        <xsl:attribute name="implicitOutputPorts">0</xsl:attribute>
        <xsl:attribute name="controlPorts">0</xsl:attribute>
        <xsl:attribute name="commandPorts">0</xsl:attribute>
        <xsl:attribute name="simulationFunction">
          <xsl:value-of select="@simulationFunctionName" />
        </xsl:attribute>
        <xsl:attribute name="sourceVertex">0</xsl:attribute>
        <xsl:attribute name="targetVertex">0</xsl:attribute>
        <xsl:attribute name="tarx">0</xsl:attribute>
        <xsl:attribute name="tary">0</xsl:attribute>
        <xsl:apply-templates select="node()"/>
        <Object display_parameter="" as="displayProperties"/>
        <Object as="parameter_values"/>
        
      </xsl:element>
    </xsl:template>

    <xsl:template match="Array" />
    <xsl:template match="ScilabDouble" />
    <xsl:template match="ScilabInteger" />
    <xsl:template match="SuperBlockDiagram" />
    <xsl:template match="ScilabString" />
</xsl:stylesheet>
