def CUMSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CUMSUM'

    para1 = int(parameters[0])
    para2 = int(parameters[1])

    datatype = ''
    if para1 == 1:
        datatype = 'z'

    sum = 'm'
    if para2 == 1:
        sum = 'r'
    elif para2 == 2:
        sum = 'c'

    simulation_func_name = 'cumsum' + datatype + '_' + sum

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_CUMSUM(cell):
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
