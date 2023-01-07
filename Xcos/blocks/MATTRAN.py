def MATTRAN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATTRAN'

    data_type = ['', 'mattran_m', 'matztran_m']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    if para2 == 2 and para1 == 2:
        simulation_func_name = 'mathermit_m'
    else:
        simulation_func_name = data_type[para1]

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