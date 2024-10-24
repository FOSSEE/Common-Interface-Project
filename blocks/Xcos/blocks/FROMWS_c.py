from common.AAAAAA import *


def FROMWS_c(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'FROMWS_c'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'fromws_c', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 4, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    array = ['1', '-31', '1', '1', '0']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 5, array)
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


def get_from_FROMWS_c(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = get_number_power(parameters[0])

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
