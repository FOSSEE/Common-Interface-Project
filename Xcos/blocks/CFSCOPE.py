def CFSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CFSCOPE'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='cfscope',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=9, width=1)
   
    for i in range(9):
        addDataData(node, parameters[i])
    
    return outnode
