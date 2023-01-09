def DEBUG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEBUG'

    code = parameters[0]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering, parent=1,
                      simulationFunctionName='%debug_scicos',
                      simulationFunctionType=func_name,
                      style=func_name)

    node = addExprsArrayNode(outnode, 'ScilabString', 1, [''], codeLines)

    return outnode


def get_from_DEBUG(cell):
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
