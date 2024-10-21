#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from xcosblocks import *

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
if model.tag != 'mxGraphModel':
    print(model.tag, '!= mxGraphModel')
    sys.exit(2)
outdiagram = ET.Element('XcosDiagram')
outdiagram.set('background', '-1')
outdiagram.set('finalIntegrationTime', '30.0')   # TODO: From POST
outdiagram.set('title', title)
dt = datetime.datetime(2021, 7, 15, 15, 31)
comment = ET.Comment(dt.strftime('Xcos - 2.0 - scilab-6.1.1 - %Y%m%d %H%M'))
outdiagram.append(comment)
outmodel = ET.SubElement(outdiagram, 'mxGraphModel')
outmodel.set('as', 'model')


def check_point_on_array(array, point, left_right_direction=True):
    if array is None:
        return False, array, []

    pointX = float(point['x'])
    pointY = float(point['y'])

    for i in range(len(array) - 1):
        leftX = float(array[i]['x'])
        leftY = float(array[i]['y'])
        rightX = float(array[i + 1]['x'])
        rightY = float(array[i + 1]['y'])

        print("RANGE:", pointX, pointY, leftX, leftY, rightX, rightY, left_right_direction)

        # Check if the point lies on the line segment between array[i] and array[i + 1]
        if -40 <= leftY - pointY <= 40 and \
                -40 <= rightY - pointY <= 40 and \
                leftX <= pointX <= rightX:
            return True, array[:i + 1] + [point], [point] + array[i + 1:]
        if -40 <= leftX - pointX <= 40 and \
                -40 <= rightX - pointX <= 40 and \
                leftY <= pointY <= rightY:
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        # if left_right_direction:
        if -20 <= leftX - pointX <= 20:
            print('to the left / right')
            return True, array[:i + 1] + [point], [point] + array[i + 1:]
        # else:
        if -20 <= leftY - pointY <= 20:
            print('on the up / down')
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        # switch direction for the next waypoint
        left_right_direction = not left_right_direction
    return False, array, []


def get_int(s):
    try:
        return int(s)
    except ValueError:
        return -1


def identify_segment(array, point):
    for i, segment in enumerate(array):
        print('COUNT:', len(segment))
        result, left_array, right_array = check_point_on_array(segment[6], point)
        if result:
            print("OK")
            return result, i, left_array, right_array
    print("ERror11:", point, "does not lie on", array)
    return False, -1, array, []


