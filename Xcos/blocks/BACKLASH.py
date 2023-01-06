def BACKLASH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BACKLASH'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        simulationFunctionName='backlash',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name,
        blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=3, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    
    return outnode
