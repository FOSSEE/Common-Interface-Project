def TCLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TCLSS'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnT=1,
                      simulationFunctionName='tcslti4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode


def get_from_TCLSS(cell):
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
