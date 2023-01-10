def EDGE_TRIGGER(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EDGE_TRIGGER'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='c',
                      ordering=ordering, parent=1,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode


def get_from_EDGE_TRIGGER(cell):
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
