    <xsl:template match="mxCell[contains(@id, '#identifier')]" />
    <xsl:template match="mxCell[@as = 'defaultParent']" />
    <xsl:template match="mxPoint[@as = 'origin']" />
    <xsl:template match="Array[@as != 'points']"/>
    <xsl:template match="ScilabDouble" />
    <xsl:template match="ScilabInteger" />
    <xsl:template match="SuperBlockDiagram" />
    <xsl:template match="ScilabString" />
    <xsl:template match="ExplicitInputPort" />
    <xsl:template match="ExplicitOutputPort" />
    <xsl:template match="ImplicitInputPort" />
    <xsl:template match="ImplicitOutputPort" />
    <xsl:template match="CommandPort" />
    <xsl:template match="ControlPort" />
</xsl:stylesheet>
