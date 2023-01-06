def EVTDLY_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EVTDLY_c'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='evtdly4',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
    
    for i in range(2):
        addDataData(node, parameters[i])
   
    return outnode
