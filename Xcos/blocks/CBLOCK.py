def CBLOCK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CBLOCK'

    type = ''
    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    depends_t = 0
    if parameters[13] == 'y':
        depends_t = 1
    else:
        depends_t = 0

    depends_u = 0
    if parameters[12] == 'y':
        depends_u = 1
    else:
        depends_u = 0

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    code = parameters[14]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=depends_u,
                      dependsOnT=depends_t,
                      blockType='c',
                      simulationFunctionName=parameters[0],
                      simulationFunctionType=simulation_func_type,
                      style=func_name)

    addExprsArrayNode(outnode, 'ScilabString', 14, parameters, codeLines)

    return outnode


def get_from_CBLOCK(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')

    parameters = []
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
