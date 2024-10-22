from common.AAAAAA import *


def CLSS(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CLSS'

    para4 = int(float(parameters[3]))

    if para4 == 0:
        depends_u = '0'
    else:
        depends_u = '1'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csslti4', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU=depends_u,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 16, realParts=[0.0,
                 0.0, -1.0, 1.0, 0.0, -2.0, 0.0, 1.0, -4.0, 0.0,
                 0.0, 10.0, 1.0, 0.0, 0.0, 0.0]
                 )
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_STATE,
                 3, realParts=[0.0, 0.0, 1.0])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CLSS(cell):
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
