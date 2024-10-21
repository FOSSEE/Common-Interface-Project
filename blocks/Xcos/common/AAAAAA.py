import re
import xml.etree.ElementTree as ET
import math
import random
import uuid

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
BLOCK_SUPER = 'SuperBlock'

BLOCKTYPE_C = 'c'
BLOCKTYPE_D = 'd'
BLOCKTYPE_H = 'h'
BLOCKTYPE_L = 'l'
BLOCKTYPE_X = 'x'
BLOCKTYPE_Z = 'z'

TYPE_INTEGER = 'ScilabInteger'
CLASS_TLIST = 'ScilabTList'
GEOMETRY = 'mxGeometry'
AS_REAL_PARAM = 'realParameters'
AS_INT_PARAM = 'integerParameters'
AS_NBZERO = 'nbZerosCrossing'
AS_NMODE = 'nmode'
AS_STATE = 'state'
AS_DSTATE = 'dState'
AS_OBJ_PARAM = 'objectsParameters'
AS_ODSTATE = 'oDState'
AS_EQUATIONS = 'equations'
TYPE_SUPER = 'SuperBlockDiagram'
TYPE_ADD = 'add'
TYPE_MODEL = 'mxGraphModel'
AS_MODEL = 'model'
TYPE_ROOT = 'root'
TYPE_MXCELL = 'mxCell'
TYPE_EVENTOUT = 'EventOutBlock'
TYPE_CNTRL = 'ControlPort'
TYPE_CMD = 'CommandPort'
TYPE_LINK = 'CommandControlLink'
TYPE_EXLINK = 'ExplicitLink'
AS_VALUE = 'OpAmp'
TYPE_EXPLICITOUTPORT = 'ExplicitOutputPort'
TYPE_EXPLICITINPORT = 'ExplicitInputPort'
AS_EXPRS = 'exprs'


def addNode(node, subNodeType, **kwargs):
    subNode = ET.SubElement(node, subNodeType)
    for (key, value) in kwargs.items():
        if value is not None:
            subNode.set(key, str(value))
    return subNode


def addObjNode(node, subNodeType, scilabClass, type, parameters):
    subNode = addDNode(node, subNodeType,
                       **{'as': type}, scilabClass=scilabClass)
    return subNode


