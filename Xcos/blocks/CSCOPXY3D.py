def CSCOPXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPXY3D'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='cscopxy3d',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 11, parameters)

    return outnode


def get_from_CSCOPXY3D(cell):
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
