def OUTIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUTIMPL_f'
    outnode = addNode(outroot,
                      'ImplicitOutBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
        simulationFunctionName='outimpl',
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
