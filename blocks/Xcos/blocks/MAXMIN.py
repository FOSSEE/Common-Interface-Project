from common.AAAAAA import *


def MAXMIN(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'MAXMIN'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'minmax', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, ['0'])
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


def get_from_MAXMIN(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = 'MIN' if parameters[0] == '1' else 'MAX'

    eiv = 1 if parameters[1] == '1' else 2
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
