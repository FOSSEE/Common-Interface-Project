def MUX_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MUX_f'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='mux',
                      simulationFunctionType='TYPE_1',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=1,
                       width=1)

    for i in range(1):
        addDataData(node, parameters[i])
    return outnode
