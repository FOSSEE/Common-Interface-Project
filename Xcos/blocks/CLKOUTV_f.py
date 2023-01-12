def CLKOUTV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKOUTV_f'

    outnode = addNode(outroot, BLOCK_EVENT_OUT,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='output',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_CLKOUTV_f(cell):
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
