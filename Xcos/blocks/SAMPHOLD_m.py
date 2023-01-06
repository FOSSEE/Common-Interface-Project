def SAMPHOLD_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SAMPHOLD_m'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      dependsOnU=1,
                      simulationFunctionName='samphold4_m',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
