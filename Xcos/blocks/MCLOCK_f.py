def MCLOCK_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MCLOCK_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='h',
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode
