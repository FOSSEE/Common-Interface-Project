def READC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'READC_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'readc', 'TYPE_2',
                         func_name, 'd')

    addExprsNode(outnode, TYPE_STRING, 8, parameters)

    return outnode


def get_from_READC_f(cell):
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
