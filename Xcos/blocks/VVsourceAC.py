def VVsourceAC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VVsourceAC'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='VVsourceAC',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=1,
                       width=1)
    addDataData(node, parameters[0])
    

    return outnode
