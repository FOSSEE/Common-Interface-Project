from common.AAAAAA import *


def BOUNCEXY(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'BOUNCEXY'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'bouncexy', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 8, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                   format_real_number(parameters[4]),
                   format_real_number(parameters[5]),
                   format_real_number(parameters[6]),
                   format_real_number(parameters[7])
                   ])
    param = ["-1", "1", "1", "2"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 4, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addScilabDNode(outnode, AS_DSTATE, width=12, realParts=[
                   "0.0", "0.0", "2.0", "2.0", "0.0", "23040.0",
                   "0.0", "0.0", "2.0", "2.0", "0.0", "23040.0"])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_BOUNCEXY(cell):
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
