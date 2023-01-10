def c_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'c_block'

    code = parameters[4]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName=parameters[3],
                      simulationFunctionType='DYNAMIC_C_1',
                      style=func_name,
                      blockType='c')

    addExprsArrayNode(outnode, 'ScilabString', 4, parameters, codeLines)

    return outnode


def get_from_c_block(cell):
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
