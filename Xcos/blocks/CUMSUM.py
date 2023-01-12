def CUMSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CUMSUM'

    para1 = int(parameters[0])
    para2 = int(parameters[1])

    datatype = ''
    if para1 == 1:
        datatype = 'z'

    sum = 'm'
    if para2 == 1:
        sum = 'r'
    elif para2 == 2:
        sum = 'c'

    simulation_func_name = 'cumsum' + datatype + '_' + sum

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
