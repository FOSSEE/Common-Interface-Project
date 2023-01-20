def EXPRESSION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXPRESSION'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'evaluate_expr', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 0, parameters)

    return outnode


def get_from_EXPRESSION(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = 'Expression:\n' + parameters[1]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
