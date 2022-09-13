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
    print('Not mxGraphModel')
    sys.exit(2)
outdiagram = ET.Element('XcosDiagram')
outdiagram.set('background', '-1')
outdiagram.set('finalIntegrationTime', '30.0')   # TODO: From POST
outdiagram.set('title', title)
dt = datetime.datetime(2016, 4, 6, 20, 40)
comment = ET.Comment(dt.strftime('Xcos - 1.0 - scilab-5.5.2 - %Y%m%d %H%M'))
outdiagram.append(comment)
outmodel = ET.SubElement(outdiagram, 'mxGraphModel')
outmodel.set('as', 'model')

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
    for cell in list(root):
        try:
            attrib = cell.attrib
            attribid = attrib['id']
            if nextattribid <= int(attribid):
                nextattribid = int(attribid) + 1

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
                componentGeometry = {}
                componentGeometry['height'] = 40
                componentGeometry['width'] = 40
                componentGeometry['x'] = 0
                componentGeometry['y'] = 0
                componentOrdering += 1
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
                mxGeometry = cell.find('mxGeometry')
                if mxGeometry is not None:
                    componentGeometry['height'] = mxGeometry.attrib['height']
                    componentGeometry['width'] = mxGeometry.attrib['width']
                    componentGeometry['x'] = mxGeometry.attrib['x']
                    componentGeometry['y'] = mxGeometry.attrib['y']
                EIV[attribid] = []
                IIV[attribid] = []
                CON[attribid] = []
                EOV[attribid] = []
                IOV[attribid] = []
                COM[attribid] = []
                IDLIST[attribid] = cell_type
                globals()[style](outroot, attribid, componentOrdering, componentGeometry, parameters)
            elif 'vertex' in attrib:
                style = attrib['style']
                geometry = {}
                geometry['height'] = 40
                geometry['width'] = 40
                geometry['x'] = 0
                geometry['y'] = 0
                ParentComponent = attrib['ParentComponent']
                if style == 'ExplicitInputPort':
                    styleArray = EIV[ParentComponent]
                elif style == 'ImplicitInputPort':
                    styleArray = IIV[ParentComponent]
                elif style == 'ControlPort':
                    styleArray = CON[ParentComponent]
                elif style == 'ExplicitOutputPort':
                    styleArray = EOV[ParentComponent]
                elif style == 'ImplicitOutputPort':
                    styleArray = IOV[ParentComponent]
                elif style == 'CommandPort':
                    styleArray = COM[ParentComponent]
                styleArray.append(attribid)
                mxGeometry = cell.find('mxGeometry')
                if mxGeometry is not None:
                    geometry['height'] = mxGeometry.attrib['height']
                    geometry['width'] = mxGeometry.attrib['width']
                    geometry['x'] = mxGeometry.attrib.get('x', 0)
                    geometry['y'] = mxGeometry.attrib.get('y', 0)
                    if mxGeometry.attrib.get('relative', '0') == '1':
                        geometry['x'] = float(componentGeometry['x']) + float(componentGeometry['width']) * float(geometry['x'])
                        geometry['y'] = float(componentGeometry['y']) + float(componentGeometry['height']) * float(geometry['y'])
                ordering = len(styleArray)
                IDLIST[attribid] = style
                globals()[style](outroot, attribid, ParentComponent, ordering, geometry)
            elif 'edge' in attrib:
                sourceVertex = attrib['sourceVertex']
                targetVertex = attrib['targetVertex']
                sourceType = IDLIST[sourceVertex]
                targetType = IDLIST[targetVertex]

                # switch vertices if required
                if sourceType in ['ExplicitInputPort', 'ImplicitInputPort', 'ControlPort'] and targetType in ['ExplicitOutputPort', 'ExplicitLink', 'ImplicitOutputPort', 'ImplicitLink', 'CommandPort', 'CommandControlLink']:
                    (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                    (sourceType, targetType) = (targetType, sourceType)
                elif sourceType in ['ExplicitInputPort', 'ExplicitLink', 'ImplicitInputPort', 'ImplicitLink', 'ControlPort', 'CommandControlLink'] and targetType in ['ExplicitOutputPort', 'ImplicitOutputPort', 'CommandPort']:
                    (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
                    (sourceType, targetType) = (targetType, sourceType)

                style = None
                addSplit = False
                if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'ImplicitInputPort', 'ImplicitOutputPort', 'CommandPort', 'ControlPort'] and targetType == sourceType:
                    print('cannot connect two ports of', sourceType, 'and', targetType)
                elif sourceType in ['ExplicitOutputPort'] and targetType in ['ExplicitInputPort']:
                    style = 'ExplicitLink'
                elif sourceType in ['ExplicitOutputPort', 'ExplicitLink'] and targetType in ['ExplicitInputPort', 'ExplicitLink']:
                    addSplit = True
                elif sourceType in ['ImplicitOutputPort'] and targetType in ['ImplicitInputPort']:
                    style = 'ImplicitLink'
                elif sourceType in ['ImplicitOutputPort', 'ImplicitLink'] and targetType in ['ImplicitInputPort', 'ImplicitLink']:
                    addSplit = True
                elif sourceType in ['CommandPort'] and targetType in ['ControlPort']:
                    style = 'CommandControlLink'
                elif sourceType in ['CommandPort', 'CommandControlLink'] and targetType in ['ControlPort', 'CommandControlLink']:
                    addSplit = True
                else:
                    print(attribid, 'Unknown combination of', sourceType, 'and', targetType)
                    continue

                if style is not None:
                    edgeDict[attribid] = (style, sourceVertex, targetVertex, sourceType, targetType)
                    edgeDict2[attribid] = (style, sourceVertex, targetVertex, sourceType, targetType)
                    IDLIST[attribid] = style
                if addSplit:
                    mxGeometry = cell.find('mxGeometry')
                    if mxGeometry is not None:
                        mxPoint = mxGeometry.find('mxPoint')
                        if mxPoint is not None:
                            geometry = {}
                            geometry['width'] = mxPoint.attrib.get('width', '7')
                            geometry['height'] = mxPoint.attrib.get('height', '7')
                            geometry['x'] = mxPoint.attrib.get('x', '0')
                            geometry['y'] = mxPoint.attrib.get('y', '0')
                            splitList.append((attribid, sourceVertex, targetVertex, sourceType, targetType, geometry))
                            try:
                                del edgeDict[sourceVertex]
                            except KeyError:
                                pass
                            try:
                                del edgeDict[targetVertex]
                            except KeyError:
                                pass
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

outnode = ET.SubElement(outdiagram, 'mxCell')
outnode.set('id', str(1))
outnode.set('parent', str(0))
outnode.set('as', 'defaultParent')

outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = basename + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
