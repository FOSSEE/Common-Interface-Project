def FROMWSB(outroot, attribid, ordering, geometry, parameters):
    func_name = 'FROMWSB'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='h')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_FROMWSB(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
