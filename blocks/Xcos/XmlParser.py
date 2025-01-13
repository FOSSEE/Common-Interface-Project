#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET
import uuid

from xcosblocks import num2str, style_to_object

if len(sys.argv) != 2:
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(101)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)

if ext != '.xml':
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(101)

tree = goodET.parse(filename)

model = tree.getroot()
if model.tag != 'mxGraphModel':
    print(model.tag, '!= mxGraphModel')
    sys.exit(102)


def remove_dot_number(s):
    return re.sub(r'\.\d+$', '', s)


def get_int(s):
    try:
        return int(s)
    except ValueError:
        return -1


def portType1(sType, sType2, tType2):
    # port1
    if sType == 'ExplicitLink':
        if sType2 == 'ExplicitOutputPort' or sType2 == 'ExplicitLink':
            return 'explicitInputPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    elif sType == 'ImplicitLink':
        if sType2 == 'ImplicitOutputPort' or sType2 == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if sType2 == 'CommandPort' or sType2 == 'CommandControlLink':
            return 'controlPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    else:
        print('Error: (sourceType, sourceType2, targetType2) =',
              '(', sType, ',', sType2, ',', tType2, ')')


def portType2(sType, sType2, tType2):
    # port2
    if sType == 'ExplicitLink':
        if tType2 == 'ExplicitInputPort' or tType2 == 'ExplicitLink':
            return 'explicitOutputPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    elif sType == 'ImplicitLink':
        if tType2 == 'ImplicitOutputPort' or tType2 == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if tType2 == 'ControlPort' or tType2 == 'CommandControlLink':
            return 'commandPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')


def portType3(sType, tType):
    # port3
    if sType == 'ExplicitLink':
        if tType == 'ExplicitInputPort' or tType == 'ExplicitLink':
            return 'explicitOutputPort'
        else:
            print('Error: (sourceType, targetType) =',
                  '(', sType, ',', tType, ')')
    elif sType == 'ImplicitLink':
        if tType == 'ImplicitOutputPort' or tType == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if tType == 'ControlPort' or tType == 'CommandControlLink':
            return 'commandPort'
        else:
            print('Error: (sourceType, targetType) =',
                  '(', sType, ',', tType, ')')


def create_mxCell(style, id, vertex="1", connectable="0", CellType="Component", blockprefix="XCOS",
                  explicitInputPorts="0", implicitInputPorts="0", explicitOutputPorts="0", implicitOutputPorts="0",
                  controlPorts="0", commandPorts="0", simulationFunction="split", sourceVertex="0", targetVertex="0",
                  tarx="0", tary="0", geometry=None):

    mxCell = ET.Element("mxCell", {
        "style": style,
        "id": id,
        "vertex": vertex,
        "connectable": connectable,
        "CellType": CellType,
        "blockprefix": blockprefix,
        "explicitInputPorts": str(explicitInputPorts),
        "implicitInputPorts": str(implicitInputPorts),
        "explicitOutputPorts": str(explicitOutputPorts),
        "implicitOutputPorts": str(implicitOutputPorts),
        "controlPorts": str(controlPorts),
        "commandPorts": str(commandPorts),
        "simulationFunction": simulationFunction,
        "sourceVertex": sourceVertex,
        "targetVertex": targetVertex,
        "tarx": tarx,
        "tary": tary,
    })

    if geometry:
        x, y, width, height = geometry
        ET.SubElement(mxCell, "mxGeometry", {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry"
        })

    ET.SubElement(mxCell, "Object", {
        "display_parameter": str(),
        "as": "displayProperties"
    })

    ET.SubElement(mxCell, "Object", {
        "as": "parameter_values"
    })

    return mxCell


def create_mxCell_port(style, id, parentComponent, ordering="1", vertex="1", cellType="Pin",
                       sourceVertex="0", targetVertex="0", tarx="0", tary="0", geometry=None):
    mxcell = ET.Element('mxCell', {
        'style': style,
        'id': str(id),
        'ordering': ordering,
        'vertex': vertex,
        'CellType': cellType,
        'ParentComponent': str(parentComponent),
        'sourceVertex': sourceVertex,
        'targetVertex': targetVertex,
        'tarx': tarx,
        'tary': tary,
    })

    if geometry:
        x, y, width, height = geometry
        mxgeometry = ET.SubElement(mxcell, 'mxGeometry', {
            'x': str(x),
            'y': str(y),
            'width': str(width),
            'height': str(height),
            'relative': '1',
            'as': 'geometry'
        })

        ET.SubElement(mxgeometry, 'mxPoint', {
            'y': '-4',
            'as': 'offset'
        })

        ET.SubElement(mxcell, "Object", {
            "as": "parameter_values"
        })

        ET.SubElement(mxcell, "Object", {
            "as": "displayProperties"
        })

    return mxcell


