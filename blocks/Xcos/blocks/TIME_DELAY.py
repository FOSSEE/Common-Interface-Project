from common.AAAAAA import *

def TIME_DELAY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TIME_DELAY'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'time_delay', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_X,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_TIME_DELAY(cell):
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
