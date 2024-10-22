from common.AAAAAA import *


def BPLATFORM(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'BPLATFORM'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'bplatform2', 'SCILAB',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 7, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=7, realParts=[
        format_real_number(parameters[0]),
        format_real_number(parameters[1]),
        format_real_number(parameters[2]),
        format_real_number(parameters[3]),
        format_real_number(parameters[4]),
        format_real_number(parameters[5]),
        format_real_number(parameters[6])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addScilabDNode(outnode, AS_DSTATE, width=1, realParts=['0.0'])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_BPLATFORM(cell):
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
