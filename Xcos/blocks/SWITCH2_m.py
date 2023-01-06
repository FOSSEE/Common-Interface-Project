def SWITCH2_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SWITCH2_m'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU=1,
                      simulationFunctionName='switch2_m',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 4, parameters)

    return outnode
