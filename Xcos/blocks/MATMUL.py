def MATMUL(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATMUL'

    data_type = ['', 'matmul_m', 'matzmul_m',
                 'matmul_i32', 'matmul_i16', 'matmul_i8',
                 'matmul_ui32', 'matmul_ui16', 'matmul_ui8']
    overflow = ['n', 's', 'e']
    para1 = int(float(parameters[0]))
    para2 = int(float(parameters[1]))
    para3 = int(float(parameters[2]))

    simulation_func_name = ''
    if para2 == 1:
        if para1 == 1 or para1 == 2:
            simulation_func_name = data_type[para1]
        else:
            simulation_func_name = data_type[para1] + overflow[para3]
    elif para2 == 2:
        if para3 == 2:
            if para1 != 2:
                simulation_func_name = 'matmul2_m'
            else:
                simulation_func_name = 'mutmul2_e'
        elif para3 == 1:
            simulation_func_name = 'matmul2_s'
        else:
            simulation_func_name = 'matmul2_m'
    elif para2 == 3:
        if para1 != 2:
            if para3 == 1 or para3 == 2:
                simulation_func_name = 'matbyscal_' + overflow[para3]
        else:
            simulation_func_name = 'matbyscal'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, 'c',
                         dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_MATMUL(cell):
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
