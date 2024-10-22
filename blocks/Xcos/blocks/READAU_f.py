from common.AAAAAA import *


def READAU_f(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'READAU_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'readau', 'TYPE_2',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    param = ["7", "117", "99", "32", "0", "20", "1", "0", "1",
             "116", "101", "115", "116", "46", "97", "117", "1"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 17, param)
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


def get_from_READAU_f(cell):
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
