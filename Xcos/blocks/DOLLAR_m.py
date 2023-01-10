def DOLLAR_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DOLLAR_m'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering, parent=1,
                      simulationFunctionName='dollar4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_DOLLAR_m(cell):
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
