from common.AAAAAA import *


def GOTO(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'GOTO'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'goto', 'DEFAULT',
                         style, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
    innernode = addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    param = ['V_or']
    addSciStringNode(innernode, 1, param)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_GOTO(cell):
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
