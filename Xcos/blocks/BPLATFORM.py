def BPLATFORM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BPLATFORM'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='bplatform2',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, TYPE_STRING, 7, parameters)

    return outnode


def get_from_BPLATFORM(cell):
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
