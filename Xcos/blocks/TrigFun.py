def TrigFun(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TrigFun'
    simulation_func_name = str(paramters[0]) + '_blk'
    
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
                       height=1,
                       width=1)
    addDataData(node, parameters[0])
    
    

    return outnode
