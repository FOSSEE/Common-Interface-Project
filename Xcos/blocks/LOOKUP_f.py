def LOOKUP_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOOKUP_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering,
                      simulationFunctionName='lookup',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode


def get_from_LOOKUP_f(cell):
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
