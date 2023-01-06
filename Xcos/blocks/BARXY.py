def BARXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BARXY'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        simulationFunctionName='BARXY_sim',
        simulationFunctionType='SCILAB',
        style=func_name,
        blockType='d')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=5, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])
    
    return outnode
