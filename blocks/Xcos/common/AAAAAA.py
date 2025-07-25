import ast
import os
from os.path import abspath, isfile, join
import pexpect
import re
import sys
import traceback
import xml.etree.ElementTree as ET
import math
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
AS_VALUE = 'OpAmp'
AS_EXPRS = 'exprs'

PORT_EXPLICITINPUT = 'ExplicitInputPort'
PORT_EXPLICITOUTPUT = 'ExplicitOutputPort'
PORT_IMPLICITINPUT = 'ImplicitInputPort'
PORT_IMPLICITOUTPUT = 'ImplicitOutputPort'
PORT_CONTROL = 'ControlPort'
PORT_COMMAND = 'CommandPort'

LINK_EXPLICIT = 'ExplicitLink'
LINK_IMPLICIT = 'ImplicitLink'
LINK_COMMANDCONTROL = 'CommandControlLink'

SCILAB_DIR = '../../scilab_for_xcos_on_cloud'
SCILAB_DIR = abspath(SCILAB_DIR)
SCILAB = join(SCILAB_DIR, 'bin', 'scilab-cli')

WORKSPACE = None
ANSI_ESCAPE_PATTERN = r'(?:\x1b\[[0-9;]*m)'
ANSI_ESCAPE = re.compile(ANSI_ESCAPE_PATTERN)
SCILAB_PROMPT = re.compile(rf'{ANSI_ESCAPE_PATTERN}*--> {ANSI_ESCAPE_PATTERN}*')
BACKSPACE = re.compile(r'.\x08')


# Following are system command which are not permitted in sci files
# (Reference scilab-on-cloud project)
SYSTEM_COMMANDS = (
    r'ascii|dir\(|execstr|host|mputl|newfun|system|unix(_[gswx])?\('
)
SPECIAL_CHARACTERS = r'["\'\\]'

SCILAB_CURVE_C_SCI = "macros/Sources/CURVE_c.sci"
SCILAB_EXPRESSION_SCI = "macros/Misc/EXPRESSION.sci"

CONT_FRM_WRITE = "ajax-scilab/cont_frm_write.sci"
CLEANDATA_SCI_FUNC_WRITE = "ajax-scilab/scifunc-cleandata-do_spline.sci"
EXP_SCI_FUNC_WRITE = "ajax-scilab/expression-sci-function.sci"
GET_COLORMAP_VALUES_SCI_FUNC_WRITE = "ajax-scilab/get_colormap_values.sci"
RANDFUNC = "ajax-scilab/randfunc.sci"

INTERNAL = {
    'getOutput': {
        'scriptfiles': [CONT_FRM_WRITE],
        'function': 'calculate_cont_frm',
        'parameters': ['num', 'den'],
    },
    'getExpressionOutput': {
        'scriptfiles': [SCILAB_EXPRESSION_SCI, EXP_SCI_FUNC_WRITE],
        'function': 'callFunctionAcctoMethod',
        'parameters': ['head', 'exx'],
    },
    'cleandata': {
        'scriptfiles': [SCILAB_CURVE_C_SCI, CLEANDATA_SCI_FUNC_WRITE],
        'function': 'callFunctioncleandata',
        'parameters': ['xye'],
    },
    'do_Spline': {
        'scriptfiles': [SCILAB_CURVE_C_SCI, CLEANDATA_SCI_FUNC_WRITE],
        'function': 'callFunction_do_Spline',
        'parameters': ['N', 'order', 'x', 'y'],
    },
    'get_colormap_values': {
        'scriptfiles': [GET_COLORMAP_VALUES_SCI_FUNC_WRITE],
        'function': 'getvaluesfromcolormap',
        'parameters': ['colormapString'],
    },
    'randfunc': {
        'scriptfiles': [RANDFUNC],
        'function': 'randfunc',
        'parameters': ['inputvalue'],
    }
}


def load_variables(filename):
    '''
    add scilab commands to load only user defined variables
    '''

    command = "[__V1,__V2]=listvarinfile('%s');" % filename
    command += "__V5=grep(string(__V2),'/^([124568]|1[07])$/','r');"
    command += "__V1=__V1(__V5);"
    command += "__V2=__V2(__V5);"
    command += "__V5=grep(__V1,'/^[^%]+$/','r');"
    command += "if ~isempty(__V5) then;"
    command += "__V1=__V1(__V5);"
    command += "__V2=__V2(__V5);"
    command += "__V6=''''+strcat(__V1,''',''')+'''';"
    command += "__V7='load(''%s'','+__V6+');';" % filename
    command += "execstr(__V7);"
    command += "end;"
    command += "clear __V1 __V2 __V5 __V6 __V7;"
    return command


def load_scripts():
    # handle duplicate scriptfiles
    scriptfiles = set()
    for internal in INTERNAL.values():
        for scriptfile in internal['scriptfiles']:
            scriptfiles.add(scriptfile)

    cmd = ''
    for scriptfile in scriptfiles:
        cmd += f"exec('{scriptfile}');"

    p = 's'
    cmd += f"{p}=poly(0,'{p}');"
    p = 'z'
    cmd += f"{p}=poly(0,'{p}');"

    cmd += 'format(17);'

    return cmd


