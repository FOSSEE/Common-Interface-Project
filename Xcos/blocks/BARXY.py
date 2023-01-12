def BARXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BARXY'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='BARXY_sim',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d',
                      dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 5, parameters)

    return outnode


def get_from_BARXY(cell):
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
