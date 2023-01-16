def CLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLR'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csslti4', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_CLR(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

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
