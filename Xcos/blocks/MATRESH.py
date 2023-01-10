def MATRESH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATRESH'

    data_type = ['', 'mat_reshape', 'matz_reshape']

    simulation_func_name = data_type[int(parameters[0])]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_MATRESH(cell):
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