for root in model:
    if root.tag != 'root':
        print('Not root')
        sys.exit(2)
    outroot = ET.SubElement(outmodel, 'root')

    portCount = {}
    IDLIST = {}
    componentOrdering = 0
    nextattribid = 0
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
    while cellslength > 0 and cellslength != oldcellslength :
        for cell in cells:
            try:
                attrib = cell.attrib
                attribid = attrib['id']
                attribint = get_int(attribid)
                if nextattribid <= attribint:
                    nextattribid = attribint + 1

                if attribid == '0':
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    continue

                if attribid == '1':
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    outnode.set('parent', '0')
                    continue

                cell_type = attrib['CellType']

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
                    componentGeometry = {}
                    componentGeometry['height'] = 40
                    componentGeometry['width'] = 40
                    componentGeometry['x'] = 0
                    componentGeometry['y'] = 0
                    mxGeometry = cell.find('mxGeometry')
                    if mxGeometry is not None:
                        componentGeometry['height'] = mxGeometry.attrib['height']
                        componentGeometry['width'] = mxGeometry.attrib['width']
                        componentGeometry['x'] = mxGeometry.attrib.get('x', '0')
                        componentGeometry['y'] = mxGeometry.attrib.get('y', '0')
                    parameter_values = cell.find('./Object[@as="parameter_values"]')
                    parameters = []
                    if parameter_values is not None:
                        parameter_values = parameter_values.attrib
                        for i in range(100):
                            parameter = 'p%03d_value' % i
                            if parameter in parameter_values:
                                parameters.append(parameter_values[parameter])
                            else:
                                break

                    style = style_to_object(style)['default']
                    globals()[style](outroot, attribid, componentOrdering, componentGeometry, parameters)

                    IDLIST[attribid] = cell_type
                    blkgeometry[attribid] = componentGeometry

                elif 'vertex' in attrib:

                    style = attrib['style']
                    ParentComponent = attrib['ParentComponent']
                    portCount[ParentComponent][style] += 1
                    ordering = portCount[ParentComponent][style]
                    geometry = dict(componentGeometry)
                    mxGeometry = cell.find('mxGeometry')
                    if mxGeometry is not None:
                        geometry['height'] = mxGeometry.attrib['height']
                        geometry['width'] = mxGeometry.attrib['width']
                        geometryX = mxGeometry.attrib.get('x', 0)
                        geometryY = mxGeometry.attrib.get('y', 0)
                        if mxGeometry.attrib.get('relative', '0') == '1':
                            geometryX = num2str(float(componentGeometry['x']) +
                                                float(componentGeometry['width']) * float(geometryX))
                            geometryY = num2str(float(componentGeometry['y']) +
                                                float(componentGeometry['height']) * float(geometryY))
                        geometry['x'] = geometryX
                        geometry['y'] = geometryY
                    globals()[style](outroot, attribid, ParentComponent, ordering, geometry)

                    IDLIST[attribid] = style
                    blkgeometry[attribid] = geometry

                elif 'edge' in attrib:

                    mxGeometry = cell.find('mxGeometry')
                    waypoints = []
                    arrayElement = mxGeometry.find('Array')
                    if arrayElement is not None:
                        for arrayChild in arrayElement:
                            if arrayChild.tag == 'mxPoint':
                                waypoints.append(arrayChild.attrib)

                    sourceVertex = attrib['sourceVertex']
                    targetVertex = attrib['targetVertex']
                    
                    try:
                        sourceType = IDLIST[sourceVertex]
                        targetType = IDLIST[targetVertex]
                    except KeyError:
                        remainingcells.append(cell)
                        continue
                    

                    # switch vertices if required
                    if sourceType in ['ExplicitInputPort', 'ImplicitInputPort', 'ControlPort'] and \
                            targetType in ['ExplicitOutputPort', 'ExplicitLink', 'ImplicitOutputPort', 'ImplicitLink', 'CommandPort', 'CommandControlLink']:
                        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                        (sourceType, targetType) = (targetType, sourceType)
                        waypoints.reverse()
                    elif sourceType in ['ExplicitInputPort', 'ExplicitLink', 'ImplicitInputPort', 'ImplicitLink', 'ControlPort', 'CommandControlLink'] and \
                            targetType in ['ExplicitOutputPort', 'ImplicitOutputPort', 'CommandPort']:
                        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                        (sourceType, targetType) = (targetType, sourceType)
                        waypoints.reverse()

                    style = None
                    addSplit = False
                    if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'CommandPort', 'ControlPort'] and \
                            targetType == sourceType:
                        print(attribid, 'cannot connect two ports of', sourceType, 'and', targetType)
                    elif sourceType in ['ExplicitLink', 'ImplicitLink', 'CommandControlLink'] and \
                            targetType == sourceType:
                        print(attribid, 'cannot connect two links of', sourceType, 'and', targetType)
                    elif sourceType in ['ExplicitOutputPort'] and \
                            targetType in ['ExplicitInputPort']:
                        style = 'ExplicitLink'
                    elif sourceType in ['ExplicitOutputPort', 'ExplicitLink'] and \
                            targetType in ['ExplicitInputPort', 'ExplicitLink']:
                        style = 'ExplicitLink'
                        addSplit = True
                    elif sourceType in ['ImplicitOutputPort', 'ImplicitInputPort'] and \
                            targetType in ['ImplicitInputPort', 'ImplicitOutputPort']:
                        style = 'ImplicitLink'
                    elif sourceType in ['ImplicitOutputPort', 'ImplicitInputPort', 'ImplicitLink'] and \
                            targetType in ['ImplicitInputPort', 'ImplicitOutputPort', 'ImplicitLink']:
                        style = 'ImplicitLink'
                        addSplit = True
                    elif sourceType in ['CommandPort'] and \
                            targetType in ['ControlPort']:
                        style = 'CommandControlLink'
                    elif sourceType in ['CommandPort', 'CommandControlLink'] and \
                            targetType in ['ControlPort', 'CommandControlLink']:
                        style = 'CommandControlLink'
                        addSplit = True
                    else:
                        print(attribid, 'Unknown combination of', sourceType, 'and', targetType)

                    if style is None:
                        continue

                    split_point = None

                    if sourceVertex in blkgeometry:
                        vertex = blkgeometry[sourceVertex]
                        point = {'x': vertex['x'], 'y': vertex['y']}
                        waypoints.insert(0, point)
                    elif 'tarx' in attrib and 'tary' in attrib:
                        point = {'x': attrib['tarx'], 'y': attrib['tary']}
                        split_point = point
                        waypoints.insert(0, point)

                    if targetVertex in blkgeometry:
                        vertex = blkgeometry[targetVertex]
                        point = {'x': vertex['x'], 'y': vertex['y']}
                        waypoints.append(point)

                    IDLIST[attribid] = style
                    link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point)
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
            

