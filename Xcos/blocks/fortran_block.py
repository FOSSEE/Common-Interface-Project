def fortran_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'fortran_block'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName=parameters[3],
        simulationFunctionType='DYNAMIC_FORTRAN_1',
        style=func_name)
    
    node = addNode(outnode, 'Array', **{'as': 'exprs'}, scilabClass='ScilabList')
    
    innode = addDataNode(node, 'ScilabString', height=4, width=1)
    for i in range(4):
        addDataData(innode, parameters[i])
    
    code = parameters[4]
    codeLines = code.split('\n')
    innode = addDataNode(node, 'ScilabString', height=len(codeLines), width=1)
    for i in range(len(codeLines)):
        addDataData(innode, codeLines[i])
   
    return outnode
