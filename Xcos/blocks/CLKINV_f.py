def CLKINV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKINV_f'

    outnode = addNode(outroot, 'EventInBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_CLKINV_f(cell):
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
