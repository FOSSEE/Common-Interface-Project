def CLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLSS'
    
    depends_u = 1
    if int(float(parameters[3]))==0:
        depends_u=0
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnT=1,
        dependsOnU=depends_u,
        blockType='c',
        simulationFunctionName='csslti4',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=5, width=1)
   
    for i in range(5):
        addDataData(node, parameters[i])
    
    return outnode
