def Diode(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Diode'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    dependsOnU=1,
                    blockType='c',
                    ordering=ordering, parent=1,
                    simulationFunctionName='Diode',
                    simulationFunctionType='DEFAULT',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=4,width=1)
    
    for i in range(4):
        addDataData(node,parameters[i])

    return outnode
