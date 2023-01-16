def SUMMATION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SUMMATION'

    data_type = ['', '', '_z', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']
    overflow = ['n', 's', 'e']

    para1 = int(float(parameters[0]))
    para3 = int(float(parameters[2]))

    if para1 == 1 or para1 == 2:
        simulation_func_name = 'summation' + data_type[para1]
    else:
        simulation_func_name = 'summation' + data_type[para1] + overflow[para3]

    outnode = addOutNode(outroot, BLOCK_SUMMATION,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_SUMMATION(cell):
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
