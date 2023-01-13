def CLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLSS'

    para4 = int(float(parameters[3]))

    depends_u = 1
    if para4 == 0:
        depends_u = 0

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csslti4', 'C_OR_FORTRAN',
                         func_name, 'c',
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
