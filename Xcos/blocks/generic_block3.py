def generic_block3(outroot, attribid, ordering, geometry, parameters):
    func_name = 'generic_block3'

    depends_t = 0
    if parameters[18] == 'y':
        depends_t = 1

    depends_u = 0
    if parameters[17] == 'y':
        depends_u = 1

    outnode = addNode(outroot, BLOCK_BASIC, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=depends_u,
                      dependsOnT=depends_t,
                      blockType='c',
                      simulationFunctionName=parameters[0],
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, TYPE_STRING, 19, parameters)

    return outnode


def get_from_generic_block3(cell):
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
