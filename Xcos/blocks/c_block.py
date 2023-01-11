def c_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'c_block'

    code = parameters[4]
    codeLines = code.split('\n')

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName=parameters[3],
                      simulationFunctionType='DYNAMIC_C_1',
                      style=func_name,
                      blockType='c')

    addExprsArrayNode(outnode, TYPE_STRING, 4, parameters, codeLines)

    return outnode


def get_from_c_block(cell):
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
