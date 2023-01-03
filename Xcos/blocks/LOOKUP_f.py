def LOOKUP_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOOKUP_f'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      blockType = 'c',
                      dependsOnU=1,
                      ordering=ordering,
        simulationFunctionName='lookup',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    	
    node = addDataNode(outnode, 'ScilabDouble',
                       **{'as': 'exprs'},
                       height=0,
                       width=0)
    
    

    return outnode
