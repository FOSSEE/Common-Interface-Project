def ConstantVoltage(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ConstantVoltage'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='ConstantVoltage',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_ConstantVoltage(cell):
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
