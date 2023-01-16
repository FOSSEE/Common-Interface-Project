def MATEIG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATEIG'

    data_type = ['', 'mat_', 'matz_']
    decomposition_type = ['', 'vps', 'vpv']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    simulation_func_name = data_type[para1] + decomposition_type[para2]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_MATEIG(cell):
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
