def DELAYV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAYV_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      dependsOnU=1,
                      blockType='d',
                      ordering=ordering, parent=1,
                      simulationFunctionName='delayv',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_DELAYV_f(cell):
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
