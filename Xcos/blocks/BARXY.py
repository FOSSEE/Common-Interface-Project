def BARXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BARXY'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName='BARXY_sim',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode


def get_from_BARXY(cell):
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
