from common.AAAAAA import *


def EXTRACTBITS(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'EXTRACTBITS'
    if style is None:
        style = func_name

    d_type = ['', 'UH', 'LH', 'MSB', 'LSB', 'RB']
    type1 = ['', '', '', '32', '16', '8', 'u32', 'u16', 'u8']
    type2 = ['', '', '', '32', '16', '8', '32', '16', '8']

    para1 = int(float(parameters[0]))
    para2 = int(float(parameters[1]))
    para4 = int(float(parameters[3]))

    if para2 == 2 or para2 == 4:
        bits_extract = type2[para1] + '_' + d_type[para2]
        bit_int = ''
    else:
        if para4 == 0:
            bits_extract = type2[para1] + '_' + d_type[para2]
        else:
            bits_extract = type1[para1] + '_' + d_type[para2]
        bit_int = str(para4)

    simulation_func_name = 'extract_bit_' + bits_extract + bit_int

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 4, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])

    param = [parameters[2], parameters[3]]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 2, param)
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


def get_from_EXTRACTBITS(cell):
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
