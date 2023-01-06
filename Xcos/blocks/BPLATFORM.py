def BPLATFORM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BPLATFORM'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='bplatform2',
                      simulationFunctionType='SCILAB',
                      style=func_name,
                      blockType='d')

    node = addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode
