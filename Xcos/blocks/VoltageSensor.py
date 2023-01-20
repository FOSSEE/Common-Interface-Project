def VoltageSensor(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VoltageSensor'

    outnode = addOutNode(outroot, BLOCK_VOLTAGESENSOR,
                         attribid, ordering, 1,
                         func_name, 'VoltageSensor', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_VoltageSensor(cell):
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
