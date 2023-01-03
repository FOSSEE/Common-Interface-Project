def BOUNCEXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BOUNCEXY'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        simulationFunctionName='bouncexy',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        blockType='d')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=8, width=1)
    
    for i in range(8):
        addDataData(node, parameters[i])
    
    return outnode

