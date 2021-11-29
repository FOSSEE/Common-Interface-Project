#!/usr/bin/env python

import datetime
import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

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

    a1 = ''
    blocks = {}
    EIV = {}
    IIV = {}
    CON = {}
    EOV = {}
    IOV = {}
    COM = {}
    links = {}
    sourceLinks = {}
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
                outnode = ET.SubElement(outroot, style)
                parameter_values = cell.find('./Object[@as="parameter_values"]')
                if parameter_values is not None:
                    parameter_values = parameter_values.attrib
                    parameters = []
                    for i in range(40):
                        parameter = 'p%03d_value' % i
                        if parameter in parameter_values:
                            parameters.append(parameter_values[parameter])
                        else:
                            break
                    a1 += 'BP%s = list(%s);\n' % (attribid, ', '.join(parameters))
                    a1 += 'SV%s = list();\n' % attribid
                    EIV[attribid] = []
                    IIV[attribid] = []
                    CON[attribid] = []
                    EOV[attribid] = []
                    IOV[attribid] = []
                    COM[attribid] = []
            elif 'vertex' in attrib:
                style = attrib['style']
                ParentComponent = attrib['ParentComponent']
                if style in ['ExplicitInputPort', 'ImplicitInputPort',
                             'ControlPort']:
                    a1 += 'P%s = 0;\n' % attribid
                if style == 'ExplicitInputPort':
                    EIV[ParentComponent].append('P%s' % attribid)
                elif style == 'ImplicitInputPort':
                    IIV[ParentComponent].append('P%s' % attribid)
                elif style == 'ControlPort':
                    CON[ParentComponent].append('P%s' % attribid)
                elif style == 'ExplicitOutputPort':
                    EOV[ParentComponent].append('P%s' % attribid)
                elif style == 'ImplicitOutputPort':
                    IOV[ParentComponent].append('P%s' % attribid)
                elif style == 'CommandPort':
                    COM[ParentComponent].append('P%s' % attribid)
            elif 'edge' in attrib:
                links['P' + attrib['sourceVertex']] = 'P' + attrib['targetVertex']
                links['P' + attrib['targetVertex']] = 'P' + attrib['sourceVertex']
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

ET.SubElement(outdiagram, 'mxCell')

outtree = ET.ElementTree(outdiagram)
outfile = basename + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
