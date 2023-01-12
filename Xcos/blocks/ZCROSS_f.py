def ZCROSS_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ZCROSS_f'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='zcross',
                      simulationFunctionType='TYPE_1',
                      style=func_name,
                      blockType='z',
                      dependsOnU=1)

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
