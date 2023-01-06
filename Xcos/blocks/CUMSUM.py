def CUMSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CUMSUM'

    datatype = ''
    if int(parameters[0]) == 1:
        datatype = 'z'

    sum = 'm'
    if int(parameters[1]) == 1:
        sum = 'r'
    elif int(parameters[1]) == 2:
        sum = 'c'

    simulation_func_name = 'cumsum' + datatype + '_' + sum

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
