def AUTOMAT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AUTOMAT'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'automat', 'IMPLICIT_C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)

    return outnode


def get_from_AUTOMAT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)
    modes = parameters[0] + ' modes'
    states = parameters[2] + ' states'
    display_parameter = 'Automaton\n' + modes + ' | ' + states

    eiv = int(float(parameters[0]))
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
