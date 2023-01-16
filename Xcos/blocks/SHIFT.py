def SHIFT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SHIFT'

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
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_SHIFT(cell):
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
