def LOGICAL_OP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOGICAL_OP'
    d_type = ['i32','i16','i8','ui32','ui16','ui8']
    para3 = int(float(parameters[2]))
    datatype = ''
    
    if para3!=1:
        datatype = '_' + d_type[para3-3]
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='logicalop' + datatype,
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=4, width=1)
    
    for i in range(4):
        ddDataData(node, parameters[i])
        
    return outnode
