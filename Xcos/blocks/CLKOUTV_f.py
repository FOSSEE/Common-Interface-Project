def CLKOUTV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKOUTV_f'

    outnode = addNode(outroot, 'EventOutBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='output',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