class ScilabWorkspace:
    def __init__(self, title, workspace, context=None):
        self.title = title
        self.workspace = workspace
        self.context = context

        cmd = load_scripts()
        if workspace not in [None, '', 'None']:
            print('workspace=', workspace)
            cmd += load_variables(workspace)
        if context not in [None, '', 'None']:
            context = context.strip(' \t\n\r\f\v;')
            if context:
                context += ';'
            msg = is_safe_string('context', context)
            if not msg:
                print(f'setting context={context}')
                cmd += f"execstr('{context}');"
            else:
                print(f"Ignoring unsafe context {context}: {msg}")

        scilab_cmd = [SCILAB,
                      "-noatomsautoload",
                      "-nogui",
                      "-nouserstartup",
                      "-nb",
                      "-e", cmd
                      ]

        env = os.environ.copy()
        env['TERM'] = 'dumb'
        self.child = pexpect.spawn(scilab_cmd[0], scilab_cmd[1:], env=env, encoding='utf-8', timeout=15)
        self.child.expect(SCILAB_PROMPT)

    def add_context(self, context):
        if context in [None, '', 'None']:
            return

        msg = is_safe_string('context', context)
        if msg:
            print(f"Ignoring unsafe context {context}: {msg}")
            return

        if self.context == context:
            print(f'context already set to {context}')
            return

        if self.context not in [None, '', 'None']:
            print(f'adding new context={context}')
            self.context += context
        else:
            print(f'setting context={context}')
            self.context = context

        self.send_command(f"execstr('{context}');")

    def clean_output(self, text, expr):
        # Remove echoed input and Scilab formatting
        text = re.sub(ANSI_ESCAPE, '', text)
        text = re.sub(BACKSPACE, '', text)
        lines = [line.strip() for line in text.splitlines()]
        if lines and lines[0] == expr:
            lines = lines[1:]
        text = '\n'.join(lines).strip()
        return text

    def send_expression(self, expression):
        """Send a line to the process and return its output"""
        expression = expression.strip(' \t\n\r\f\v;')
        if expression == '':
            print('No expression')
            return ''

        expr = f'disp({expression})'
        self.child.sendline(expr)
        self.child.expect(SCILAB_PROMPT)
        output = self.child.before.strip()

        return self.clean_output(output, expr)

    def send_command(self, command):
        """Send a line to the process and return its output"""
        command = command.strip(' \t\n\r\f\v')
        if command == '':
            print('No command')
            return ''

        self.child.sendline(command)
        self.child.expect(SCILAB_PROMPT)
        output = self.child.before.strip()

        return self.clean_output(output, command)

    def clean(self):
        """Terminate the process cleanly"""
        self.child.sendline('exit')
        self.child.close()
        self.child = None


def addNode(node, subNodeType, **kwargs):
    subNode = ET.SubElement(node, subNodeType)
    for key, value in kwargs.items():
        if value is not None:
            subNode.set(key, str(value))
    return subNode


def addObjNode(node, subNodeType, scilabClass, type):
    subNode = addDNode(node, subNodeType,
                       **{'as': type}, scilabClass=scilabClass)
    return subNode


def addPrecisionNode(node, subNodeType, type, height, parameters):
    width = 1 if height > 0 else 0
    subNode = addAsDataNode(node,
                            subNodeType, type, height, width,
                            parameters, False, intPrecision='sci_int32')
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
    subNode = addAsDataNode(node, subNodeType, type, height, width, parameters, False)
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
    scilabDoubleNode = addADataNode(node, 'ScilabDouble', type, height, width)
    for i, realPart in enumerate(realParts):
        addDData(scilabDoubleNode, column=i, line=0, realPart=realPart)
    return scilabDoubleNode


def addNodeScilabDB(node, type, realParts, height):
    width = 1 if height > 0 else 0
    scilabDoubleNode = addADataNode(node, 'ScilabDouble', type, height, width)
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
                             x=x, y=y, width=width, height=height)
    return geometryNode


def addOutNode(node, subNodeType,
               attribid, ordering, parent,
               interface_func_name, simulation_func_name, simulation_func_type,
               style, blockType,
               **kwargs):
    newkwargs = {'id': attribid, 'parent': parent,
                 'interfaceFunctionName': interface_func_name,
                 'blockType': blockType,
                 'simulationFunctionName': simulation_func_name,
                 'simulationFunctionType': simulation_func_type,
                 'style': style}
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


def addAsDataNode(node, subNodeType, a, height, width, parameters, isReal, **kwargs):
    newkwargs = {'as': a, 'height': height, 'width': width}
    newkwargs.update(kwargs)
    subNode = addDataNode(node, subNodeType, **newkwargs)

    for param in parameters:
        addDataData(subNode, param, isReal)
    return subNode


def addADataNode(node, subNodeType, a, height, width):
    newkwargs = {'as': a, 'height': height, 'width': width}
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


def getParametersFromExprsNode(node, subNodeType=TYPE_STRING):
    parameters = []

    if node is None:
        pass
    elif isinstance(node, dict):
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

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    return (parameters, display_parameter, eiv, iiv, con, eov, iov, com)


