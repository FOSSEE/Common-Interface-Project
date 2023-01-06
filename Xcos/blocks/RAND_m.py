def RAND_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RAND_m'
    data_type = ['rndblk_m','rndblkz_m']
    simulation_func_name = data_type[int(parameters[0])-1]
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'd',
                      ordering=ordering,
        simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=5,
                       width=1)
    
    for i in range(5):
        addDataData(node, parameters[i])
    
    

    return outnode
