def LOGICAL_OP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'LOGICAL_OP'

    d_type = ['', '', '', 'i32', 'i16', 'i8', 'ui32', 'ui16', 'ui8']
    para3 = int(float(parameters[2]))
    datatype = ''
    if para3 != 1:
        datatype = '_' + d_type[para3]

    simulation_func_name = 'logicalop' + datatype

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

    addExprsNode(outnode, TYPE_STRING, 4, parameters)

    return outnode


def get_from_LOGICAL_OP(cell):
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
