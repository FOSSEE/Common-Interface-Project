def MATTRAN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATTRAN'

    data_type = ['', 'mattran_m', 'matztran_m']

    if int(parameters[1]) == 2 and int(parameters[0]) == 2:
        simulation_func_name = 'mathermit_m'
    else:
        simulation_func_name = data_type[int(parameters[0])]

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
