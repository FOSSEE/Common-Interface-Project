def MAXMIN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MAXMIN'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU='1',
                      simulationFunctionName='minmax',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_MAXMIN(cell):
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
