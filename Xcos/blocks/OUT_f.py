def OUT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUT_f'

    outnode = addOutNode(outroot, BLOCK_EXPLICIT_OUT,
                         attribid, ordering, 1,
                         func_name, 'output', 'DEFAULT',
                         func_name, 'c')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_OUT_f(cell):
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
