def TOWS_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TOWS_c'
    b_type=''
    if int(parameters[2])==1:
        b_type = 'x'
    else:
        b_type = 'd'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = b_type,
        simulationFunctionName='tows_c',
                      simulationFunctionType='C_OR_FORTRAN',
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
