import re
import sys
import xml.etree.ElementTree as ET

from xcosblocks import addExplicitInputPortForSplit, addExplicitOutputPortForSplit
from xcosblocks import addImplicitInputPortForSplit, addImplicitOutputPortForSplit
from xcosblocks import addControlPortForSplit, addCommandPortForSplit
from xcosblocks import num2str


def remove_hyphen_number(s):
    return re.sub(r'-\d+$', '', s)


def get_int(s):
    try:
        return int(s)
    except ValueError:
        return -1


def getNextAttribId(attribid, nextattribid):
    attribint = get_int(attribid)
    if nextattribid <= attribint:
        nextattribid = attribint + 1
    return nextattribid


def checkModelTag(model):
    if model.tag != 'mxGraphModel':
        print(model.tag, '!= mxGraphModel')
        sys.exit(102)


def checkRootTag(root):
    if root.tag != 'root':
        print('Not root')
        sys.exit(102)


def createOutnode(i, outroot, rootattribid, parentattribid):
    if i == 0:
        outnode = ET.SubElement(outroot, 'mxCell')
        outnode.set('id', rootattribid)
    elif i == 1:
        outnode = ET.SubElement(outroot, 'mxCell')
        outnode.set('id', parentattribid)
        outnode.set('parent', rootattribid)
    else:
        outnode = None
    return outnode


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


def addPort1ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array):
    if sourceType == 'ExplicitLink':
        if sourceType2 == 'ExplicitOutputPort' or sourceType2 == 'ExplicitLink':
            return addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if sourceType2 == 'ImplicitOutputPort' or targetType2 == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
    elif sourceType == 'CommandControlLink':
        if sourceType2 == 'CommandPort' or sourceType2 == 'CommandControlLink':
            return addControlPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def addPort2ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array):
    if sourceType == 'ExplicitLink':
        if targetType2 == 'ExplicitInputPort' or targetType2 == 'ExplicitLink':
            return addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if targetType2 == 'ImplicitOutputPort' or sourceType2 == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
    elif sourceType == 'CommandControlLink':
        if targetType2 == 'ControlPort' or targetType2 == 'CommandControlLink':
            return addCommandPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def addPort3ForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, array3):
    if sourceType == 'ExplicitLink':
        if targetType == 'ExplicitInputPort':
            return addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if targetType == 'ImplicitOutputPort' or sourceType == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
    elif sourceType == 'CommandControlLink':
        if targetType == 'ControlPort':
            return addCommandPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def create_mxCell(style, id, vertex="1", connectable="0", CellType="Component", blockprefix="XCOS",
                  explicitInputPorts="0", explicitOutputPorts="0", implicitInputPorts="0", implicitOutputPorts="0", controlPorts="0", commandPorts="0",
                  simulationFunction="split", sourceVertex="0", targetVertex="0", tarx="0", tary="0", geometry=None):

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
                       sourceVertex="0", targetVertex="0", tarx="0", tary="0", tar2x="0", tar2y="0", source_point="0", target_point="0", waypoints=None):
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


def getOrdering(attrib, portCount, ParentComponent, orderingname):
    try:
        ordering = attrib['ordering']
    except KeyError:
        ordering = portCount[ParentComponent][orderingname]
    return ordering


def switchPorts(sourceVertex, sourceType, targetVertex, targetType, waypoints):
    # switch vertices if required
    switch_split = False

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

    return (sourceVertex, sourceType, targetVertex, targetType, switch_split)


def getLinkStyle(attribid, sourceVertex, sourceType, targetVertex, targetType, waypoints):
    (sourceVertex, sourceType, targetVertex, targetType, switch_split) = switchPorts(sourceVertex, sourceType, targetVertex, targetType, waypoints)

    style = None

    if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'CommandPort', 'ControlPort'] and \
            targetType == sourceType:
        print(attribid, 'cannot connect two ports of', sourceType, 'and', targetType)
    elif sourceType in ['ExplicitLink', 'CommandControlLink'] and \
            targetType == sourceType:
        print(attribid, 'cannot connect two links of', sourceType, 'and', targetType)
    elif sourceType in ['ExplicitOutputPort', 'ExplicitLink'] and \
            targetType in ['ExplicitInputPort', 'ExplicitLink']:
        style = 'ExplicitLink'
    elif sourceType in ['ImplicitOutputPort', 'ImplicitInputPort', 'ImplicitLink'] and \
            targetType in ['ImplicitInputPort', 'ImplicitOutputPort', 'ImplicitLink']:
        style = 'ImplicitLink'
    elif sourceType in ['CommandPort', 'CommandControlLink'] and \
            targetType in ['ControlPort', 'CommandControlLink']:
        style = 'CommandControlLink'
    else:
        print(attribid, 'Unknown combination of', sourceType, 'and', targetType)

    addSplit = sourceType.endswith('Link') or targetType.endswith('Link')

    return (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints)


def initLinks(attribid, graph_value, removable_value, key1, graph_link, removable_link):
    # for ports, the graph_value and the removable_value are empty lists
    # for links, the graph_value is a list containing itself and the
    # removable_value is a list containing itself if it has a split point and an
    # empty list otherwise
    key1[attribid] = attribid
    graph_link[attribid] = graph_value
    removable_link[attribid] = removable_value


def mergeLinks(attribid, vertex, key1, graph_link, removable_link):
    # for links only
    # merge the ports/links of the source/target vertex into itself
    # also, remove the ports/links of the source/target vertex
    if vertex in key1:
        key = key1[vertex]
        for v in graph_link[key]:
            key1[v] = attribid

        graph_link[attribid].extend(graph_link[key])
        removable_link[attribid].extend(removable_link[key])

        del graph_link[key]
        del removable_link[key]


def getlinkdetails(port, sourceVertex2, targetVertex2, otherVertex, tarx, tary, tar2x, tar2y, otherx, othery,
                   left_array, right_array, array3, biglinkid, smalllinkid):
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
    return port_index, portx, porty, waypoints, linkid


def addtolinklist(port, explicitInputPorts, explicitOutputPorts, implicitInputPorts, implicitOutputPorts, controlPorts, commandPorts,
                  port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid, linklist):
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
    return port_type, link_type


def getComponentGeometry(mxGeometry):
    componentGeometry = {}
    componentGeometry['height'] = 40
    componentGeometry['width'] = 40
    componentGeometry['x'] = 0
    componentGeometry['y'] = 0
    if mxGeometry is not None:
        componentGeometry['height'] = mxGeometry.attrib['height']
        componentGeometry['width'] = mxGeometry.attrib['width']
        componentGeometry['x'] = mxGeometry.attrib.get('x', '0')
        componentGeometry['y'] = mxGeometry.attrib.get('y', '0')
    return componentGeometry


def getPinGeometry(mxGeometry, componentGeometry):
    geometry = dict(componentGeometry)
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
    return geometry


def getorderingname(stylename):
    if stylename == 'ImplicitInputPort':
        orderingname = 'ExplicitInputPort'
    elif stylename == 'ImplicitOutputPort':
        orderingname = 'ExplicitOutputPort'
    else:
        orderingname = stylename
    return orderingname


def getParameters(cell):
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
    return parameters


def getWaypoints(mxGeometry):
    waypoints = []
    arrayElement = mxGeometry.find('Array')
    if arrayElement is not None:
        for arrayChild in arrayElement:
            if arrayChild.tag == 'mxPoint':
                waypoints.append(arrayChild.attrib)
    return waypoints


def getSplitPoints(attrib, switch_split, blkgeometry, sourceVertex, targetVertex, waypoints):
    split_point, split_point2 = None, None

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

    return split_point, split_point2
