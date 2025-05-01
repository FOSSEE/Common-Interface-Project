#!/usr/bin/env python

import os
import re
import sys
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from xcosblocks import process_xcos_model, remove_hyphen_number


if len(sys.argv) != 4:
    print("Usage: %s filename.xml workspace.dat context" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)
workspace_file = sys.argv[2]
context = sys.argv[3]

if ext != '.xml':
    print("Usage: %s filename.xml workspace.dat" % sys.argv[0])
    sys.exit(1)
base = r'(_[a-zA-Z]*_on_Cloud)?( *\([0-9]*\))?\.xml$'
title = re.sub(r'^.*/', r'', filename)
title = re.sub(base, r'', title)

tree = goodET.parse(filename)
model = tree.getroot()

rootattribid = '0:1:0'
parentattribid = '0:2:0'
outdiagram = process_xcos_model(model, title, rootattribid, parentattribid,
                                workspace_file, context)


outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = remove_hyphen_number(basename) + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
