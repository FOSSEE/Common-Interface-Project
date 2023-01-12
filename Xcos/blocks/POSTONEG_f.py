def POSTONEG_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'POSTONEG_f'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='cscope',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, TYPE_STRING, 0, parameters)

    return outnode


def get_from_POSTONEG_f(cell):
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
