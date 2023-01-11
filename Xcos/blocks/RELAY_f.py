def RELAY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RELAY_f'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU=1,
                      dependsOnT=1,
                      simulationFunctionName='relay',
                      simulationFunctionType='TYPE_2',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_RELAY_f(cell):
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
