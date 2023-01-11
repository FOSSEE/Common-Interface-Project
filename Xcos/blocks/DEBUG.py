def DEBUG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEBUG'

    code = parameters[0]
    codeLines = code.split('\n')

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='%debug_scicos',
                      simulationFunctionType=func_name,
                      style=func_name)

    addExprsArrayNode(outnode, TYPE_STRING, 1, [''], codeLines)

    return outnode


def get_from_DEBUG(cell):
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
