def TKSCALE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TKSCALE'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      simulationFunctionName='tkscaleblk',
                      simulationFunctionType='SCILAB',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
