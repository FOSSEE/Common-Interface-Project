def ZCROSS_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ZCROSS_f'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'z',
                      dependsOnU=1,
        simulationFunctionName='zcross',
                      simulationFunctionType='TYPE_1',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    addDataData(node, parameters[0])

    return outnode
