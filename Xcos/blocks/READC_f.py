def READC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'READC_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      simulationFunctionName='readc',
                      simulationFunctionType='TYPE_2',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 8, parameters)

    return outnode


def get_from_READC_f(cell):
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
