from common.AAAAAA import *


def AUTOMAT(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'AUTOMAT'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'automat', 'IMPLICIT_C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=1, realParts=[
                   format_real_number(parameters[3])
                   ])
    param = ["2", "1", "1", "1", "1", "2", "1"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 7, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addScilabDNode(outnode, AS_STATE, width=2, realParts=[
                   format_real_number(parameters[1]),
                   format_real_number(parameters[2])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_AUTOMAT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)
    display_parameter = parameters[0] + ',' + parameters[2]

    eiv = int(float(parameters[0]))
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
