<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:ext="http://exslt.org/common"
  xmlns:fCondInInterval="f:fCondInInterval"
  xmlns:fScaleByE="f:fScaleByE"
  xmlns:x="f:x-exp.xsl"
  exclude-result-prefixes="xsl ext fCondInInterval fScaleByE x"
>

<!--
===========================================================================
 Stylesheet: iter.xsl       General Iteration of a Function
    Version: 1.0 (2002-03-16)
     Author: Dimitre Novatchev
     Notice: Copyright (c)2002 D.Novatchev  ALL RIGHTS RESERVED.
             No limitation on use - except this code may not be published,
             in whole or in part, without prior written consent of the
             copyright owner.
===========================================================================
-->
<!--
===========================================================================
       this implements functional power composition,
       that is f(f(...f(x)))))...)

       f composed with itself n - 1 times

       The corresponding Haskell code is:
        > iter :: (Ord a, Num a) => a -> (b -> b) -> b -> b
        > iter n f
        >    | n > 0     = f . iter (n-1) f
        >    | otherwise = id
===========================================================================
-->
<!--
===========================================================================
       This is a variation of the iter function.
       Iterations are performed only while the predicate p
       is true on the argument of the iteration
===========================================================================
-->
<!--
    Template: iterUntil
     Purpose: Iterate (compose a function with itself)
              until a condition is satisfied
  Parameters:-
    $pCond  - a template reference to a predicate that tests
              the iteration stop-condition. Returns 0 or 1
    $pFun   - a template reference to the function that's to be iterated
    $arg1   - an initial argument to the function
========================================================================== 
-->
   <xsl:template name="iterUntil">
    <xsl:param name="pCond" select="/.."/>
    <xsl:param name="pFun" select="/.."/>
    <xsl:param name="arg1" select="/.."/>

    <xsl:variable name="vCond">
      <xsl:apply-templates select="$pCond">
        <xsl:with-param name="arg1" select="$arg1"/>
      </xsl:apply-templates>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="$vCond = 1" >
        <xsl:copy-of select="$arg1"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="vrtfFunResult">
            <xsl:apply-templates select="$pFun">
              <xsl:with-param name="arg1" select="$arg1"/>
            </xsl:apply-templates>
        </xsl:variable>

        <xsl:call-template name="iterUntil">
          <xsl:with-param name="pCond" select="$pCond"/>
          <xsl:with-param name="pFun" select="$pFun"/>
          <xsl:with-param name="arg1"
                 select="ext:node-set($vrtfFunResult)/node()"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

<!--
===========================================================================
 Stylesheet: iter.xsl       General Iteration of a Function
===========================================================================
-->

<!--
===========================================================================
 Stylesheet: exp.xsl
    Version: 1.0 (2002-03-16)
     Author: Dimitre Novatchev
     Notice: Copyright (c)2002 D.Novatchev  ALL RIGHTS RESERVED.
             No limitation on use - except this code may not be published,
             in whole or in part, without prior written consent of the
             copyright owner.
===========================================================================
-->
<!--
      Template: ln
      Purpose : Return the value of ln(X)
    Parameters:
    $pX       - the real value X, to be used in calculating ln(X)
    $pEps     - [optional] accuracy required
                increase the number of decimal places for greater accuracy
                but at the expense of performance.
========================================================================== 
-->
   <xsl:template name="ln">
     <xsl:param name="pX"/>
     <xsl:param name="pEps" select=".00000001"/>

     <xsl:if test="not($pX > 0)">
       <xsl:message terminate="yes">
         <xsl:value-of
         select="concat('[Error]ln: non-positive argument passed:',
                        $pX)"/>
       </xsl:message>
     </xsl:if>

     <xsl:variable name="vrtfReduceArg">
       <cnt>0</cnt>
       <x><xsl:value-of select="$pX"/></x>
     </xsl:variable>

     <xsl:variable name="vCondInInterval"
                   select="$x:st/fCondInInterval:*[1]"/>
     <xsl:variable name="vScaleByE"
                   select="$x:st/fScaleByE:*[1]"/>

     <xsl:variable name="vrtfScaledArg">
         <xsl:call-template name="iterUntil">
           <xsl:with-param name="pCond" select="$vCondInInterval"/>
           <xsl:with-param name="pFun" select="$vScaleByE"/>
           <xsl:with-param name="arg1"
                           select="ext:node-set($vrtfReduceArg)/*"/>
         </xsl:call-template>
     </xsl:variable>

     <xsl:variable name="vIntTerm"
     select="ext:node-set($vrtfScaledArg)/cnt"/>

     <xsl:variable name="vFracTerm"
     select="ext:node-set($vrtfScaledArg)/x"/>

     <xsl:variable name="vPartResult">
         <xsl:call-template name="lnIter">
           <xsl:with-param name="pX" select="$vFracTerm - 1"/>
           <xsl:with-param name="pRslt" select="$vFracTerm - 1"/>
           <xsl:with-param name="pElem" select="$vFracTerm - 1"/>
           <xsl:with-param name="pN" select="1"/>
           <xsl:with-param name="pEps" select="$pEps"/>
         </xsl:call-template>
     </xsl:variable>

     <xsl:value-of select="$vIntTerm + $vPartResult"/>
   </xsl:template>

