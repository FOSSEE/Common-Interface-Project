def ZCROSS_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ZCROSS_f'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='z',
                      dependsOnU=1,
                      simulationFunctionName='zcross',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_ZCROSS_f(cell):
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
