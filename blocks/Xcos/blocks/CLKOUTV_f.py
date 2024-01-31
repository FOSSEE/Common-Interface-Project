def CLKOUTV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKOUTV_f'

    outnode = addOutNode(outroot, BLOCK_EVENT_OUT,
                         attribid, ordering, 1,
                         func_name, 'output', 'DEFAULT',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_CLKOUTV_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
