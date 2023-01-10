def IN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'IN_f'

    outnode = addNode(outroot, 'ExplicitInBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_IN_f(cell):
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
