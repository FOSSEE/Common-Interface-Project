def DLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DLSS'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    ordering=ordering, parent=1,
                    simulationFunctionName='dsslti4',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=5,width=1)
    
    for i in range(5):
        addDataData(node,parameters[i])

    return outnode
