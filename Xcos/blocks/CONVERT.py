def CONVERT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONVERT'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='convert',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=3, width=1)
   
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    
    return outnode
