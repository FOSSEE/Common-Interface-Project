def CLKGOTO(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKGOTO'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='clkgoto',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      value='Goto')

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