def create_mxCell_edge(id, edge="1", cellType="Unknown",
                       sourceVertex="0", targetVertex="0", tarx="0", tary="0", tar2x="0", tar2y="0", source_point="0", target_point="0", array=None):
    mxcell = ET.Element('mxCell', {
        'id': str(id),
        'edge': edge,
        'CellType': cellType,
        'sourceVertex': str(sourceVertex),
        'targetVertex': str(targetVertex),
        'tarx': tarx,
        'tary': tary,
        'tar2x': tar2x,
        'tar2y': tar2y,
    })

    mxgeometry = ET.SubElement(mxcell, 'mxGeometry', {
        'relative': '1',
        'as': 'geometry'
    })

    ET.SubElement(mxgeometry, 'mxPoint', {
        'x': str(source_point[0]),
        'y': str(source_point[1]),
        'as': 'sourcePoint'
    })

    ET.SubElement(mxgeometry, 'mxPoint', {
        'x': str(target_point[0]),
        'y': str(target_point[1]),
        'as': 'targetPoint'
    })

    array_element = ET.SubElement(mxgeometry, 'Array', {
        'as': 'points'
    })

    for waypoint in waypoints[1:-1]:
        ET.SubElement(array_element, 'mxPoint', {
            'x': waypoint['x'],  # Access 'x' key
            'y': waypoint['y']   # Access 'y' key
        })

    ET.SubElement(mxcell, "Object", {
        "as": "parameter_values"
    })

    ET.SubElement(mxcell, "Object", {
        "as": "displayProperties"
    })

    return mxcell


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

        # Check if the point lies on the line segment between array[i] and array[i + 1]

        pointbetweenleftrightx = leftX <= pointX <= rightX or leftX >= pointX >= rightX
        samey = -40 <= leftY - pointY <= 40 and -40 <= rightY - pointY <= 40
        sameleftorrighty = -20 <= leftY - pointY <= 20 or -20 <= rightY - pointY <= 20

        if pointbetweenleftrightx and (samey or sameleftorrighty):
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        pointbetweenleftrighty = leftY <= pointY <= rightY or leftY >= pointY >= rightY
        samex = -40 <= leftX - pointX <= 40 and -40 <= rightX - pointX <= 40
        sameleftorrightx = -20 <= leftX - pointX <= 20 or -20 <= rightX - pointX <= 20

        if pointbetweenleftrighty and (samex or sameleftorrightx):
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        # switch direction for the next waypoint
        left_right_direction = not left_right_direction
    return False, array, []


def identify_segment(array, point):
    for i, waypoint in enumerate(array):
        result, left_array, right_array = check_point_on_array(waypoint, point)
        if result:
            return result, i, left_array, right_array
    print("Error:", point, "does not lie on", array)
    return False, -1, array, []


def getLinkStyle(sourceVertex, sourceType, targetVertex, targetType, waypoints):
    # switch vertices if required
    switch_split = False
    style = None
    addSplit = False

    if sourceType in ['ExplicitInputPort', 'ImplicitInputPort', 'ControlPort'] and \
            targetType in ['ExplicitOutputPort', 'ExplicitLink', 'ImplicitOutputPort', 'ImplicitLink', 'CommandPort', 'CommandControlLink']:
        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
        (sourceType, targetType) = (targetType, sourceType)
        waypoints.reverse()
        switch_split = True
    elif sourceType in ['ExplicitInputPort', 'ExplicitLink', 'ImplicitInputPort', 'ImplicitLink', 'ControlPort', 'CommandControlLink'] and \
            targetType in ['ExplicitOutputPort', 'ImplicitOutputPort', 'CommandPort']:
        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
        (sourceType, targetType) = (targetType, sourceType)
        waypoints.reverse()
        switch_split = True

    if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'CommandPort', 'ControlPort'] and \
            targetType == sourceType:
        print(attribid, 'cannot connect two ports of', sourceType, 'and', targetType)
    elif sourceType in ['ExplicitLink', 'CommandControlLink'] and \
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

    return (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints)


