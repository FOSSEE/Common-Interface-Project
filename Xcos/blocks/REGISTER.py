def REGISTER(outroot, attribid, ordering, geometry, parameters):
    func_name = 'REGISTER'

    data_type = ['', '', '', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']
    para2 = int(parameters[1])

    simulation_func_name = 'delay4'
    if para2 >= 3:
        simulation_func_name = simulation_func_name + data_type[para2]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode