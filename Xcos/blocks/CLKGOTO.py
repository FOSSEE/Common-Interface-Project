def CLKGOTO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKGOTO'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='clkgoto',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='d',
                      value='Goto')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_CLKGOTO(cell):
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
