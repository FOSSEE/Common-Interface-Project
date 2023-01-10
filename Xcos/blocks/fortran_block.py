def fortran_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'fortran_block'

    code = parameters[4]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=parameters[3],
                      simulationFunctionType='DYNAMIC_FORTRAN_1',
                      style=func_name)

    addExprsArrayNode(outnode, 'ScilabString', 4, parameters, codeLines)

    return outnode


def get_from_fortran_block(cell):
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
