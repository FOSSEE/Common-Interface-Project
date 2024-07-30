from common.AAAAAA import *

def CANIMXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CANIMXY'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'canimxy', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 11, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                   format_real_number(parameters[6]),
                   format_real_number(parameters[7]),
                   format_real_number(parameters[8]),
                   format_real_number(parameters[9]),
                   ])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 11, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    # addScilabDNode(outnode, AS_STATE, width=2, realParts=[
    #                format_real_number(parameters[1]),
    #                format_real_number(parameters[2])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CANIMXY(cell):
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
