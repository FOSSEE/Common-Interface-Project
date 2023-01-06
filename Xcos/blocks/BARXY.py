def BARXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BARXY'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName='BARXY_sim',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d')

    node = addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode
