def SWITCH_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SWITCH_f'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='switchn',
                      simulationFunctionType='TYPE_2',
                      style=func_name,
                      blockType='c',
                      dependsOnU=1,
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_SWITCH_f(cell):
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
