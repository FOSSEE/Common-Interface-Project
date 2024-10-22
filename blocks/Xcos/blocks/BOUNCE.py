from common.AAAAAA import *


def BOUNCE(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'BOUNCE'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'bounce_ball', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=10, realParts=[
                   "1.0", "1.0", "1.0", "1.0", "0.0", "5.0",
                   "0.0", "5.0", "9.81", "0.0"])
    param = ["1", "2"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 2, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['9']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addScilabDNode(outnode, AS_STATE, width=8, realParts=["2.0",
                   "0.0", "3.0", "0.0", "2.5", "0.0", "5.0", "0.0"])
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
