def INIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INIMPL_f'

    outnode = addOutNode(outroot, BLOCK_IMPLICIT_IN,
                         attribid, ordering, 1,
                         func_name, 'inimpl', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_INIMPL_f(cell):
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
