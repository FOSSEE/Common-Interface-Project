def DLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLR'

    depends_on_flag = 0

    num_str = parameters[0]
    den_str = parameters[1]

    num_exponents = []
    den_exponents = []

    num_matches = re.findall('z\s*\^\s*\d+|z',num_str)
    den_matches = re.findall('z\s*\^\s*\d+|z',den_str)

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

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    ordering=ordering, parent=1,
                    dependsOnU = depends_on_flag,
                    simulationFunctionName='dsslti4',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=2,width=1)
    
    for i in range(2):
        addDataData(node,parameters[i])

    return outnode


def get_from_DLR(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
