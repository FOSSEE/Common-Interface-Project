def AFFICH_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AFFICH_m'

    outnode = addNode(outroot, 'AfficheBlock', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='affich2',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode


def get_from_AFFICH_m(cell):
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
