def MATINV(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATINV'

    data_type = ['', 'mat_inv', 'matz_inv']

    simulation_func_name = data_type[int(parameters[0])]

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c',
                      dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_MATINV(cell):
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
