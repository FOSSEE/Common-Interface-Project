def MFCLCK_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MFCLCK_f'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'd',
        simulationFunctionName='mfclck',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)

    for i in range(2):
        addDataData(node, parameters[i])
    return outnode
