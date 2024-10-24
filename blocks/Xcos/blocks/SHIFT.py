from common.AAAAAA import *


def SHIFT(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SHIFT'
    if style is None:
        style = func_name

    data_type = ['', '', '',
                 'shift_32_', 'shift_16_', 'shift_8_',
                 'shift_32_', 'shift_16_', 'shift_8_']
    shift_type = ['A', 'C']

    para1 = int(parameters[0])
    bits_to_shift = int(parameters[1])
    para3 = int(parameters[2])

    if bits_to_shift != 0:
        if bits_to_shift > 0:
            simulation_func_name = data_type[para1] + 'L' + shift_type[para3]
        else:
            simulation_func_name = data_type[para1] + 'R' + shift_type[para3]
    else:
        simulation_func_name = 'shift_32_LA'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 1, parameters[1])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_SHIFT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[1]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