# Super Block Diagram
def addSuperNode(node, subNodeType,
                 a, background, gridEnabled,
                 title, **kwargs):
    newkwargs = {'as': a, 'background': background,
                 'gridEnabled': gridEnabled,
                 'title': title}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addSuperBlkNode(node, subNodeType,
                    a, scilabClass,
                    **kwargs):
    newkwargs = {'as': a, 'scilabClass': scilabClass}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def superAddNode(node, subNodeType,
                 value,
                 **kwargs):
    newkwargs = {'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxGraphModelNode(node, subNodeType,
                        a,
                        **kwargs):
    newkwargs = {'as': a}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxCellNode(node, subNodeType,
                  id,
                  **kwargs):
    newkwargs = {'id': id}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addNodemxCell(node, subNodeType, a,
                  id,
                  **kwargs):
    newkwargs = {'as': a, 'id': id}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addmxCell(node, subNodeType,
              id,
              **kwargs):
    newkwargs = {'id': id}
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
            initialState,
            style, value,
            **kwargs):
    newkwargs = {'id': id, 'parent': parent,
                 'ordering': ordering,
                 'initialState': initialState,
                 'style': style, 'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addExplicitInputPort(root, id, parent, ordering, initialState,
                         style="ExplicitInputPort;align=left;verticalAlign=middle;spacing=10.0;rotation=0;flip=false;mirror=false",
                         value="",
                         **kwargs):
    return addPort(root, PORT_EXPLICITINPUT,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addExplicitOutputPort(root, id, parent, ordering, initialState,
                          style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0;flip=false;mirror=false",
                          value="",
                          **kwargs):
    return addPort(root, PORT_EXPLICITOUTPUT,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addImplicitInputPort(root, id, parent, ordering, initialState,
                         style="ImplicitInputPort;align=left;verticalAlign=middle;spacing=10.0;rotation=0;flip=false;mirror=false",
                         value="",
                         **kwargs):
    return addPort(root, PORT_IMPLICITINPUT,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addImplicitOutputPort(root, id, parent, ordering, initialState,
                          style="ImplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0;flip=false;mirror=false",
                          value="",
                          **kwargs):
    return addPort(root, PORT_IMPLICITOUTPUT,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addControlPort(root, id, parent, ordering, initialState,
                   style="ControlPort;align=center;verticalAlign=top;spacing=10.0;rotation=0;flip=false;mirror=false",
                   value="",
                   **kwargs):
    return addPort(root, PORT_CONTROL,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addCommandPort(root, id, parent, ordering, initialState,
                   style="CommandPort;align=center;verticalAlign=bottom;spacing=10.0;rotation=0;flip=false;mirror=false",
                   value="",
                   **kwargs):
    return addPort(root, PORT_COMMAND,
                   id, parent, ordering,
                   initialState,
                   style, value,
                   **kwargs)


def addLink(node, subNodeType, id, parent, source, target,
            style, value, **kwargs):
    newkwargs = {'id': id, 'parent': parent, 'source': source, 'target': target,
                 'style': style, 'value': value}
    newkwargs.update(kwargs)
    return addNode(node, subNodeType, **newkwargs)


def addExplicitLink(node, id, parent, source, target,
                    style=LINK_EXPLICIT, value="", **kwargs):
    return addLink(node, LINK_EXPLICIT, id, parent, source, target,
                   style, value, **kwargs)


def addImplicitLink(node, id, parent, source, target,
                    style=LINK_IMPLICIT, value="", **kwargs):
    return addLink(node, LINK_IMPLICIT, id, parent, source, target,
                   style, value, **kwargs)


def addCommandControlLink(node, id, parent, source, target,
                          style=LINK_COMMANDCONTROL, value="", **kwargs):
    return addLink(node, LINK_COMMANDCONTROL, id, parent, source, target,
                   style, value, **kwargs)


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
    subNode = addAsDataNode(node, subNodeType, type, height, width, parameters, False)
    return subNode


def addSciDBNode(node, subNodeType, type, width, realParts):
    height = 1 if width > 0 else 0
    subNode = addAsDataNode(node, subNodeType, type, height, width, realParts, True)
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
                            parameters, False, intPrecision='sci_int32')
    return subNode


def addEquationsNode(node, scilabStringParameters=None,
                     additionalStringsArray=None,
                     parameterNames=None, parameters=None):
    equationsArrayNode = addArrayNode(node, scilabClass="ScilabTList", **{'as': 'equations'})

    if scilabStringParameters:
        addScilabStringNode(equationsArrayNode, width=len(scilabStringParameters),
                            parameters=scilabStringParameters)

    if additionalStringsArray:
        for additionalStrings in additionalStringsArray:
            additionalStringNode = addDataNode(equationsArrayNode,
                                               'ScilabString',
                                               height=1, width=len(additionalStrings))
            for param in additionalStrings:
                addDataData(additionalStringNode, param)

    if parameterNames and parameters and len(parameterNames) == len(parameters):
        innerArrayNode = addArrayNode(equationsArrayNode,
                                      scilabClass="ScilabList")
        addSciStringNode(innerArrayNode, len(parameterNames), parameterNames)
        addNodeScilabDouble(innerArrayNode, height=len(parameters), realParts=[
            format_real_number(x) for x in parameters
        ])

    return equationsArrayNode


def strarray(parameter):
    param = parameter[0].split(" ")
    params = parameter[3].strip('[]').split(';')
    parameters = ['-1', '1'] + [parameter[7]] + param + ['-1', '-1'] + params
    return parameters


def stringtoarray(parameter):
    array = re.split(r'[;, ]+', parameter)
    return array


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


def convert_scientific_notation(parameter):
    def repl(match):
        if match.group('bare_exp'):  # Case: '10^3' with no coefficient
            return f"1e{match.group('bare_exp')}"
        elif match.group('with_coeff'):  # Case: '2*10^3' or '*10^3'
            return 'e' + match.group('with_coeff')
        elif match.group('fortran'):  # Case: '1.23d4' or '1.23D4'
            return f"{match.group('num')}e{match.group('exp')}"
        return match.group(0)  # Fallback (shouldn't happen)

    pattern = re.compile(
        r"(?P<bare> (?<![\d*])10\^(?P<bare_exp>[-+]?\d+))"
        r"|(?P<with_star>\*?10\^(?P<with_coeff>[-+]?\d+))"
        r"|(?P<fortran>(?P<num>\d+\.?\d*)[dD](?P<exp>[-+]?\d+))",
        re.VERBOSE
    )

    return pattern.sub(repl, parameter)


def format_real_number(parameter):
    if type(parameter) is not str:
        return parameter
    if re.search(r'[a-zA-Z]', parameter):  # Check if parameter contains alphabetic characters
        if WORKSPACE is None:
            print(f'No Scilab workspace available for {parameter} evaluation')
            return parameter
        msg = is_safe_string('parameter', parameter)
        if msg:
            print(f"Ignoring unsafe parameter {parameter}: {msg}")
            return parameter
        print(f'send {parameter} to Scilab')
        parameter = WORKSPACE.send_expression(parameter)
        print(f'received {parameter} from Scilab')
        if re.search(r'^Undefined', parameter):
            raise ValueError(f"Scilab workspace: {parameter}")
    if not parameter.strip():  # Handle empty strings
        return '0'
    try:
        parameter = convert_scientific_notation(parameter)
        parameter = eval(parameter)
        return "{:.17g}".format(float(parameter))  # Convert numeric strings safely
    except ValueError:
        return parameter  # Return original non-numeric string


def format_real_numbers(parameters):
    return [format_real_number(p) for p in parameters]


def num2str(num):
    """Converts a float to an integer first if it ends in .0."""
    if num % 1 == 0:
        num = int(num)
    return str(num)


def get_max_exponent(polynomial, chr='s'):
    exponents = []
    regex = chr + r'\s*\^\s*\d+|' + chr
    matches = re.findall(regex, polynomial)
    if len(matches) == 0:
        exponents.append(0)
    else:
        for match in matches:
            splits = re.split(r'\s*\^\s*', match)
            exponent = int(splits[1]) if len(splits) == 2 else 1
            exponents.append(exponent)
    return max(exponents)


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


# parserfunction
def remove_hyphen_number(s):
    return re.sub(r'-\d+$', '', s)


def get_int(s):
    try:
        return int(s)
    except ValueError:
        return -1


def getNextAttribId(attribid, nextattribid):
    attribint = get_int(attribid)
    if nextattribid <= attribint:
        nextattribid = attribint + 1
    return nextattribid


def checkModelTag(model):
    if model.tag != 'mxGraphModel':
        print(model.tag, '!= mxGraphModel')
        sys.exit(102)


def checkXcosDiagramTag(diagram):
    if diagram.tag != 'XcosDiagram' and diagram.tag != 'SuperBlockDiagram':
        print(diagram.tag, '!= XcosDiagram')
        sys.exit(102)


def checkRootTag(root):
    if root.tag != 'root':
        print('Not root')
        sys.exit(102)


def createOutnode(i, outroot, rootattribid, parentattribid):
    if i == 0:
        outnode = ET.SubElement(outroot, 'mxCell')
        outnode.set('id', rootattribid)
    elif i == 1:
        outnode = ET.SubElement(outroot, 'mxCell')
        outnode.set('id', parentattribid)
        outnode.set('parent', rootattribid)
    else:
        outnode = None
    return outnode


def portType1(sType, sType2, tType2):
    # port1
    if sType == 'ExplicitLink':
        if sType2 == 'ExplicitOutputPort' or sType2 == 'ExplicitLink':
            return 'explicitInputPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    elif sType == 'ImplicitLink':
        if sType2 == 'ImplicitOutputPort' or sType2 == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if sType2 == 'CommandPort' or sType2 == 'CommandControlLink':
            return 'controlPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    else:
        print('Error: (sourceType, sourceType2, targetType2) =',
              '(', sType, ',', sType2, ',', tType2, ')')


def portType2(sType, sType2, tType2):
    # port2
    if sType == 'ExplicitLink':
        if tType2 == 'ExplicitInputPort' or tType2 == 'ExplicitLink':
            return 'explicitOutputPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')
    elif sType == 'ImplicitLink':
        if tType2 == 'ImplicitOutputPort' or tType2 == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if tType2 == 'ControlPort' or tType2 == 'CommandControlLink':
            return 'commandPort'
        else:
            print('Error: (sourceType, sourceType2, targetType2) =',
                  '(', sType, ',', sType2, ',', tType2, ')')


def portType3(sType, tType):
    # port3
    if sType == 'ExplicitLink':
        if tType == 'ExplicitInputPort' or tType == 'ExplicitLink':
            return 'explicitOutputPort'
        else:
            print('Error: (sourceType, targetType) =',
                  '(', sType, ',', tType, ')')
    elif sType == 'ImplicitLink':
        if tType == 'ImplicitOutputPort' or tType == 'ImplicitLink':
            return 'implicitInputPort'
        else:
            return 'implicitOutputPort'
    elif sType == 'CommandControlLink':
        if tType == 'ControlPort' or tType == 'CommandControlLink':
            return 'commandPort'
        else:
            print('Error: (sourceType, targetType) =',
                  '(', sType, ',', tType, ')')


def addPort1ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array):
    if sourceType == 'ExplicitLink':
        if sourceType2 == 'ExplicitOutputPort' or sourceType2 == 'ExplicitLink':
            return addExplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if sourceType2 == 'ImplicitOutputPort' or targetType2 == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
    elif sourceType == 'CommandControlLink':
        if sourceType2 == 'CommandPort' or sourceType2 == 'CommandControlLink':
            return addControlPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def addPort2ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array):
    if sourceType == 'ExplicitLink':
        if targetType2 == 'ExplicitInputPort' or targetType2 == 'ExplicitLink':
            return addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if targetType2 == 'ImplicitOutputPort' or sourceType2 == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
    elif sourceType == 'CommandControlLink':
        if targetType2 == 'ControlPort' or targetType2 == 'CommandControlLink':
            return addCommandPortForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def addPort3ForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, array3):
    if sourceType == 'ExplicitLink':
        if targetType == 'ExplicitInputPort':
            return addExplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    elif sourceType == 'ImplicitLink' or targetType == 'ImplicitLink':
        if targetType == 'ImplicitOutputPort' or sourceType == 'ImplicitOutputPort':
            return addImplicitInputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            return addImplicitOutputPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
    elif sourceType == 'CommandControlLink':
        if targetType == 'ControlPort':
            return addCommandPortForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)
        else:
            print('Error: (sourceType, targetType, sourceType2, targetType2) =',
                  '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    else:
        print('Error: (sourceType, targetType, sourceType2, targetType2) =',
              '(', sourceType, ',', targetType, ',', sourceType2, ',', targetType2, ')')
    return (None, None, None, None)


def create_mxCell(style, id, vertex="1", connectable="0", CellType="Component", blockprefix="XCOS",
                  explicitInputPorts="0", explicitOutputPorts="0", implicitInputPorts="0", implicitOutputPorts="0", controlPorts="0", commandPorts="0",
                  simulationFunction="split", sourceVertex="0", targetVertex="0", tarx="0", tary="0", geometry=None):

    mxCell = ET.Element("mxCell", {
        "style": style,
        "id": id,
        "vertex": vertex,
        "connectable": connectable,
        "CellType": CellType,
        "blockprefix": blockprefix,
        "explicitInputPorts": str(explicitInputPorts),
        "implicitInputPorts": str(implicitInputPorts),
        "explicitOutputPorts": str(explicitOutputPorts),
        "implicitOutputPorts": str(implicitOutputPorts),
        "controlPorts": str(controlPorts),
        "commandPorts": str(commandPorts),
        "simulationFunction": simulationFunction,
        "sourceVertex": sourceVertex,
        "targetVertex": targetVertex,
        "tarx": tarx,
        "tary": tary,
    })

    if geometry:
        x, y, width, height = geometry
        ET.SubElement(mxCell, "mxGeometry", {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry"
        })

    ET.SubElement(mxCell, "Object", {
        "display_parameter": str(),
        "as": "displayProperties"
    })

    ET.SubElement(mxCell, "Object", {
        "as": "parameter_values"
    })

    return mxCell


def create_mxCell_port(style, id, parentComponent, ordering="1", vertex="1", cellType="Pin",
                       sourceVertex="0", targetVertex="0", tarx="0", tary="0", geometry=None):
    mxcell = ET.Element('mxCell', {
        'style': style,
        'id': str(id),
        'ordering': ordering,
        'vertex': vertex,
        'CellType': cellType,
        'ParentComponent': str(parentComponent),
        'sourceVertex': sourceVertex,
        'targetVertex': targetVertex,
        'tarx': tarx,
        'tary': tary,
    })

    if geometry:
        x, y, width, height = geometry
        mxgeometry = ET.SubElement(mxcell, 'mxGeometry', {
            'x': str(x),
            'y': str(y),
            'width': str(width),
            'height': str(height),
            'relative': '1',
            'as': 'geometry'
        })

        ET.SubElement(mxgeometry, 'mxPoint', {
            'y': '-4',
            'as': 'offset'
        })

        ET.SubElement(mxcell, "Object", {
            "as": "parameter_values"
        })

        ET.SubElement(mxcell, "Object", {
            "as": "displayProperties"
        })

    return mxcell


def create_mxCell_edge(id, edge="1", cellType="Unknown",
                       sourceVertex="0", targetVertex="0", tarx="0", tary="0", tar2x="0", tar2y="0", source_point="0", target_point="0", waypoints=None):
    mxcell = ET.Element('mxCell', {
        'id': str(id),
        'edge': edge,
        'CellType': cellType,
        'sourceVertex': str(sourceVertex),
        'targetVertex': str(targetVertex),
        'tarx': tarx,
        'tary': tary,
        'tar2x': tar2x,
        'tar2y': tar2y,
    })

    mxgeometry = ET.SubElement(mxcell, 'mxGeometry', {
        'relative': '1',
        'as': 'geometry'
    })

    ET.SubElement(mxgeometry, 'mxPoint', {
        'x': str(source_point[0]),
        'y': str(source_point[1]),
        'as': 'sourcePoint'
    })

    ET.SubElement(mxgeometry, 'mxPoint', {
        'x': str(target_point[0]),
        'y': str(target_point[1]),
        'as': 'targetPoint'
    })

    array_element = ET.SubElement(mxgeometry, 'Array', {
        'as': 'points'
    })

    for waypoint in waypoints[1:-1]:
        ET.SubElement(array_element, 'mxPoint', {
            'x': waypoint['x'],  # Access 'x' key
            'y': waypoint['y']   # Access 'y' key
        })

    ET.SubElement(mxcell, "Object", {
        "as": "parameter_values"
    })

    ET.SubElement(mxcell, "Object", {
        "as": "displayProperties"
    })

    return mxcell


def check_point_on_array(array, point, left_right_direction=True):
    if array is None:
        return False, array, []

    pointX = float(point['x'])
    pointY = float(point['y'])

    for i in range(len(array) - 1):
        leftX = float(array[i]['x'])
        leftY = float(array[i]['y'])
        rightX = float(array[i + 1]['x'])
        rightY = float(array[i + 1]['y'])

        # Check if the point lies on the line segment between array[i] and array[i + 1]

        pointbetweenleftrightx = leftX <= pointX <= rightX or leftX >= pointX >= rightX
        samey = -40 <= leftY - pointY <= 40 and -40 <= rightY - pointY <= 40
        sameleftorrighty = -20 <= leftY - pointY <= 20 or -20 <= rightY - pointY <= 20

        if pointbetweenleftrightx and (samey or sameleftorrighty):
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        pointbetweenleftrighty = leftY <= pointY <= rightY or leftY >= pointY >= rightY
        samex = -40 <= leftX - pointX <= 40 and -40 <= rightX - pointX <= 40
        sameleftorrightx = -20 <= leftX - pointX <= 20 or -20 <= rightX - pointX <= 20

        if pointbetweenleftrighty and (samex or sameleftorrightx):
            return True, array[:i + 1] + [point], [point] + array[i + 1:]

        # switch direction for the next waypoint
        left_right_direction = not left_right_direction
    return False, array, []


def identify_segment(array, point):
    for i, waypoint in enumerate(array):
        result, left_array, right_array = check_point_on_array(waypoint, point)
        if result:
            return result, i, left_array, right_array
    print("Error:", point, "does not lie on", array)
    return False, -1, array, []


def getOrdering(attrib, portCount, ParentComponent, orderingname):
    try:
        ordering = attrib['ordering']
    except KeyError:
        ordering = portCount[ParentComponent][orderingname]
    return ordering


def switchPorts(sourceVertex, sourceType, targetVertex, targetType, waypoints):
    # switch vertices if required
    switch_split = False

    if sourceType in ['ExplicitInputPort', 'ImplicitInputPort', 'ControlPort'] and \
            targetType in ['ExplicitOutputPort', 'ExplicitLink', 'ImplicitOutputPort', 'ImplicitLink', 'CommandPort', 'CommandControlLink']:
        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
        (sourceType, targetType) = (targetType, sourceType)
        waypoints.reverse()
        switch_split = True
    elif sourceType in ['ExplicitInputPort', 'ExplicitLink', 'ImplicitInputPort', 'ImplicitLink', 'ControlPort', 'CommandControlLink'] and \
            targetType in ['ExplicitOutputPort', 'ImplicitOutputPort', 'CommandPort']:
        (sourceVertex, targetVertex) = (targetVertex, sourceVertex)
        (sourceType, targetType) = (targetType, sourceType)
        waypoints.reverse()
        switch_split = True

    return (sourceVertex, sourceType, targetVertex, targetType, switch_split)


def getLinkStyle(attribid, sourceVertex, sourceType, targetVertex, targetType, waypoints):
    (sourceVertex, sourceType, targetVertex, targetType, switch_split) = switchPorts(sourceVertex, sourceType, targetVertex, targetType, waypoints)

    style = None

    if sourceType in ['ExplicitInputPort', 'ExplicitOutputPort', 'CommandPort', 'ControlPort'] and \
            targetType == sourceType:
        print(attribid, 'cannot connect two ports of', sourceType, 'and', targetType)
    elif sourceType in ['ExplicitLink', 'CommandControlLink'] and \
            targetType == sourceType:
        print(attribid, 'cannot connect two links of', sourceType, 'and', targetType)
    elif sourceType in ['ExplicitOutputPort', 'ExplicitLink'] and \
            targetType in ['ExplicitInputPort', 'ExplicitLink']:
        style = 'ExplicitLink'
    elif sourceType in ['ImplicitOutputPort', 'ImplicitInputPort', 'ImplicitLink'] and \
            targetType in ['ImplicitInputPort', 'ImplicitOutputPort', 'ImplicitLink']:
        style = 'ImplicitLink'
    elif sourceType in ['CommandPort', 'CommandControlLink'] and \
            targetType in ['ControlPort', 'CommandControlLink']:
        style = 'CommandControlLink'
    else:
        print(attribid, 'Unknown combination of', sourceType, 'and', targetType)

    addSplit = sourceType.endswith('Link') or targetType.endswith('Link')

    return (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints)


def initLinks(attribid, graph_value, removable_value, key1, graph_link, removable_link):
    # for ports, the graph_value and the removable_value are empty lists
    # for links, the graph_value is a list containing itself and the
    # removable_value is a list containing itself if it has a split point and an
    # empty list otherwise
    key1[attribid] = attribid
    graph_link[attribid] = graph_value
    removable_link[attribid] = removable_value


def mergeLinks(attribid, vertex, key1, graph_link, removable_link):
    # for links only
    # merge the ports/links of the source/target vertex into itself
    # also, remove the ports/links of the source/target vertex
    if vertex in key1:
        key = key1[vertex]
        for v in graph_link[key]:
            key1[v] = attribid

        graph_link[attribid].extend(graph_link[key])
        removable_link[attribid].extend(removable_link[key])

        del graph_link[key]
        del removable_link[key]


def getlinkdetails(port, sourceVertex2, targetVertex2, otherVertex, tarx, tary, tar2x, tar2y, otherx, othery,
                   left_array, right_array, array3, biglinkid, smalllinkid):
    if port == 0:
        port_index = sourceVertex2
        portx = tarx
        porty = tary
        waypoints = left_array
        linkid = biglinkid
    elif port == 1:
        port_index = targetVertex2
        portx = tar2x
        porty = tar2y
        waypoints = right_array
        linkid = biglinkid
    else:
        port_index = otherVertex
        portx = otherx
        porty = othery
        waypoints = array3
        linkid = smalllinkid
    return port_index, portx, porty, waypoints, linkid


def addtolinklist(port, explicitInputPorts, explicitOutputPorts, implicitInputPorts, implicitOutputPorts, controlPorts, commandPorts,
                  port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid, linklist):
    if port < explicitInputPorts:
        port_type = "ExplicitInputPort"
        link_type = "ExplicitLink"
        linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
    elif port < explicitInputPorts + implicitInputPorts:
        port_type = "ImplicitInputPort"
        link_type = "ImplicitLink"
        linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
    elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts:
        port_type = "ExplicitOutputPort"
        link_type = "ExplicitLink"
        linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
    elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts + implicitOutputPorts:
        port_type = "ImplicitOutputPort"
        link_type = "ImplicitLink"
        linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
    elif port < explicitInputPorts + implicitInputPorts + explicitOutputPorts + implicitOutputPorts + controlPorts:
        port_type = "ControlPort"
        link_type = "CommandControlLink"
        linklist.append((link_type, port_id, thisx, thisy, port_index, portx, porty, waypoints, linkid))
    else:
        port_type = "CommandPort"
        link_type = "CommandControlLink"
        linklist.append((link_type, port_index, portx, porty, port_id, thisx, thisy, waypoints, linkid))
    return port_type, link_type


def getComponentGeometry(mxGeometry):
    componentGeometry = {}
    componentGeometry['height'] = 40
    componentGeometry['width'] = 40
    componentGeometry['x'] = 0
    componentGeometry['y'] = 0
    if mxGeometry is not None:
        componentGeometry['height'] = mxGeometry.attrib['height']
        componentGeometry['width'] = mxGeometry.attrib['width']
        componentGeometry['x'] = mxGeometry.attrib.get('x', '0')
        componentGeometry['y'] = mxGeometry.attrib.get('y', '0')
    return componentGeometry


def getPinGeometry(mxGeometry, componentGeometry):
    geometry = dict(componentGeometry)
    if mxGeometry is not None:
        geometry['height'] = mxGeometry.attrib['height']
        geometry['width'] = mxGeometry.attrib['width']
        geometryX = mxGeometry.attrib.get('x', 0)
        geometryY = mxGeometry.attrib.get('y', 0)
        if mxGeometry.attrib.get('relative', '0') == '1':
            geometryX = num2str(float(componentGeometry['x']) +
                                float(componentGeometry['width']) * float(geometryX))
            geometryY = num2str(float(componentGeometry['y']) +
                                float(componentGeometry['height']) * float(geometryY))
        geometry['x'] = geometryX
        geometry['y'] = geometryY
    return geometry


def getorderingname(stylename):
    if stylename == 'ImplicitInputPort':
        orderingname = 'ExplicitInputPort'
    elif stylename == 'ImplicitOutputPort':
        orderingname = 'ExplicitOutputPort'
    else:
        orderingname = stylename
    return orderingname


def getParameters(cell):
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
    return parameters


def getSuperblock(cell):
    if "style" in cell.attrib and "SUPER_f" in cell.attrib["style"]:
        mxGraphModel = cell.find("./SuperBlockDiagram")

        return mxGraphModel

    return None


def getWaypoints(mxGeometry):
    waypoints = []
    arrayElement = mxGeometry.find('Array')
    if arrayElement is not None:
        for arrayChild in arrayElement:
            if arrayChild.tag == 'mxPoint':
                waypoints.append(arrayChild.attrib)
    return waypoints


def getSplitPoints(attrib, switch_split, blkgeometry, sourceVertex, targetVertex, waypoints):
    split_point, split_point2 = None, None

    if 'tarx' in attrib and 'tary' in attrib and (attrib['tarx'] != '0' or attrib['tary'] != '0'):
        point = {'x': attrib['tarx'], 'y': attrib['tary']}
        if switch_split:
            split_point2 = point
            waypoints.append(point)
        else:
            split_point = point
            waypoints.insert(0, point)
    elif sourceVertex in blkgeometry:
        vertex = blkgeometry[sourceVertex]
        point = {'x': vertex['x'], 'y': vertex['y']}
        waypoints.insert(0, point)

    if 'tar2x' in attrib and 'tar2y' in attrib and (attrib['tar2x'] != '0' or attrib['tar2y'] != '0'):
        point = {'x': attrib['tar2x'], 'y': attrib['tar2y']}
        if switch_split:
            split_point = point
            waypoints.insert(0, point)
        else:
            split_point2 = point
            waypoints.append(point)
    elif targetVertex in blkgeometry:
        vertex = blkgeometry[targetVertex]
        point = {'x': vertex['x'], 'y': vertex['y']}
        waypoints.append(point)

    return split_point, split_point2


def createDefaultParent(parentattribid, rootattribid):
    defaultParent = ET.Element('mxCell')
    defaultParent.set('as', 'defaultParent')
    defaultParent.set('id', parentattribid)
    defaultParent.set('parent', rootattribid)
    return defaultParent


def process_xcos_model(diagram, title, rootattribid, parentattribid,
                       workspace_file=None, context=None):
    global WORKSPACE

    started_workspace = False
    if WORKSPACE is None:
        WORKSPACE = ScilabWorkspace(title, workspace_file, context)
        started_workspace = True
    checkXcosDiagramTag(diagram)

    context_array = diagram.find('Array[@as="context"]')
    if context_array is not None:
        context = ''
        for context_add in context_array:
            if context_add.tag == 'add':
                context_value = context_add.attrib['value']
                if context_value:
                    context_value = context_value.strip(' \t\n\r\f\v;')
                    if context_value:
                        context += context_value + ';'
        if context:
            WORKSPACE.add_context(context)

    model = diagram.find('mxGraphModel')
    checkModelTag(model)
    outmodel = ET.Element('mxGraphModel')
    outmodel.set('as', 'model')

    for root in model:
        checkRootTag(root)

        outroot = ET.SubElement(outmodel, 'root')

        portCount = {}
        IDLIST = {}
        componentOrdering = 0
        nextattribid = 1
        nextAttribForSplit = 10000
        edgeDict = {}
        edgeList = []
        blkgeometry = {}
        cells = list(root)
        remainingcells = []
        cellslength = len(cells)
        oldcellslength = 0
        print('cellslength=', cellslength)
        while cellslength > 0 and cellslength != oldcellslength:
            for i, cell in enumerate(cells):
                try:
                    if i <= 1 and oldcellslength == 0:
                        createOutnode(i, outroot, rootattribid, parentattribid)
                        continue

                    attrib = cell.attrib
                    if 'id' not in attrib:
                        continue
                    attribid = attrib['id']
                    nextattribid = getNextAttribId(attribid, nextattribid)

                    # cell_type = attrib['CellType']
                    cell_type = attrib.get('CellType')
                    mxGeometry = cell.find('mxGeometry')

                    if cell_type == 'Component':

                        style = attrib['style']
                        componentOrdering += 1
                        portCount[attribid] = {
                            'ExplicitInputPort': 0,
                            'ImplicitInputPort': 0,
                            'ControlPort': 0,
                            'ExplicitOutputPort': 0,
                            'ImplicitOutputPort': 0,
                            'CommandPort': 0
                        }
                        componentGeometry = getComponentGeometry(mxGeometry)
                        parameters = getParameters(cell)
                        superblock = getSuperblock(cell)

                        # print(style_to_object(style))
                        # stylename = style_to_object(style)['default']
                        style_dict = style_to_object(style)
                        stylename = style_dict.get('default', 'TEXT_f')

                        getattr(Blocks, stylename)(outroot, attribid, componentOrdering, componentGeometry, parameters,
                                                   parent=parentattribid, style=style, superblock=superblock)

                        IDLIST[attribid] = cell_type
                        blkgeometry[attribid] = componentGeometry

                    elif 'vertex' in attrib:

                        style = attrib['style']
                        stylename = style_to_object(style)['default']
                        ParentComponent = attrib['ParentComponent']
                        orderingname = getorderingname(stylename)

                        portCount[ParentComponent][orderingname] += 1

                        ordering = getOrdering(attrib, portCount, ParentComponent, orderingname)

                        geometry = getPinGeometry(mxGeometry, componentGeometry)

                        getattr(Ports, stylename)(outroot, attribid, ParentComponent, ordering, geometry, style=style)

                        IDLIST[attribid] = stylename
                        blkgeometry[attribid] = geometry

                    elif 'edge' in attrib:

                        waypoints = getWaypoints(mxGeometry)

                        sourceVertex = attrib['sourceVertex']
                        targetVertex = attrib['targetVertex']
                        if sourceVertex not in IDLIST or targetVertex not in IDLIST:
                            remainingcells.append(cell)
                            continue
                        sourceType = IDLIST[sourceVertex]
                        targetType = IDLIST[targetVertex]

                        (sourceVertex, sourceType, targetVertex, targetType, switch_split, style, addSplit, waypoints) = getLinkStyle(attribid, sourceVertex, sourceType, targetVertex, targetType, waypoints)

                        split_point, split_point2 = getSplitPoints(attrib, switch_split, blkgeometry, sourceVertex, targetVertex, waypoints)

                        IDLIST[attribid] = style
                        link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)
                        edgeDict[attribid] = link_data
                        edgeList.append(link_data)
                except Exception:
                    traceback.print_exc()
                    sys.exit(127)
            oldcellslength = cellslength
            cells = remainingcells
            cellslength = len(remainingcells)
            remainingcells = []
            print('cellslength=', cellslength, ', oldcellslength=', oldcellslength)

    newEdgeDict = {}
    LINKTOPORT = {}
    LINKWAYPOINTS = {}
    for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2) in edgeList:
        link_data = (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)

        if not addSplit:
            newEdgeDict[attribid] = [link_data]
            LINKWAYPOINTS[attribid] = waypoints
            for key, value in newEdgeDict.items():
                print('newEdgeDict:', key, value)
            continue

        for attribid2 in sourceVertex, targetVertex:
            try:
                linkSegments = newEdgeDict[attribid2]
                waypoints2 = LINKWAYPOINTS[attribid2]
            except KeyError:
                continue

            print('split_point:', split_point, linkSegments, waypoints2)
            if attribid2 == sourceVertex:
                splitpoint = split_point2
                # print('SP:', splitpoint)
            else:
                splitpoint = split_point2
            result, i, left_array, right_array = identify_segment(waypoints2, splitpoint)
            if not result:
                sys.exit(0)
            (linkid, sourceVertex2, targetVertex2, sourceType2, targetType2, style2, waypoints2, addSplit2, split_point_new, split_point2_new) = linkSegments[i]
            array3 = waypoints

            componentOrdering += 1
            geometry = {}
            geometry['height'] = 7
            geometry['width'] = 7
            geometry['x'] = splitpoint['x']
            geometry['y'] = splitpoint['y']
            if sourceType2 == 'ControlPort' or sourceType2 == 'CommandPort' or sourceType2 == 'CommandControlLink':
                split_style = 'CLKSPLIT_f'
                func_name = 'CLKSPLIT_f'
            else:
                split_style = 'SPLIT_f;flip=false;mirror=false'
                func_name = 'SPLIT_f'
            SplitBlock(outroot, nextattribid, componentOrdering, geometry, [], parent=parentattribid, style=split_style, func_name=func_name)
            splitblockid = nextattribid
            nextattribid += 1

            inputCount = 0
            outputCount = 0
            port1 = nextattribid
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort1ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, left_array)
            port2 = nextattribid
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort2ForSplit(outroot, splitblockid, sourceVertex2, targetVertex2, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, right_array)
            port3 = nextattribid
            (inputCount, outputCount, nextattribid, nextAttribForSplit) = addPort3ForSplit(outroot, splitblockid, sourceVertex, targetVertex, sourceType, targetType, sourceType2, targetType2, inputCount, outputCount, nextattribid, nextAttribForSplit, array3)

            newEdgeDict[attribid2][i] = ((nextAttribForSplit, sourceVertex2, port1, sourceType2, targetType, style2, left_array, addSplit2, split_point, split_point2))
            nextAttribForSplit += 1
            newEdgeDict[attribid2].insert(i + 1, (nextAttribForSplit, port2, targetVertex2, sourceType, targetType2, style2, right_array, addSplit2, split_point, split_point2))
            nextAttribForSplit += 1
            if attribid2 == sourceVertex:
                waypoints.reverse()
                newEdgeDict[attribid] = [(nextAttribForSplit, port3, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)]
            else:
                newEdgeDict[attribid] = [(nextAttribForSplit, port3, sourceVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2)]
            nextAttribForSplit += 1
            LINKTOPORT[linkid] = port3

    for key, newEdges in newEdgeDict.items():
        for (attribid, sourceVertex, targetVertex, sourceType, targetType, style, waypoints, addSplit, split_point, split_point2) in newEdges:
            try:
                sourceVertex = LINKTOPORT[sourceVertex]
            except KeyError:
                pass

            try:
                targetVertex = LINKTOPORT[targetVertex]
            except KeyError:
                pass

            if get_int(attribid) >= 10000:
                attribid = nextattribid
                nextattribid += 1

            getattr(Links, style)(outroot, attribid, sourceVertex, targetVertex, waypoints[1:-1], parent=parentattribid)

    if started_workspace:
        print('Terminating workspace')
        WORKSPACE.clean()
        WORKSPACE = None
        started_workspace = False

    return outmodel


