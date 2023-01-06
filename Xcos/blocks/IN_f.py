def IN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'IN_f'
    
    outnode = addNode(outroot, 'ExplicitInBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='c',
        simulationFunctionName='input',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=3, width=1)
    
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])

    return outnode

