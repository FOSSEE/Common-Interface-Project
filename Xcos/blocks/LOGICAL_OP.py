def LOGICAL_OP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOGICAL_OP'

    d_type = ['', '', '', 'i32', 'i16', 'i8', 'ui32', 'ui16', 'ui8']
    para3 = int(float(parameters[2]))
    datatype = ''
    if para3 != 1:
        datatype = '_' + d_type[para3]

    simulation_func_name = 'logicalop' + datatype

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 4, parameters)

    return outnode