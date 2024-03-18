from common.AAAAAA import *

def CLINDUMMY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLINDUMMY_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cdummy', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, parameters[0])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_STATE, 1, realParts=[0.0])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE,
                0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CLINDUMMY_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
