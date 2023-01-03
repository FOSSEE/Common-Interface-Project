def WRITEC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'WRITEC_f'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'd',
                      dependsOnU=1,
        simulationFunctionName='writec',
                      simulationFunctionType='TYPE_2',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=5,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])

    return outnode
