def CONSTRAINT_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONSTRAINT_c'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      blockType='c',
                      simulationFunctionName='constraint_c',
                      simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
