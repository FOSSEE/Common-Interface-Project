def CUMSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CUMSUM'

    para1 = int(parameters[0])
    para2 = int(parameters[1])

    if para1 == 1:
        datatype = 'z'
    else:
        datatype = ''

    if para2 == 1:
        sum = 'r'
    elif para2 == 2:
        sum = 'c'
    else:
        sum = 'm'

    simulation_func_name = 'cumsum' + datatype + '_' + sum

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_CUMSUM(cell):
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