def addPrecisionNode(node, subNodeType, type, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addAsDataNode(node,
                            subNodeType, type, height, width,
                            parameters, intPrecision='sci_int32')
    return subNode


# BITSET
def addNodePrecision(node, subNodeType, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addDataNode(node, subNodeType, height=1, width=width, intPrecision='sci_uint32')
    for i, param in enumerate(parameters):
        addDataData(subNode, param)
    return subNode


def addTypeNode(node, subNodeType, type, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addAsDataNode(node, subNodeType, type, height, width, parameters)
    return subNode


# equations node start
def addArrayNode(node, scilabClass, **kwargs):
    kwargs['scilabClass'] = scilabClass
    return addDNode(node, 'Array', **kwargs)


def addScilabStringNode(node, width, parameters):
    scilabStringNode = addDataNode(node, 'ScilabString', height=1, width=width)
    for i, param in enumerate(parameters):
        addDataData(scilabStringNode, param)


def addScilabBoolNode(node, width, parameters):
    scilabBooleanNode = addDataNode(node, 'ScilabBoolean', height=1, width=width)
    for i, param in enumerate(parameters):
        addDataData(scilabBooleanNode, param)


def addScilabDNode(node, type, realParts, width):
    height = 1 if width > 0 else 0
    scilabDoubleNode = addADataNode(node, 'ScilabDouble', type, height, width, realParts)
    for i, realPart in enumerate(realParts):
        addDData(scilabDoubleNode, column=i, line=0, realPart=realPart)
    return scilabDoubleNode


def addNodeScilabDB(node, type, realParts, height):
    width = 1 if height > 0 else 0
    scilabDoubleNode = addADataNode(node, 'ScilabDouble', type, height, width, realParts)
    for i, realPart in enumerate(realParts):
        addDData(scilabDoubleNode, column=i, line=0, realPart=realPart)
    return scilabDoubleNode


def addScilabDoubleNode(node, realParts, width):
    scilabDoubleNode = addDataNode(node, 'ScilabDouble', height=1, width=width)
    for i, realPart in enumerate(realParts):
        addDData(scilabDoubleNode, column=i, line=0, realPart=realPart)


def addNodeScilabDouble(node, realParts, height):
    scilabDoubleNode = addDataNode(node, 'ScilabDouble', height=height, width=1)
    for i, realPart in enumerate(realParts):
        addDData(scilabDoubleNode, column=i, line=0, realPart=realPart)


def addDData(parent, column=None, line=None, realPart=None):
    data_attributes = {}
    if line is not None:
        data_attributes['line'] = str(line)
    if column is not None:
        data_attributes['column'] = str(column)
    if realPart is not None:
        data_attributes['realPart'] = str(realPart)

    data_element = ET.Element('data', attrib=data_attributes)
    parent.append(data_element)
# equations node ends


def addgeometryNode(node, subNodeType, height, width, x, y):
    geometryNode = addDtNode(node, subNodeType, **{'as': 'geometry'},
                             height=height, width=width, x=x, y=y)
    return geometryNode


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
    data.set('line', str(line))
    data.set('column', str(column))
    if isinstance(value, (float, int)) or isReal:
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
    if 'height' in kwargs:
        DATA_HEIGHT = kwargs['height']
    if 'width' in kwargs:
        DATA_WIDTH = kwargs['width']
    DATA_LINE = 0
    DATA_COLUMN = 0
    subNode = addNode(node, subNodeType, **kwargs)
    return subNode


def addAsDataNode(node, subNodeType, a, height, width, parameters, **kwargs):
    newkwargs = {'as': a, 'height': height, 'width': width}
    newkwargs.update(kwargs)
    subNode = addDataNode(node, subNodeType, **newkwargs)

    for param in parameters:
        addDataData(subNode, param)
    return subNode


def addADataNode(node, subNodeType, a, height, width, parameters, **kwargs):
    newkwargs = {'as': a, 'height': height, 'width': width}
    newkwargs.update(kwargs)
    subNode = addDataNode(node, subNodeType, **newkwargs)
    return subNode


def addDNode(node, subNodeType, **kwargs):
    subNode = addNode(node, subNodeType, **kwargs)
    return subNode


# for x & y in mxgeometry
def addDtNode(node, subNodeType, **kwargs):
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
        if i < len(parameters):
            addDataData(subNode, parameters[i])
    return subNode


def addExprsArrayNode(node, subSubNodeType, height, parameters,
                      codeLines, additionalSubNodeType, func_name):
    subNode = addDataNode(node, TYPE_ARRAY, **{'as': 'exprs'},
                          scilabClass=CLASS_LIST)

    subSubNode = addDataNode(subNode, subSubNodeType, height=height, width=1)
    for i in range(height):
        addDataData(subSubNode, parameters[i])

    if additionalSubNodeType == TYPE_DOUBLE:
        addDataNode(subNode, additionalSubNodeType, height=0, width=0)
    elif additionalSubNodeType == TYPE_ARRAY:
        nestedArrayNode = addDataNode(subNode, TYPE_ARRAY, scilabClass=CLASS_LIST)
        addDataNode(nestedArrayNode, TYPE_DOUBLE, height=0, width=0)
    elif additionalSubNodeType == TYPE_STRING:
        if func_name == 'CONSTRAINT2_c':
            nestedArrayNode = addDataNode(subNode, additionalSubNodeType, height=1, width=1)
            addDataData(nestedArrayNode, '0')
            nestedArrayNode = addDataNode(subNode, additionalSubNodeType, height=1, width=1)
            addDataData(nestedArrayNode, '0')
        elif func_name == 'DEBUG':
            nestedArrayNode = addDataNode(subNode, additionalSubNodeType, height=1, width=1)
            addDataData(nestedArrayNode, 'xcos_debug_gui(flag,block);')

    return subNode


def getParametersFromExprsNode(node, subNodeType):
    parameters = []

    if isinstance(node, dict):
        parameters = node['parameters']
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


# Super Block Diagram
def addSuperNode(node, subNodeType,
                 a, background, gridEnabled,
                 title, **kwargs):
    newkwargs = {'as': a, 'background': background,
                 'gridEnabled': gridEnabled,
                 'title': title
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addSuperBlkNode(node, subNodeType,
                    a, scilabClass,
                    **kwargs):
    newkwargs = {'as': a, 'scilabClass': scilabClass
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def superAddNode(node, subNodeType,
                 value,
                 **kwargs):
    newkwargs = {'value': value
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxGraphModelNode(node, subNodeType,
                        a,
                        **kwargs):
    newkwargs = {'as': a
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxCellNode(node, subNodeType,
                  id,
                  **kwargs):
    newkwargs = {'id': id
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addNodemxCell(node, subNodeType, a,
                  id,
                  **kwargs):
    newkwargs = {'as': a, 'id': id
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxCell(node, subNodeType,
              id,
              **kwargs):
    newkwargs = {'id': id
                 }
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addEventOutBlock(node, subNodeType,
                     id, parent,
                     interfaceFunctionName,
                     simulationFunctionName,
                     simulationFunctionType,
                     style, blockType,
                     dependsOnU, dependsOnT,
                     **kwargs):
    newkwargs = {'id': id, 'parent': parent,
                 'interfaceFunctionName': interfaceFunctionName,
                 'simulationFunctionName':
                 simulationFunctionName,
                 'simulationFunctionType':
                 simulationFunctionType,
                 'style': style,
                 'blockType': blockType,
                 'dependsOnU': dependsOnU,
                 'dependsOnT': dependsOnT}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addPort(node, subNodeType,
            id, parent, ordering,
            dataType, dataColumns, dataLines, initialState,
            style, value,
            **kwargs):
    newkwargs = {'id': id, 'parent': parent,
                 'ordering': ordering,
                 'dataType': dataType,
                 'dataColumns': dataColumns,
                 'dataLines': dataLines,
                 'initialState': initialState,
                 'style': style, 'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def adPort(node, subNodeType,
           id, parent, ordering,
           initialState,
           style, value,
           **kwargs):
    newkwargs = {'id': id, 'parent': parent,
                 'ordering': ordering,
                 'initialState': initialState,
                 'style': style, 'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addLink(node, subNodeType,
            id, parent,
            source, target,
            style, value,
            **kwargs):
    newkwargs = {'id': id, 'parent': parent,
                 'source': source,
                 'target': target,
                 'style': style, 'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addGeoNode(node, subNodeType,
               a,
               **kwargs):
    newkwargs = {'as': a}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxPointNode(node, subNodeType,
                   a, x, y,
                   **kwargs):
    newkwargs = {'as': a, 'x': x, 'y': y}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addPointNode(node, subNodeType,
                 x, y,
                 **kwargs):
    newkwargs = {'x': x, 'y': y}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addArray(node, subNodeType,
             a,
             **kwargs):
    newkwargs = {'as': a}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


# OpAmp
def addSciStringNode(node, height, parameters):
    scilabStringNode = addDataNode(node, 'ScilabString', height=height, width=1)
    for i in range(height):
        addDataData(scilabStringNode, parameters[i])


def addScilabDBNode(node, height):
    addDataNode(node, 'ScilabDouble', height=height, width=0)


# Sine Voltage
def addTNode(node, subNodeType, type, width, parameters):
    height = 1 if width > 0 else 0
    subNode = addAsDataNode(node, subNodeType, type, height, width, parameters)
    return subNode


def addSciDBNode(node, subNodeType, type, width, realParts):
    height = 1 if width > 0 else 0
    subNode = addAsDataNode(node, subNodeType, type, height, width, realParts)
    return subNode


# DOLLAR_m
def addScilabIntNode(node, width, parameters):
    height = 1 if width > 0 else 0
    subNode = addDataNode(node, 'ScilabInteger', height=height, width=width,
                          intPrecision='sci_int8')
    for i, param in enumerate(parameters):
        addDataData(subNode, param)
    return subNode


# Logic
def addSciIntNode(node, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addDataNode(node, 'ScilabInteger', height=height, width=width,
                          intPrecision='sci_int8')
    for i, param in enumerate(parameters):
        addDataData(subNode, param)
    return subNode


# CSCope
def addPrecNode(node, subNodeType, type, width, parameters):
    height = 1 if width > 0 else 0
    subNode = addAsDataNode(node,
                            subNodeType, type, height, width,
                            parameters, intPrecision='sci_int32')
    return subNode


def strarray(parameter):
    param = list(map(str, parameter[0].split(" ")))
    params = parameter[3][1:8].split(";")
    parameters = ['-1', '1'] + [parameter[7]] + param + ['-1', '-1'] + params
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
        {SIGN: 'p', LOWER_LIMIT: -11, UPPER_LIMIT: -9, VALUE: 1E-12})
    pos_prefixes = (
        {SIGN: '', LOWER_LIMIT: 1, UPPER_LIMIT: 3, VALUE: 1},
        {SIGN: 'k', LOWER_LIMIT: 4, UPPER_LIMIT: 6, VALUE: 1E3},
        {SIGN: 'M', LOWER_LIMIT: 7, UPPER_LIMIT: 9, VALUE: 1E6},
        {SIGN: 'G', LOWER_LIMIT: 10, UPPER_LIMIT: 12, VALUE: 1E9},
        {SIGN: 'T', LOWER_LIMIT: 13, UPPER_LIMIT: 15, VALUE: 1E12})
    splits = si_form.split('e')
    base = float(splits[0])
    exp = int(splits[1])
    if exp < lower_limit or exp > upper_limit:
        return str(base) + ' 10^' + str(exp)
    else:
        if exp <= 0:
            for p in neg_prefixes:
                if exp >= p.get(LOWER_LIMIT) and exp <= p.get(UPPER_LIMIT):
                    return str(round(number / p.get(VALUE))) + ' ' + p.get(SIGN)
        else:
            for p in pos_prefixes:
                if exp >= p.get(LOWER_LIMIT) and exp <= p.get(UPPER_LIMIT):
                    return str(round(number / p.get(VALUE))) + ' ' + p.get(SIGN)


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
    return get_number_power(v1)


def get_number_power(value):
    return re.sub(r'(\^|\*\*) *([a-zA-Z0-9]+|\([^()]*\)) *', r'<SUP>\2</SUP>',
                  value)


def format_real_number(parameter):
    if 'e' in parameter or 'E' in parameter:
        real_number = float(parameter.replace('*10^', 'e').replace('10^', '1e'))
        formatted_number = "{:.1E}".format(real_number)
    else:
        formatted_number = "{:.1f}".format(float(parameter))
    return formatted_number


def num2str(num):
    """Converts a float to an integer first if it ends in .0."""
    if num % 1 == 0:
        num = int(num)
    return str(num)


def generate_id(block_count, port_count, link_count):
    def random_hex(part1, sequence):
        part3 = f"{sequence:x}"
        return f"{part1}:{part3}"

    part1 = f"{uuid.uuid4().int >> 64 & 0xffffffff:x}"
    all_ids = [random_hex(part1, i) for i in range(block_count + port_count + link_count)]
    block_ids = all_ids[0:block_count]
    port_ids = all_ids[block_count:block_count + port_count]
    link_ids = all_ids[block_count + port_count:block_count + port_count + link_count]

    return block_ids, port_ids, link_ids


def style_to_object(style):
    if not style.endswith(';'):
        style += ';'
    
    style_object = {}
    remaining_style = style

    while remaining_style:
        index_of_key_value = remaining_style.find(';')
        
        index_of_key = remaining_style.find('=')
        if 0 < index_of_key < index_of_key_value:
            key = remaining_style[:index_of_key]
            value = remaining_style[index_of_key + 1:index_of_key_value]
            style_object[key] = value
        else:
            key = 'default'
            value = remaining_style[:index_of_key_value]
            if value and key not in style_object:
                style_object[key] = value

        remaining_style = remaining_style[index_of_key_value + 1:]
    
    return style_object
