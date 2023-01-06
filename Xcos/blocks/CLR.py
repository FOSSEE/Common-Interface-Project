def CLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLR'

    outnode = addNode(outroot, 'BasicBlock', dependsOnT=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1, blockType='c',
        simulationFunctionName='csslti4', simulationFunctionType='C_OR_FORTRAN', style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])

    return outnode

def get_from_CLR(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')
    i = 0
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
        (v1, v2) = (value, re.sub(r'\([^()]*\)', r'', value))
        while v1 != v2:
            (v1, v2) = (v2, re.sub(r'\([^()]*\)', r'', v2))
        if i == 1:
            display_parameter += '/'
        display_parameter += '(' + value + ')' if re.search(r'[^ 0-9a-zA-Z^*/]', v2) else value
        i += 1
    return (parameters, display_parameter)
