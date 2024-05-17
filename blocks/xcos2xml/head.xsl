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
    <xsl:template name="mxGeometry" match="mxGeometry">
        <xsl:element name="mxGeometry">
            <xsl:if test="@x">
                <xsl:attribute name="x">
                    <xsl:value-of select="@x" />
                </xsl:attribute>
            </xsl:if>
            <xsl:if test="@y">
                <xsl:attribute name="y">
                    <xsl:value-of select="@y" />
                </xsl:attribute>
            </xsl:if>
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
            <xsl:if test="@as">
                <xsl:attribute name="as">
                    <xsl:value-of select="@as" />
                </xsl:attribute>
            </xsl:if>
            <xsl:if test="@y">
                <xsl:attribute name="y">
                    <xsl:value-of select="@y" />
                </xsl:attribute>
            </xsl:if>
            <!-- <xsl:apply-templates /> -->
        </xsl:element>
    </xsl:template>
