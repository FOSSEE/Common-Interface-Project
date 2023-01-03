def MATSING(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATSING'
    data_type = ['mat_','matz_']
    decomposition_type = ['sing','svd']
    simulation_func_name = data_type[int(parameters[0])-1] + decomposition_type[int(parameters[1])-1]
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
                       height=2,
                       width=1)
    
    for i in range(2):
        addDataData(node, parameters[i])
    
    

    return outnode
