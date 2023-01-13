def TKSCALE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TKSCALE'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'tkscaleblk', 'SCILAB',
                         func_name, 'd')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_TKSCALE(cell):
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
