def MUX(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MUX'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='multiplex',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=1,
                       width=1)

    for i in range(1):
        addDataData(node, parameters[i])
    return outnode
