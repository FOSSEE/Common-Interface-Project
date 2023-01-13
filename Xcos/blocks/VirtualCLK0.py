def VirtualCLK0(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VirtualCLK0'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cscope', 'C_OR_FORTRAN',
                         func_name, 'c')

    addExprsNode(outnode, TYPE_STRING, 0, parameters)

    return outnode


def get_from_VirtualCLK0(cell):
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
