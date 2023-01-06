def EXTRACT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTRACT'
    data_type = ['extract','extractz']
    simulation_func_name = data_type[int(parameters[0])-1]
    
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

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=3,width=1)

    for i in range(3):
        addDataData(node,parameters[i])
        
    return outnode

