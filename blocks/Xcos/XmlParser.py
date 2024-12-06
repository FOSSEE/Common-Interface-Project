#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from xcosblocks import SplitBlock
from xcosblocks import addExplicitInputPortForSplit, addExplicitOutputPortForSplit
from xcosblocks import addImplicitInputPortForSplit, addImplicitOutputPortForSplit
from xcosblocks import addControlPortForSplit, addCommandPortForSplit
from xcosblocks import num2str, style_to_object

if len(sys.argv) != 2:
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)

if ext != '.xml':
    print("Usage: %s filename.xml" % sys.argv[0])
    sys.exit(1)

tree = goodET.parse(filename)

model = tree.getroot()
if model.tag != 'mxGraphModel':
    print(model.tag, '!= mxGraphModel')
    sys.exit(2)
outdiagram = ET.Element('XcosDiagram')
outdiagram.set('background', '-1')
outdiagram.set('finalIntegrationTime', '30.0')   # TODO: From POST
outdiagram.set('title', 'output_9_2_xml.xml')
dt = datetime.datetime(2021, 7, 15, 15, 31)
comment = ET.Comment(dt.strftime('Xcos - 2.0 - scilab-6.1.1 - %Y%m%d %H%M'))
outdiagram.append(comment)
outmodel = ET.SubElement(outdiagram, 'mxGraphModel')
outmodel.set('as', 'model')

def get_int(s):
    try:
        return int(s)
    except ValueError:
        return -1

def extract_points(node):
    geometry = node.find(".//mxGeometry")
    if geometry is not None:
        array = geometry.find(".//Array[@as='points']")
        if array is not None:
            for point in array.findall("mxPoint"):
                x = point.get("x")
                y = point.get("y")
                points.append(x)
                points.append(y)
                print(f"mxPoint in removable node: x={x}, y={y}")

for root in model:
    if root.tag != 'root':
        print('Not root')
        sys.exit(2)
    outroot = ET.SubElement(outmodel, 'root')

    portCount = {}
    IDLIST = {}
    nodeList = {}
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
    rootattribid = None
    parentattribid = None
    key1 = {}
    graph_port = {}
    graph_link = {}
    removable_link = {}
    removablesort = {}
    points = []
    print('cellslength=', cellslength)
    while cellslength > 0 and cellslength != oldcellslength:
        for i, cell in enumerate(cells):
            try:
                attrib = cell.attrib
                try:
                    attribid = attrib['id']
                except KeyError:
                    continue
                attribint = get_int(attribid)
                if nextattribid <= attribint:
                    nextattribid = attribint + 1

                if i == 0 and oldcellslength == 0:
                    attribid = '0:1:0'
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    rootattribid = attribid
                    continue

                if i == 1 and oldcellslength == 0:
                    attribid = '0:2:0'
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    outnode.set('parent', rootattribid)
                    parentattribid = attribid
                    continue

                cell_type = attrib['CellType']

                if cell_type == 'Component':

                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    IDLIST[attribid] = cell_type
                    nodeList[attribid] = cell

                elif 'vertex' in attrib:

                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    IDLIST[attribid] = stylename
                    nodeList[attribid] = cell
                    # print(attribid, stylename)
                    key1[attribid] = attribid
                    graph_port[attribid] = [attribid]
                    graph_link[attribid] = []
                    removable_link[attribid] = []
                    # print('setting port', attribid)

                elif 'edge' in attrib:

                    sourceVertex = attrib['sourceVertex']
                    targetVertex = attrib['targetVertex']

                    try:
                        sourceType = IDLIST[sourceVertex]
                        targetType = IDLIST[targetVertex]
                        # print('ST,TT', sourceType, targetType)
                    except KeyError:
                        remainingcells.append(cell)
                        continue

                    style = None
                    addSplit = False

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
                    #key structure
                    key1[attribid] = attribid
                    graph_port[attribid] = []
                    graph_link[attribid] = [attribid]
                    removable_link[attribid] = [attribid] if addSplit else []
                    removablesort[attribid] = []

                    if sourceVertex in key1:
                        key = key1[sourceVertex]
                        for v in graph_port[key]:
                            key1[v] = attribid
                        for v in graph_link[key]:
                            key1[v] = attribid

                        graph_port[attribid].extend(graph_port[key]) #merge
                        graph_link[attribid].extend(graph_link[key])
                        removable_link[attribid].extend(removable_link[key])  
                        
                        del graph_port[key]
                        del graph_link[key]
                        del removable_link[key]
                    

                    if targetVertex in key1:
                        key = key1[targetVertex]
                        for v in graph_port[key]:
                            key1[v] = attribid
                        for v in graph_link[key]:
                            key1[v] = attribid
                        # print('replacing', targetVertex, key, attribid)
                        graph_port[attribid].extend(graph_port[key]) #merge
                        graph_link[attribid].extend(graph_link[key])
                        removable_link[attribid].extend(removable_link[key])

                        del graph_port[key]
                        del graph_link[key]
                        del removable_link[key]
    

                    IDLIST[attribid] = style
                    nodeList[attribid] = cell

            except BaseException:
                traceback.print_exc()
                sys.exit(0)

        oldcellslength = cellslength
        cells = remainingcells
        cellslength = len(remainingcells)
        remainingcells = []
        print('cellslength=', cellslength, ', oldcellslength=', oldcellslength)
for k, port in graph_port.items():
    if len(port) > 2:
        print(f"GRAPH port: k: {k}, port: {port}")
    link = graph_link[k]
    if len(link) > 1:
        print(f"GRAPH link: k: {k}, link: {link}")
    r_link = removable_link[k]
    if len(r_link) > 0:
        node = nodeList[r_link[0]]
        root.remove(node)
        print(f"removable link: k: {k}, link: {r_link}")
        sourceVertex = node.attrib.get('sourceVertex')
        targetVertex = node.attrib.get('targetVertex')
        if sourceVertex in link:
            node2 = nodeList[sourceVertex]
            root.remove(node2)
        elif targetVertex in link:
            node2 = nodeList[targetVertex]
            root.remove(node2)

        extract_points(node)
        extract_points(node2)
        print("POINTS:", points)
        # SplitBlock(outroot, nextattribid, componentOrdering, geometry, parent=parentattribid, style=split_style, func_name=func_name)

#key structure


# Save the modified XML
output_path = "../blocks/modified_graph.xml"
tree.write(output_path)

print(f"Modified XML saved to: {output_path}")
