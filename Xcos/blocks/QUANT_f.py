def QUANT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'QUANT_f'

    data_type = ['', 'qzrnd', 'qztrn', 'qzflr', 'qzcel']

    simulation_func_name = data_type[int(parameters[1])]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'DEFAULT',
                         func_name, 'c',
                         dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_QUANT_f(cell):
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
