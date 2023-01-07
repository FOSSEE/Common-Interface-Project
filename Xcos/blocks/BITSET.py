def BITSET(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BITSET'

    datatype = ['', '', '', '32', '16', '8', '32', '16', '8']
    para1 = int(float(parameters[0]))

    simulation_func_name = 'bit_set_' + datatype[para1]

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
