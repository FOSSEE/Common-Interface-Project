def CLKGOTO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKGOTO'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='clkgoto',
        simulationFunctionType='DEFAULT',
        style=func_name,
        value='Goto')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
   
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    return outnode
