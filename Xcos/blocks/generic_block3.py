def generic_block3(outroot, attribid, ordering, geometry, parameters):
    func_name = 'generic_block3'

    depends_t = 0
    if parameters[18] == 'y':
        depends_t = 1

    depends_u = 0
    if parameters[17] == 'y':
        depends_u = 1

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=depends_u,
                      dependsOnT=depends_t,
                      blockType='c',
                      simulationFunctionName=parameters[0],
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 19, parameters)

    return outnode


def get_from_generic_block3(cell):
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
