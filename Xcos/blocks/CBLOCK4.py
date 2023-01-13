def CBLOCK4(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CBLOCK4'

    type = ''
    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    depends_t = 0
    if parameters[18] == 'y':
        depends_t = 1
    else:
        depends_t = 0

    depends_u = 0
    if parameters[17] == 'y':
        depends_u = 1
    else:
        depends_u = 0

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    code = parameters[19]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[0], simulation_func_type,
                         func_name, 'c',
                         dependsOnU=depends_u,
                         dependsOnT=depends_t)

    addExprsArrayNode(outnode, TYPE_STRING, 19, parameters, codeLines)

    return outnode


def get_from_CBLOCK4(cell):
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
