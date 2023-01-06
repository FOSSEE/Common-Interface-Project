def INIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INIMPL_f'

    outnode = addNode(outroot, 'ImplicitInBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='inimpl',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
