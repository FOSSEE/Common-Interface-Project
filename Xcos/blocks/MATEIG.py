def MATEIG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATEIG'

    data_type = ['', 'mat_', 'matz_']
    decomposition_type = ['', 'vps', 'vpv']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    simulation_func_name = data_type[para1] + decomposition_type[para2]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_MATEIG(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
