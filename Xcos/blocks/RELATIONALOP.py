def RELATIONALOP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RELATIONALOP'

    data_type = ['', '', '', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']
    para3 = int(parameters[2])

    simulation_func_name = 'relational_op'
    if para3 >= 3:
        simulation_func_name = simulation_func_name + data_type[para3]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode