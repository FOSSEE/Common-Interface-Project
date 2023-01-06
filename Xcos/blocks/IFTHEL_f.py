def IFTHEL_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'IFTHEL_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='l',
                      simulationFunctionName='ifthel',
                      simulationFunctionType='IFTHENELSE',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
