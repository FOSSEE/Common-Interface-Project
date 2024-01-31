from common.AAAAAA import *

def TOWS_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TOWS_c'

    para3 = int(parameters[2])

    if para3 == 1:
        b_type = BLOCKTYPE_X
    else:
        b_type = BLOCKTYPE_D

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'tows_c', 'C_OR_FORTRAN',
                         func_name, b_type)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_TOWS_c(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[1] + ',' + parameters[0]

    eiv = ''
    iiv = ''
    con = 1 if parameters[2] == '0' else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
