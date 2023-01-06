def CMSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CMSCOPE'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='cmscope',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        value=parameters[10])

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=11, width=1)
   
    for i in range(11):
        addDataData(node, parameters[i])
    
    return outnode
