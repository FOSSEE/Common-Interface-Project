def GOTOMO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'GOTOMO'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='gotomo',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_GOTOMO(cell):
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
