from common.AAAAAA import *

def AFFICH_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AFFICH_m'

    outnode = addOutNode(outroot, BLOCK_AFFICHE,
                         attribid, ordering, 1,
                         func_name, 'affich2', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 0, [])
    array = ["1", "1", "1", "1000", "5", "1", "1"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 7, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_DSTATE,
                 7, realParts=[-1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_AFFICH_m(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = print_affich_m_by_param(parameters[0], parameters[5])

    eiv = ''
    iiv = ''
    con = 1 if parameters[6] == '0' else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
