def OUT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUT_f'

    outnode = addNode(outroot, BLOCK_EXPLICIT_OUT, **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      simulationFunctionName='output',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_OUT_f(cell):
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
