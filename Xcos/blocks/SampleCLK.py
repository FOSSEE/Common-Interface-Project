def SampleCLK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SampleCLK'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='sampleclk',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_SampleCLK(cell):
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
