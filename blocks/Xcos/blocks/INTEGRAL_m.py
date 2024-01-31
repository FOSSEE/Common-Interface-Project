from common.AAAAAA import *

def INTEGRAL_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTEGRAL_m'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'integral_func', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)

    return outnode


def get_from_INTEGRAL_m(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = 2 if parameters[1] == '1' else 1
    iiv = ''
    con = 1 if parameters[1] == '1' else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
