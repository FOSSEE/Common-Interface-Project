def DLRADAPT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLRADAPT_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    dependsOnU=1,
                    ordering=ordering, parent=1,
                    simulationFunctionName='dlradp',
                    simulationFunctionType='DEFAULT',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=6,width=1)
    
    for i in range(6):
        addDataData(node,parameters[i])

    return outnode
