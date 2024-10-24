from common.AAAAAA import *


def READC_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'READC_f'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'readc', 'TYPE_2',
                         style, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 8, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    param = ["3", "100", "32", "32", "0", "20", "1", "0", "1",
             "102", "111", "111", "0", "1"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 14, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addScilabDNode(outnode, AS_DSTATE, width=23, realParts=[
                   "1.0", "1.0", "0.0", "0.0", "0.0", "0.0",
                   "0.0", "0.0", "0.0", "0.0", "0.0", "0.0",
                   "0.0", "0.0", "0.0", "0.0", "0.0", "0.0",
                   "0.0", "0.0", "0.0", "0.0", "0.0"
                   ])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_READC_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    temp = parameters[0]
    temp = temp.replace('[', '')
    temp = temp.replace(']', '')

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = 1 if len(temp) > 0 else 0

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
