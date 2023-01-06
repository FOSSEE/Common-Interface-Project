def CLKFROM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKFROM'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='clkfrom',
        simulationFunctionType='DEFAULT',
        style=func_name,
        value='From')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
   
    addDataData(node, parameters[0])
    
    return outnode
