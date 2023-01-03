def GOTO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'GOTO'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='c',
        simulationFunctionName='goto',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
    
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    return outnode

