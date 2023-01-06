def OUT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUT_f'
    outnode = addNode(outroot,
                      'ExplicitOutBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
        simulationFunctionName='output',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=1,
                       width=1)

    for i in range(1):
        addDataData(node, parameters[i])
    return outnode
