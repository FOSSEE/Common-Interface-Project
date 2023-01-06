def EVTVARDLY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EVTVARDLY'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='c',
                    dependsOnU=1,
                    ordering=ordering, parent=1,
                    simulationFunctionName='evtvardly',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=1,width=1)

    for i in range(1):
        addDataData(node,parameters[i])
        
    return outnode

