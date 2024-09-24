<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    
    <!-- Main processing template -->
    <xsl:template match="SplitBlock">
        <!-- Process the first part exactly once and store it -->
        <xsl:variable name="processedPart">
            <xsl:call-template name="process-part-one"/>
        </xsl:variable>

        <!-- Now process the second part, using the stored result -->
        <root xmlns="http://www.example.org/root"> <!-- Namespace added -->
            <!-- Copy the processed first part -->
            <xsl:copy-of select="$processedPart"/>
            
            <!-- Process the second part, passing the processed first part -->
            <xsl:apply-templates select="//part[@id='2']" mode="process-dependently">
                <xsl:with-param name="dependency" select="$processedPart"/>
            </xsl:apply-templates>
        </root>
    </xsl:template>

    <!-- Template to process the first part -->
    <xsl:template name="process-part-one">
        <!-- Define necessary variables -->
        <xsl:variable name="InputPort" select="key('k-input', @id)" />
        <xsl:variable name="OutputPort" select="key('k-output', @id)" />
        <xsl:variable name="InputPorts" select="count($InputPort)" />
        <xsl:variable name="OutputPorts" select="count($OutputPort)" />
        <xsl:variable name="targetoneid" select="$InputPort/@id" />
        <xsl:variable name="sourceoneid" select="$OutputPort/@id" />
        <xsl:variable name="targetonelink" select="key('k-tgtlink', $targetoneid)" />
        <xsl:variable name="sourceonelink" select="key('k-srclink', $sourceoneid)" />
        <xsl:variable name="newidone" select="generate-id()" />

        <!-- Create mxCell for the first part -->
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
            <xsl:attribute name="CellType">Unknown</xsl:attribute>

            <!-- Copy mxGeometry points -->
            <mxGeometry relative="1" as="geometry">
                <Array as="points">
                    <xsl:for-each select="$targetonelink/mxGeometry/Array/mxPoint">
                        <xsl:copy-of select="." />
                    </xsl:for-each>
                    <xsl:for-each select="$sourceonelink/mxGeometry/Array/mxPoint">
                        <xsl:copy-of select="." />
                    </xsl:for-each>
                </Array>
            </mxGeometry>
        </xsl:element>

        <!-- Conditionally process other ports -->
        <xsl:choose>
            <xsl:when test="$OutputPorts = 2">
                <xsl:variable name="OutputtwoPort" select="$OutputPort[position()=2]" />
                <xsl:variable name="sourcetwoid" select="$OutputtwoPort/@id" />
                <xsl:variable name="sourcetwolink" select="key('k-srclink', $sourcetwoid)" />
                <xsl:element name="mxCell">
                    <xsl:attribute name="id">
                        <xsl:value-of select="generate-id($sourcetwolink)" />
                    </xsl:attribute>
                    <xsl:attribute name="edge">1</xsl:attribute>
                    <xsl:attribute name="sourceVertex">
                        <xsl:value-of select="$sourcetwolink/@target" />
                    </xsl:attribute>
                    <xsl:attribute name="targetVertex">
                        <xsl:value-of select="$newidone" />
                    </xsl:attribute>
                    <xsl:attribute name="CellType">Unknown</xsl:attribute>
                </xsl:element>
            </xsl:when>

            <xsl:otherwise>
                <!-- Similar block for InputPorts if needed -->
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- Template to process the second part -->
    <xsl:template match="part[@id='2']" mode="process-dependently">
        <xsl:param name="dependency"/>
        <part id="2">
            <xsl:text>Dependent on part 1: </xsl:text>
            <xsl:value-of select="$dependency"/>
        </part>
    </xsl:template>

</xsl:stylesheet>


