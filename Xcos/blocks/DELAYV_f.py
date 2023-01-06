def DELAYV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAYV_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    dependsOnU=1,
                    blockType='d',
                    ordering=ordering, parent=1,
                    simulationFunctionName='delayv',
                    simulationFunctionType='TYPE_1',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=3,width=1)
    
    for i in range(3):
        addDataData(node,parameters[i])

    return outnode
