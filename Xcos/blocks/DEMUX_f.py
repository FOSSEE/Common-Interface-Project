def DEMUX_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEMUX_f'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      dependsOnU=1,
                      blockType='c',
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='demux',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_DEMUX_f(cell):
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
