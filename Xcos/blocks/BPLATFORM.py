def BPLATFORM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BPLATFORM'

    outnode = addNode(outroot, 'BasicBlock',
        **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        simulationFunctionName='bplatform2',
        simulationFunctionType='SCILAB',
        style=func_name,
        blockType='d')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=7, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, parameters[6])
    
    return outnode
