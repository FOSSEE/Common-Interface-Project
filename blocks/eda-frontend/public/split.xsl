<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:ext="http://exslt.org/common"
  xmlns:fCondInInterval="f:fCondInInterval"
  xmlns:fScaleByE="f:fScaleByE"
  xmlns:x="f:x-exp.xsl"
  exclude-result-prefixes="xsl ext fCondInInterval fScaleByE x"
>
<xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
<xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
<xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
<xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />
<xsl:key name="k-exin" match="ExplicitInputPort" use="@id" />
<xsl:key name="k-exout" match="ExplicitOutputPort" use="@id" />
<xsl:key name="k-split" match="SplitBlock" use="@id" />

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
    
    <xsl:template match="SplitBlock">
        <xsl:for-each select="key('k-input', @id)">
            <xsl:for-each select="key('k-tgtlink', @id)">
                <xsl:for-each select="key('k-exout', @source)">
                    <newlink id="{generate-id()}">
                        <xsl:attribute name="linkid">
                            <xsl:value-of select="@id"/>
                        </xsl:attribute>
                    </newlink>
                </xsl:for-each>
            </xsl:for-each> 
        </xsl:for-each>

        <xsl:for-each select="key('k-output', @id)">
            <xsl:for-each select="key('k-srclink', @id)">
                <xsl:for-each select="key('k-exin', @target)">
                    <newlink id="{generate-id()}">
                        <xsl:attribute name="linkid1">
                            <xsl:value-of select="@id"/>
                        </xsl:attribute>
                    </newlink>
                </xsl:for-each>
            </xsl:for-each>
        </xsl:for-each>
        
    </xsl:template>

    <xsl:template match="ExplicitLink">
      <xsl:variable name="sourceId" select="@source"/>
      <xsl:variable name="sourceElement" select="//*[@id = $sourceId]"/>
      <xsl:variable name="sourceElemId" select="$sourceElement[@parent]"/>
      <xsl:variable name="parentElement" select="//*[@id = sourceElemId]"/>
      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
              <xsl:attribute name="test4">
                <xsl:value-of select="name($sourceElement)" />
              </xsl:attribute>
              <xsl:attribute name="test5">
                <xsl:value-of select="$sourceId" />
              </xsl:attribute>
              <xsl:attribute name="test6">
                <xsl:value-of select="name($parentElement)" />
              </xsl:attribute>
              <xsl:attribute name="test7">
                <xsl:value-of select="sourceElemId" />
              </xsl:attribute>
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

    <xsl:template match="ExplicitInputPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $parentId]"/>
      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
              <!-- <xsl:attribute name="test">
                <xsl:value-of select="name($parentElement)" />
              </xsl:attribute>
              <xsl:attribute name="test1">
                <xsl:value-of select="$parentId" />
              </xsl:attribute> -->
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

     <xsl:template match="ExplicitOutputPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $parentId]"/>
      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
              <!-- <xsl:attribute name="test2">
                <xsl:value-of select="name($parentElement)" />
              </xsl:attribute>
              <xsl:attribute name="test3">
                <xsl:value-of select="$parentId" />
              </xsl:attribute> -->
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

     
     <!-- select="key('k-split', @parent)"/> -->
  


    <xsl:template match="*">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:copy/>
    </xsl:template>
    
  <!-- <xsl:template match="SplitBlock"/> -->
<!-- <xsl:template match="ExplicitLink[
    (@source = //newlink[@linkid = current()/@id]/@id)]"/>
  <xsl:template match="ExplicitInputPort[@parent=current()/@id]"/> -->
  <!-- <xsl:template match="ExplicitOutputPort[@parent='14']"/> -->
  <!-- <xsl:template match="ExplicitLink[@parent='1' and (@source='7' or @source='16' or @source='17')]"/> -->
</xsl:stylesheet>