def initLinks(vertex, key1, graph_link, graph_value, removable_link, removable_value):
    # key structure
    key1[vertex] = vertex
    graph_link[vertex] = graph_value
    removable_link[vertex] = removable_value


def mergeLinks(vertex, key1, graph_link, removable_link):
    if vertex in key1:
        key = key1[vertex]
        for v in graph_link[key]:
            key1[v] = attribid

        graph_link[attribid].extend(graph_link[key])
        removable_link[attribid].extend(removable_link[key])

        del graph_link[key]
        del removable_link[key]


for root in model:
    if root.tag != 'root':
        print('Not root')
        sys.exit(102)

    IDLIST = {}
    nodeList = {}
    nextattribid = 1
    cells = list(root)
    remainingcells = []
    cellslength = len(cells)
    oldcellslength = 0
    blkgeometry = {}
    rootattribid = None
    parentattribid = None
    key1 = {}
    graph_link = {}
    removable_link = {}
    split_point = None
    edgeDict = {}

    print('cellslength=', cellslength)
    while cellslength > 0 and cellslength != oldcellslength:
        for i, cell in enumerate(cells):
            try:
                if i == 0 and oldcellslength == 0:
                    attribid = '0:1:0'
                    rootattribid = attribid
                    continue

                if i == 1 and oldcellslength == 0:
                    attribid = '0:2:0'
                    parentattribid = attribid
                    continue

                try:
                    attrib = cell.attrib
                    attribid = attrib['id']
                    attribint = get_int(attribid)
                    if nextattribid <= attribint:
                        nextattribid = attribint + 1
                except KeyError:
                    continue

                cell_type = attrib['CellType']
                nodeList[attribid] = cell

                if cell_type == 'Component':

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

                    IDLIST[attribid] = cell_type
                    blkgeometry[attribid] = componentGeometry

                elif cell_type == 'Pin':

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
                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    IDLIST[attribid] = stylename
                    blkgeometry[attribid] = geometry

                    initLinks(attribid, key1, graph_link, [], removable_link, [])

                elif 'edge' in attrib:
                    mxGeometry = cell.find('mxGeometry')
                    waypoints = []
                    waypoints2 = []
                    arrayElement = mxGeometry.find('Array')
                    if arrayElement is not None:
                        for arrayChild in arrayElement:
                            if arrayChild.tag == 'mxPoint':
                                waypoints.append(arrayChild.attrib)
                    try:
                        sourceVertex = attrib['sourceVertex']
                        sourceType = IDLIST[sourceVertex]
                        targetVertex = attrib['targetVertex']
                        targetType = IDLIST[targetVertex]
                    except KeyError:
                        remainingcells.append(cell)
                        continue

                    (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints) = getLinkStyle(sourceVertex, sourceType, targetVertex, targetType, waypoints)

                    split_point = None
                    split_point2 = None

                    if 'tarx' in attrib and 'tary' in attrib and (attrib['tarx'] != '0' or attrib['tary'] != '0'):
                        point = {'x': attrib['tarx'], 'y': attrib['tary']}
                        if switch_split:
                            split_point2 = point
                            waypoints.append(point)
                        else:
                            split_point = point
                            waypoints.insert(0, point)
                    elif sourceVertex in blkgeometry:
                        vertex = blkgeometry[sourceVertex]
                        point = {'x': vertex['x'], 'y': vertex['y']}
                        waypoints.insert(0, point)

                    if 'tar2x' in attrib and 'tar2y' in attrib and (attrib['tar2x'] != '0' or attrib['tar2y'] != '0'):
                        point = {'x': attrib['tar2x'], 'y': attrib['tar2y']}
                        if switch_split:
                            split_point = point
                            waypoints.insert(0, point)
                        else:
                            split_point2 = point
                            waypoints.append(point)
                    elif targetVertex in blkgeometry:
                        vertex = blkgeometry[targetVertex]
                        point = {'x': vertex['x'], 'y': vertex['y']}
                        waypoints.append(point)

                    IDLIST[attribid] = style

                    link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)
                    edgeDict[attribid] = link_data

                    initLinks(attribid, key1, graph_link, [attribid], removable_link, [attribid] if addSplit else [])
                    mergeLinks(sourceVertex, key1, graph_link, removable_link)
                    mergeLinks(targetVertex, key1, graph_link, removable_link)

            except BaseException:
                traceback.print_exc()
                sys.exit(103)

        oldcellslength = cellslength
        cells = remainingcells
        cellslength = len(remainingcells)
        remainingcells = []
        print('cellslength=', cellslength, ', oldcellslength=', oldcellslength)


