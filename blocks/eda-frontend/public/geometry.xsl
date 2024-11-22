<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:ext="http://exslt.org/common"
  exclude-result-prefixes="xsl ext">

  <!-- copy all other nodes {{{1 -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
  <!-- }}}1 -->
  <xsl:key name="k-cell" match="mxCell" use="@id" />

<xsl:template match="mxPoint[@as='sourcePoint']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />
      
    <!-- variable newx -->
    <xsl:variable name="newx">
    <xsl:choose>
    <xsl:when test="(@x != '0.0' or @y != '0.0')">
        <xsl:value-of select="@x"/>
    </xsl:when>
    <xsl:when test="(@x = '0.0' and @y = '0.0')">
        <!-- Check for mxCell with sourceVertex -->
        
            <xsl:for-each select="key('k-cell', ancestor::mxCell/@sourceVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@x" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort' or $port = 'ControlPort'">
                                <xsl:value-of select="(@x + @width * (2 * $ordering -1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@x + @width" />
                            </xsl:when>
                        
                        </xsl:choose>
                    </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:variable name="newy">
    <xsl:choose>
    <xsl:when test="(@x != '0.0' or @y != '0.0')">
        <xsl:value-of select="@y"/>
    </xsl:when>
    <xsl:when test="(@x = '0.0' and @y = '0.0')">
        <!-- Check for mxCell with sourceVertex -->
            <xsl:for-each select="key('k-cell', ancestor::mxCell/@sourceVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                        <xsl:choose>
                            <xsl:when test="($port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort') or ($port = 'ImplicitInputPort' or $port = 'ExplicitInputPort')">
                                <xsl:value-of select="(@y + @height * (2 * $ordering - 1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@y + @height" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@y" />
                            </xsl:when>
                        
                        </xsl:choose>
                        </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:attribute name="x"> 
        <xsl:value-of select="$newx"/>
    </xsl:attribute>
    <xsl:attribute name="y">
        <xsl:value-of select="$newy"/>
    </xsl:attribute> 
    <xsl:apply-templates select="node()" />

    </xsl:copy>
</xsl:template>

<!-- targetpoint -->
<xsl:template match="mxPoint[@as='targetPoint']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />
      
    <!-- variable newx -->
    <xsl:variable name="newx">
    <xsl:choose>
    <xsl:when test="(@x != '0.0' or @y != '0.0')">
        <xsl:value-of select="@x"/>
    </xsl:when>
    <xsl:when test="(@x = '0.0' and @y = '0.0')">
        <!-- Check for mxCell with sourceVertex -->
        
            <xsl:for-each select="key('k-cell', ancestor::mxCell/@targetVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@x" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort' or $port = 'ControlPort'">
                                <xsl:value-of select="(@x + @width * (2 * $ordering -1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@x + @width" />
                            </xsl:when>
                        
                        </xsl:choose>
                    </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:variable name="newy">
    <xsl:choose>
    <xsl:when test="(@x != '0.0' or @y != '0.0')">
        <xsl:value-of select="@y"/>
    </xsl:when>
    <xsl:when test="(@x = '0.0' and @y = '0.0')">
        <!-- Check for mxCell with targetVertex -->
            <xsl:for-each select="key('k-cell', ancestor::mxCell/@targetVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches targetVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                        <xsl:choose>
                            <xsl:when test="($port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort') or ($port = 'ImplicitInputPort' or $port = 'ExplicitInputPort')">
                                <xsl:value-of select="(@y + @height * (2 * $ordering - 1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@y + @height" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@y" />
                            </xsl:when>
                        
                        </xsl:choose>
                        </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:attribute name="x"> 
        <xsl:value-of select="$newx"/>
    </xsl:attribute>
    <xsl:attribute name="y">
        <xsl:value-of select="$newy"/>
    </xsl:attribute> 
    <xsl:apply-templates select="node()" />

    </xsl:copy>
