def M_freq(outroot, attribid, ordering, geometry, parameters):
    func_name = 'M_freq'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'd',
                      ordering=ordering,
        simulationFunctionName='m_frequ',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)
    
    for i in range(2):
        addDataData(node, parameters[i])
    
    

    return outnode
