def RFILE_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RFILE_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'readf', 'DEFAULT',
                         func_name, 'd')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)

    return outnode


def get_from_RFILE_f(cell):
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
