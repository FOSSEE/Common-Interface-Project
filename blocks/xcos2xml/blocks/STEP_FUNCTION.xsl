    <xsl:template match="BasicBlock[@interfaceFunctionName='STEP_FUNCTION']">
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
