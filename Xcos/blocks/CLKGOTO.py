def CLKGOTO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKGOTO'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='clkgoto',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      value='Goto')

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_CLKGOTO(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
