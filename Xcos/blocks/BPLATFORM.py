def BPLATFORM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BPLATFORM'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='bplatform2',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode


def get_from_BPLATFORM(cell):
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
