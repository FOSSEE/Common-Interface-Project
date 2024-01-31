def MATZREIM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATZREIM'

    data_type = ['', 'matz_reim', 'matz_reimc']

    simulation_func_name = data_type[int(parameters[0])]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_MATZREIM(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = int(parameters[0])
    iiv = ''
    con = ''
    eov = 2 if parameters[0] == '1' else 1
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
