from common.AAAAAA import *


def SAWTOOTH_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SAWTOOTH_f'
    if style is None:
        style = func_name

    parameters = [' ']

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'sawtth', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_DSTATE, 1, realParts=[0.0])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_SAWTOOTH_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
