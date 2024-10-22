from common.AAAAAA import *


def CURVE_c(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CURVE_c'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'curve_c', 'DEFAULT',
                         func_name, BLOCKTYPE_D, dependsOnU='0',
                         dependsOnT='1')

    param = []
    for item in parameters:
        if item.startswith('[') and item.endswith(']'):
            values = item[1:-1].split(',')
            param.extend(values)
        else:
            param.append(item)
    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=6, realParts=[
                   format_real_number(param[1]),
                   format_real_number(param[2]),
                   format_real_number(param[3]),
                   format_real_number(param[4]),
                   format_real_number(param[5]),
                   format_real_number(param[6])
                   ])
    para = ['3', '3', '1']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 3, para)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)

    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, arr)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CURVE_c(cell):
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
