from common.AAAAAA import *


def GOTOMO(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'GOTOMO'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'gotomo', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, parameters[1])
    innerNode = addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    additionalStringNode = addDataNode(innerNode, 'ScilabString', height=1, width=1)
    addDataData(additionalStringNode, 'A')
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


def get_from_GOTOMO(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
