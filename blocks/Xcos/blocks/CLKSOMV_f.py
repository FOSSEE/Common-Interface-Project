from common.AAAAAA import *

def CLKSOMV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKSOMV_f'

    outnode = addOutNode(outroot, BLOCK_ROUND,
                         attribid, ordering, 1,
                         func_name, 'sum', 'DEFAULT',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_CLKSOMV_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
