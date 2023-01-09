def BOUNCEXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BOUNCEXY'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='bouncexy',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='d')

    node = addExprsNode(outnode, 'ScilabString', 8, parameters)

    return outnode


def get_from_BOUNCEXY(cell):
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