<!--
      Template: log
      Purpose : Return the value of log(base, X)
                (the logarithm of X using base base)
    Parameters:
    $pX       - the real value X, to be used in calculating log(base, X)
    $pBase    - [optional] the value for the base of the logarithm (10)
    $pEps     - [optional] accuracy required
                increase the number of decimal places for greater accuracy
                but at the expense of performance.
========================================================================== 
-->
   <xsl:template name="log">
     <xsl:param name="pX"/>
     <xsl:param name="pBase" select="10"/>
     <xsl:param name="pEps" select=".00000001"/>

     <xsl:if test="not($pBase > 0 and $pBase != 1)">
       <xsl:message terminate="yes">
         <xsl:value-of select="concat('[Error]log: Invalid log base: ',
                                      $pBase
                                      )"/>
       </xsl:message>
     </xsl:if>

     <xsl:variable name="vLogBase">
       <xsl:call-template name="ln">
         <xsl:with-param name="pX" select="$pBase"/>
         <xsl:with-param name="pEps" select="$pEps"/>
       </xsl:call-template>
     </xsl:variable>

     <xsl:variable name="vLnX">
       <xsl:call-template name="ln">
         <xsl:with-param name="pX" select="$pX"/>
         <xsl:with-param name="pEps" select="$pEps"/>
       </xsl:call-template>
     </xsl:variable>

     <xsl:value-of select="round($vLnX div $vLogBase)"/>
   </xsl:template>

<!--
      Template: log2
      Purpose : Return the value of the binary logarithm of X
                (the logarithm of X using base 2)
    Parameters:
    $pX       - the real value X, to be used in calculating log2(X)
    $pEps     - [optional] accuracy required
                increase the number of decimal places for greater accuracy
                but at the expense of performance.
========================================================================== 
-->
   <xsl:template name="log2">
     <xsl:param name="pX"/>
     <xsl:param name="pEps" select=".00000001"/>

     <xsl:call-template name="log">
       <xsl:with-param name="pX" select="$pX"/>
       <xsl:with-param name="pBase" select="2"/>
       <xsl:with-param name="pEps" select="$pEps"/>
     </xsl:call-template>
   </xsl:template>

  <!-- ************************************************************* -->
  <!-- ********************* INTERNAL USE ONLY ********************* -->
  <!-- ************************************************************* -->
  <!-- defined constants -->
   <xsl:variable name="vE" select="2.71828182845904"/>
   <xsl:variable name="x:st" select="document('')/*"/>

   <fCondInInterval:fCondInInterval/>
   <fScaleByE:fScaleByE/>

   <xsl:template name="lnIter">
       <xsl:param name="pX"/>
       <xsl:param name="pRslt"/>
       <xsl:param name="pElem"/>
       <xsl:param name="pN"/>
       <xsl:param name="pEps"/>

       <xsl:variable name="vnextN" select="$pN+1"/>

       <xsl:variable name="vnewElem" select="-$pElem*$pX"/>

       <xsl:variable name="vnewResult"
                     select="$pRslt + $vnewElem div $vnextN"/>

       <xsl:variable name="vdiffResult" select="$vnewResult - $pRslt"/>
       <xsl:choose>
         <xsl:when test="$vdiffResult > $pEps or $vdiffResult &lt; -$pEps">
           <xsl:call-template name="lnIter">
             <xsl:with-param name="pX" select="$pX"/>
             <xsl:with-param name="pRslt" select="$vnewResult"/>
             <xsl:with-param name="pElem" select="$vnewElem"/>
             <xsl:with-param name="pN" select="$vnextN"/>
             <xsl:with-param name="pEps" select="$pEps"/>
           </xsl:call-template>
         </xsl:when>
         <xsl:otherwise>
           <xsl:value-of select="$vnewResult"/>
         </xsl:otherwise>
       </xsl:choose>
   </xsl:template>

   <xsl:template match="fCondInInterval:*">
     <xsl:param name="arg1" select="/.."/>

     <xsl:variable name="vX" select="number($arg1[name()='x'])"/>

     <xsl:choose>
       <xsl:when test="$vX >= 0.5 and $vX &lt;= 1.5">1</xsl:when>
       <xsl:otherwise>0</xsl:otherwise>
     </xsl:choose>
   </xsl:template>

   <xsl:template match="fScaleByE:*">
     <xsl:param name="arg1" select="/.."/>

     <xsl:variable name="vCnt" select="number($arg1[name()='cnt'])"/>
     <xsl:variable name="vX" select="number($arg1[name()='x'])"/>

     <xsl:choose>
       <xsl:when test="$vX > 1.5">
         <cnt><xsl:value-of select="$vCnt + 1"/></cnt>
         <x><xsl:value-of select="$vX div $vE"/></x>
       </xsl:when>
       <xsl:otherwise>
         <cnt><xsl:value-of select="$vCnt - 1"/></cnt>
         <x><xsl:value-of select="$vX * $vE"/></x>
       </xsl:otherwise>
     </xsl:choose>
   </xsl:template>
<!--
===========================================================================
 Stylesheet: exp.xsl
===========================================================================
-->

    <xsl:output method="xml" indent="no" />
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
            <!-- <xsl:apply-templates /> -->
        </xsl:element>
    </xsl:template>
    <xsl:template name="Array" match="Array[@as = 'points']">
        <xsl:element name="Array">
            <xsl:if test="@as">
                <xsl:attribute name="as">
                    <xsl:value-of select="@as" />
                </xsl:attribute>
            </xsl:if>
            <xsl:apply-templates />
        </xsl:element>
    </xsl:template>
