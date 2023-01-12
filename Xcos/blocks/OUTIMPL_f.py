def OUTIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUTIMPL_f'

    outnode = addNode(outroot, BLOCK_IMPLICIT_OUT,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='outimpl',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_OUTIMPL_f(cell):
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
