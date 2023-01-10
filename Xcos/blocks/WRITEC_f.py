def WRITEC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'WRITEC_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      dependsOnU=1,
                      simulationFunctionName='writec',
                      simulationFunctionType='TYPE_2',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode


def get_from_WRITEC_f(cell):
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