linklist = []
return_value = 0
LINKTOLINK = {}
for k, r_link in removable_link.items():
    try:
        if len(r_link) == 0:
            continue
        link = graph_link[k]

        return_value += len(r_link) - 1
        r_link_0 = r_link[0]
        node = nodeList[r_link_0]
        link_data = edgeDict[r_link_0]  # small removed link

        sourceVertex = link_data[1]  # small link
        targetVertex = link_data[2]  # small link

        if sourceVertex in link:
            node2 = nodeList[sourceVertex]
            link_data2 = edgeDict[sourceVertex]  # big removed link

            thisVertex = sourceVertex
            thisx = link_data[8]['x']
            thisy = link_data[8]['y']

            otherVertex = targetVertex
            otherx = link_data[9]['x']
            othery = link_data[9]['y']

            split_point = link_data[8]

        elif targetVertex in link:
            node2 = nodeList[targetVertex]
            link_data2 = edgeDict[targetVertex]  # big removed link

            thisVertex = targetVertex
            thisx = link_data[9]['x']
            thisy = link_data[9]['y']

            otherVertex = sourceVertex
            otherx = link_data[8]['x']
            othery = link_data[8]['y']

            split_point = link_data[9]

        sourceVertex2 = link_data2[1]  # big link
        targetVertex2 = link_data2[2]  # big link

        tarx = link_data2[8]['x']
        tary = link_data2[8]['y']

        tar2x = link_data2[9]['x']
        tar2y = link_data2[9]['y']

        root.remove(node)
        root.remove(node2)

        sType = IDLIST[thisVertex]
        tType = IDLIST[otherVertex]
        sType2 = IDLIST[sourceVertex2]
        tType2 = IDLIST[targetVertex2]
        height = '7.0'
        width = '7.0'
        waypoints = link_data[6]    # small link
        waypoints2 = link_data2[6]  # big link
        # split_point = link_data[9]
        biglinkid = link_data2[0]
        smalllinkid = link_data[0]
        result, left_array, right_array = check_point_on_array(waypoints2, split_point)
        array3 = waypoints

        port1 = portType1(sType, sType2, tType2)
        port2 = portType2(sType, sType2, tType2)
        port3 = portType3(sType, tType)

        ports = [port1, port2, port3]
        implicitInputPorts = 0
        implicitOutputPorts = 0
        explicitInputPorts = 0
        explicitOutputPorts = 0
        controlPorts = 0
        commandPorts = 0

        # Count ports
        for port in ports:
            if port == 'implicitInputPort':
                implicitInputPorts += 1
            elif port == 'implicitOutputPort':
                implicitOutputPorts += 1
            elif port == 'explicitInputPort':
                explicitInputPorts += 1
            elif port == 'explicitOutputPort':
                explicitOutputPorts += 1
            elif port == 'controlPort':
                controlPorts += 1
            elif port == 'commandPort':
                commandPorts += 1

        # add splitblock
        geometry = (thisx, thisy, width, height)
        block_id = str(nextattribid)
        xml_output = create_mxCell(
            style="SplitBlock",
            id=block_id,
            explicitInputPorts=explicitInputPorts,
            implicitInputPorts=implicitInputPorts,
            explicitOutputPorts=explicitOutputPorts,
            implicitOutputPorts=implicitOutputPorts,
            controlPorts=controlPorts,
            commandPorts=commandPorts,
            simulationFunction="split",
            tarx="0",
            tary="0",
            geometry=geometry
        )

        splitblockid = nextattribid
        nextattribid += 1

        root.append(xml_output)

        # add splitblock port
        ordering_counters = {
            "ExplicitInputPort": 0,
            "ImplicitInputPort": 0,
            "ExplicitOutputPort": 0,
            "ImplicitOutputPort": 0,
            "ControlPort": 0,
            "CommandPort": 0
        }
        p_width = "8"
        p_height = "8"
        count_of_ports = 3
        port_geometry = ("1", "0.5", p_width, p_height)
        for port in range(count_of_ports):
            port_index = 0
            portx = 0
            porty = 0
            if port == 0:
                port_index = sourceVertex2
                portx = tarx
                porty = tary
                waypoints = left_array
                linkid = biglinkid
            elif port == 1:
                port_index = targetVertex2
                portx = tar2x
                porty = tar2y
                waypoints = right_array
                linkid = biglinkid
            else:
                port_index = otherVertex
                portx = otherx
                porty = othery
                waypoints = array3
                linkid = smalllinkid

            port_id = nextattribid

            if port < explicitInputPorts:
                port_type = "ExplicitInputPort"
                link_type = "ExplicitLink"
                linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
            elif port < explicitInputPorts + implicitInputPorts:
                port_type = "ImplicitInputPort"
                link_type = "ImplicitLink"
                linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
            elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts:
                port_type = "ExplicitOutputPort"
                link_type = "ExplicitLink"
                linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
            elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts + implicitOutputPorts:
                port_type = "ImplicitOutputPort"
                link_type = "ImplicitLink"
                linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
            elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts + implicitOutputPorts + controlPorts:
                port_type = "ControlPort"
                link_type = "CommandControlLink"
                linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
            else:
                port_type = "CommandPort"
                link_type = "CommandControlLink"
                linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
            ordering = ordering_counters[port_type] + 1
            ordering_counters[port_type] += 1

            xml_output_port = create_mxCell_port(
                style=port_type,
                id=port_id,
                ordering=str(ordering),
                parentComponent=str(splitblockid),
                sourceVertex="0",
                targetVertex="0",
                tarx="0",
                tary="0",
                geometry=port_geometry
            )

            nextattribid += 1

            root.append(xml_output_port)

    except BaseException:
        traceback.print_exc()
        sys.exit(103)

