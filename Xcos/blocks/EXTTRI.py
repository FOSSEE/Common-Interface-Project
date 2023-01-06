def EXTTRI(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTTRI'
    extration_type = ['exttril','exttriu','extdiag']
    data_type = ['','z']
    simulation_func_name = extration_type[int(parametrs[1])-1]+data_type[int(parameters[0])-1]
    
    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='c',
                    dependsOnU=1,
                    ordering=ordering, parent=1,
                    simulationFunctionName=simulation_func_name,
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=2,width=1)

    for i in range(2):
        addDataData(node,parameters[i])
        
    return outnode

