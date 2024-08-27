from common.AAAAAA import *

def ZCROSS_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ZCROSS_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'zcross', 'TYPE_1',
                         func_name, BLOCKTYPE_Z,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                   "-1.0", "-1.0", "0.0", "0.0"])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_ZCROSS_f(cell):
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
