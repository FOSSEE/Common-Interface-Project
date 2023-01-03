def JKFLIPFLOP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'JKFLIPFLOP'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='h',
        simulationFunctionName='csuper',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'exprs'}, height=0, width=0)
        
    return outnode
