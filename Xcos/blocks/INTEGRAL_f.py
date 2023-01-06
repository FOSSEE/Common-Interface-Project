def INTEGRAL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTEGRAL_f'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnT=1,
        blockType='c',
        simulationFunctionName='integr',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    
    addDataData(node, parameters[0])

    return outnode
