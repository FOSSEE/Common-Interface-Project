def DIFF_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DIFF_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    dependsOnT=1,
                    blockType='c',
                    ordering=ordering, parent=1,
                    simulationFunctionName='diffblk',
                    simulationFunctionType='OLDBLOCKS',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=2,width=1)
    
    for i in range(2):
        addDataData(node,parameters[i])

    return outnode
