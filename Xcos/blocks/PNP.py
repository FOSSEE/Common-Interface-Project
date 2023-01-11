def PNP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PNP'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnT=1,
                      simulationFunctionName='PNP',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 17, parameters)

    return outnode


def get_from_PNP(cell):
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
