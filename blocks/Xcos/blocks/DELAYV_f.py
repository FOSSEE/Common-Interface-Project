from common.AAAAAA import *


def DELAYV_f(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'DELAYV_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'delayv', 'TYPE_1',
                         func_name, BLOCKTYPE_D,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 1, realParts=[0.1])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    param = parameters[1].split(";")
    addScilabDNode(outnode, AS_DSTATE, width=11, realParts=[
                   format_real_number(param[0]),
                   format_real_number(param[1]),
                   format_real_number(param[2]),
                   format_real_number(param[3]),
                   format_real_number(param[4]),
                   format_real_number(param[5]),
                   format_real_number(param[6]),
                   format_real_number(param[7]),
                   format_real_number(param[8]),
                   format_real_number(param[9]),
                   format_real_number(param[0])])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_DELAYV_f(cell):
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
