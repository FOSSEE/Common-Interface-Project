def MATRESH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATRESH'
    data_type = ['mat_reshape','matz_reshape']
    simulation_func_name = data_type[int(parameters[0])-1]
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'c',
                      dependsOnU=1,
                      ordering=ordering,
        simulationFunctionName=simulation_func_name,
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
