def FROM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'FROM'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='c',
        simulationFunctionName='from',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    
    addDataData(node, parameters[0])
   
    return outnode
