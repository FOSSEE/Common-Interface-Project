from common.AAAAAA import *

def REGISTER(outroot, attribid, ordering, geometry, parameters):
    func_name = 'REGISTER'

    data_type = ['', '', '', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']

    para2 = int(parameters[1])

    if para2 >= 3:
        simulation_func_name = 'delay4' + data_type[para2]
    else:
        simulation_func_name = 'delay4'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    numbers = parameters[0].split(';')
    formatted_numbers = []
    for num in numbers:
        formatted_numbers.append(num)
    addScilabDNode(outnode, AS_DSTATE, width=5, realParts=[
                   format_real_number(formatted_numbers[0]),
                   format_real_number(formatted_numbers[1]),
                   format_real_number(formatted_numbers[2]),
                   format_real_number(formatted_numbers[3]),
                   format_real_number(formatted_numbers[4])])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, [])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_REGISTER(cell):
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
