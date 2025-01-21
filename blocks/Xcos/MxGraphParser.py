#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from xcosblocks import SplitBlock
from xcosblocks import num2str, style_to_object
from xcosblocks import *
from ParserFunctions import addPort1ForSplit, addPort2ForSplit, addPort3ForSplit
from ParserFunctions import createOutnode, checkModelTag, checkRootTag
from ParserFunctions import getComponentGeometry, get_int, getLinkStyle, getNextAttribId, getOrdering, getorderingname, getParameters, getPinGeometry, getSplitPoints, getWaypoints
from ParserFunctions import identify_segment, remove_hyphen_number

if len(sys.argv) != 2:
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)

if ext != '.xml':
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(1)
base = r'(_[a-zA-Z]*_on_Cloud)?( *\([0-9]*\))?\.xml$'
title = re.sub(r'^.*/', r'', filename)
title = re.sub(base, r'', title)

tree = goodET.parse(filename)

model = tree.getroot()
checkModelTag(model)
outdiagram = ET.Element('XcosDiagram')
outdiagram.set('background', '-1')
outdiagram.set('finalIntegrationTime', '30.0')   # TODO: From POST
outdiagram.set('title', title)
dt = datetime.datetime(2021, 7, 15, 15, 31)
comment = ET.Comment(dt.strftime('Xcos - 2.0 - scilab-6.1.1 - %Y%m%d %H%M'))
outdiagram.append(comment)
outmodel = ET.SubElement(outdiagram, 'mxGraphModel')
outmodel.set('as', 'model')

for root in model:
    checkRootTag(root)

    outroot = ET.SubElement(outmodel, 'root')

    portCount = {}
    IDLIST = {}
    componentOrdering = 0
    nextattribid = 1
    nextAttribForSplit = 10000
    edgeDict = {}
    edgeList = []
    mxPointList = {}
    blkgeometry = {}
    points1 = []
    cells = list(root)
    remainingcells = []
    cellslength = len(cells)
    oldcellslength = 0
    rootattribid = '0:1:0'
    parentattribid = '0:2:0'
    print('cellslength=', cellslength)
    while cellslength > 0 and cellslength != oldcellslength:
        for i, cell in enumerate(cells):
            try:
                if i <= 1 and oldcellslength == 0:
                    createOutnode(i, outroot, rootattribid, parentattribid)
                    continue

                attrib = cell.attrib
                if 'id' not in attrib:
                    continue
                attribid = attrib['id']
                nextattribid = getNextAttribId(attribid, nextattribid)

                cell_type = attrib['CellType']
                mxGeometry = cell.find('mxGeometry')

                if cell_type == 'Component':

                    style = attrib['style']
                    componentOrdering += 1
                    portCount[attribid] = {
                        'ExplicitInputPort': 0,
                        'ImplicitInputPort': 0,
                        'ControlPort': 0,
                        'ExplicitOutputPort': 0,
                        'ImplicitOutputPort': 0,
                        'CommandPort': 0
                    }
                    componentGeometry = getComponentGeometry(mxGeometry)
                    parameters = getParameters(cell)

                    stylename = style_to_object(style)['default']
                    globals()[stylename](outroot, attribid, componentOrdering, componentGeometry, parameters, parent=parentattribid, style=style)

                    IDLIST[attribid] = cell_type
                    blkgeometry[attribid] = componentGeometry

                elif 'vertex' in attrib:

                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    ParentComponent = attrib['ParentComponent']
                    orderingname = getorderingname(stylename)

                    portCount[ParentComponent][orderingname] += 1

                    ordering = getOrdering(attrib, portCount, ParentComponent, orderingname)

                    geometry = getPinGeometry(mxGeometry, componentGeometry)

                    globals()[stylename](outroot, attribid, ParentComponent, ordering, geometry, style=style)

                    IDLIST[attribid] = stylename
                    blkgeometry[attribid] = geometry

                elif 'edge' in attrib:

                    waypoints = getWaypoints(mxGeometry)

                    sourceVertex = attrib['sourceVertex']
                    targetVertex = attrib['targetVertex']
                    if sourceVertex not in IDLIST or targetVertex not in IDLIST:
                        remainingcells.append(cell)
                        continue
                    sourceType = IDLIST[sourceVertex]
                    targetType = IDLIST[targetVertex]

                    (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints) = getLinkStyle(attribid, sourceVertex, sourceType, targetVertex, targetType, waypoints)

                    split_point, split_point2 = getSplitPoints(attrib, switch_split, blkgeometry, sourceVertex, targetVertex, waypoints)

                    IDLIST[attribid] = style
                    link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)
                    edgeDict[attribid] = link_data
                    edgeList.append(link_data)
            except BaseException:
                traceback.print_exc()
                sys.exit(0)
        oldcellslength = cellslength
        cells = remainingcells
        cellslength = len(remainingcells)
        remainingcells = []
        print('cellslength=', cellslength, ', oldcellslength=', oldcellslength)

