def EDGE_TRIGGER(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EDGE_TRIGGER'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='c',
                      ordering=ordering, parent=1,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode
