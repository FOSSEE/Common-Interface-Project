from common.AAAAAA import *

def CSCOPXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPXY3D'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cscopxy3d', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 11, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 8, realParts=[-1.0, 1.0, -0.5, 2.5, 0.0, 10.0, 45.0, -45.0])
    array = ["-1", "8", "64", "1", "2", "3", "4", "5", "6", "7", "13", "1", "1", "1", "1", "1", "1", "1", "1", "1", "-1", "-1", "600", "400", "1"]
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 25, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CSCOPXY3D(cell):
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
