def EXTRACTOR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTRACTOR'
    
    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='c',
                    dependsOnU=1,
                    ordering=ordering, parent=1,
                    simulationFunctionName='extractor',
                    simulationFunctionType='C_OR_FORTRAN',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=1,width=1)
    
    addDataData(node,parameters[0])
    
    return outnode
