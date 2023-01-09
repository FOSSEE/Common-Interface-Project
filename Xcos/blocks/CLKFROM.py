def CLKFROM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKFROM'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='clkfrom',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      value='From')

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_CLKFROM(cell):
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
