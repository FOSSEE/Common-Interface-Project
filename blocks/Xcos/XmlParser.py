#!/usr/bin/env python

import os
import sys
import traceback
import defusedxml.ElementTree as goodET

from xcosblocks import style_to_object
from xcosblocks import addtolinklist
from xcosblocks import create_mxCell, create_mxCell_edge, create_mxCell_port, checkModelTag, checkXcosDiagramTag, check_point_on_array, checkRootTag
from xcosblocks import getComponentGeometry, getlinkdetails, getLinkStyle, getNextAttribId, getPinGeometry, getSplitPoints, getWaypoints
from xcosblocks import identify_segment, initLinks, mergeLinks, portType1, portType2, portType3, remove_hyphen_number


if len(sys.argv) != 2:
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(101)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)

if ext != '.xml':
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(101)

tree = goodET.parse(filename)

diagram = tree.getroot()
checkXcosDiagramTag(diagram)

model = diagram.find('mxGraphModel')
checkModelTag(model)

for root in model:
    checkRootTag(root)

    IDLIST = {}
    nodeList = {}
    nextattribid = 1
    cells = list(root)
    remainingcells = []
    cellslength = len(cells)
    oldcellslength = 0
    blkgeometry = {}
    rootattribid = '0:1:0'
    parentattribid = '0:2:0'
    key1 = {}
    graph_link = {}
    removable_link = {}
    split_point = None
    edgeDict = {}

    print('cellslength=', cellslength)
    while cellslength > 0 and cellslength != oldcellslength:
        for i, cell in enumerate(cells):
            try:
                if i <= 1 and oldcellslength == 0:
                    continue

                attrib = cell.attrib
                if 'id' not in attrib:
                    continue
                attribid = attrib['id']
                nextattribid = getNextAttribId(attribid, nextattribid)

                cell_type = attrib['CellType']
                nodeList[attribid] = cell
                mxGeometry = cell.find('mxGeometry')

                if cell_type == 'Component':

                    componentGeometry = getComponentGeometry(mxGeometry)

                    IDLIST[attribid] = cell_type
                    blkgeometry[attribid] = componentGeometry

                elif cell_type == 'Pin':

                    geometry = getPinGeometry(mxGeometry, componentGeometry)

                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    IDLIST[attribid] = stylename
                    blkgeometry[attribid] = geometry

                    initLinks(attribid, [], [], key1, graph_link, removable_link)

                elif 'edge' in attrib:

                    waypoints = getWaypoints(mxGeometry)

                    sourceVertex = attrib['sourceVertex']
                    targetVertex = attrib['targetVertex']
                    if sourceVertex == '' or targetVertex == '':
                        continue
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

                    initLinks(attribid, [attribid], [attribid] if addSplit else [], key1, graph_link, removable_link)
                    mergeLinks(attribid, sourceVertex, key1, graph_link, removable_link)
                    mergeLinks(attribid, targetVertex, key1, graph_link, removable_link)

            except Exception:
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
        portcount = {
            "explicitInputPort": 0,
            "explicitOutputPort": 0,
            "implicitInputPort": 0,
            "implicitOutputPort": 0,
            "controlPort": 0,
            "commandPort": 0
        }

        # Count ports
        for port in ports:
            portcount[port] += 1

        explicitInputPorts = portcount["explicitInputPort"]
        explicitOutputPorts = portcount["explicitOutputPort"]
        implicitInputPorts = portcount["implicitInputPort"]
        implicitOutputPorts = portcount["implicitOutputPort"]
        controlPorts = portcount["controlPort"]
        commandPorts = portcount["commandPort"]

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
            port_index, portx, porty, waypoints, linkid = getlinkdetails(port, sourceVertex2, targetVertex2, otherVertex, tarx, tary, tar2x, tar2y, otherx, othery,
                                                                         left_array, right_array, array3, biglinkid, smalllinkid)

            port_id = nextattribid

            port_type, link_type = addtolinklist(port, explicitInputPorts, explicitOutputPorts, implicitInputPorts, implicitOutputPorts, controlPorts, commandPorts,
                                                 port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid, linklist)

            ordering_counters[port_type] += 1
            ordering = ordering_counters[port_type]

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

    except Exception:
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
        waypoints=waypoints
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
output_path = f'{remove_hyphen_number(basename)}-{return_value}.xml'
tree.write(output_path)

sys.exit(return_value)
