from common.AAAAAA import *


def c_block(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'c_block'
    if style is None:
        style = func_name

    code = parameters[3]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, parameters[3], 'DYNAMIC_C_1',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsArrayNode(outnode, TYPE_STRING, 4, parameters, codeLines, TYPE_ARRAY, func_name)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    param = ['0']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_c_block(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = parameters[3]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
