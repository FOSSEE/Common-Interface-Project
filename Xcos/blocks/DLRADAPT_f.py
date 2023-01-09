def DLRADAPT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLRADAPT_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      dependsOnU=1,
                      ordering=ordering, parent=1,
                      simulationFunctionName='dlradp',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 6, parameters)

    return outnode


def get_from_DLRADAPT_f(cell):
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
