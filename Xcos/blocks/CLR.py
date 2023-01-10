def CLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLR'

    outnode = addNode(outroot, 'BasicBlock', dependsOnT=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='csslti4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode


def get_from_CLR(cell):
    parameters = getParametersFromExprsNode(cell)

    value = parameters[0]
    (v1, v2) = (value, re.sub(r'\([^()]*\)', r'', value))
    while v1 != v2:
        (v1, v2) = (v2, re.sub(r'\([^()]*\)', r'', v2))
    dp1 = '(' + value + ')' if re.search(r'[^ 0-9a-zA-Z^*/]', v2) else value
    value = parameters[1]
    (v1, v2) = (value, re.sub(r'\([^()]*\)', r'', value))
    while v1 != v2:
        (v1, v2) = (v2, re.sub(r'\([^()]*\)', r'', v2))
    dp2 = '(' + value + ')' if re.search(r'[^ 0-9a-zA-Z^*/]', v2) else value
    display_parameter = dp1 + '/' + dp2

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
