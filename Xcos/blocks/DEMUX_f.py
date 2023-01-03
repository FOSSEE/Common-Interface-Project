def DEMUX_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEMUX_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    dependsOnU=1,
                    blockType='c',
                    ordering=ordering, parent=1,
                    simulationFunctionName='demux',
                    simulationFunctionType='TYPE_1',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=1,width=1)
    
    for i in range(1):
        addDataData(node,parameters[i])

    return outnode
