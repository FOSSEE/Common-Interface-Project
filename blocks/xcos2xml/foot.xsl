    <xsl:template match="mxCell[contains(@id, '#identifier')]" />
    <xsl:template match="mxCell[@as = 'defaultParent']" />
    <xsl:template match="Array[@as != 'points']"/>
    <xsl:template match="ScilabDouble" />
    <xsl:template match="ScilabInteger" />
    <xsl:template match="SuperBlockDiagram" />
    <xsl:template match="ScilabString" />
</xsl:stylesheet>
