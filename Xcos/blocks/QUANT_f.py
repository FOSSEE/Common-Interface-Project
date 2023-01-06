def QUANT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'QUANT_f'

    data_type = ['', 'qzrnd', 'qztrn', 'qzflr', 'qzcel']

    simulation_func_name = data_type[int(parameters[1])]

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnU=1,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
