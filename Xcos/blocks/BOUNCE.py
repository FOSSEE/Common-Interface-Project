def BOUNCE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BOUNCE'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      simulationFunctionName='bounce_ball',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode
