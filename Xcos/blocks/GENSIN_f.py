def GENSIN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'GENSIN_f'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnT=1,
        blockType='c',
        simulationFunctionName='gensin',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=3, width=1)
    
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    
    return outnode
