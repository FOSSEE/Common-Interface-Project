def DLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLR'

    depends_on_flag = 0

    num_str = parameters[0]
    den_str = parameters[1]

    num_exponents = []
    den_exponents = []

    num_matches = re.findall(r'z\s*\^\s*\d+|z', num_str)
    den_matches = re.findall(r'z\s*\^\s*\d+|z', den_str)

    if len(num_matches) == 0 and len(den_matches) == 0:
        depends_on_flag = 1
    else:

        for match in num_matches:
            splits = match.split('^')

            if len(splits) == 1:
                num_exponents.append(1)
            else:
                num_exponents.append(int(splits[1]))

        for match in den_matches:
            splits = match.split('^')

            if len(splits) == 1:
                den_exponents.append(1)
            else:
                den_exponents.append(int(splits[1]))

        if max(num_exponents) == max(den_exponents):
            depends_on_flag = 1

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'dsslti4', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D,
                         dependsOnU=depends_on_flag)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_DLR(cell):
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
