def LOGIC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOGIC'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'c',
                      dependsOnU=1,
                      ordering=ordering,
        simulationFunctionName='logic',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)
    
    for i in range(2):
        addDataData(node, parameters[i])
    
    

    return outnode
