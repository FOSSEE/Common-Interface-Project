def CANIMXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CANIMXY'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        simulationFunctionName='canimxy',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        blockType='d')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=11, width=1)
    
    for i in range(11):
        addDataData(node, parameters[i])
        
    return outnode
