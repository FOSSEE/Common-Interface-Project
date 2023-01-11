def EXTTRI(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTTRI'

    extration_type = ['', 'exttril', 'exttriu', 'extdiag']
    data_type = ['', '', 'z']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    simulation_func_name = extration_type[para2] + data_type[para1]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering, parent=1,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

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
