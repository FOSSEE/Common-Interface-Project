def MATSUM(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATSUM'

    data_type = ['', 'mat_', 'matz_']
    sum_along = ['sum', 'sumc', 'suml']

    simulation_func_name = data_type[int(parameters[0])] + sum_along[int(parameters[1])]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
