def DELAYV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAYV_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      dependsOnU=1,
                      blockType='d',
                      ordering=ordering, parent=1,
                      simulationFunctionName='delayv',
                      simulationFunctionType='TYPE_1',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
