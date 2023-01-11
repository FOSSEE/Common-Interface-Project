import re
import xml.etree.ElementTree as ET

TYPE_ARRAY = 'Array'
TYPE_DOUBLE = 'ScilabDouble'
TYPE_STRING = 'ScilabString'

CLASS_LIST = 'ScilabList'


def addNode(node, subNodeType, **kwargs):
    subNode = ET.SubElement(node, subNodeType)
    for (key, value) in kwargs.items():
        subNode.set(key, str(value))
    return subNode


def addData(node, column, line, value, isReal=False):
    data = ET.SubElement(node, 'data')
    data.set('column', str(column))
    data.set('line', str(line))
    if type(value) == float or type(value) == int or isReal:
        data.set('realPart', str(value))
    else:
        data.set('value', value)
    return data


DATA_HEIGHT = 0
DATA_WIDTH = 0
DATA_LINE = 0
DATA_COLUMN = 0


def addDataNode(node, subNodeType, **kwargs):
    global DATA_HEIGHT, DATA_WIDTH, DATA_LINE, DATA_COLUMN
    DATA_HEIGHT = kwargs['height']
    DATA_WIDTH = kwargs['width']
    DATA_LINE = 0
    DATA_COLUMN = 0
    subNode = addNode(node, subNodeType, **kwargs)
    return subNode


def addDataData(node, value, isReal=False):
    global DATA_HEIGHT, DATA_WIDTH, DATA_LINE, DATA_COLUMN
    if DATA_LINE >= DATA_HEIGHT or DATA_COLUMN >= DATA_WIDTH:
        print('Invalid: height=', DATA_HEIGHT, ',width=', DATA_WIDTH,
              ',line=', DATA_LINE, ',column=', DATA_COLUMN)
    data = addData(node, DATA_COLUMN, DATA_LINE, value, isReal)
    if DATA_LINE < DATA_HEIGHT - 1:
        DATA_LINE += 1
    else:
        DATA_COLUMN += 1
    return data


def addExprsNode(node, subNodeType, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addDataNode(node, subNodeType, **{'as': 'exprs'},
                          height=height, width=width)
    for i in range(height):
        addDataData(subNode, parameters[i])
    return subNode


def addExprsArrayNode(node, subSubNodeType, height, parameters, codeLines):
    subNode = addDataNode(node, TYPE_ARRAY, **{'as': 'exprs'},
                          scilabClass=CLASS_LIST)

    subSubNode = addDataNode(subNode, subSubNodeType, height=height, width=1)
    for i in range(height):
        addDataData(subSubNode, parameters[i])

    codeHeight = len(codeLines)
    subSubNode = addDataNode(subNode, TYPE_STRING,
                             height=codeHeight, width=1)
    for i in range(codeHeight):
        addDataData(subSubNode, codeLines[i])

    return subNode


def getParametersFromExprsNode(node, subNodeType):
    tag = subNodeType + '[@as="exprs"]'
    subNodes = node.find('./' + tag)

    parameters = []
    if subNodes is not None:
        for data in subNodes:
            value = data.attrib.get('value')
            parameters.append(value)
    else:
        print(tag, ': Not found')

    return parameters
