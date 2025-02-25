#!/usr/bin/env python

import os
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

from xcosblocks import remove_hyphen_number
from xcosblocks import process_xcos_model


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

rootattribid = '0:1:0'
parentattribid = '0:2:0'
outdiagram = process_xcos_model(model, title, rootattribid, parentattribid)


outtree = ET.ElementTree(outdiagram)
ET.indent(outtree)
outfile = remove_hyphen_number(basename) + '.xcos'
outtree.write(outfile, encoding='UTF-8', xml_declaration=True)
sys.exit(0)
