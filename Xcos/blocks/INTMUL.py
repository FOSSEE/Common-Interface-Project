def INTMUL(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTMUL'

    datatype = ['', '', '', 'i32', 'i16', 'i8', 'ui32', 'ui16', 'ui8']
    para1 = int(float(parameters[0]))
    para2 = int(float(parameters[1]))

    overflow = 'n'
    if para2 == 1:
        overflow = 's'
    elif para2 == 2:
        overflow = 'e'

    simulation_func_name = 'matmul_' + datatype[para1] + overflow

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_INTMUL(cell):
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
