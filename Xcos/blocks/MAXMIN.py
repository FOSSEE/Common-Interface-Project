def MAXMIN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MAXMIN'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU='1',
        simulationFunctionName='minmax',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)

    for i in range(3):
        addDataData(node, parameters[i])
        
    return outnode
