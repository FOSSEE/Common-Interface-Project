def ABS_VALUE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ABS_VALUE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='absolute_value',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_ABS_VALUE(cell):
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
