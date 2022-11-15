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
    print("Usage: %s filename.xcos" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)

if ext != '.xcos':
    print("Usage: %s filename.xcos" % sys.argv[0])
    sys.exit(1)
base = r'(_[a-zA-Z]*_on_Cloud)?( *\([0-9]*\))?\.xcos$'
title = re.sub(r'^.*/', r'', filename)
title = re.sub(base, r'', title)

tree = goodET.parse(filename)

diagram = tree.getroot()
if diagram.tag != 'XcosDiagram':
    print(diagram.tag, '!= XcosDiagram')
    sys.exit(2)

for model in diagram:
    if model.tag == 'mxCell' and model.attrib['as'] == 'defaultParent':
        continue

    if model.tag != 'mxGraphModel':
        print(model.tag, '!= mxGraphModel')
        sys.exit(2)
    outmodel = ET.Element('mxGraphModel')

    for root in model:
        if root.tag != 'root':
            print('Not root')
            sys.exit(2)
        outroot = ET.SubElement(outmodel, 'root')

        EIV = {}
        IIV = {}
        CON = {}
        EOV = {}
        IOV = {}
        COM = {}
        IDLIST = {}
        componentOrdering = 0
        nextattribid = 0
        nextAttribForSplit = 10000
        edgeDict = {}
        edgeDict2 = {}
        splitList = []
        splitBlockList = []
        for cell in list(root):
            try:
                tag = cell.tag
                attrib = cell.attrib
                attribid = attrib['id']

                if attribid == '0' or attribid == '0:1:0':
                    parentattribid = attribid
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    outnode.set('appname', 'Xcos')
                    outnode.set('description', '')
                    outnode.set('CellType', 'Unknown')
                    outnode.set('sourceVertex', str(0))
                    outnode.set('targetVertex', str(0))
                    outnode.set('tarx', str(0))
                    outnode.set('tary', str(0))

                    node = ET.SubElement(outnode, 'Object')
                    node.set('as', 'parameter_values')

                    node = ET.SubElement(outnode, 'Object')
                    node.set('as', 'displayProperties')
                    continue

                if attribid == '1' or attribid == '0:2:0':
                    childattribid = attribid
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('id', attribid)
                    outnode.set('CellType', 'Unknown')
                    outnode.set('sourceVertex', str(0))
                    outnode.set('targetVertex', str(0))
                    outnode.set('tarx', str(0))
                    outnode.set('tary', str(0))

                    node = ET.SubElement(outnode, 'Object')
                    node.set('as', 'parameter_values')

                    node = ET.SubElement(outnode, 'Object')
                    node.set('as', 'displayProperties')
                    continue

                if tag == 'SplitBlock':
                    print('SplitBlock', attribid)
                    splitBlockList.append(attribid)
                    continue

                try:
                    interfaceFunctionName = attrib['interfaceFunctionName']
                except KeyError as e:
                    interfaceFunctionName = None

                if interfaceFunctionName is not None:
                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('style', interfaceFunctionName)
                    outnode.set('id', attribid)
                    outnode.set('vertex', str(1))
                    outnode.set('connectable', str(0))
                    outnode.set('CellType', 'Component')
                    outnode.set('blockprefix', 'XCOS')
                    outnode.set('sourceVertex', str(0))
                    outnode.set('targetVertex', str(0))
                    outnode.set('tarx', str(0))
                    outnode.set('tary', str(0))

                    mxGeometry = cell.find('mxGeometry')
                    outMxGeometry = ET.SubElement(outnode, 'mxGeometry')
                    outMxGeometry.set('x', mxGeometry.attrib['x'] if mxGeometry is not None else str(0))
                    outMxGeometry.set('y', mxGeometry.attrib['y'] if mxGeometry is not None else str(0))
                    outMxGeometry.set('width', mxGeometry.attrib['width'] if mxGeometry is not None else str(40))
                    outMxGeometry.set('height', mxGeometry.attrib['height'] if mxGeometry is not None else str(40))
                    if mxGeometry is not None and mxGeometry.attrib.get('relative', '0') != '0':
                        outMxGeometry.set('relative', mxGeometry.attrib['relative'])
                    outMxGeometry.set('as', 'geometry')

                    try:
                        (parameters, display_parameter) = globals()['get_from_' + interfaceFunctionName](cell)
                    except BaseException as e:
                        print(repr(e), 'in', tag, attrib)
                        (parameters, display_parameter) = ([], '')

                    outObject = ET.SubElement(outnode, 'Object')
                    for i in range(0, 20):
                        outObject.set(f'p{i:03d}_value', parameters[i] if i < len(parameters) else '')
                    outObject.set('as', 'parameter_values')

                    outObject = ET.SubElement(outnode, 'Object')
                    outObject.set('display_parameter', display_parameter)
                    outObject.set('as', 'displayProperties')
                    continue
                elif tag.endswith('Port'):
                    ParentComponent = attrib['parent']
                    IDLIST[attribid] = tag

                    outnode = ET.SubElement(outroot, 'mxCell')
                    outnode.set('style', tag)
                    outnode.set('id', attribid)
                    outnode.set('vertex', str(1))
                    outnode.set('CellType', 'Pin')
                    outnode.set('ParentComponent', ParentComponent)
                    outnode.set('sourceVertex', str(0))
                    outnode.set('targetVertex', str(0))
                    outnode.set('tarx', str(0))
                    outnode.set('tary', str(0))

                    mxGeometry = cell.find('mxGeometry')
                    outMxGeometry = ET.SubElement(outnode, 'mxGeometry')
                    outMxGeometry.set('x', mxGeometry.attrib['x'] if mxGeometry is not None else str(0))
                    outMxGeometry.set('y', mxGeometry.attrib['y'] if mxGeometry is not None else str(0))
                    outMxGeometry.set('width', mxGeometry.attrib['width'] if mxGeometry is not None else str(40))
                    outMxGeometry.set('height', mxGeometry.attrib['height'] if mxGeometry is not None else str(40))
                    if mxGeometry is not None and mxGeometry.attrib.get('relative', '0') != '0':
                        outMxGeometry.set('relative', mxGeometry.attrib['relative'])
                    outMxGeometry.set('as', 'geometry')

                    outObject = ET.SubElement(outnode, 'Object')
                    outObject.set('as', 'parameter_values')

                    outObject = ET.SubElement(outnode, 'Object')
                    outObject.set('as', 'displayProperties')
                    continue
                elif tag.endswith('Link'):
                    sourceVertex = attrib['source']
                    targetVertex = attrib['target']
                    sourceType = IDLIST[sourceVertex]
                    targetType = IDLIST[targetVertex]
                    print('sourceType=', sourceType, 'targetType=',targetType)

                    sourcePorts = ['ExplicitOutputPort', 'ImplicitOutputPort', 'CommandPort']
                    targetPorts = ['ExplicitInputPort', 'ImplicitInputPort', 'ControlPort']
                    links = ['ExplicitLink', 'ImplicitLink', 'CommandControlLink']

                    # switch vertices if required
                    if sourceType in targetPorts and targetType in [*sourcePorts, *links]:
                        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                        (sourceType, targetType) = (targetType, sourceType)
                    elif sourceType in [*targetPorts, *links] and targetType in sourcePorts:
                        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                        (sourceType, targetType) = (targetType, sourceType)

                    style = None
                    if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'ImplicitInputPort', 'ImplicitOutputPort', 'CommandPort', 'ControlPort'] and targetType == sourceType:
                        print('cannot connect two ports of', sourceType, 'and', targetType)
                    elif sourceType in ['ExplicitOutputPort'] and targetType in ['ExplicitInputPort']:
                        style = 'ExplicitLink'
                    elif sourceType in ['ImplicitOutputPort'] and targetType in ['ImplicitInputPort']:
                        style = 'ImplicitLink'
                    elif sourceType in ['CommandPort'] and targetType in ['ControlPort']:
                        style = 'CommandControlLink'
                    else:
                        print(attribid, 'Unknown combination of', sourceType, 'and', targetType)
                        continue

                    if style is not None:
                        edgeDict[attribid] = (style, sourceVertex, targetVertex, sourceType, targetType)
                        edgeDict2[attribid] = (style, sourceVertex, targetVertex, sourceType, targetType)
                        IDLIST[attribid] = style
            except KeyError as e:
                print(repr(e), 'in', tag, attrib)
            except BaseException:
                traceback.print_exc()

    for (attribid, sourceVertex, targetVertex, sourceType, targetType, geometry) in splitList:
        componentOrdering += 1
        SplitBlock(outroot, nextattribid, componentOrdering, geometry)
        splitblockid = nextattribid
        nextattribid += 1
        inputCount = 0
        outputCount = 0
        if sourceType == 'ExplicitOutputPort':
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[targetVertex]
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
        elif sourceType == 'ImplicitOutputPort':
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
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[sourceVertex]
        elif sourceType == 'ControlPort':
            geometry = {}
            geometry['width'] = 8
            geometry['height'] = 8
            geometry['x'] = -4
            geometry['y'] = -8
            inputCount += 1
            CommandPort(outroot, nextattribid, splitblockid, inputCount, geometry, forSplitBlock=True)
            portid = nextattribid
            nextattribid += 1
            linkid = nextAttribForSplit
            nextAttribForSplit += 1
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[sourceVertex]
        if targetType == 'ExplicitInputPort':
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[sourceVertex]
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, edgeDict, inputCount, outputCount, nextattribid, nextAttribForSplit)
        elif targetType == 'ImplicitInputPort':
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
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[targetVertex]
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
        elif targetType == 'CommandPort':
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
            (style2, sourceVertex2, targetVertex2, sourceType2, targetType2) = edgeDict2[targetVertex]

    for (attribid, (style, sourceVertex, targetVertex, sourceType, targetType)) in edgeDict.items():
        if int(attribid) >= 10000:
            attribid = nextattribid
            nextattribid += 1
        globals()[style](outroot, attribid, sourceVertex, targetVertex)

outtree = ET.ElementTree(outmodel)
ET.indent(outtree)
outfile = basename + '.xml'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
