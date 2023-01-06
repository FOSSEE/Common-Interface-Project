def WRITEC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'WRITEC_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      dependsOnU=1,
                      simulationFunctionName='writec',
                      simulationFunctionType='TYPE_2',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode
