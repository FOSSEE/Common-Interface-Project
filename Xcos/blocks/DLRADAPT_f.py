def DLRADAPT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLRADAPT_f'

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      dependsOnU=1,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='dlradp',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 6, parameters)

    return outnode


def get_from_DLRADAPT_f(cell):
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
