def BITSET(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BITSET'
    datatype=['32', '16', '8', '32','16','8']

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        simulationFunctionName='bit_set_' + datatype[int(float(parameters[0]))-3],
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    return outnode