</xsl:template>
<!-- mxcell tarx & tary & tar2x & tar2y -->
<xsl:template match="mxCell[@edge='1']">
    <xsl:copy>
      <xsl:apply-templates select="@*" />
      <xsl:variable name="newtarx">
        <xsl:choose>
            <xsl:when test="(@tarx != '0.0' or @tary != '0.0')">
                <xsl:value-of select="@tarx"/>
            </xsl:when>
            <xsl:when test="(@tarx = '0.0' and @tary = '0.0')">
                <xsl:for-each select="key('k-cell', @sourceVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@x" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort' or $port = 'ControlPort'">
                                <xsl:value-of select="(@x + @width * (2 * $ordering -1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@x + @width" />
                            </xsl:when>
                        
                        </xsl:choose>
                    </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:variable name="newtary">
    <xsl:choose>
    <xsl:when test="(@tarx != '0.0' or @tary != '0.0')">
        <xsl:value-of select="@tary"/>
    </xsl:when>
    <xsl:when test="(@tarx = '0.0' and @tary = '0.0')">
        <!-- Check for mxCell with sourceVertex -->
            <xsl:for-each select="key('k-cell', @sourceVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                        <xsl:choose>
                            <xsl:when test="($port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort') or ($port = 'ImplicitInputPort' or $port = 'ExplicitInputPort')">
                                <xsl:value-of select="(@y + @height * (2 * $ordering - 1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@y + @height" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@y" />
                            </xsl:when>
                        
                        </xsl:choose>
                        </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
     

<!-- tar2x & tar2y -->
    <xsl:variable name="newtar2x">
    <xsl:choose>
    <xsl:when test="(@tar2x != '0.0' or @tar2y != '0.0')">
        <xsl:value-of select="@tar2x"/>
    </xsl:when>
    <xsl:when test="(@tar2x = '0.0' and @tar2y = '0.0')">
        <!-- Check for mxCell with sourceVertex -->
        
            <xsl:for-each select="key('k-cell', @targetVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches sourceVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@x" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort' or $port = 'ControlPort'">
                                <xsl:value-of select="(@x + @width * (2 * $ordering -1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@x + @width" />
                            </xsl:when>
                        
                        </xsl:choose>
                    </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>
    <xsl:variable name="newtar2y">
    <xsl:choose>
    <xsl:when test="(@tar2x != '0.0' or @tar2y != '0.0')">
        <xsl:value-of select="@tar2y"/>
    </xsl:when>
    <xsl:when test="(@tar2x = '0.0' and @tar2y = '0.0')">
        <!-- Check for mxCell with targetVertex -->
            <xsl:for-each select="key('k-cell', @targetVertex)">
                <xsl:variable name="ordering">
                    <xsl:value-of select="@ordering"/>
                </xsl:variable>
               
                <xsl:variable name="port" select="substring-before(@style, ';')"/>
            
            <!-- Find the mxCell whose id matches targetVertex -->
                <xsl:for-each select="key('k-cell', @ParentComponent)">
                    <xsl:variable name="noofport">
                        <xsl:choose>
                            <xsl:when test="$port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort'">
                                <xsl:value-of select="@implicitOutputPorts + @explicitOutputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ImplicitInputPort' or $port = 'ExplicitInputPort'">
                                <xsl:value-of select="@implicitInputPorts + @explicitInputPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@commandPorts" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@controlPorts" />
                            </xsl:when>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:for-each select="mxGeometry">
                        <xsl:choose>
                            <xsl:when test="($port = 'ImplicitOutputPort' or $port = 'ExplicitOutputPort') or ($port = 'ImplicitInputPort' or $port = 'ExplicitInputPort')">
                                <xsl:value-of select="(@y + @height * (2 * $ordering - 1) div (2 * $noofport))" />
                            </xsl:when>
                            <xsl:when test="$port = 'CommandPort'">
                                <xsl:value-of select="@y + @height" />
                            </xsl:when>
                            <xsl:when test="$port = 'ControlPort'">
                                <xsl:value-of select="@y" />
                            </xsl:when>
                        
                        </xsl:choose>
                        </xsl:for-each> 

                </xsl:for-each>
            </xsl:for-each>
 
    </xsl:when>
    </xsl:choose>
    </xsl:variable>

    <xsl:attribute name="tarx"> 
        <xsl:value-of select="$newtarx"/>
    </xsl:attribute>
    <xsl:attribute name="tary">
        <xsl:value-of select="$newtary"/>
    </xsl:attribute>
    <xsl:attribute name="tar2x"> 
        <xsl:value-of select="$newtar2x"/>
    </xsl:attribute>
    <xsl:attribute name="tar2y">
        <xsl:value-of select="$newtar2y"/>
    </xsl:attribute> 
    <xsl:apply-templates select="node()" />

    </xsl:copy>
</xsl:template>
</xsl:stylesheet>
