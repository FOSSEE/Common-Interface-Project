def SHIFT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SHIFT'

    data_type = ['', '', '',
                 'shift_32_', 'shift_16_', 'shift_8_',
                 'shift_32_', 'shift_16_', 'shift_8_']
    shift_type = ['A', 'C']
    para1 = int(parameters[0])
    bits_to_shift = int(parameters[1])
    para3 = int(parameters[2])

    simulation_func_name = ''
    if bits_to_shift != 0:
        simulation_func_name = simulation_func_name + data_type[para1]
        if bits_to_shift > 0:
            simulation_func_name = simulation_func_name + 'L' + shift_type[para3]
        else:
            simulation_func_name = simulation_func_name + 'R' + shift_type[para3]
    else:
        simulation_func_name = 'shift_32_LA'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c',
                      dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_SHIFT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
