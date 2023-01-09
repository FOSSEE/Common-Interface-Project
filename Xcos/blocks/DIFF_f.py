def DIFF_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DIFF_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      dependsOnT=1,
                      blockType='c',
                      ordering=ordering, parent=1,
                      simulationFunctionName='diffblk',
                      simulationFunctionType='OLDBLOCKS',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_DIFF_f(cell):
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
