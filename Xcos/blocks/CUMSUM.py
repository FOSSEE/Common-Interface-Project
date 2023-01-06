def CUMSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CUMSUM'
    
    datatype = ''
    if int(parameters[0])==1:
        datatype = 'z'
    
    sum = 'm'
    if int(parameters[1])==1:
        sum = 'r'
    elif int(parameters[1])==2:
        sum = 'c'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='cumsum' + datatype + '_' + sum,
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
   
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    return outnode
