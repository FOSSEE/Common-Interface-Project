def EXTTRI(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTTRI'

    extration_type = ['', 'exttril', 'exttriu', 'extdiag']
    data_type = ['', '', 'z']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    simulation_func_name = extration_type[para2] + data_type[para1]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, 'c',
                         dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_EXTTRI(cell):
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
