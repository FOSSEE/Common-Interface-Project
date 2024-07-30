from common.AAAAAA import *

def CONSTRAINT_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONSTRAINT_c'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'constraint_c', 'IMPLICIT_C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    # addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 2, [])
    addScilabDNode(outnode, AS_STATE, width=2, realParts=[
                   format_real_number(parameters[0])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CONSTRAINT_c(cell):
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
