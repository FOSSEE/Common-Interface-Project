def CMSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CMSCOPE'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName='cmscope',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      value=parameters[10])

    addExprsNode(outnode, TYPE_STRING, 11, parameters)

    return outnode


def get_from_CMSCOPE(cell):
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
