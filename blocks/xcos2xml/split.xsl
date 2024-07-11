<xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
<xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
<xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
<xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />
<xsl:key name="k-link" match="ExplicitLink" use="@id" />
<xsl:key name="k-exin" match="ExplicitInputPort" use="@id" />
<xsl:key name="k-exout" match="ExplicitOutputPort" use="@id" />
<xsl:key name="k-split" match="SplitBlock" use="@id" />

    <xsl:template match="SplitBlock">
        <xsl:for-each select="key('k-input', @id)">
            <xsl:for-each select="key('k-tgtlink', @id)">
                <!-- <link>
                  <xsl:attribute name="tgtlinkid">
                    <xsl:value-of select="@id"/>
                  </xsl:attribute>
                </link> -->
                <xsl:for-each select="key('k-exout', @source)">
                    <newlink id="{generate-id()}">
                        <xsl:attribute name="linkid">
                            <xsl:value-of select="@id"/>
                        </xsl:attribute>
                    </newlink>
                </xsl:for-each>
                <!-- <xsl:if test="@id = key('k-link', @id)">
                <xsl:copy>
                    <xsl:copy-of select="@*"/>
                </xsl:copy>
            </xsl:if> -->
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
      <xsl:variable name="sourceElemId" select="$sourceElement/@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $sourceElemId]"/>
      <xsl:variable name="targetId" select="@target"/>
      <xsl:variable name="targetElement" select="//*[@id = $targetId]"/>
      <xsl:variable name="targetElemId" select="$targetElement/@parent"/>
      <xsl:variable name="parentTargetElement" select="//*[@id = $targetElemId]"/>

      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock' and name($parentTargetElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
              <!-- <xsl:attribute name="test4">
                <xsl:value-of select="$sourceId" />
              </xsl:attribute>
              <xsl:attribute name="test5">
                <xsl:value-of select="name($sourceElement)" />
              </xsl:attribute> -->
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort">
      <xsl:variable name="parentId" select="@parent"/>
      <xsl:variable name="parentElement" select="//*[@id = $parentId]"/>
      <xsl:choose>
        <xsl:when test="name($parentElement) != 'SplitBlock'" >
          
          <xsl:copy>
            <xsl:copy-of select="@*"/>
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>
     
     <!-- select="key('k-split', @parent)"/> --> 

    <!-- <xsl:template match="*">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:copy/>
    </xsl:template> -->
