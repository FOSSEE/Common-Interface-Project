def READAU_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'READAU_f'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'd',
        simulationFunctionName='readau',
                      simulationFunctionType='TYPE_2',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)

    for i in range(3):
        addDataData(node, parameters[i])
    return outnode
