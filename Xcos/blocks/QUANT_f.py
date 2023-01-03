def QUANT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'QUANT_f'
    data_type = ['qzrnd','qztrn','qzflr','qzcel']
    simulation_func_name = data_type[int(parameters[1])-1]
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU=1,
        simulationFunctionName=simulation_func_name,
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
