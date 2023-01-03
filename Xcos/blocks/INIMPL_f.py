def INIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INIMPL_f'
    
    outnode = addNode(outroot, 'ImplicitInBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='c',
        simulationFunctionName='inimpl',
        simulationFunctionType='DEFAULT',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    
    addDataData(node, parameters[0])

    return outnode

