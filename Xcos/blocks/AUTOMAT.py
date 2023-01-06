def AUTOMAT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AUTOMAT'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnT=1,
        simulationFunctionName='automat',
        simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
        style=func_name,
        blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=7, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, parameters[6])
    
    return outnode
