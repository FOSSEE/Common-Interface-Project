import re
import xml.etree.ElementTree as ET
import math

TYPE_ARRAY = 'Array'
TYPE_DOUBLE = 'ScilabDouble'
TYPE_STRING = 'ScilabString'

CLASS_LIST = 'ScilabList'

BLOCK_AFFICHE = 'AfficheBlock'
BLOCK_BASIC = 'BasicBlock'
BLOCK_BIGSOM = 'BigSom'
BLOCK_EVENT_IN = 'EventInBlock'
BLOCK_EVENT_OUT = 'EventOutBlock'
BLOCK_EXPLICIT_IN = 'ExplicitInBlock'
BLOCK_EXPLICIT_OUT = 'ExplicitOutBlock'
BLOCK_GROUND = 'GroundBlock'
BLOCK_IMPLICIT_IN = 'ImplicitInBlock'
BLOCK_IMPLICIT_OUT = 'ImplicitOutBlock'
BLOCK_PRODUCT = 'Product'
BLOCK_ROUND = 'RoundBlock'
BLOCK_SPLIT = 'SplitBlock'
BLOCK_SUMMATION = 'Summation'
BLOCK_TEXT = 'TextBlock'
BLOCK_VOLTAGESENSOR = 'VoltageSensorBlock'

BLOCKTYPE_C = 'c'
BLOCKTYPE_D = 'd'
BLOCKTYPE_H = 'h'
BLOCKTYPE_L = 'l'
BLOCKTYPE_X = 'x'
BLOCKTYPE_Z = 'z'


def addNode(node, subNodeType, **kwargs):
    subNode = ET.SubElement(node, subNodeType)
    for (key, value) in kwargs.items():
        if value is not None:
            subNode.set(key, str(value))
    return subNode


def addOutNode(node, subNodeType,
               attribid, ordering, parent,
               interface_func_name, simulation_func_name, simulation_func_type,
               style, blockType,
               **kwargs):
    newkwargs = {'id': attribid, 'ordering': ordering, 'parent': parent,
                 'interfaceFunctionName': interface_func_name,
                 'simulationFunctionName': simulation_func_name,
                 'simulationFunctionType': simulation_func_type,
                 'style': style, 'blockType': blockType}
    newkwargs.update(kwargs)

    return addNode(node, subNodeType, **newkwargs)


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
    parameters = []

    if isinstance(node, dict):
        lastindex = None
        for i in range(100):
            parameter = 'p%03d_value' % i
            if parameter in node:
                value = node[parameter]
                parameters.append(value)
                if value != '':
                    lastindex = None
                elif lastindex is None:
                    lastindex = i
            else:
                break
        if lastindex is not None:
            del parameters[lastindex:]
    else:
        tag = subNodeType + '[@as="exprs"]'
        subNodes = node.find('./' + tag)

        if subNodes is not None:
            for data in subNodes:
                value = data.attrib.get('value')
                parameters.append(value)
        else:
            print(tag, ': Not found')

    return parameters

# Convert number into scientific notation
# Used by blocks Capacitor,ConstantVoltage,Inductor and Resistor


LOWER_LIMIT = 'lower_limit'
UPPER_LIMIT = 'upper_limit'
SIGN = 'sign'
VALUE = 'value'


def si_format(num):
    lower_limit = -11
    upper_limit = 15
    number = float(num)
    si_form = '{:.1e}'.format(number)
    neg_prefixes = (
                {SIGN: 'm', LOWER_LIMIT: -2, UPPER_LIMIT: 0, VALUE: 1E-3},
                {SIGN: 'μ', LOWER_LIMIT: -5, UPPER_LIMIT: -3, VALUE: 1E-6},
                {SIGN: 'n', LOWER_LIMIT: -8, UPPER_LIMIT: -6, VALUE: 1E-9},
                {SIGN: 'p', LOWER_LIMIT: -11, UPPER_LIMIT: -9, VALUE: 1E-12}
                )
    pos_prefixes = (
                {SIGN: '', LOWER_LIMIT: 1, UPPER_LIMIT: 3, VALUE: 1},
                {SIGN: 'k', LOWER_LIMIT: 4, UPPER_LIMIT: 6, VALUE: 1E3},
                {SIGN: 'M', LOWER_LIMIT: 7, UPPER_LIMIT: 9, VALUE: 1E6},
                {SIGN: 'G', LOWER_LIMIT: 10, UPPER_LIMIT: 12, VALUE: 1E9},
                {SIGN: 'T', LOWER_LIMIT: 13, UPPER_LIMIT: 15, VALUE: 1E12}
                )
    splits = si_form.split('e')
    base = float(splits[0])
    exp = int(splits[1])
    if exp < lower_limit or exp > upper_limit:
        return str(base) + ' 10^' + str(exp)
    else:
        if exp <= 0:
            for p in neg_prefixes:
                if exp >= p.get(LOWER_LIMIT) and exp <= p.get(UPPER_LIMIT):
                    return str(round(number/p.get(VALUE)))+' '+p.get(SIGN)
        else:
            for p in pos_prefixes:
                if exp >= p.get(LOWER_LIMIT) and exp <= p.get(UPPER_LIMIT):
                    return str(round(number/p.get(VALUE)))+' '+p.get(SIGN)


def print_affich_m(rows, columns, prec):
    s = '<TABLE>'
    for i in range(rows):
        s += '<TR>'
        for j in range(columns):
            s += '<TD>{:.{prec}f}</TD>'.format(0.0, prec=prec)
        s += '</TR>'
    s += '</TABLE>'
    return s


def print_affich_m_by_param(p0, p5):
    s = re.sub(r' *[\[\]] *', r'', p0)
    rc = re.split(' *[;,] *', s)
    rows = int(rc[0])
    columns = int(rc[1])
    prec = int(p5)
    return print_affich_m(rows, columns, prec)


def get_value_min(value):
    (v1, v2) = (value, re.sub(r'\([^()]*\)', r'', value))
    while v1 != v2:
        (v1, v2) = (v2, re.sub(r'\([^()]*\)', r'', v2))
    return re.sub(r'\^ *([a-zA-Z0-9]+|\([^()]*\)) *', r'<SUP>\1</SUP>', v1)
