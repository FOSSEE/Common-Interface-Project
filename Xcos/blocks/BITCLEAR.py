def BITCLEAR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BITCLEAR'

    datatype = ['', '', '', '32', '16', '8', '32', '16', '8']

    simulation_func_name = 'bit_clear_' + datatype[int(float(parameters[0]))]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
