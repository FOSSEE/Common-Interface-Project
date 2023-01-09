def INTRP2BLK_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTRP2BLK_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName='intrp2',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode


def get_from_INTRP2BLK_f(cell):
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
