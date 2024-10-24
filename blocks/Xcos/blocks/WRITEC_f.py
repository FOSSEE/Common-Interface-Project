from common.AAAAAA import *


def WRITEC_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'WRITEC_f'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'writec', 'TYPE_2',
                         style, BLOCKTYPE_D,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    param = ["3", "99", "32", "32", "2", "0", "102", "111",
             "111"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 9, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addScilabDNode(outnode, AS_DSTATE, width=6, realParts=[
                   "-1.0", "0.0", "0.0", "0.0", "0.0", "0.0"])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_WRITEC_f(cell):
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
