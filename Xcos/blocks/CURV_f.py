def CURV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CURV_f'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnT=1,
        blockType='c',
        simulationFunctionName='intplt',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'exprs'}, height=0, width=0)
   
    return outnode