newEdgeDict = {}
LINKTOPORT = {}
for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2) in edgeList:
    link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)

    if not addSplit:
        newEdgeDict[attribid] = [link_data]
        continue

    for attribid2 in sourceVertex, targetVertex:
        try:
            linkSegments = newEdgeDict[attribid2]
        except KeyError:
            continue

        print('split_point:', split_point, linkSegments)
        if attribid2 == sourceVertex:
            splitpoint = split_point
        else:
            splitpoint = split_point2
        result, i, left_array, right_array = identify_segment(linkSegments, splitpoint)
        if not result:
            sys.exit(0)
        (linkid, sourceVertex2, targetVertex2, sourceType2, targetType2, style2, waypoints2, addSplit2, split_point_new, split_point2_new) = linkSegments[i]
        array3 = waypoints

        componentOrdering += 1
        geometry = {}
        geometry['height'] = 7
        geometry['width'] = 7
        geometry['x'] = splitpoint['x']
        geometry['y'] = splitpoint['y']
        if sourceType2 == 'ControlPort' or sourceType2 == 'CommandPort' or sourceType2 == 'CommandControlLink':
            split_style = 'CLKSPLIT_f'
            func_name = 'CLKSPLIT_f'
        else:
            split_style = 'SPLIT_f;flip=false;mirror=false'
            func_name = 'SPLIT_f'
        SplitBlock(outroot, nextattribid, componentOrdering, geometry, [], parent=parentattribid, style=split_style, func_name=func_name)
        splitblockid = nextattribid
        nextattribid += 1

        inputCount = 0
        outputCount = 0
        port1 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort1ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        port2 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort2ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        port3 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort3ForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)

        newEdgeDict[attribid2][i] = ((nextAttribForSplit, sourceVertex2, port1, sourceType2, targetType, style2, left_array, addSplit2, split_point, split_point2))
        nextAttribForSplit += 1
        newEdgeDict[attribid2].insert(i + 1, (nextAttribForSplit, port2, targetVertex2, sourceType, targetType2, style2, right_array, addSplit2, split_point, split_point2))
        nextAttribForSplit += 1
        if attribid2 == sourceVertex:
            waypoints.reverse()
            newEdgeDict[attribid] = [(nextAttribForSplit, port3, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)]
        else:
            newEdgeDict[attribid] = [(nextAttribForSplit, port3, sourceVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)]
        nextAttribForSplit += 1
        LINKTOPORT[linkid] = port3


for key, newEdges in newEdgeDict.items():
    for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2) in newEdges:
        try:
            sourceVertex = LINKTOPORT[sourceVertex]
        except KeyError:
            pass

        try:
            targetVertex = LINKTOPORT[targetVertex]
        except KeyError:
            pass

        if get_int(attribid) >= 10000:
            attribid = nextattribid
            nextattribid += 1
        globals()[style](outroot, attribid, sourceVertex, targetVertex,
                         waypoints[1:-1], parent=parentattribid)

outnode = ET.SubElement(outdiagram, 'mxCell')
outnode.set('as', 'defaultParent')
outnode.set('id', parentattribid)
outnode.set('parent', rootattribid)


outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = remove_hyphen_number(basename) + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
