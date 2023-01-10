def CONST_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONST_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='cstblk',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_CONST_f(cell):
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
