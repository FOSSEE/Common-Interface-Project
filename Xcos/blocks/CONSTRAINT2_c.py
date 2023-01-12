def CONSTRAINT2_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONSTRAINT2_c'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='constraint_c',
                      simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
                      style=func_name,
                      blockType='c',
                      dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_CONSTRAINT2_c(cell):
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
