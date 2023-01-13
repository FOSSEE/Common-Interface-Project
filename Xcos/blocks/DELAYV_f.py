def DELAYV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAYV_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'delayv', 'TYPE_1',
                         func_name, 'd',
                         dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_DELAYV_f(cell):
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
