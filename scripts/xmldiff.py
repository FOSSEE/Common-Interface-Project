#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as goodET

def remove_keys(elem):
    for key in ['x', 'y', 'height', 'width', 'style']:
        if key in elem:
            del elem[key]
    return elem

def compare_xml_files(file1, file2):
    tree1 = goodET.parse(file1)
    tree2 = goodET.parse(file2)

    root1 = tree1.getroot()
    root2 = tree2.getroot()

    differences = []

    compare_elements(root1, root2, differences)

    return differences

def compare_elements(elem1, elem2, differences):
    if elem1.tag != elem2.tag:
        differences.append(f"Tags differ: {elem1.tag} != {elem2.tag}")
        return

    if elem1.text != elem2.text:
        differences.append(f"Text differs: {elem1.text} != {elem2.text}")

    remove_keys(elem1.attrib)
    remove_keys(elem2.attrib)
    if elem1.attrib != elem2.attrib:
        s1 = set(elem1.attrib.items())
        s2 = set(elem2.attrib.items())
        s1ms2 = s1 - s2
        s2ms1 = s2 - s1
        if s1ms2:
            differences.append(f"< {elem1.tag} {s1ms2}")
        if s2ms1:
            differences.append(f"> {elem1.tag} {s2ms1}")

    for child1, child2 in zip(elem1, elem2):
        compare_elements(child1, child2, differences)

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} file1 file2")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

differences = compare_xml_files(file1, file2)

for difference in differences:
    print(difference)
