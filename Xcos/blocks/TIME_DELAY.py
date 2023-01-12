def TIME_DELAY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TIME_DELAY'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='time_delay',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='x',
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_TIME_DELAY(cell):
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