def is_safe_string(parameter, value):
    try:
        value.encode('ascii')
    except UnicodeEncodeError:
        return f"{parameter} parameter has non-ascii characters"
    if re.search(SYSTEM_COMMANDS, value):
        return f"{parameter} parameter has unsafe value"
    if re.search(SPECIAL_CHARACTERS, value):
        return f"{parameter} parameter has value with special characters"
    return None


def internal_fun(internal_key, **kwargs):
    try:
        internal = INTERNAL[internal_key]
        function = internal['function']
        parameters = internal['parameters']
        cmd = ""
        file_name = f"{WORKSPACE.title}-{internal_key}.txt"
        cmd += f"{function}('{file_name}'"
        for parameter in parameters:
            value = kwargs[parameter]
            msg = is_safe_string(parameter, value)
            if msg:
                print(msg)
                return {'msg': msg}
            cmd += f",{value}" if 'num' in parameters else f",'{value}'"
        cmd += ");"
        print(f"send command {cmd} to Scilab")
        WORKSPACE.send_command(cmd)
        if not isfile(file_name):
            msg = f"output {file_name} does not exist"
            print(msg)
            return {'msg': msg}
        with open(file_name, 'r') as f:
            data = f.read()
            data = ast.literal_eval(data)
            # flatten only if data is a list of lists with length 1
            if type(data) is list and \
                    all(type(item) is list and len(item) == 1 for item in data):
                data = [item[0] for item in data]
            print(f"data: {data}")
        os.remove(file_name)
        return data
    except Exception as e:
        msg = f"Error in internal function '{internal_key}': {str(e)}"
        print(msg)
        return {'msg': msg}


def cont_frm(num, den):
    return internal_fun('getOutput', num=num, den=den)
