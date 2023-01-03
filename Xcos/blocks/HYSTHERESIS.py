def HYSTHERESIS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'HYSTHERESIS'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='hystheresis',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=5, width=1)
    
    for i in range(5):
        addDataData(node, parameters[i])
    
    return outnode
