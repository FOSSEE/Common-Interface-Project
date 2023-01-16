def EXTRACTBITS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTRACTBITS'

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
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 4, parameters)

    return outnode


def get_from_EXTRACTBITS(cell):
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
