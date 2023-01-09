def DELAY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAY_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='h',
                      ordering=ordering, parent=1,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode


def get_from_DELAY_f(cell):
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