# add splitblock edges

LINKWAYPOINTS = {}

for edge_index, (link_type, source_vertex, sourcex, sourcey, target_vertex, targetx, targety, waypoints, linkid) in enumerate(linklist):
    edge_id = nextattribid

    if linkid not in LINKTOLINK:
        LINKTOLINK[linkid] = [edge_id]
        LINKWAYPOINTS[linkid] = [waypoints]
    else:
        LINKTOLINK[linkid].append(edge_id)
        LINKWAYPOINTS[linkid].append(waypoints)

    # LINKTOLINK update

    xml_output_edge = create_mxCell_edge(
        id=edge_id,
        edge="1",
        sourceVertex=source_vertex,
        targetVertex=target_vertex,
        tarx=sourcex,
        tary=sourcey,
        tar2x=targetx,
        tar2y=targety,
        source_point=(sourcex, sourcey),
        target_point=(targetx, targety),
        array=waypoints
    )

    nextattribid += 1

    root.append(xml_output_edge)

cells = list(root)
# secondary link
for i, cell in enumerate(cells):
    try:
        attrib = cell.attrib
        attribid = attrib['id']
    except KeyError:
        continue

    cell_type = attrib['CellType']

    if i < 2 or cell_type in ['Component', 'Pin'] or 'edge' not in attrib:
        continue

    try:
        sourceVertex = attrib['sourceVertex']
        targetVertex = attrib['targetVertex']
    except KeyError:
        continue

    if sourceVertex not in LINKTOLINK and targetVertex not in LINKTOLINK:
        continue

    try:
        point = {'x': nodeList[sourceVertex].attrib['tarx'], 'y': nodeList[sourceVertex].attrib['tary']}
        result, i, left_array, right_array = identify_segment(LINKWAYPOINTS[sourceVertex], point)
        sourceVertex = str(LINKTOLINK[sourceVertex][i])
    except KeyError:
        pass

    try:
        point = {'x': nodeList[targetVertex].attrib['tar2x'], 'y': nodeList[targetVertex].attrib['tar2y']}
        result, i, left_array, right_array = identify_segment(LINKWAYPOINTS[targetVertex], point)

        targetVertex = str(LINKTOLINK[targetVertex][i])
    except KeyError:
        pass

    cell.set('sourceVertex', sourceVertex)
    cell.set('targetVertex', targetVertex)


# Save the modified XML
output_path = f'{remove_dot_number(basename)}.{return_value}.xml'
tree.write(output_path)

sys.exit(return_value)
