def LOGIC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOGIC'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'logic', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_LOGIC(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''
    inputs = parameters[0].split(';')

    eiv = int(math.log2(len(inputs)))
    iiv = ''
    con = 1 if parameters[1] == '0' else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
