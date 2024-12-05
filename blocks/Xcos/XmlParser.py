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

for root in model:
    if root.tag != 'root':
        print('Not root')
        sys.exit(2)
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
    rootattribid = None
    parentattribid = None
    key1 = {}
    graph_port = {}
    graph_link = {}
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

                elif 'vertex' in attrib:

                    style = attrib['style']
                    stylename = style_to_object(style)['default']
                    IDLIST[attribid] = stylename
                    print(attribid, stylename)
                    key1[attribid] = attribid
                    graph_port[attribid] = [attribid]
                    graph_link[attribid] = []
                    print('setting port', attribid)

                elif 'edge' in attrib:

                    sourceVertex = attrib['sourceVertex']
                    targetVertex = attrib['targetVertex']

                    try:
                        sourceType = IDLIST[sourceVertex]
                        targetType = IDLIST[targetVertex]
                        print('ST,TT', sourceType, targetType)
                    except KeyError:
                        remainingcells.append(cell)
                        continue

                    #key structure
                    key1[attribid] = attribid
                    graph_port[attribid] = []
                    graph_link[attribid] = [attribid]
                    print('setting link', attribid)
                    if sourceVertex in key1:
                        key = key1[sourceVertex]
                        key1[sourceVertex] = attribid
                        print('replacing', sourceVertex, key, attribid)
                        graph_port[attribid].extend(graph_port[key]) #merge
                        graph_link[attribid].extend(graph_link[key])
                        del graph_port[key]
                        del graph_link[key]
                        print('extending', attribid)
                        print('removing', key)

                    if targetVertex in key1:
                        key = key1[targetVertex]
                        key1[targetVertex] = attribid
                        print('replacing', sourceVertex, key, attribid)
                        graph_port[attribid].extend(graph_port[key]) #merge
                        graph_link[attribid].extend(graph_link[key])
                        del graph_port[key]
                        del graph_link[key]
                        print('extending', attribid)
                        print('removing', key)

                    print('key1', len(key1))
                    key1values = set(key1.values())
                    print('unique keys', len(key1values))
                    graph_port_keys = set(graph_port.keys())
                    print('graph_port', len(graph_port_keys))
                    port1_diff = key1values - graph_port_keys
                    if len(port1_diff) > 0:
                        print('dp1:', port1_diff)
                    port1_diff2 = graph_port_keys - key1values
                    if len(port1_diff2) > 0:
                        print('dp2:', port1_diff2)
                    graph_link_keys = set(graph_link.keys())
                    print('graph_link', len(graph_link_keys))
                    link1_diff = key1values - graph_link_keys
                    if len(link1_diff) > 0:
                        print('dl1:', link1_diff)
                    link1_diff2 = graph_link_keys - key1values
                    if len(link1_diff2) > 0:
                        print('dl2:', link1_diff2)

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

                    IDLIST[attribid] = style
            except BaseException:
                traceback.print_exc()
                sys.exit(0)
        oldcellslength = cellslength
        cells = remainingcells
        cellslength = len(remainingcells)
        remainingcells = []
        print('cellslength=', cellslength, ', oldcellslength=', oldcellslength)
for k, port in graph_port.items():
    if len(port) > 0:
        print(f"GRAPH port: k: {k}, port: {port}")
    link = graph_link[k]
    if len(link) > 0:
        print(f"GRAPH link: k: {k}, link: {link}")


#key structure


# Save the modified XML
output_path = "../blocks/modified_graph.xml"
tree.write(output_path)

print(f"Modified XML saved to: {output_path}")
