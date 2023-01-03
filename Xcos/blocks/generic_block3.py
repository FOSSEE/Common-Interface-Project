def generic_block3(outroot, attribid, ordering, geometry, parameters):
    func_name = 'generic_block3'
    depends_t = 0
    if parameters[18]=='y':
        depends_t = 1
    
    depends_u = 0
    if parameters[17]=='y':
        depends_u = 1
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=depends_u,
        dependsOnT=depends_t,
        blockType='c',
        simulationFunctionName=parameters[0],
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=19, width=1)
    
    for i in range(19):
        addDataData(node, parameters[i])
    
    return outnodes
