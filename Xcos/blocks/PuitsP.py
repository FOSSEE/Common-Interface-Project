def PuitsP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PuitsP'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='Puits',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=4,
                       width=1)

    for i in range(4):
        addDataData(node, parameters[i])
    return outnode
