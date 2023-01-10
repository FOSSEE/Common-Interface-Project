def CLOCK_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLOCK_c'

    outnode = addNode(outroot, 'BasicBlock', blockType='h', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode


def get_from_CLOCK_c(cell):
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
