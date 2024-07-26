      <xsl:template name="port">
        <xsl:param name="id" />
        <xsl:param name="explicitInputPorts" />
        <xsl:param name="explicitOutputPorts" />
        <xsl:param name="implicitInputPorts" />
        <xsl:param name="implicitOutputPorts" />
        <xsl:param name="controlPorts" />
        <xsl:param name="commandPorts" />
        <xsl:for-each select="key('k-in', $id)">
          <xsl:element name="mxCell">
            <xsl:attribute name="style">
            <xsl:value-of select="name(.)" />
            </xsl:attribute>
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
            <xsl:attribute name="vertex">1</xsl:attribute>
            <xsl:attribute name="CellType">Pin</xsl:attribute>
            <xsl:attribute name="ParentComponent">
              <xsl:value-of select="@parent" />
            </xsl:attribute>
            <xsl:attribute name="sourceVertex">0</xsl:attribute>
            <xsl:attribute name="targetVertex">0</xsl:attribute>
            <xsl:attribute name="tarx">0</xsl:attribute>
            <xsl:attribute name="tary">0</xsl:attribute>
            <mxGeometry x="0" width="8" height="8" relative="1" as="geometry">
              <xsl:variable name="numerator" select="2 * number($explicitInputPorts + $implicitInputPorts) - (2 * (position() - 1) + 1)" />
              <xsl:attribute name="y">
                <xsl:value-of select="$numerator div (2 * number($explicitInputPorts + $implicitInputPorts))"/>
              </xsl:attribute>
              <mxPoint x="-8" y="-4" as="offset"/>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>
        </xsl:for-each> 
        <xsl:for-each select="key('k-out', $id)">
          <xsl:element name="mxCell">
            <xsl:attribute name="style">
            <xsl:value-of select="name(.)" />
            </xsl:attribute>
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
            <xsl:attribute name="vertex">1</xsl:attribute>
            <xsl:attribute name="CellType">Pin</xsl:attribute>
            <xsl:attribute name="ParentComponent">
              <xsl:value-of select="@parent" />
            </xsl:attribute>
            <xsl:attribute name="sourceVertex">0</xsl:attribute>
            <xsl:attribute name="targetVertex">0</xsl:attribute>
            <xsl:attribute name="tarx">0</xsl:attribute>
            <xsl:attribute name="tary">0</xsl:attribute>
            <mxGeometry x="1" width="8" height="8" relative="1" as="geometry">
            <xsl:variable name="numerator" select="2 * number($explicitOutputPorts + $implicitOutputPorts) - (2 * (position() - 1) + 1)" />
            <xsl:attribute name="y">
              <xsl:value-of select="$numerator div (2 * number($explicitOutputPorts + $implicitOutputPorts))"/>
            </xsl:attribute>
            <mxPoint x="0" y="-4" as="offset"/>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>
        </xsl:for-each>
        <xsl:for-each select="key('k-command', $id)">
          <xsl:element name="mxCell">
            <xsl:attribute name="style">
            <xsl:value-of select="name(.)" />
            </xsl:attribute>
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
            <xsl:attribute name="vertex">1</xsl:attribute>
            <xsl:attribute name="CellType">Pin</xsl:attribute>
            <xsl:attribute name="ParentComponent">
              <xsl:value-of select="@parent" />
            </xsl:attribute>
            <xsl:attribute name="sourceVertex">0</xsl:attribute>
            <xsl:attribute name="targetVertex">0</xsl:attribute>
            <xsl:attribute name="tarx">0</xsl:attribute>
            <xsl:attribute name="tary">0</xsl:attribute>
            <mxGeometry x="0" width="8" height="8" relative="1" as="geometry">
              <xsl:variable name="numerator" select="2 * number($commandPorts) - (2 * (position() - 1) + 1)" />
              <xsl:attribute name="y">
                <xsl:value-of select="$numerator div (2 * number($commandPorts))"/>
              </xsl:attribute>
              <mxPoint x="-4" y="0" as="offset"/>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>
        </xsl:for-each>
        <xsl:for-each select="key('k-control', $id)">
          <xsl:element name="mxCell">
            <xsl:attribute name="style">
            <xsl:value-of select="name(.)" />
            </xsl:attribute>
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
            <xsl:attribute name="vertex">1</xsl:attribute>
            <xsl:attribute name="CellType">Pin</xsl:attribute>
            <xsl:attribute name="ParentComponent">
              <xsl:value-of select="@parent" />
            </xsl:attribute>
            <xsl:attribute name="sourceVertex">0</xsl:attribute>
            <xsl:attribute name="targetVertex">0</xsl:attribute>
            <xsl:attribute name="tarx">0</xsl:attribute>
            <xsl:attribute name="tary">0</xsl:attribute>
            <mxGeometry x="0" width="8" height="8" relative="1" as="geometry">
              <xsl:variable name="numerator" select="2 * number($controlPorts) - (2 * (position() - 1) + 1)" />
              <xsl:attribute name="y">
                <xsl:value-of select="$numerator div (2 * number($controlPorts))"/>
              </xsl:attribute>
              <mxPoint x="-4" y="-8" as="offset"/>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>
        </xsl:for-each>
      </xsl:template>
