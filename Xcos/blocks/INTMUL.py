def INTMUL(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTMUL'

    datatype = ['', '', '', 'i32', 'i16', 'i8', 'ui32', 'ui16', 'ui8']
    overflow = 'n'
    if int(float(parameters[1])) == 1:
        overflow = 's'
    elif int(float(parameters[1])) == 2:
        overflow = 'e'

    simulation_func_name = 'matmul_' + datatype[int(float(parameters[0]))] + overflow

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
