def VARIABLE_DELAY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VARIABLE_DELAY'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'd',
        simulationFunctionName='variable_delay',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=3,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[1])
    

    return outnode
