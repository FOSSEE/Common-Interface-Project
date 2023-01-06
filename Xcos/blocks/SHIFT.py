def SHIFT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SHIFT'
    data_type = ['shift_32_','shift_16_','shift_8_','shift_32_','shift_16_','shift_8_']
    shift_type = ['A','C']
    bits_to_shift  = int(paramters[1])
    simulation_func_name = ''

    if bits_to_shift != 0:
        simulation_func_name = simulation_func_name + data_type[int(parameters[0])-3]

        if bits_to_shift > 0:
            simulation_func_name = simulation_func_name + 'L' + shift_type[int(parameters[2])]
        else:
            simulation_func_name = simulation_func_name + 'R' + shift_type[int(parameters[2])]
    else:
        simulation_func_name = 'shift_32_LA'
    
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
                       height=3,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
                 

    
    

    return outnode
