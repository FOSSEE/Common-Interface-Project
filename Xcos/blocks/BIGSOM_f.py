def BIGSOM_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BIGSOM_f'

    outnode = addNode(outroot, 'BigSom', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='sum',
                      simulationFunctionType='TYPE_2',
                      style=func_name,
                      blockType='c',
                      value='+')

    addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_BIGSOM_f(cell):
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
