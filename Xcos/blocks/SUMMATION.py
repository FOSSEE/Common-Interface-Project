def SUMMATION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SUMMATION'

    data_type = ['', '', '_z', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']
    overflow = ['n', 's', 'e']
    para1 = int(float(parameters[0]))
    para3 = int(float(parameters[2]))

    if para1 == 1 or para1 == 2:
        simulation_func_name = 'summation' + data_type[para1]
    else:
        simulation_func_name = 'summation' + data_type[para1] + overflow[para3]

    outnode = addNode(outroot, 'Summation', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU=1,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_SUMMATION(cell):
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

    ports = [eiv, iiv, con, eov, eov, com]

    return (parameters, display_parameter, ports)
