def CSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1, blockType='c',
        simulationFunctionName='cscope', simulationFunctionType='C_OR_FORTRAN', style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=10, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, parameters[6])
    addDataData(node, parameters[7])
    addDataData(node, parameters[8])
    addDataData(node, parameters[9])

    return outnode

def get_from_CSCOPE(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
