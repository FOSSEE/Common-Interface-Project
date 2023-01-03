def TKSCALE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TKSCALE'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'd',
        simulationFunctionName='tkscaleblk',
                      simulationFunctionType='SCILAB',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    
    return outnode
