def BIGSOM_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BIGSOM_f'

    outnode = addNode(outroot, BLOCK_BIGSOM,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='sum',
                      simulationFunctionType='TYPE_2',
                      style=func_name,
                      blockType='c',
                      dependsOnU=1,
                      value='+')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_BIGSOM_f(cell):
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
