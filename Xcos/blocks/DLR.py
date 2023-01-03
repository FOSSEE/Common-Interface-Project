def DLR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLR'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    ordering=ordering, parent=1,
                    simulationFunctionName='dsslti4',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=2,width=1)
    
    for i in range(2):
        addDataData(node,parameters[i])

    return outnode
