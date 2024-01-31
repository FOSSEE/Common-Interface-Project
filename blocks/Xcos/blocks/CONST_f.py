def CONST_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONST_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cstblk', 'TYPE_1',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_CONST_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = get_number_power(parameters[0])

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
