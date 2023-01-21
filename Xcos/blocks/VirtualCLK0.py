def VirtualCLK0(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VirtualCLK0'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'vrtclk0', 'DEFAULT',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_VirtualCLK0(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
