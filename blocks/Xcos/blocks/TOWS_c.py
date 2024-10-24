from common.AAAAAA import *


def TOWS_c(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'TOWS_c'
    if style is None:
        style = func_name

    para3 = int(parameters[2])

    if para3 == 1:
        blocktype = BLOCKTYPE_X
    else:
        blocktype = BLOCKTYPE_D

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'tows_c', 'C_OR_FORTRAN',
                         style, blocktype)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 0, [])
    array = ['128', '2', '117', '49']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 4, array)
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


def get_from_TOWS_c(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[1] + ',' + parameters[0]

    eiv = ''
    iiv = ''
    con = 1 if parameters[2] == '0' else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
