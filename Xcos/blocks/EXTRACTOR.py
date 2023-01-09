def EXTRACTOR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTRACTOR'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering, parent=1,
                      simulationFunctionName='extractor',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_EXTRACTOR(cell):
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
