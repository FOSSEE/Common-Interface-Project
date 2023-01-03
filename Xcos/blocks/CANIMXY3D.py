def CANIMXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CANIMXY3D'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        simulationFunctionName='canimxy3d',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        blockType='d')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=11, width=1)
    
    for i in range(11):
        addDataData(node, parameters[i])
        
    return outnode
