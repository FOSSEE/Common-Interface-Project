def TIME_DELAY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TIME_DELAY'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='x',
                      dependsOnT=1,
                      simulationFunctionName='time_delay',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
