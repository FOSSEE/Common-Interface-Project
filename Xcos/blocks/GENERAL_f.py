def GENERAL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'GENERAL_f'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='z',
                      simulationFunctionName='zcross',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_GENERAL_f(cell):
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
