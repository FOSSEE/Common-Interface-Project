def CLKFROM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKFROM'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='clkfrom',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      value='From')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_CLKFROM(cell):
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
