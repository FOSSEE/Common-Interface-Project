def Gyrator(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Gyrator'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='Gyrator',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='c',
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_Gyrator(cell):
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
