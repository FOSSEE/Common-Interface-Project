#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from blocks import *

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

    blocks = {}
    EIV = {}
    IIV = {}
    CON = {}
    EOV = {}
    IOV = {}
    COM = {}
    IDLIST = {}
    links = {}
    sourceLinks = {}
    componentOrdering = 0
    for cell in list(root):
        try:
            attrib = cell.attrib
            attribid = attrib['id']

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
                parameter_values = cell.find('./Object[@as="parameter_values"]')
                if parameter_values is not None:
                    parameter_values = parameter_values.attrib
                    parameters = []
                    for i in range(100):
                        parameter = 'p%03d_value' % i
                        if parameter in parameter_values:
                            parameters.append(parameter_values[parameter])
                        else:
                            break
                EIV[attribid] = []
                IIV[attribid] = []
                CON[attribid] = []
                EOV[attribid] = []
                IOV[attribid] = []
                COM[attribid] = []
                IDLIST[attribid] = cell_type
                globals()[style](outroot, attribid, componentOrdering)
            elif 'vertex' in attrib:
                style = attrib['style']
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
                ordering = len(styleArray)
                IDLIST[attribid] = style
                globals()[style](outroot, attribid, ParentComponent, ordering)
            elif 'edge' in attrib:
                links['P' + attrib['sourceVertex']] = 'P' + attrib['targetVertex']
                links['P' + attrib['targetVertex']] = 'P' + attrib['sourceVertex']
                IDLIST[attribid] = 'link'
        except BaseException:
            traceback.print_exc()

        for attribid in blocks:
            for i, aid in enumerate(EOV[attribid]):
                sourceLinks[aid] = 1
            for i, aid in enumerate(IOV[attribid]):
                sourceLinks[aid] = 1
            for i, aid in enumerate(COM[attribid]):
                sourceLinks[aid] = 1
        for sourceLink in sourceLinks:
            pass

outnode = ET.SubElement(outdiagram, 'mxCell')
outnode.set('as', 'defaultParent')
outnode.set('id', str(1))
outnode.set('parent', str(0))

outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = basename + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
