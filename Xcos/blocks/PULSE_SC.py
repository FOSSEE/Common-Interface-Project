def PULSE_SC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PULSE_SC'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'h',
        simulationFunctionName='csuper',
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
