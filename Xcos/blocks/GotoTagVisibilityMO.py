def GotoTagVisibilityMO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'GotoTagVisibilityMO'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'gototagvisibilitymo', 'DEFAULT',
                         func_name, 'c')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_GotoTagVisibilityMO(cell):
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
