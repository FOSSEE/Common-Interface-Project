def PRODUCT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PRODUCT'

    outnode = addOutNode(outroot, BLOCK_PRODUCT,
                         attribid, ordering, 1,
                         func_name, 'product', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_PRODUCT(cell):
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
