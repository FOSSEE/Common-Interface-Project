from common.AAAAAA import *

def CSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPE'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cscope', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 10, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 4, realParts=[0.0, 1.0, 3.0, 10.0])

    param = strarray(parameters)
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 15, param)
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


def get_from_CSCOPE(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = 1 if int(float(parameters[8])) == 0 else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
