def DEADBAND(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEADBAND'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      dependsOnU=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='deadband',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_DEADBAND(cell):
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
