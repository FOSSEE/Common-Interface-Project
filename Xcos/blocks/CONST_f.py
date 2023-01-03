def CONST_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONST_f'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='cstblk',
        simulationFunctionType='TYPE_1',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
   
    addDataData(node, parameters[0])
    
    return outnode
