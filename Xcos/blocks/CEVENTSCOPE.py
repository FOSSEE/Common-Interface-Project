def CEVENTSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CEVENTSCOPE'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='cevscpe',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=6, width=1)
   
    for i in range(6):
        addDataData(node, parameters[i])
    
    return outnode
