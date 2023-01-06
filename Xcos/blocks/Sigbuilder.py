def Sigbuilder(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Sigbuilder'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'h',
        simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabDouble',
                       **{'as': 'exprs'},
                       height=0,
                       width=0)
    return outnode
