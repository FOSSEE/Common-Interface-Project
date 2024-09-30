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
            <mxGeometry>
              <xsl:variable name="numerator" select="2 * position() - 1" />
              <xsl:attribute name="y">
                <xsl:value-of select="$numerator div (2 * number($explicitInputPorts + $implicitInputPorts))"/>
              </xsl:attribute>
              <xsl:attribute name="width">8</xsl:attribute>
              <xsl:attribute name="height">8</xsl:attribute>
              <xsl:attribute name="relative">1</xsl:attribute>
              <xsl:attribute name="as">geometry</xsl:attribute>
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
            <mxGeometry>
              <xsl:variable name="numerator" select="2 * position() - 1" />
              <xsl:attribute name="x">1</xsl:attribute>
              <xsl:attribute name="y">
                <xsl:value-of select="$numerator div (2 * number($explicitOutputPorts + $implicitOutputPorts))"/>
              </xsl:attribute>
              <xsl:attribute name="width">8</xsl:attribute>
              <xsl:attribute name="height">8</xsl:attribute>
              <xsl:attribute name="relative">1</xsl:attribute>
              <xsl:attribute name="as">geometry</xsl:attribute>
              <mxPoint y="-4" as="offset"/>
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
            <mxGeometry>
              <xsl:variable name="numerator" select="2 * position() - 1" />
              <xsl:attribute name="x">
                <xsl:value-of select="$numerator div (2 * number($commandPorts))"/>
              </xsl:attribute>
              <xsl:attribute name="y">1</xsl:attribute>
              <xsl:attribute name="width">8</xsl:attribute>
              <xsl:attribute name="height">8</xsl:attribute>
              <xsl:attribute name="relative">1</xsl:attribute>
              <xsl:attribute name="as">geometry</xsl:attribute>
              <mxPoint x="-4" as="offset"/>
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
            <mxGeometry>
              <xsl:variable name="numerator" select="2 * position() - 1" />
              <xsl:attribute name="x">
                <xsl:value-of select="$numerator div (2 * number($controlPorts))"/>
              </xsl:attribute>
              <xsl:attribute name="width">8</xsl:attribute>
              <xsl:attribute name="height">8</xsl:attribute>
              <xsl:attribute name="relative">1</xsl:attribute>
              <xsl:attribute name="as">geometry</xsl:attribute>
              <mxPoint x="-4" y="-8" as="offset"/>
            </mxGeometry>
            <Object as="parameter_values"/>
            <Object as="displayProperties"/>
          </xsl:element>
        </xsl:for-each>
      </xsl:template>
