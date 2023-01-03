def PMOS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PMOS'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='PMOS',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=9,
                       width=1)

    for i in range(9):
        addDataData(node, parameters[i])
    return outnode
