def AUTOMAT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AUTOMAT'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      simulationFunctionName='automat',
                      simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode


def get_from_AUTOMAT(cell):
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
