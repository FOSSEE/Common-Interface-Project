def DEADBAND(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEADBAND'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      dependsOnU=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering, parent=1,
                      blockType='c',
                      simulationFunctionName='deadband',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
