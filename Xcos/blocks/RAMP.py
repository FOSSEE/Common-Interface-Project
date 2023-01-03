def RAMP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RAMP'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnT=1,
        simulationFunctionName='ramp',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)

    for i in range(3):
        addDataData(node, parameters[i])
    return outnode
