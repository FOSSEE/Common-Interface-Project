from common.AAAAAA import *

def BOUNCE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BOUNCE'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'bounce_ball', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)
    # addScilabDNode(outnode, AS_REAL_PARAM, width=10, realParts=[
    #                format_real_number(parameters[0]),
    #                format_real_number(parameters[1]),
    #                format_real_number(parameters[2]),
    #                format_real_number(parameters[3]),
    #                format_real_number(parameters[4]),
    #                format_real_number(parameters[5]),
    #                format_real_number(parameters[6]),
    #                format_real_number(parameters[7]),
    #                format_real_number(parameters[8]),
    #                format_real_number(parameters[9])
    #                ])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 2, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['9']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addScilabDNode(outnode, AS_STATE, width=8, realParts=[
                   parameters[0],
                   parameters[1],
                   parameters[2],
                   parameters[3],
                   parameters[4],
                   parameters[5],
                   parameters[6],
                   parameters[7]])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_BOUNCE(cell):
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
