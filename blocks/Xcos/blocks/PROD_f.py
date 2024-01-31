def PROD_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PROD_f'

    outnode = addOutNode(outroot, BLOCK_ROUND,
                         attribid, ordering, 1,
                         func_name, 'prod', 'TYPE_2',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_PROD_f(cell):
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
