def EXPBLK_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXPBLK_m'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='c',
                    dependsOnU=1,
                    ordering=ordering, parent=1,
                    simulationFunctionName='expblk_m',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=1,width=1)

    for i in range(1):
        addDataData(node,parameters[i])
        
    return outnode

