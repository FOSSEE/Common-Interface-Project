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
