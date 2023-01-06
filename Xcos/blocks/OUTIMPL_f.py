def OUTIMPL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'OUTIMPL_f'

    outnode = addNode(outroot, 'ImplicitOutBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      simulationFunctionName='outimpl',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
