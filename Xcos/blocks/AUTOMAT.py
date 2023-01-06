def AUTOMAT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AUTOMAT'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      simulationFunctionName='automat',
                      simulationFunctionType='IMPLICIT_C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode
