def PNP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PNP'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnT=1,
        simulationFunctionName='PNP',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=17,
                       width=1)

    for i in range(17):
        addDataData(node, parameters[i])
    return outnode
