def SUMMATION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SUMMATION'
    data_type = ['','_z','_i32','_i16','_i8','_ui32','_ui16','_ui8']
    overflow = ['n','s','e']
    para1 = int(float(parameters[0]))
    para3 = int(float(parameters[2]))
    
    if para1==1 or para1==2:
        simulation_func_name = 'summation' + data_type[para1-1]
    else:
        simulation_func_name = 'summation' + data_type[para1-1] + overflow[para3]
    
    outnode = addNode(outroot,
                      'Summation',
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
