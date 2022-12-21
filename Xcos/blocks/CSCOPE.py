def CSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='cscope', simulationFunctionType='C_OR_FORTRAN', style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=10, width=1)
    addDataData(node, '1 3 5 7 9 11 13 15')
    addDataData(node, '-1')
    addDataData(node, '[]')
    addDataData(node, '[600;400]')
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, '30')
    addDataData(node, '20')
    addDataData(node, '0')
    addDataData(node, '')

    return outnode

def get_from_CSCOPE(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
