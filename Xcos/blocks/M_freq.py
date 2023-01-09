def M_freq(outroot, attribid, ordering, geometry, parameters):
    func_name = 'M_freq'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering,
                      simulationFunctionName='m_frequ',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_M_freq(cell):
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
