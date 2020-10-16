#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Usage: %s filename" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
tree = ET.parse(filename)
mxGraphModel = tree.getroot()
if mxGraphModel.tag != 'mxGraphModel':
    print('Not mxGraphModel')
    sys.exit(2)

for root in mxGraphModel:
    if root.tag != 'root':
        print('Not root')
        sys.exit(2)

    a1 = ''
    a1 += 'outf = tempname(\'Xcos\');\n'
    a1 += 'outfd = mopen(outf, \'wt\');\n'
    a1 += '\n'
    a1 += 'SIMULATION_ET = 30;\n'   # TODO: From POST
    a1 += 'SIMULATION_DT = 0.1;\n'  # TODO: From POST
    a1 += 't = 0;\n'
    blocks = {}
    EIV = {}
    IIV = {}
    CON = {}
    EOV = {}
    IOV = {}
    COM = {}
    links = {}
    sourceLinks = {}
    for mxCell in list(root):
        attrib = mxCell.attrib
        attribid = attrib['id']
        if 'block_id' in attrib:
            parameter_values = mxCell.find('./Object[@as="parameter_values"]')
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
                blocks[attribid] = attrib['value']
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

    print(a1, end='')
    print('while t <= SIMULATION_ET do')
    for attribid in blocks:
        print('    EIV%s = list(%s); IIV%s = list(%s); CON%s = list(%s);' % (
            attribid, ', '.join(EIV[attribid]),
            attribid, ', '.join(IIV[attribid]),
            attribid, ', '.join(CON[attribid])))
        print(('    [EOV%s, IOV%s, COM%s, SV%s] = '
               'Xcos_%s(outfd, t, EIV%s, IIV%s, CON%s, BP%s, SV%s);') % (
            attribid, attribid, attribid, attribid, blocks[attribid],
            attribid, attribid, attribid, attribid, attribid))
        for i, aid in enumerate(EOV[attribid]):
            print('    %s = EOV%s(%d);' % (aid, attribid, i + 1))
            sourceLinks[aid] = 1
        for i, aid in enumerate(IOV[attribid]):
            print('    %s = IOV%s(%d);' % (aid, attribid, i + 1))
            sourceLinks[aid] = 1
        for i, aid in enumerate(COM[attribid]):
            print('    %s = COM%s(%d);' % (aid, attribid, i + 1))
            sourceLinks[aid] = 1
    print()
    for sourceLink in sourceLinks:
        print('    %s = %s;' % (links[sourceLink], sourceLink))
    print('    t = t + SIMULATION_DT;')
    print('end')
    print('')
    print('mclose(outfd);')