print('EDGES:')
for key, value in edgeDict.items():
    print(f'{key}: {value}')
print()

newEdgeDict = {}
for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point) in edgeList:
    link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point)

    if not addSplit:
        newEdgeDict[attribid] = [link_data]
        continue

    try:
        linkSegments = newEdgeDict[sourceVertex]
        attribid2 = sourceVertex
    except KeyError:
        pass
    try:
        linkSegments = newEdgeDict[targetVertex]
        attribid2 = targetVertex
    except KeyError:
        pass

    result, i, left_array, right_array = identify_segment(linkSegments, split_point)
    if not result:
        sys.exit(0)
    (linkid, sourceVertex2, targetVertex2, sourceType2, targetType2, style2, waypoints2, addSplit2, split_point2) = linkSegments[i]
    array3 = waypoints

    componentOrdering += 1
    geometry = {}
    geometry['height'] = 7
    geometry['width'] = 7
    geometry['x'] = split_point['x']
    geometry['y'] = split_point['y']
    SplitBlock(outroot, nextattribid, componentOrdering, geometry)
    splitblockid = nextattribid
    nextattribid += 1

    inputCount = 0
    outputCount = 0
    if sourceType == 'ExplicitLink':
        port1 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        port2 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        port3 = nextattribid
        (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)

    elif sourceType == 'ImplicitLink':
        geometry = {}
        geometry['width'] = 8
        geometry['height'] = 8
        geometry['x'] = 7
        geometry['y'] = -4
        outputCount += 1
        ImplicitOutputPort(outroot, nextattribid, splitblockid, outputCount, geometry, forSplitBlock=True)
        portid = nextattribid
        nextattribid += 1
        linkid = nextAttribForSplit
        nextAttribForSplit += 1
        (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = newEdgeDict.get(targetVertex, (None, None, None, None, None))
        geometry = {}
        geometry['width'] = 8
        geometry['height'] = 8
        geometry['x'] = -8
        geometry['y'] = -4
        inputCount += 1
        ImplicitInputPort(outroot, nextattribid, splitblockid, inputCount, geometry, forSplitBlock=True)
        portid = nextattribid
        nextattribid += 1
        linkid = nextAttribForSplit
        nextAttribForSplit += 1
        geometry = {}
        geometry['width'] = 8
        geometry['height'] = 8
        geometry['x'] = 7
        geometry['y'] = -4
        outputCount += 1
        ImplicitOutputPort(outroot, nextattribid, splitblockid, outputCount, geometry, forSplitBlock=True)
        portid = nextattribid
        nextattribid += 1
        linkid = nextAttribForSplit
        nextAttribForSplit += 1

    elif sourceType == 'CommandControlLink':
        geometry = {}
        geometry['width'] = 8
        geometry['height'] = 8
        geometry['x'] = -4
        geometry['y'] = 7
        outputCount += 1
        ControlPort(outroot, nextattribid, splitblockid, outputCount, geometry, forSplitBlock=True)
        portid = nextattribid
        nextattribid += 1
        linkid = nextAttribForSplit
        nextAttribForSplit += 1
        (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = newEdgeDict[targetVertex]

    newEdgeDict[attribid2][i] = ((nextAttribForSplit, sourceVertex2, port1, sourceType2, targetType, style2, left_array, addSplit2, split_point2))
    nextAttribForSplit += 1
    newEdgeDict[attribid2].insert(i + 1, (nextAttribForSplit, port2, targetVertex2, sourceType, targetType2, style2, right_array, addSplit2, split_point2))
    nextAttribForSplit += 1
    newEdgeDict[attribid] = [(nextAttribForSplit, port3, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point)]
    nextAttribForSplit += 1

print()
for key, newEdges in newEdgeDict.items():
    print(f'{key}: {newEdges}')
    for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point) in newEdges:
        if get_int(attribid) >= 10000:
            attribid = nextattribid
            nextattribid += 1
        globals()[style](outroot, attribid, sourceVertex, targetVertex,
                         waypoints[1:-1])

outnode = ET.SubElement(outdiagram, 'mxCell')
outnode.set('id', str(1))
outnode.set('parent', str(0))
outnode.set('as', 'defaultParent')

outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = basename + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
