def ROOTCOEF(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ROOTCOEF'
    data_type = ['root_coef','rootz_coef']
    simulation_func_name = data_type[int(parameters[0])-1]
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    
    

    return outnode
