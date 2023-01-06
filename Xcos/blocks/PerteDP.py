def PerteDP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PerteDP'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='PerteDP',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=6,
                       width=1)

    for i in range(6):
        addDataData(node, parameters[i])
    return outnode
