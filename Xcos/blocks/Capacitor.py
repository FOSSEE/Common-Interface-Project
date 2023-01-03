def Capacitor(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Capacitor'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        simulationFunctionName='Capacitor',
        simulationFunctionType='DEFAULT',
        style=func_name,
        blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=2, width=1)
   
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    return outnode
