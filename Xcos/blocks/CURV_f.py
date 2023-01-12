def CURV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CURV_f'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='intplt',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='c',
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_CURV_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
