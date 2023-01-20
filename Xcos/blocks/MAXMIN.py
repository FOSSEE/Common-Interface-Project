def MAXMIN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MAXMIN'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'minmax', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_MAXMIN(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = 'MIN' if parameters[0] == '1' else 'MAX'

    eiv = 1 if parameters[1] == '1' else 2
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
