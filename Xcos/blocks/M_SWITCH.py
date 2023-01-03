def M_SWITCH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'M_SWITCH'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'c',
                      dependsOnU=1,
                      ordering=ordering,
        simulationFunctionName='mswitch',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)
    
    for i in range(3):
        addDataData(node, parameters[i])
    
    

    return outnode
