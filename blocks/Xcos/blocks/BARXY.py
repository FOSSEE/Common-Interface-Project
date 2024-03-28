from common.AAAAAA import *

def BARXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BARXY'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'BARXY_sim', 'SCILAB',
                         func_name, BLOCKTYPE_D,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                  format_real_number(parameters[0]),
                  format_real_number(parameters[1]),
                  format_real_number(parameters[2]),
                  format_real_number(parameters[3])]
                  )
    param = [parameters[4]]
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


def get_from_BARXY(cell):
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
