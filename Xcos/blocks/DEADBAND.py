def DEADBAND(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEADBAND'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    dependsOnU=1, 
                    interfaceFunctionName=func_name,
                    ordering=ordering, parent=1,
                    blockType='c',
                    simulationFunctionName='deadband',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=3, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])

    return outnode
