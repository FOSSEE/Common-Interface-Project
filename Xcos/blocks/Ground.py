def Ground(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Ground'
    parameters = [""]
    outnode = addOutNode(outroot, BLOCK_GROUND,
                         attribid, ordering, 1,
                         func_name, 'Ground', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_Ground(cell):
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
