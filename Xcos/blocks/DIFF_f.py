def DIFF_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DIFF_f'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='diffblk',
                      simulationFunctionType='OLDBLOCKS',
                      style=func_name,
                      blockType='c',
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_DIFF_f(cell):
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
