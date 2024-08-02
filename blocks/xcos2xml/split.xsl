<xsl:key name="k-input" match="ExplicitInputPort" use="@parent" />
<xsl:key name="k-output" match="ExplicitOutputPort" use="@parent" />
<xsl:key name="k-srclink" match="ExplicitLink" use="@source" />
<xsl:key name="k-tgtlink" match="ExplicitLink" use="@target" />
<xsl:key name="k-control" match="ControlPort" use="@parent" />
<xsl:key name="k-command" match="CommandPort" use="@parent" />
<xsl:key name="k-commandsrclink" match="CommandControlLink" use="@source" />
<xsl:key name="k-commandtgtlink" match="CommandControlLink" use="@target" />
<xsl:key name="k-implicitinput" match="ImplicitInputPort | ImplicitOutputPort" use="@parent" />
<!-- <xsl:key name="k-implicitoutput" match="ImplicitOutputPort" use="@parent" /> -->
<xsl:key name="k-implicitsrclink" match="ImplicitLink" use="@source" />
<xsl:key name="k-implicittgtlink" match="ImplicitLink" use="@target" />

    <xsl:template match="SplitBlock">
      
        <xsl:variable name="InputPort" select="key('k-input', @id)" />
        <xsl:variable name="OutputPort" select="key('k-output', @id)" />
        <xsl:variable name="InputPorts" select="count($InputPort)" />
        <xsl:variable name="OutputPorts" select="count($OutputPort)" />
        <xsl:variable name="targetoneid" select="$InputPort/@id" />
        <xsl:variable name="sourceoneid" select="$OutputPort/@id" />
        <xsl:variable name="targetonelink" select="key('k-tgtlink', $targetoneid)" />
        <xsl:variable name="sourceonelink" select="key('k-srclink', $sourceoneid)" />
        
        <xsl:variable name="ControlPort" select="key('k-control', @id)" />
        <xsl:variable name="CommandPort" select="key('k-command', @id)" />
        <xsl:variable name="ControlPorts" select="count($ControlPort)" />
        <xsl:variable name="CommandPorts" select="count($CommandPort)" />
        <xsl:variable name="targetcommandoneid" select="$ControlPort/@id" />
        <xsl:variable name="sourcecommandoneid" select="$CommandPort/@id" />
        <xsl:variable name="targetcommandonelink" select="key('k-commandtgtlink', $targetcommandoneid)" />
        <xsl:variable name="sourcecommandonelink" select="key('k-commandsrclink', $sourcecommandoneid)" />

        <xsl:variable name="ImplicitPort" select="key('k-implicitinput', @id)" />
        <!-- <xsl:variable name="ImplicitOutputPort" select="key('k-implicitoutput', @id)" /> -->
        <xsl:variable name="ImplicitPorts" select="count($ImplicitPort)" />
        <!-- <xsl:variable name="ImplicitOutputPorts" select="count($ImplicitOutputPort)" /> -->
        <xsl:variable name="targetimplicitoneid" select="$ImplicitPort/@id" />
        <xsl:variable name="sourceimplicitoneid" select="$ImplicitPort/@id" />
        <xsl:variable name="targetimplicitonelink" select="key('k-implicittgtlink', $targetimplicitoneid)" />
        <xsl:variable name="sourceimplicitonelink" select="key('k-implicitsrclink', $sourceimplicitoneid)" />
        <xsl:variable name="newidone" select="generate-id()" />
        <xsl:element name="TEST">
        <xsl:attribute name="ABC">
            <xsl:value-of select="$ImplicitPorts" />
        </xsl:attribute>
        <!-- <xsl:attribute name="ABC1">
            <xsl:value-of select="$targetimplicitoneid" />
        </xsl:attribute>
        <xsl:attribute name="DEF">
            <xsl:value-of select="$InputPorts" />
        </xsl:attribute>
        <xsl:attribute name="DEF1">
            <xsl:value-of select="$OutputPorts" />
        </xsl:attribute> -->
        </xsl:element>
        <xsl:variable name="geometry" select="mxGeometry" />
        <xsl:variable name="x" select="$geometry/@x" />
        <xsl:variable name="y" select="$geometry/@y" />

          <xsl:choose>
          <xsl:when test="($InputPorts + $OutputPorts) > 0">
            <xsl:element name="mxCell">
              <xsl:attribute name="id">
                <xsl:value-of select="$newidone" />
              </xsl:attribute>
              <xsl:attribute name="edge">1</xsl:attribute>

              <xsl:attribute name="sourceVertex">
                <xsl:value-of select="$targetonelink/@source" />
              </xsl:attribute>
              <xsl:attribute name="targetVertex">
                <xsl:value-of select="$sourceonelink/@target" />
              </xsl:attribute>
              <xsl:attribute name="node">.null</xsl:attribute>
              <xsl:attribute name="CellType">Unknown</xsl:attribute>
              <xsl:attribute name="tarx">0</xsl:attribute>
              <xsl:attribute name="tary">0</xsl:attribute>

              <mxGeometry relative="1" as="geometry">
                <Array as="points">
                  <xsl:for-each select="$sourceonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                  <xsl:element name="mxPoint">
                    <xsl:attribute name="x">
                        <xsl:value-of select="$x" />
                    </xsl:attribute>
                    <xsl:attribute name="y">
                        <xsl:value-of select="$y" />
                    </xsl:attribute>
                  </xsl:element>
                  <xsl:for-each select="$targetonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                </Array>
              </mxGeometry>
              <Object as="parameter_values"/>
              <Object as="displayProperties"/>
            </xsl:element>

            <xsl:choose>
              <xsl:when test="$OutputPorts = 2">
                <xsl:variable name="OutputtwoPort" select="$OutputPort[position()=2]" />
                <xsl:variable name="sourcetwoid" select="$OutputtwoPort/@id" />
                <xsl:variable name="sourcetwolink" select="key('k-srclink', $sourcetwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($targetonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$sourcetwolink/@target" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:when>

              <xsl:otherwise>
                <xsl:variable name="InputtwoPort" select="$InputPort[position()=2]" />
                <xsl:variable name="targettwoid" select="$InputtwoPort/@id" />
                <xsl:variable name="targettwolink" select="key('k-tgtlink', $targettwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($sourceonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$targettwolink/@source" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>

          <xsl:when test="($ControlPorts + $CommandPorts) > 0">
            <xsl:element name="mxCell">
              <xsl:attribute name="id">
                <xsl:value-of select="$newidone" />
              </xsl:attribute>
              <xsl:attribute name="edge">1</xsl:attribute>

              <xsl:attribute name="sourceVertex">
                <xsl:value-of select="$targetcommandonelink/@source" />
              </xsl:attribute>
              <xsl:attribute name="targetVertex">
                <xsl:value-of select="$sourcecommandonelink/@target" />
              </xsl:attribute>
              <xsl:attribute name="node">.null</xsl:attribute>
              <xsl:attribute name="CellType">Unknown</xsl:attribute>
              <xsl:attribute name="tarx">0</xsl:attribute>
              <xsl:attribute name="tary">0</xsl:attribute>

              <mxGeometry relative="1" as="geometry">
                <Array as="points">
                  <xsl:for-each select="$sourcecommandonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                  <xsl:element name="mxPoint">
                    <xsl:attribute name="x">
                        <xsl:value-of select="$x" />
                    </xsl:attribute>
                    <xsl:attribute name="y">
                        <xsl:value-of select="$y" />
                    </xsl:attribute>
                  </xsl:element>
                  <xsl:for-each select="$targetcommandonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                </Array>
              </mxGeometry>
              <Object as="parameter_values"/>
              <Object as="displayProperties"/>
            </xsl:element>

            <xsl:choose>
              <xsl:when test="$CommandPorts = 2">
                <xsl:variable name="CommmandtwoPort" select="$CommandPort[position()=2]" />
                <xsl:variable name="sourcecommandtwoid" select="$CommandtwoPort/@id" />
                <xsl:variable name="sourcecommandtwolink" select="key('k-commandsrclink', $sourcecommandtwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($targetcommandonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$sourcecommandtwolink/@target" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:when>

              <xsl:otherwise>
                <xsl:variable name="ControltwoPort" select="$ControlPort[position()=2]" />
                <xsl:variable name="targetcommandtwoid" select="$ControltwoPort/@id" />
                <xsl:variable name="targetcommandtwolink" select="key('k-commandtgtlink', $targetcommandtwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($sourcecommandonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$targetcommandtwolink/@source" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          
          <xsl:otherwise>  
            <xsl:element name="mxCell">
              <xsl:attribute name="id">
                <xsl:value-of select="$newidone" />
              </xsl:attribute>
              <xsl:attribute name="edge">1</xsl:attribute>

              <xsl:attribute name="sourceVertex">
                <xsl:value-of select="$targetimplicitonelink/@source" />
              </xsl:attribute>
              <xsl:attribute name="targetVertex">
                <xsl:value-of select="$sourceimplicitonelink/@target" />
              </xsl:attribute>
              <xsl:attribute name="node">.null</xsl:attribute>
              <xsl:attribute name="CellType">Unknown</xsl:attribute>
              <xsl:attribute name="tarx">0</xsl:attribute>
              <xsl:attribute name="tary">0</xsl:attribute>

              <mxGeometry relative="1" as="geometry">
                <Array as="points">
                  <xsl:for-each select="$sourceimplicitonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                  <xsl:element name="mxPoint">
                    <xsl:attribute name="x">
                        <xsl:value-of select="$x" />
                    </xsl:attribute>
                    <xsl:attribute name="y">
                        <xsl:value-of select="$y" />
                    </xsl:attribute>
                  </xsl:element>
                  <xsl:for-each select="$targetimplicitonelink/mxGeometry/Array/mxPoint">
                    <xsl:copy-of select="." />
                  </xsl:for-each>
                </Array>
              </mxGeometry>
              <Object as="parameter_values"/>
              <Object as="displayProperties"/>
            </xsl:element>

            <xsl:choose>
              <xsl:when test="$ImplicitPorts = 3">
                <xsl:variable name="ImplicittwoPort" select="$ImplicitPort[position()=3]" />
                <xsl:variable name="sourceimplicittwoid" select="$ImplicittwoPort/@id" />
                <xsl:variable name="sourceimplicittwolink" select="key('k-implicitsrclink', $sourceimplicittwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($targetimplicitonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$sourceimplicittwolink/@target" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:when>

              <xsl:otherwise>
                <xsl:variable name="ImplicitInputtwoPort" select="$ImplicitPort[position()=2]" />
                <xsl:variable name="targetimplicittwoid" select="$ImplicitInputtwoPort/@id" />
                <xsl:variable name="targetimplicittwolink" select="key('k-implicittgtlink', $targetimplicittwoid)" />
                  <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                      <xsl:value-of select="generate-id($sourceimplicitonelink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                      <xsl:value-of select="$targetimplicittwolink/@source" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                      <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="node">.null</xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                    <xsl:attribute name="tarx">0</xsl:attribute>
                    <xsl:attribute name="tary">0</xsl:attribute>
                    <Object as="parameter_values"/>
                    <Object as="displayProperties"/>
                  </xsl:element>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ExplicitLink | CommandControlLink | ImplicitLink">
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
          </xsl:copy>
        </xsl:when>
      </xsl:choose>
     </xsl:template>

    <xsl:template match="ExplicitInputPort | ExplicitOutputPort | ImplicitInputPort | ImplicitOutputPort | ControlPort | CommandPort">
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
