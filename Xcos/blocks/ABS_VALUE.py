def ABS_VALUE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ABS_VALUE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='absolute_value',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
