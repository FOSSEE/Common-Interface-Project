def CLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLSS'

    para4 = int(float(parameters[3]))

    depends_u = 1
    if para4 == 0:
        depends_u = 0

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='csslti4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c',
                      dependsOnU=depends_u,
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 5, parameters)

    return outnode


def get_from_CLSS(cell):
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
